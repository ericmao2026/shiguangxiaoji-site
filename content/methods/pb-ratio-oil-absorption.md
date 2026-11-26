---
title: "颜基比、吸油量，和那个体积口径的临界点"
date: 2026-12-30
draft: false
description: "颜基比是质量口径，CPVC 是体积口径。吸油量把两者连起来，但只是定性桥梁，不是换算公式。"
section_label: "方法库"
tags: ["基础计算", "配方", "颜料"]
---

三个数经常被混着用，它们其实在回答三个不同的问题。

## 三个定义

| 量 | 定义 | 口径 | 回答什么 |
|---|---|---|---|
| 颜基比 P/B | 颜料与填料质量 / 基料质量 | 质量 | 用量与遮盖力的粗调 |
| 吸油量 | 100 g 颜料调到连贯糊状所需的油质量 | g/100 g | 颜料需要多少树脂润湿 |
| CPVC | 树脂刚好填满颗粒间隙时的 PVC | 体积 | 膜是致密还是故意留孔 |

吸油量按公开的刮刀研磨法标准测定；具体数值以标准方法和实测为准，不用文献里的典型值替代。

## 它们怎么连

吸油量高，说明颜料比表面积大、表面粗糙，需要更多树脂才能包住。于是达到「刚好填满」所需的树脂更多，**CPVC 更低**。这是定性关系，不是可以直接代入的换算式——粒径分布、颗粒形状、树脂润湿能力都会插进来。

所以正确的用法是分工，不是互相替代：

- 想快速看颜料用量与遮盖力 → 看 P/B（质量口径，好算）
- 想预估树脂需求量 → 看吸油量
- 想判断膜是致密还是多孔 → 看 PVC 与 CPVC 的比值（**两者都是体积口径**）

## 最容易被算错的一步

体积口径的 PVC 是这么算的：

> **PVC = 颜料与填料体积 / (颜料与填料体积 + 基料不挥发分体积)**

每一项都要先除以各自密度，从质量份换成体积份。跳过这一步，拿质量份直接除，得到的不是 PVC。

> **CPVC 没有通用精算式。** 它由颜料的吸油量、粒径分布与颗粒形状共同决定，公开资料给出的是经验区间。任何声称能从 P/B 直接换算 CPVC 的做法都不可靠。

## 怎么算：四步手算表

| 步骤 | 填入已知数 | 算什么 | 说明 |
|---|---|---|---|
| 1 | 颜料、填料、基料质量份 | `P/B = (颜料+填料质量) / 基料质量` | 质量口径，只做粗调 |
| 2 | 各组分密度 | `体积份 = 质量份 / 密度` | 先转成体积口径 |
| 3 | 上一步的颜料填料体积、基料体积 | `PVC = V(颜料填料) / (V(颜料填料)+V(基料))` | 与 CPVC 同口径 |
| 4 | 实测或资料给出的 CPVC | 比较 PVC 与 CPVC | 小于则致密，接近或超过则多孔 |

**用法要点**：

1. 第 2 步是整张表的关键。P/B 与 CPVC 不在同一尺度，密度差几倍时尤其如此。
2. 第 4 步的 CPVC 必须用实测值或标注来源的经验值，不能从 P/B 推。
3. 吸油量只用来**预估树脂需求趋势**：吸油量高 → 基料需求大 → CPVC 低。它不参与 PVC 的数值计算。
4. 富锌底漆是刻意让 PVC 超过 CPVC 的例外，判断时不能套用常规底漆的「超过即缺陷」逻辑。

## 最常见的错

拿质量口径的 P/B 去和体积口径的 CPVC 比较。密度差几倍时，这两个数根本不在一个尺度上——这一点在富锌底漆那篇里已经用具体数字拆过。

## 口诀

> **颜基比管钱，吸油量管润湿，CPVC 管孔隙。质量和体积别串门。**

## English Summary

Pigment-to-binder ratio and oil absorption are two old-fashioned numbers that still constrain a formulation before any testing starts. The first is a mass ratio: pigment and extender mass divided by non-volatile binder mass. It moves with cost, hiding power and rheology, but because it is a mass ratio it says nothing about whether the particles touch. Critical pigment volume concentration does, and that is a volume concept. Oil absorption is the mass of oil needed to bring 100 grams of pigment to a coherent paste, measured by a standard spatula rub-out method. A high value means a large pigment surface and a higher binder demand, so the critical volume concentration tends to be lower. The relationship is qualitative; it is not a substitute for measurement. To get PVC, divide each component's mass by its density first, then take the volume fraction of pigment and extender among non-volatile solids. Compare that number with a measured or sourced CPVC only. There is no general formula that converts a mass-based pigment-to-binder ratio into a critical volume concentration. Mixing a mass ratio with a volume threshold is the most common way to misread a formulation.

---

本文只讨论公开文献与标准中的通用原理，不涉及任何具体工程项目的方案、选型与数据。
