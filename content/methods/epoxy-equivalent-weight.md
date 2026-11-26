---
title: "配比不是按重量相加，是两边当量数相等"
date: 2026-11-26
draft: false
description: "环氧值、胺值、活泼氢当量——三个数决定固化剂用量。把胺值当活泼氢，是配比算错一倍的最常见来源。"
section_label: "方法库"
tags: ["基础计算", "环氧", "当量"]
---

同一桶环氧树脂、同一桶胺固化剂，两个人各算一遍用量。一个算出 103 份固化剂，另一个算出 51 份。计算器都没按错——差在一个人把胺值直接当成了活泼氢当量。

这类错误不会立刻暴露。混合比错了，固化照样发生，只是交联密度偏了：轻则膜软、耐化学品性下降，重则发脆、开裂。等性能出问题，很少有人回头怀疑第一步的算术。

## 先说结论：等的是当量数，不是质量

环氧—胺固化的反应式很简单：**一个环氧基消耗一个活泼氢**。所以配比要相等的是两边的**摩尔数**，不是公斤数。

把摩尔数换算成可称量的质量，就得到「当量」：含 1 mol 反应基团的物质质量（g/eq）。两边当量数相等，配比才成立。

## 三个数从哪来

| 量 | 符号 | 定义 | 单位 | 换算式 |
|---|---|---|---|---|
| 环氧值 | EV | 每 100 g 树脂中环氧基的物质的量 | mol/100 g | 由供应商给出 |
| 环氧当量 | EEW | 含 1 mol 环氧基的树脂质量 | g/eq | `100 / EV` |
| 胺值 | AV | 中和 1 g 固化剂中碱性氮所需 KOH 的毫克数 | mg KOH/g | 由滴定给出 |
| 活泼氢当量 | AHEW | 含 1 mol 活泼氢的固化剂质量 | g/eq | `56100 / (AV × fn)` |

`100` 来自环氧值的定义口径：每 100 g 树脂。`56100` 是 KOH 的摩尔质量 56.1 g/mol 乘以 1000 mg/g——胺值以 mg KOH 计，换算成当量必须带上这个 1000。

`fn` 是胺型修正系数，下一节专门讲它。

## 用量怎么算

以 100 份树脂为基准：

> **PHR = AHEW / EEW × 100**

如果两组分都含溶剂，不能直接拿这个数去配料。先把各自稀释到实际固含量，再取比值：

> **溶液基 PHR = 纯树脂基 PHR × (树脂固含量 / 固化剂固含量)**

两个固含量都用百分数数值代入，比值不变。

## 一道完整算例

已知：环氧值 0.44 mol/100 g；胺值 240 mg KOH/g；固化剂为乙二胺型，fn = 2；两组分均为 100% 固含。

| 步骤 | 计算 | 结果 |
|---|---|---|
| 环氧当量 EEW | 100 / 0.44 | 227.3 g/eq |
| 活泼氢当量 AHEW | 56100 / (240 × 2) | 116.9 g/eq |
| 纯树脂基 PHR | 116.9 / 227.3 × 100 | 51.4 份 |

如果把 fn 漏掉、直接按 56100 / 240 = 233.75 g/eq 计算，PHR 变成 102.85 份（约 103 份）。**正好翻倍**——这就是开头那两个人的差别。

再加一层：若树脂固含量 70%、固化剂固含量 60%，则溶液基 PHR = 51.4 × 70 / 60 = 60.0 份（每 100 份树脂溶液配 60.0 份固化剂溶液）。

## 怎么算：四步手算表

不用专门工具，纸笔或任意电子表格按行填即可。

| 步骤 | 填入已知数 | 算什么 | 上式结果 |
|---|---|---|---|
| 1 | 环氧值 EV | `EEW = 100 / EV` | 227.3 g/eq |
| 2 | 胺值 AV、胺型 fn | `AHEW = 56100 / (AV × fn)` | 116.9 g/eq |
| 3 | 前两步的 EEW、AHEW | `PHR = AHEW / EEW × 100` | 51.4 份 |
| 4 | 树脂固含、固化剂固含 | `溶液基 PHR = PHR × 树脂固含 / 固化剂固含` | 60.0 份 |

**用法要点**：

1. 第 2 步的 `fn` 必须先按胺型定下来，不能空着直接算。
2. 第 3 步得出的是**纯树脂基**，两组分有溶剂时必须走第 4 步。
3. 固含量用百分数数值代入（70 而不是 0.70），取的是比值，结果不变。
4. 算完回头核对：伯胺体系若 AHEW 接近 `56100 / AV`，说明 fn 漏乘了，结果会翻倍。

## 那个最贵的坑：胺值不是活泼氢当量

胺值是酸碱滴定的结果，它数的是**碱性氮**，不是活泼氢。两者不是一回事：

| 胺型 | 每个氮带的活泼氢 | fn | 说明 |
|---|---|---|---|
| 伯胺（-NH2） | 2 | 2 | 一个氮上两个氢都能反应 |
| 仲胺（-NH-） | 1 | 1 | 只剩一个氢 |
| 多亚乙基多胺型聚酰胺 | 介于 1 与 2 之间 | 经验值 | 乙二胺型 2、二亚乙基三胺型约 1.5、三亚乙基四胺型约 1.34 |

所以 `56100 / 胺值` 给出的是「每摩尔碱性氮对应的固化剂质量」。要得到活泼氢当量，必须按胺型除以 fn。直接把胺值当活泼氢当量，等于默认「每个氮只带一个氢」——对伯胺体系就会高估一倍。

上表的 fn 取值来自公开技术资料中的多亚乙基多胺经验系数，**不是普适常数**。需要说明的是，按分子结构逐氮计数得到的值与上表经验值可能不同（例如二亚乙基三胺按结构为 5/3≈1.67、三亚乙基四胺为 6/4=1.5）——这是我根据分子结构做的推断，未逐一核对原始资料口径，差异可能与聚酰胺化后氮形态变化有关。改性胺、酮亚胺、曼尼期碱各有自己的算法，不能用这张表硬套。厂商给出的活泼氢当量数据优先于任何估算。

## 口诀

> **当量对当量，不看公斤看摩尔。胺值数的是氮，活泼氢要另算。**

## English Summary

Two people can calculate the same epoxy formulation from the same two drums and get 103 parts of hardener or 51. The gap is not arithmetic; it is the definition of an equivalent. One epoxy group consumes one active hydrogen, so the ratio must balance moles, not kilograms. Epoxies are specified by epoxy value in mol per 100 g, giving an epoxy equivalent weight of 100 divided by that value. Amine hardeners are specified by amine value in mg KOH per g, titrated per basic nitrogen, not per active hydrogen. The amine hydrogen equivalent weight is 56100 divided by (amine value x fn), where 56100 is 56.1 g/mol expressed in milligrams. A primary diamine carries two active hydrogens per nitrogen and takes fn = 2; a secondary amine takes fn = 1. Omit fn for a primary diamine and the calculated hardener doubles. Solvents add a second basis change: divide each equivalent weight by its own non-volatile fraction before taking the ratio. Published fn values for polyethyleneamine polyamides are empirical, not universal; a supplier's stated active hydrogen equivalent wins. Keep all four inputs visible in the working table, and check that the arithmetic is not being asked to verify cure.

---

本文只讨论公开文献与标准中的通用原理，不涉及任何具体工程项目的方案、选型与数据。
