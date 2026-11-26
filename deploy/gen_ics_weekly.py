#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重生成 技术站日历.ics：52 篇周更计划 + 3 个运维事件
RFC5545：每行 ≤75 octet、CRLF、续行以空格开头（按 UTF-8 字符边界折，不切断中文）
"""
import datetime

TZ = "Asia/Shanghai"
DOMAIN = "shiguangxiaoji.com"

# (日期, 型, 编号, 标题)
SCHED = [
    ("2026-11-17", "H", "A02", "阴极剥离不是附着力不够，是系统自己造碱"),
    ("2026-11-24", "L", "L01", "拉拔附着力和阴极剥离，方向差 90°"),
    ("2026-12-01", "H", "A03", "富锌底漆的导电通路与牺牲阳极作用"),
    ("2026-12-08", "L", "L02", "富锌底漆里的锌，是不是越多越好"),
    ("2026-12-15", "H", "A04", "玻璃鳞片的屏蔽机理：迷宫效应到底有多少用"),
    ("2026-12-22", "L", "L03", "玻璃鳞片的长径比：为什么不是越薄越好"),
    ("2026-12-29", "H", "A11", "涂层体系设计里的配套性"),
    ("2027-01-05", "L", "L04", "面漆换牌号，为什么必须重做配套性"),
    ("2027-01-12", "H", "A06", "石墨烯环氧涂层的微电偶腐蚀：为什么添加量有最优值"),
    ("2027-01-19", "L", "L05", "石墨烯加多了为什么反而更差"),
    ("2027-01-26", "H", "A07", "附着力测试三法对比：拉拔、划格、划圈各答什么问题"),
    ("2027-02-02", "L", "L06", "划格法的 1mm 间距是怎么定的"),
    ("2027-02-09", "H", "A12", "湿膜厚度与干膜厚度的换算陷阱"),
    ("2027-02-16", "L", "L07", "湿膜 200μm，干膜一定不是 200"),
    ("2027-02-23", "H", "A08", "ISO 12944 的 C1-CX 分级怎么读，以及它不告诉你的事"),
    ("2027-03-02", "L", "L08", "CX 和 Im4，两个标签不是一回事"),
    ("2027-03-09", "H", "A09", "盐雾试验与真实海洋环境的差距在哪"),
    ("2027-03-16", "L", "L09", "盐雾箱里的 5% NaCl，为什么不是海水浓度"),
    ("2027-03-23", "H", "A10", "前处理等级 Sa2.5 与 Sa3 对寿命的实际影响（A 系列收官）"),
    ("2027-03-30", "L", "L10", "Sa2.5 和 Sa3 的差别，肉眼能不能分辨"),
    ("2027-04-06", "H", "P1", "标准里的条款号会故意留空"),
    ("2027-04-13", "L", "L11", "工程判断里，什么叫证实"),
    ("2027-04-20", "H", "B1", "EIS 谱图怎么读：Bode 与 Nyquist 各自说什么"),
    ("2027-04-27", "L", "L12", "Nyquist 半圆不闭合，说明什么"),
    ("2027-05-04", "H", "B2", "涂层电阻与吸水率：低频阻抗意味着什么"),
    ("2027-05-11", "L", "L13", "低频 0.01Hz 这个点为什么关键"),
    ("2027-05-18", "H", "B3", "极化曲线测的是什么，为什么不能直接换算腐蚀速率"),
    ("2027-05-25", "L", "L14", "Tafel 外推的两个前提"),
    ("2027-06-01", "H", "B4", "开路电位与线性极化、电化学噪声：三种方法的适用边界"),
    ("2027-06-08", "L", "L15", "LPR 的 B 值为什么必须有出处"),
    ("2027-06-15", "H", "B5", "三电极体系搭错的五种常见情形"),
    ("2027-06-22", "L", "L16", "参比电极放错位置，数据还能用吗"),
    ("2027-06-29", "H", "B6", "参比电极换算：为什么必须注明参比（B 系列收官）"),
    ("2027-07-06", "L", "L17", "饱和甘汞与 Ag/AgCl 差多少 mV"),
    ("2027-07-13", "H", "P2", "测试序列：流水线还是树"),
    ("2027-07-20", "L", "L18", "标准里为什么总写除非另有规定"),
    ("2027-07-27", "H", "C1", "加速因子不能跨体系套用"),
    ("2027-08-03", "L", "L19", "Arrhenius 在什么情况下会骗你"),
    ("2027-08-10", "H", "C2", "小样本怎么估寿命：Weibull 的用法与误用"),
    ("2027-08-17", "L", "L20", "Weibull 的形状参数在说什么"),
    ("2027-08-24", "H", "C3", "置信区间与样本量：为什么 3 个样品通过不算证据"),
    ("2027-08-31", "L", "L21", "3 个样品全过，置信度是多少"),
    ("2027-09-07", "H", "C4", "剔除规则必须前置"),
    ("2027-09-14", "L", "L22", "数据剔除为什么要先写规则"),
    ("2027-09-21", "H", "C5", "单点数据为什么不能外推（C 系列收官）"),
    ("2027-09-28", "L", "L23", "两点连线外推，错在哪"),
    ("2027-10-05", "H", "P3", "样品数量不是常数，是序列的函数"),
    ("2027-10-12", "L", "L24", "术语表：五个最容易混的强度"),
    ("2027-10-19", "H", "D1", "用 Python 处理测试数据的通用套路"),
    ("2027-10-26", "L", "L25", "Excel 里三个函数解决八成数据整理"),
    ("2027-11-02", "H", "D2", "工程师读英文标准的三个技巧"),
    ("2027-11-09", "L", "L26", "读标准先读范围还是先读定义"),
]

# 日历摘要用的短名，避免长标题在日历格里被硬截断
SHORT = {
    "A02": "阴极剥离", "L01": "拉拔 vs 剥离",
    "A03": "富锌导电通路", "L02": "锌越多越好吗",
    "A04": "玻璃鳞片迷宫", "L03": "长径比不是越薄越好",
    "A11": "涂层配套性", "L04": "换面漆要重做配套",
    "A06": "石墨烯微电偶", "L05": "石墨烯加多了更差",
    "A07": "附着力三法", "L06": "划格 1mm 哪来的",
    "A12": "湿膜转干膜", "L07": "湿膜≠干膜",
    "A08": "ISO 12944 分级", "L08": "CX vs Im4",
    "A09": "盐雾 vs 海洋", "L09": "5% NaCl 的由来",
    "A10": "前处理等级", "L10": "Sa2.5 vs Sa3",
    "P1": "条款号留空", "L11": "什么叫证实",
    "B1": "EIS 怎么读", "L12": "半圆不闭合",
    "B2": "低频阻抗", "L13": "0.01Hz 为什么关键",
    "B3": "极化曲线", "L14": "Tafel 外推前提",
    "B4": "三种方法边界", "L15": "LPR 的 B 值",
    "B5": "三电极搭错", "L16": "参比放错位置",
    "B6": "参比换算", "L17": "SCE vs Ag/AgCl",
    "P2": "流水线还是树", "L18": "除非另有规定",
    "C1": "加速因子", "L19": "Arrhenius 会骗你",
    "C2": "Weibull 估寿命", "L20": "形状参数在说什么",
    "C3": "样本量与置信", "L21": "3 个样品的置信度",
    "C4": "剔除规则前置", "L22": "先写剔除规则",
    "C5": "单点不能外推", "L23": "两点连线错在哪",
    "P3": "样品数是函数", "L24": "五个「强度」",
    "D1": "Python 处理数据", "L25": "Excel 三个函数",
    "D2": "读标准的技巧", "L26": "先读范围还是定义",
}

OPS = [
    ("2027-01-05", "ssl-check", "查 SSL 证书续签（01-27 到期）",
     "宝塔面板 → 网站 → SSL，确认自动续签开着。证书 2026-10-30 签发，2027-01-27 到期，"
     "若不自动续，当天站点会打不开。"),
    ("2027-01-06", "seo-review", "季度复盘：收录与访问",
     "看四件事：① 百度/必应是否收录首页与正文 ② 搜索资源平台有无抓取异常 "
     "③ 服务器磁盘与证书 ④ 排期是否已延误、库存是否领先两格。"),
    ("2027-04-20", "p1-watch", "P1 观察期评估：决定 P2 发不发",
     "P1 上线满两周。评估三件事：有没有陌生人来信、有没有同事或公司的人提及、"
     "搜索里出现时是否会被读成在写公司的活。任一项有不良迹象 → P 系列立即停发，"
     "全部转内部读本，日历删掉 P2 之后的格子。"),
]


def fold(line, limit=75):
    """按 UTF-8 字节折行，不切断多字节字符；续行以空格开头"""
    out, cur, cur_len = [], "", 0
    for ch in line:
        b = len(ch.encode("utf-8"))
        if cur_len + b > limit:
            out.append(cur)
            cur, cur_len = " " + ch, 1 + b
        else:
            cur += ch
            cur_len += b
    out.append(cur)
    return "\r\n".join(out)


def event(uid, datestr, start, end, summary, desc, alarms, allday=False):
    L = ["BEGIN:VEVENT"]
    L.append(f"UID:{uid}@{DOMAIN}")
    L.append("DTSTAMP:20261104T060000Z")
    if allday:
        d = datetime.date.fromisoformat(datestr)
        L.append(f"DTSTART;VALUE=DATE:{d.strftime('%Y%m%d')}")
        L.append(f"DTEND;VALUE=DATE:{(d + datetime.timedelta(days=1)).strftime('%Y%m%d')}")
    else:
        d = datetime.date.fromisoformat(datestr)
        L.append(f"DTSTART;TZID={TZ}:{d.strftime('%Y%m%d')}T{start}")
        L.append(f"DTEND;TZID={TZ}:{d.strftime('%Y%m%d')}T{end}")
    L.append(fold(f"SUMMARY:{summary}"))
    # RFC5545：TEXT 值里的换行必须编码为字面两字符 \n，不能是真换行
    L.append(fold("DESCRIPTION:" + desc.replace("\n", "\\n")))
    L.append("TRANSP:TRANSPARENT")
    for trig, msg in alarms:
        L.append("BEGIN:VALARM")
        L.append("ACTION:DISPLAY")
        L.append(f"TRIGGER:{trig}")
        L.append(fold(f"DESCRIPTION:{msg}"))
        L.append("END:VALARM")
    L.append("END:VEVENT")
    return "\r\n".join(L)


HEAD = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//shiguangxiaoji.com//publish schedule v2//CN
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:技术站发文（周更·周二 08:00）
X-WR-TIMEZONE:Asia/Shanghai
BEGIN:VTIMEZONE
TZID:Asia/Shanghai
BEGIN:STANDARD
DTSTART:19700101T000000
TZOFFSETFROM:+0800
TZOFFSETTO:+0800
TZNAME:CST
END:STANDARD
END:VTIMEZONE""".replace("\n", "\r\n")

