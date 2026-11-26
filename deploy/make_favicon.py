#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成站点 favicon（.ico 多尺寸 + .svg 矢量）
纯标准库实现，不依赖 Pillow / ImageMagick。

图形：深青圆角方块（#1f4e5f）+ 三条金色横线（#c8862b，递减透明度）
      意象 = 涂层分层剖面，与站点主题一致，16px 下仍可辨认。

用法：python3 deploy/make_favicon.py
输出：static/favicon.ico（16/32/48 三尺寸）、static/favicon.svg
"""
import struct
import pathlib

BG = (0x1F, 0x4E, 0x5F)
GOLD = (0xC8, 0x86, 0x2B)
# (y, height, alpha) —— 以 32 为基准坐标系
BARS = [(9, 3, 255), (15, 3, 190), (21, 3, 128)]


def inside_round(x, y, s, r):
    """判断点 (x,y) 是否在 s×s 的圆角矩形内，圆角半径 r。"""
    if x < r and y < r:
        return (x - r) ** 2 + (y - r) ** 2 <= r * r
    if x > s - r and y < r:
        return (x - (s - r)) ** 2 + (y - r) ** 2 <= r * r
    if x < r and y > s - r:
        return (x - r) ** 2 + (y - (s - r)) ** 2 <= r * r
    if x > s - r and y > s - r:
        return (x - (s - r)) ** 2 + (y - (s - r)) ** 2 <= r * r
    return True


def draw(size):
    """返回 size×size 的 RGBA 像素矩阵（行优先，原点在左上）。"""
    r = size * 7.0 / 32.0
    px = [[(0, 0, 0, 0)] * size for _ in range(size)]

    # 圆角方块底
    for y in range(size):
        for x in range(size):
            if inside_round(x + 0.5, y + 0.5, size, r):
                px[y][x] = BG + (255,)

    # 三条金色横线
    for by, bh, alpha in BARS:
        y0, y1 = round(by * size / 32), round((by + bh) * size / 32)
        x0, x1 = round(8 * size / 32), round(24 * size / 32)
        for y in range(max(0, y0), min(size, max(y0 + 1, y1))):
            for x in range(max(0, x0), min(size, x1)):
                if px[y][x][3]:  # 只覆盖底色区域，不越出圆角
                    px[y][x] = GOLD + (alpha,)
    return px


def ico_image(px, size):
    """把 RGBA 矩阵编码为 ICO 内部使用的 32 位 BMP（DIB）数据。"""
    # BITMAPINFOHEADER：高度填 2 倍（ICO 约定，含 AND 掩码）
    hdr = struct.pack('<IiiHHIIiiII', 40, size, size * 2, 1, 32, 0,
                      size * size * 4, 0, 0, 0, 0)
    data = bytearray()
    for y in range(size - 1, -1, -1):  # BMP 自下而上
        for x in range(size):
            rr, gg, bb, aa = px[y][x]
            data += bytes((bb, gg, rr, aa))
    row_bytes = ((size + 31) // 32) * 4  # AND 掩码每行按 4 字节对齐
    return hdr + bytes(data) + bytes(row_bytes * size)


def build_ico(sizes):
    n = len(sizes)
    images, entries = [], []
    offset = 6 + 16 * n
    for s in sizes:
        img = ico_image(draw(s), s)
        w = 0 if s >= 256 else s
        entries.append(struct.pack('<BBBBHHII', w, w, 0, 0, 1, 32, len(img), offset))
        offset += len(img)
        images.append(img)
    return struct.pack('<HHH', 0, 1, n) + b''.join(entries) + b''.join(images)


SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" role="img" aria-label="时光小记">
  <rect width="32" height="32" rx="7" fill="#1f4e5f"/>
  <rect x="8" y="9" width="16" height="3" rx="1.5" fill="#c8862b"/>
  <rect x="8" y="15" width="16" height="3" rx="1.5" fill="#c8862b" fill-opacity="0.75"/>
  <rect x="8" y="21" width="16" height="3" rx="1.5" fill="#c8862b" fill-opacity="0.5"/>
</svg>
'''


def main():
    static = pathlib.Path(__file__).resolve().parent.parent / 'static'
    if not static.is_dir():
        raise SystemExit(f'目录不存在：{static}')

    ico = build_ico([16, 32, 48])
    (static / 'favicon.ico').write_bytes(ico)
    (static / 'favicon.svg').write_text(SVG, encoding='utf-8')

    print(f'favicon.ico  {len(ico):>5} B  (16/32/48)')
    print(f'favicon.svg  {len(SVG.encode()):>5} B')


if __name__ == '__main__':
    main()
