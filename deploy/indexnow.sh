#!/usr/bin/env bash
# ============================================================
# IndexNow 主动推送：把「今天发布/更新」的 URL 提交给搜索引擎
#   用法：
#     ./deploy/indexnow.sh          # 只推今天有更新（lastmod = 今天）的 URL
#     ./deploy/indexnow.sh --all    # 推 sitemap 全部 URL（首次初始化 / 手动补齐用）
#   说明：
#     - key 文件位于 static/<KEY>.txt，部署后可通过
#       https://shiguangxiaoji.com/<KEY>.txt 访问
#     - deploy.sh 部署成功后会调用本脚本（默认模式）
#     - 支持必应 / Yandex / Seznam / Naver 等共用 IndexNow 协议
# ============================================================
set -uo pipefail

SITE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$SITE_DIR"

DOMAIN="shiguangxiaoji.com"
KEY="9233519456c6c5e0e15514d8fa14c42c"
KEY_LOCATION="https://${DOMAIN}/${KEY}.txt"
ENDPOINT="https://api.indexnow.org/indexnow"

MODE="${1:-today}"

if [ ! -f public/sitemap.xml ]; then
  echo "  跳过 IndexNow：public/sitemap.xml 不存在（需先构建）"
  exit 0
fi

/usr/bin/python3 - "$MODE" "$DOMAIN" "$KEY" "$KEY_LOCATION" "$ENDPOINT" <<'PY'
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import date

mode, domain, key, key_location, endpoint = sys.argv[1:6]
today = date.today().isoformat()

xml = open('public/sitemap.xml', encoding='utf-8').read()
urls = []
for block in re.findall(r'<url>(.*?)</url>', xml, re.S):
    loc = re.search(r'<loc>(.*?)</loc>', block, re.S)
    if not loc:
        continue
    lm = re.search(r'<lastmod>(.*?)</lastmod>', block, re.S)
    lastmod = lm.group(1)[:10] if lm else ''
    # --all：全量；默认：只取 lastmod >= 今天（Hugo 用文章 date 作 lastmod）
    if mode == '--all' or (lastmod and lastmod >= today):
        urls.append(loc.group(1).strip())

# 去重保序
urls = list(dict.fromkeys(urls))

if not urls:
    print('  IndexNow：今天没有新发布/更新的 URL，跳过')
    sys.exit(0)

print(f'  IndexNow：推送 {len(urls)} 条 URL')
for u in urls:
    print(f'    · {u}')

payload = json.dumps({
    'host': domain,
    'key': key,
    'keyLocation': key_location,
    'urlList': urls,
}).encode('utf-8')

req = urllib.request.Request(
    endpoint,
    data=payload,
    headers={'Content-Type': 'application/json; charset=utf-8'},
    method='POST',
)

try:
    with urllib.request.urlopen(req, timeout=20) as resp:
        code = resp.status
        body = resp.read().decode('utf-8', 'replace')[:300]
    if code in (200, 202):
        print(f'  ✓ IndexNow 已接收（HTTP {code}）')
    else:
        print(f'  ⚠ IndexNow 返回 HTTP {code}：{body}')
except urllib.error.HTTPError as e:
    body = e.read().decode('utf-8', 'replace')[:300]
    print(f'  ⚠ IndexNow HTTP {e.code}：{body}')
    print('    常见原因：403=key 文件不可访问；422=URL 与 host 不匹配；429=请求过于频繁')
except Exception as e:
    print(f'  ⚠ IndexNow 请求失败：{type(e).__name__}: {e}')
PY