parts = [HEAD]

for date, kind, code, title in SCHED:
    if kind == "H":
        summary = f"发 · {code} {SHORT.get(code, title[:10])}"
        desc = (
            f"标题：{title}\n"
            f"1) 提前两周出终稿（前一周周日前），front matter 写 date: {date}\n"
            f"2) 周二 08:00 之后执行 ./deploy/deploy.sh 才真正上线\n"
            f"3) 发布前过四问：公司名 / 光伏组件 / 原始数据 / 判断框架来源\n"
            f"4) 写不完用轻文顶档，不发空档、不推迟"
        )
        alarms = [
            ("-P2DT12H", f"终稿截止：明天必须出 {code} 的终稿并本地构建"),
            ("-PT10M", f"10 分钟后发 {code}"),
        ]
    else:
        summary = f"发·轻 {code} {SHORT.get(code, title[:10])}"
        desc = (
            f"标题：{title}\n"
            f"1) 1200 字以内，提前一周出稿\n"
            f"2) 从上一篇重文拆点，不查新文献、不补新数据\n"
            f"3) 周二 08:00 之后执行 ./deploy/deploy.sh"
        )
        alarms = [("-PT10M", f"10 分钟后发轻文 {code}")]
    parts.append(event(f"{date.replace('-','')}-{code}", date, "075000", "082000",
                       summary, desc, alarms))

for date, uid, summary, desc in OPS:
    tag = {"ssl-check": "🔒 ", "seo-review": "📊 ", "p1-watch": "🛑 "}[uid]
    parts.append(event(uid, date, "", "", tag + summary, desc, [], allday=True))

parts.append("END:VCALENDAR")
data = "\r\n".join(parts) + "\r\n"

with open("技术站日历.ics", "w", encoding="utf-8", newline="") as f:
    f.write(data)

# 自校验
lines = data.split("\r\n")
bad = [(i + 1, len(l.encode())) for i, l in enumerate(lines) if len(l.encode()) > 75]
print("事件数:", data.count("BEGIN:VEVENT"), "| 提醒数:", data.count("BEGIN:VALARM"))
print("超 75 octet 行:", bad[:5] if bad else "无")
print("裸 LF:", data.count("\n") - data.count("\r\n"), "| CRLF 结尾:", data.endswith("\r\n"))
