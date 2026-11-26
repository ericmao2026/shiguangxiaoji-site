---
title: "NCO 和 OH 不是按公斤配，是按当量数配"
date: 2026-12-02
draft: false
description: "NCO 当量 = 4200 / NCO%，羟当量 = 56100 / 羟值。水也要算进 OH 当量——它是反应物，不是杂质。"
section_label: "方法库"
tags: ["基础计算", "聚氨酯", "当量"]
---

一桶固化剂标着 NCO 33.6%，一桶树脂标着羟值 490。按重量凑到一起，反应不会刚好用完。原因和环氧那篇一样：**一个 NCO 基消耗一个 OH 基，配平的是摩尔数，不是公斤数。**

## 四个数怎么来

| 量 | 定义 | 单位 | 换算式 |
|---|---|---|---|
| NCO 含量 | 异氰酸酯基的质量分数 | % | 由滴定给出 |
| NCO 当量 | 含 1 mol NCO 的异氰酸酯质量 | g/eq | `4200 / NCO%` |
| 羟值 | 1 g 样品中羟基相当的 KOH 毫克数 | mg KOH/g | 由滴定给出 |
| 羟当量 | 含 1 mol OH 的多元醇质量 | g/eq | `56100 / 羟值` |

`4200` 来自 NCO 基的摩尔质量 42 g/mol 乘以 100（把质量分数改成百分数口径）。`56100` 是 KOH 的 56.1 g/mol 乘以 1000 mg/g。

还有一个最容易被漏掉的反应物：**水**。水的羟当量是 **9 g/eq**（分子量 18，一个水分子两个活泼氢），它消耗 NCO 并放出 CO₂。

## 用量怎么算

> **Index = NCO 当量数 / OH 当量数**

> **异氰酸酯用量 = Index × NCO 当量 × Σ(各组分质量 / 该组分当量)**

注意求和号里包含水：`水质量 / 9`。

## 一道完整算例

来自公开技术公报的示例配方（质量份）：

| 组分 | 质量份 | 当量 (g/eq) | 当量数 |
|---|---|---|---|
| 多元醇 A（羟值 490） | 100 | 56100 / 490 = 114.5 | 0.873 |
| 1,4-丁二醇 | 20 | 45 | 0.444 |
| 水 | 0.15 | 9 | 0.017 |

目标 Index = 1.05；异氰酸酯 NCO% = 33.6，故 NCO 当量 = 4200 / 33.6 = 125 g/eq。

异氰酸酯用量 = 1.05 × 125 × (0.873 + 0.444 + 0.017) = **175 份**。

## 怎么算：五步手算表

| 步骤 | 填入已知数 | 算什么 | 上式结果 |
|---|---|---|---|
| 1 | NCO% | `NCO 当量 = 4200 / NCO%` | 125 g/eq |
| 2 | 羟值 | `羟当量 = 56100 / 羟值` | 114.5 g/eq |
| 3 | 每个含 OH 组分的质量与当量 | `当量数 = 质量 / 当量`，再求和（含水） | 1.334 |
| 4 | 目标 Index | `Index × NCO 当量 × 总 OH 当量数` | 175 份 |
| 5 | 实测 NCO% | 用实测值重算第 1 步，与标称值比对 | — |

**用法要点**：

1. 第 3 步的求和号里**必须列水**：`水质量 / 9`。漏掉水，NCO 会少算，膜里却会发泡。
2. 水的当量是 9，不是 18——一个水分子带两个活泼氢。
3. 第 5 步不能省：NCO% 随储存下降，标称值只够初算。桶开了多久要写进记录。
4. Index 不是「多一点无所谓」。偏高，残余 NCO 遇湿气继续反应；偏低，交联不足、膜偏软。

## 口诀

> **四二除 NCO，五六除羟值。水有九个当量，别把它漏掉。**

## English Summary

One NCO group reacts with one OH group, so a two-component coating is balanced by equivalents, not by kilograms. The isocyanate equivalent weight is 4200 divided by the NCO weight percent, where 42 is the molar mass of the NCO group. A polyol's equivalent weight is 56100 divided by its hydroxyl value in mg KOH per g. Water must be counted as a reactant: it has an equivalent weight of 9 and consumes NCO while releasing carbon dioxide. The isocyanate index is the ratio of NCO equivalents to OH equivalents, and the required isocyanate mass is the index times its equivalent weight times the sum of each component's mass divided by its equivalent weight. A published technical example uses a polyol of hydroxyl value 490, 20 parts of 1,4-butanediol and 0.15 parts of water; at index 1.05 with a 33.6 percent NCO isocyanate, the calculated demand is 175 parts. Two cautions matter. The NCO content of a drum falls with age, so a measured value beats the label. Water is not an impurity to ignore in this arithmetic; it is a reactant that changes both the ratio and the film.

---

本文只讨论公开文献与标准中的通用原理，不涉及任何具体工程项目的方案、选型与数据。
