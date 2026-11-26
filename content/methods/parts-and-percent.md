---
title: "份数与百分比，是同一张表的两种读法"
date: 2027-01-06
draft: false
description: "份数换算成百分比只是除以总和，放大到批量时乘回去即可。真正麻烦的是基数没写清。"
section_label: "方法库"
tags: ["基础计算", "配方", "份数"]
---

这一步没有化学，只有算术。但这里的错会一路传到当量比和固含量，而且很难回头发现。

## 两种读法

> **质量% = 该组分份数 / 总份数 × 100%**

> **放大到批量 M 时，该组分用量 = M × 质量%**

## 一道完整算例

配方（质量份）：树脂 100、固化剂 25、颜料 40、溶剂 35、助剂 2。总份数 202。

| 组分 | 份数 | 质量% | 配 500 kg 时用量 |
|---|---|---|---|
| 树脂 | 100 | 49.5% | 247.5 kg |
| 固化剂 | 25 | 12.4% | 61.9 kg |
| 颜料 | 40 | 19.8% | 99.0 kg |
| 溶剂 | 35 | 17.3% | 86.6 kg |
| 助剂 | 2 | 1.0% | 5.0 kg |

两项合计的尾数来自四舍五入，不影响配料。

## 怎么算：四步手算表

| 步骤 | 填入已知数 | 算什么 | 上式结果 |
|---|---|---|---|
| 1 | 各组分质量份 | `总份数 = 各项相加` | 202 |
| 2 | 每项份数、总份数 | `质量% = 份数 / 总份数 × 100` | 见上表 |
| 3 | 目标批量 M | `用量 = M × 质量%` | 见上表 |
| 4 | 第 3 步各项用量 | 合计核对 | 500 kg |

**用法要点**：

1. 第 2 步保留一位小数即可；尾数不闭合是四舍五入造成的，不要反向去凑总数。
2. 第 3 步的目标批量必须是**投料总质量**。若批量指的是不挥发分质量，先按固含量换算。
3. 第 4 步的合计核对不能省——份数表抄错一行，后面所有计算都跟着错。
4. 表里要写清每一项是「投料质量」还是「不挥发分质量」。只记份数、不记基数的配方文件，无法复现批次。

## 口诀

> **份数除总和得百分比，批量乘回去得用量。基数不写，等于没记。**

## English Summary

A formulation expressed in parts by mass and the same formulation expressed in percentages are the same table read two ways. To convert, sum all parts and divide each part by the total. To scale, multiply each percentage by the target batch mass. Nothing here is chemistry, yet mistakes at this step propagate through every later calculation, including equivalent ratios and solids content. The discipline that matters is stating the basis: a part may refer to supplied mass or to non-volatile mass, and the two are not interchangeable. Keep the basis visible in the table, check that the scaled components add back to the target batch, and accept small closing differences from rounding rather than forcing the numbers to fit. A formulation file that records parts without recording the basis has lost the information needed to reproduce the batch.

---

本文只讨论公开文献与标准中的通用原理，不涉及任何具体工程项目的方案、选型与数据。
