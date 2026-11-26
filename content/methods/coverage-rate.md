---
title: "涂布率分母上的厚度，是干膜不是湿膜"
date: 2026-12-16
draft: false
description: "同一桶漆，有人算出 8.4 m²/L，有人算出 5.3。差别往往只是把湿膜厚度当成了干膜，或者把质量固含当成了体积固含。"
section_label: "方法库"
tags: ["基础计算", "涂装", "固体分"]
---

一桶体积固体分 63% 的涂料，要求干膜 75 μm。一个人算 8.4 m²/L，另一个人算 5.3 m²/L。两个人都没按错计算器——前者把 75 当干膜代入，后者先拿它除以固体分换算成湿膜，再代入同一个公式。

这类分歧不会在纸上分出对错。只有漆上墙、膜厚测出来，才知道谁的数对。

## 公式与单位

> **理论涂布率 S（m²/L）= 体积固体分(%) × 10 / 干膜厚度(μm)**

> **实际涂布率 = 理论涂布率 × (1 − 损耗率)**

> **湿膜厚度 = 干膜厚度 / (体积固体分 / 100)**

三个式子必须成套用。第一个给理想值，第二个把它拉回现场，第三个回答「施工时湿膜该刮多少」。

## 那个 10 不是经验系数

它是纯粹的单位换算：

- 1 L = 1000 cm³ = 10⁶ mm³
- 1 m² = 10⁶ mm²

所以体积固体分 100% 的涂料铺 1 μm 干膜，1 L 正好铺 1000 m²。代入实际固体分 VS%：

S = 1000 × (VS / 100) / DFT = 10 × VS / DFT

分母上的 DFT 是**干膜厚度**。如果拿湿膜厚度去除，等于把固体分重复扣了两次——这正是 8.4 变成 5.3 的原因（75 / 0.63 约 119，63 × 10 / 119 约 5.3）。

## 一道完整算例

已知：体积固体分 63%，规定干膜 75 μm，喷涂损耗 30%，施工面积 1000 m²。

| 步骤 | 计算 | 结果 |
|---|---|---|
| 理论涂布率 | 63 × 10 / 75 | 8.40 m²/L |
| 实际涂布率 | 8.40 × (1 − 0.30) | 5.88 m²/L |
| 对应湿膜厚度 | 75 / 0.63 | 119 μm |
| 该面积实际用量 | 1000 / 5.88 | 170 L |

注意损耗**不进湿膜换算**：湿膜是几何量，只跟干膜和固体分有关；损耗是施工量，只进用量估算。把 30% 损耗也塞进湿膜公式，是另一种常见错法。

## 怎么算：四步手算表

| 步骤 | 填入已知数 | 算什么 | 上式结果 |
|---|---|---|---|
| 1 | 体积固体分 VS%、规定干膜 DFT | `S = 10 × VS / DFT` | 8.40 m²/L |
| 2 | 损耗率 | `实际涂布率 = S × (1 − 损耗率)` | 5.88 m²/L |
| 3 | VS%、DFT | `湿膜 = DFT / (VS/100)` | 119 μm |
| 4 | 施工面积 | `用量 = 面积 / 实际涂布率` | 170 L |

**用法要点**：

1. 第 1 步的固体分必须是**体积**口径；规格书只给质量固含时，先按上一篇的方法换算。
2. 第 3 步校验：湿膜 × 体积固体分 = 干膜。119 × 0.63 ≈ 75，对得上才算没串口径。
3. 损耗只进第 2 步和第 4 步，**不进第 3 步**——这是最容易混的地方。
4. 第 2 步算出的损耗率是假设，不是事实。报用量时把它写出来，让读数的人知道来路。

## 坑一：质量固含不是体积固含

膜厚是几何量，体积固体分是体积口径。质量固体分是质量口径，两者只有在各组分密度相同时才相等——而颜料和树脂的密度往往差几倍。

| 口径 | 物理量 | 能直接用于膜厚与涂布率吗 |
|---|---|---|
| 质量固体分 | 不挥发分质量 / 涂料总质量 | 不能 |
| 体积固体分 | 不挥发分体积 / 涂料总体积 | 能 |

规格书上只给质量固含时，必须先按各组分密度换算成体积固含。跳过这一步，涂布率会系统性偏错。

## 坑二：损耗不是一个数

公开涂装资料给出的损耗常见区间是 25%–40%，粗糙表面或复杂结构可超过 50%。表面状态的影响是量级性的：

| 表面状态 | 底漆系数 | 中涂/面涂系数 |
|---|---|---|
| 新光面钢、酸洗钢 | 0.95 | 0.98 |
| 喷砂清理钢 | 0.90 | 0.95 |
| 动力工具清理 | 0.85 | 0.90 |
| 喷砂-轻微点蚀 | 0.85 | 0.90 |

（系数取自公开涂装计算资料的示例值，用于说明量级，不替代具体工况的实测。）

施工方法、构件形状、风速同样计入损耗。所以「损耗 30%」是一个假设，不是一个事实——报用量时要把它写出来，让读数的人知道这个数的来路。

## 口诀

> **十是单位换算，不是经验系数。分母永远问一句：干膜，还是湿膜。**

## English Summary

A coating with 63 percent volume solids at a 75 micrometre dry film gives a theoretical spreading rate of 8.4 square metres per litre. The same coating at 30 percent loss gives 5.9. Neither figure is a mystery; they answer different questions. The constant 10 in spreading rate = 10 x volume solids / dry film thickness is a unit conversion, not an empirical factor: one litre is one million cubic millimetres, one square metre is one million square millimetres, so a 100 percent solids coating lays one micrometre over 1000 square metres. Wet film is dry film divided by the volume solids fraction, so specifying 75 micrometres of wet film at 63 percent solids leaves only 47 micrometres dry. Two errors dominate. The first is substituting mass solids for volume solids in a geometric calculation; when pigment and resin differ several-fold in density, the gap reaches twenty percentage points. The second is treating loss as a fixed number. Published loss factors range from 25 to 40 percent and can exceed 50, driven by method, roughness and geometry. Keep the loss assumption visible next to the result, because the arithmetic cannot supply it.

---

本文只讨论公开文献与标准中的通用原理，不涉及任何具体工程项目的方案、选型与数据。
