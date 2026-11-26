---
title: "质量比 4:1，不等于体积比 4:1"
date: 2026-12-23
draft: false
description: "双组分混合比跨口径换算只差一个密度倒数，但量杯读的是体积，说明书给的多半是质量。"
section_label: "方法库"
tags: ["基础计算", "施工", "换算"]
---

说明书要求树脂:固化剂 = 4:1（质量比），现场用量杯按 4:1 倒。配出来的膜偏软——不是料的问题，是口径的问题。

## 换算只做一件事

> **体积比 = (m_A / ρ_A) : (m_B / ρ_B)**

反过来：

> **质量比 = (V_A × ρ_A) : (V_B × ρ_B)**

一边除以密度，一边乘以密度，仅此而已。

## 一道完整算例

已知：质量比 4:1，树脂密度 1.15 g/cm³，固化剂密度 0.98 g/cm³。

| 组分 | 质量份 | 密度 (g/cm³) | 体积份 |
|---|---|---|---|
| 树脂 | 4 | 1.15 | 3.478 |
| 固化剂 | 1 | 0.98 | 1.020 |

体积比 = 3.478 : 1.020 ≈ **3.4 : 1**。

按质量配是 4:1，按体积配是 3.4:1。差了近 18%，足够让当量比偏出可接受区间。

## 怎么算：三步手算表

| 步骤 | 填入已知数 | 算什么 | 上式结果 |
|---|---|---|---|
| 1 | 质量比 m_A : m_B | 写成 4 : 1 | 4 : 1 |
| 2 | 两侧密度 ρ_A、ρ_B | `体积份 = 质量份 / 密度` | 3.478 : 1.020 |
| 3 | 上一步结果 | 同除以较小项，归一为 1 | 3.4 : 1 |

反向换算同理：把体积份乘以各自密度，再归一。

**用法要点**：

1. 密度要用**施工温度下**的实测值，不是规格书上的 25℃ 参考值。
2. 第 3 步归一时说明基准（按 B 组分为 1，还是按 A 组分为 1），否则 3.4:1 和 1:0.29 会被当成两个数。
3. 能称重就别量体积。质量比不受温度影响，这是它更可靠的原因。
4. 量杯刻度是体积。用质量比喂给体积计量设备，必须先换算；换算用的密度要写在记录旁边，便于事后复核。

## 四个坑

1. **密度随温度变。** 冷库里量出的体积比，不是施工温度下的体积比。
2. **固化剂吸水或含残溶。** 密度和有效活性物含量一起变，换算出来的体积比跟着偏。
3. **量杯刻度是体积。** 用质量比喂给体积计量设备，必须先换算。
4. **别把混合比和当量比混为一谈。** 当量比由前面两篇的方法算，混合比只是把那个结果按计量方式翻译一遍。

## 口诀

> **质量比除以密度，才是量杯读的数。能称重就别量体积。**

## English Summary

A 4:1 mix by mass is not a 4:1 mix by volume. The two ratios differ by the densities of the components. Convert mass to volume by dividing each part by its density: with a resin at 1.15 g/cm3 and a hardener at 0.98 g/cm3, a 4:1 mass ratio becomes roughly 3.4:1 by volume. The reverse conversion multiplies each volume by its density. This matters at the bench because measuring cups and meters read volume, while most data sheets specify mass. The error is not cosmetic. A wrong ratio shifts the equivalent balance, leaving unreacted resin or hardener and changing crosslink density, chemical resistance and film hardness. Two further cautions. Density is temperature dependent, so a volume ratio measured in a cold store is not the ratio at application temperature. Absorbed moisture or residual solvent in a component changes both its density and its effective active content. Where accuracy matters, weigh. Where weighing is impossible, state the densities used for the conversion next to the volume ratio so the number can be checked later.

---

本文只讨论公开文献与标准中的通用原理，不涉及任何具体工程项目的方案、选型与数据。
