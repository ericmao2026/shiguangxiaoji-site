---
title: "拉拔附着力和阴极剥离，方向差 90°"
date: 2026-11-15
draft: false
description: "两份报告都写着「附着力」，一份是 8.4 MPa，一份是 90 天退 12 mm。同一批涂料，同一块钢——它们说的不是一件事，方向差了 90°。"
section_label: "笔记"
tags: ["涂层失效", "附着力", "判据"]
---

同一批试板，分送两家实验室，回来的报告上都写着「附着力」。

一家写：8.4 MPa，合格。另一家写：90 天后退 12 mm，不合格。

不是谁做错了。这两行字说的根本不是一件事——它们相差 90°。

## 这 90° 差在哪

![图 1 · 拉拔与阴极剥离的受力方向对比](/images/pulloff-vs-disbondment.svg)

*图 1 · 左：力垂直于界面。右：裂纹沿界面推进。示意图自绘。*

拉拔（ISO 4624 / ASTM D4541）：在涂层上粘一个锭子，沿锭子周围切一圈，切穿涂层到基材，然后垂直于表面往上拉，直到拉开。读到的是一个应力值，单位 MPa。

阴极剥离（ISO 15711 一类）：在涂层上划一道口子，泡进电解质，接上阴极保护，量从划痕边缘往外退了多少毫米、用了多少天。读到的是一个长度加一个时间。

一个力的方向垂直于界面，一个裂纹的走向平行于界面。方向差 90°，量纲也少了一个维度。

这里有个容易被忽略的共同点：两个方法都从人为缺陷开始。拉拔前那一圈切割本身就是缺陷，阴极剥离的划痕也是。所以它们其实在问同一个起点的两个不同问题——**缺陷处的垂直强度有多大，缺陷作为起点能横向扩张多快。**

## 强度和速率不是一回事

拉拔测的是**强度**：某一瞬间把界面拉断，需要多大的应力。

阴极剥离测的是**速率**：在持续供碱的条件下，界面后退得有多快。

这两个量的时间尺度差三个数量级。拉拔从加载到断裂是分钟级，当天出结果；阴极剥离的标准时长普遍在 28 到 182 天之间。一个问「此刻要多大力」，一个问「多久退多远」。

驱动它们的东西也完全不同。拉拔靠机械夹具，是力学；阴极剥离靠 OH⁻ 和水，是化学——[碱是怎么在界面里被造出来的，这条链子在另一篇里](/notes/cathodic-disbondment/)。

力学强度和化学速率之间没有换算关系。就像没有公式能把「这根绳子能承多重」和「这根绳子在酸里多久烂断」连起来。

所以「附着力 8 MPa」推不出「抗剥离好」，反过来也一样。

## 三个不能换算的理由

| 维度 | 拉拔 | 阴极剥离 |
|---|---|---|
| 量纲 | 应力 MPa | 长度 mm + 时间 d |
| 断在哪里 | 最弱的那个面 | 只沿界面 |
| 驱动 | 机械载荷 | 电化学产碱 |
| 时间尺度 | 分钟 | 28–182 天 |
| 结果形态 | 一个数 | 一条曲线（r–t） |

第一行看着像细节，其实是全部问题所在：一个有量纲，一个有两个量纲，中间没有桥。

## 拉拔数字最容易被读错的地方

这里有个陷阱，比方向问题更常被忽略。

拉开之后，断口不一定在界面。可能断在钢和涂层之间，也可能断在涂层内部，还可能断在锭子和胶之间。三种情况，同一个 MPa 说的是三件事：

- **界面破坏**：这才是通常说的「附着力」
- **内聚破坏**：测的是涂层自身的拉伸强度，跟界面结合没关系
- **胶粘剂破坏**：这个数作废，得重做

一块附着力「很高」的板子，很可能是因为涂层本身偏脆、拉拔时先在自己内部裂开，界面根本没被考验到。数字漂亮，界面却可能已经在退了。

所以 ISO 4624 要求报告里标注破坏类型，以及各类型所占面积的百分比。只写「8.4 MPa，合格」的报告，缺的正是这一行——没有它，这个数无法解释。

## 所以该问哪一个

| 你真正想知道 | 该看什么 |
|---|---|
| 涂层粘得牢不牢（机械意义上） | 拉拔，且必须带破坏类型 |
| 浸渍 + 阴极保护条件下能撑多久 | 阴极剥离，且必须带条件与时长 |
| 服役中会不会突然整片掉下来 | 两个都不够，要看界面有没有机会被打断 |

第三行要看的是[涂层失效的四种模式](/notes/coating-failure-modes/)——剥离只是其中一种，而它最容易被一个漂亮的拉拔数字盖住。

## 一句话

拉拔量的是「粘得住吗」，阴极剥离量的是「能粘多久」。

垂直方向拉得下来，是附着力；沿界面退得出去，是耐碱性。方向差 90°，结论差一个维度，中间没有换算系数。

## English Summary

Both the pull-off test and cathodic disbondment start from an artificial defect, but they measure different things. Pull-off adhesion (ISO 4624 / ASTM D4541) loads the coating perpendicular to the interface and reports a stress in MPa. Cathodic disbondment (ISO 15711) drives a crack parallel to the interface under cathodic protection and reports a disbondment radius in mm after 28 to 182 days. The two directions differ by 90°, and so do the units: one stress value, the other length plus time. No conversion relates them. A result such as "8.4 MPa, acceptable" is hard to compare unless the failure mode is stated, because the same number can mean adhesion at the steel interface, cohesion failure inside the coating, or adhesive failure at the dolly. ISO 4624 requires the failure type and its area percentage in the report. Without that line, a high value may reflect a brittle coating that split before the interface was loaded. Define the question first: adhesion strength at this moment, or adhesion durability under immersion and cathodic protection. Then choose the method. A strong pull-off value does not predict resistance to slow disbondment.

---

本文只讨论公开标准与文献中的通用原理，不涉及任何具体工程项目的方案、选型与数据。
