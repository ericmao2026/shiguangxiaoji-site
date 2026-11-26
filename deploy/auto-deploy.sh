#!/usr/bin/env bash
# ============================================================
# 自动部署包装脚本：供 launchd 每天定时调用
# 设置 AUTO_DEPLOY=1，使 deploy.sh 跳过人工确认直接上传
# 配合 Hugo 默认 buildFuture=false：只有 date <= 当天 的文章
# 才会进入 public 并被上传，因此错过几周补跑也不会乱序/多发。
# ============================================================
set -euo pipefail
SITE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$SITE_DIR"
export AUTO_DEPLOY=1
exec ./deploy/deploy.sh
