#!/usr/bin/env bash
# ============================================================
# 一键部署：本地构建 → rsync 上传到阿里云 ECS（宝塔面板站点）
#   1) 先填下面「只改这一块」的三个值
#   2) chmod +x deploy/deploy.sh
#   3) ./deploy/deploy.sh
# 首次使用前先打通免密：ssh-copy-id -i ~/.ssh/id_ed25519.pub root@你的IP
# ============================================================
set -euo pipefail

# ===== 只改这一块 =====
DOMAIN="shiguangxiaoji.com"                     # 主域名，不带 https://
# =====================

SITE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$SITE_DIR"

# 服务器地址从 deploy/.deploy.env 读取（该文件含 IP，不提交到公开仓库）
if [ -f deploy/.deploy.env ]; then
  # shellcheck disable=SC1091
  . deploy/.deploy.env
fi
HOST="${DEPLOY_HOST:?缺少 deploy/.deploy.env —— 请在文件里写 DEPLOY_HOST=root@你的服务器IP}"
TARGET="${DEPLOY_TARGET:-/www/wwwroot/shiguangxiaoji.com}"   # 宝塔站点根目录（不是 /var/www）

echo "▶ 构建（草稿不会进 public，这是 Hugo 默认行为）"
# 不用 --cleanDestinationDir：hugo 0.168 在本机 APFS 上删旧文件会报
#   ERROR error copying static files: unlinkat ... operation not permitted
# 且退出码为 1，配合 set -e 会直接中断部署。改为整体移走旧 public 再构建：
# 效果等价（不留旧文章残页）、可回退、不依赖删除权限。
if [ -d public ]; then
  PREV="$(mktemp -d)/public_prev"
  mv public "$PREV"
  echo "  旧构建已移至 $PREV"
fi
./bin/hugo --minify

# 正文页数抽查：数量突然下降，多半是某篇被误改成 draft: true
# 注意：栏目（methods/projects）下线时目录不存在，find 会返回非零；
#       配合 set -o pipefail 会让脚本在此静默中断、rsync 根本不执行。
#       故用 { ...; } || true 兜住，让统计对栏目上下线自适应。
PAGES=$({ find public/notes public/methods public/projects -name index.html 2>/dev/null || true; } | wc -l | tr -d ' ')
echo "  正文页数：$PAGES"
if [ -f .last_pages ] && [ "$PAGES" -lt "$(cat .last_pages)" ]; then
  echo "  ⚠ 比上次少，确认不是误改 draft 后继续"
  if [ -n "${AUTO_DEPLOY:-}" ]; then
    echo "  （AUTO_DEPLOY 模式：自动继续上传）"
  else
    read -r -p "  继续上传？[y/N] " ans || ans=""
    [ "$ans" = "y" ] || { echo "已中止"; exit 1; }
  fi
fi
echo "$PAGES" > .last_pages

echo "▶ 上传（$(du -sh public | cut -f1)）"
# .user.ini / .htaccess / .well-known 是宝塔生成的，必须排除，否则 --delete 会删掉
rsync -avz --delete \
  --exclude '.DS_Store' \
  --exclude '.user.ini' \
  --exclude '.htaccess' \
  --exclude '.well-known/' \
  -e "ssh -o StrictHostKeyChecking=accept-new" \
  public/ "$HOST:$TARGET/"

echo "▶ 服务器侧收尾（只改属主，不动 nginx 配置）"
# .user.ini 被宝塔加了 immutable 属性，chown 会报 Operation not permitted，要排除掉
ssh "$HOST" "find $TARGET -not -name '.user.ini' -exec chown www:www {} + 2>/dev/null || true
curl -sk -o /dev/null -w '  本机回环 HTTPS %{http_code}\n' -H 'Host: $DOMAIN' https://127.0.0.1/"

# IndexNow：页面已上线后主动通知搜索引擎抓取（失败不影响部署结果）
echo "▶ IndexNow 推送"
bash deploy/indexnow.sh || echo "  （IndexNow 推送失败，不影响本次部署）"

echo "✓ 完成：https://$DOMAIN/"
