---
title: "固含量有两个，膜厚只认体积那个"
date: 2026-12-09
draft: false
description: "质量固含与体积固含不是同一个数。密度差几倍时，两者能差十几个点，而膜厚与涂布率只能用体积口径。"
section_label: "方法库"
tags: ["基础计算", "固体分", "换算"]
---

规格书上写「固含 70%」，没说是哪种。如果拿这个数去算涂布率，很可能从一开始就错了。

## 两个定义

> **质量固含 = 不挥发分质量 / 涂料总质量 × 100%**

> **体积固含 = 不挥发分体积 / 涂料总体积 × 100%**

膜厚、涂布率、湿膜换算都是几何量，只能用**体积固含**。

## 换算怎么走

取 1 g 涂料，把质量和体积分开：

> 不挥发分体积 = 质量固含 / 不挥发分平均密度
> 溶剂体积 = (1 − 质量固含) / 溶剂密度
> **体积固含 = 不挥发分体积 / (不挥发分体积 + 溶剂体积)**

不挥发分平均密度本身也不是一个独立测出来的数，它由各组分密度按质量加权调和平均：

> **1 / ρ(不挥发分) = Σ w_i / ρ_i**（w_i 为各组分在不挥发分中的质量分数）

## 一道完整算例

已知：质量固含 70%，不挥发分平均密度 1.4 g/cm³，溶剂密度 0.9 g/cm³。

| 步骤 | 计算 | 结果 |
|---|---|---|
| 不挥发分体积 | 0.70 / 1.4 | 0.500 cm³ |
| 溶剂体积 | 0.30 / 0.9 | 0.333 cm³ |
| 体积固含 | 0.500 / (0.500 + 0.333) | 约 60% |

质量固含 70%，体积固含只有 60%。这 10 个点直接传导到涂布率和湿膜设定。

## 怎么算：四步手算表

以 1 g 涂料为基准，逐行填：

| 步骤 | 填入已知数 | 算什么 | 上式结果 |
|---|---|---|---|
| 1 | 各组分质量分数 w_i、密度 ρ_i | `1 / ρ(不挥发分) = Σ w_i / ρ_i` | 1.4 g/cm³ |
| 2 | 质量固含、ρ(不挥发分) | `不挥发分体积 = 质量固含 / ρ` | 0.500 cm³ |
| 3 | 溶剂密度 | `溶剂体积 = (1 − 质量固含) / ρ溶剂` | 0.333 cm³ |
| 4 | 前两步结果 | `体积固含 = 上一步体积 / 两步体积之和` | 约 60% |

**用法要点**：

1. 第 1 步的调和平均要逐个组分算，不能用「颜料密度 ≈ 4」「树脂密度 ≈ 1」这类印象值凑。
2. 混合溶剂同样要按体积加和。两种溶剂混合体积不一定严格可加，工程上近似可接受，但要在记录里注明是近似。
3. 只有质量固含、密度表又不全时，别自己猜密度——直接向供应商要实测体积固含。
4. 换算结果要写回规格书旁边，避免下一个人又拿 70% 去算膜厚。

## 三个坑

1. **一个「平均密度」救不了你。** 颜料、树脂、填料密度差几倍，调和平均要求逐个组分的数据。
2. **溶剂混合也要按体积加和。** 近似可接受，但要知道这是近似。
3. **数据只有质量固含时，别自己猜密度。** 向供应商要实测体积固含，或按完整密度表换算。

## 口诀

> **质量称出来，体积量出来。膜厚是几何，只认体积。**

## English Summary

Mass solids and volume solids answer different questions, and only volume solids can be used in a film thickness calculation. Mass solids is the non-volatile mass divided by the total coating mass. Volume solids is the non-volatile volume divided by the total volume. Because pigment and resin are usually several times denser than solvent, the two numbers are not close: a coating at 70 percent mass solids with a 1.4 g/cm3 non-volatile average and a 0.9 g/cm3 solvent works out to about 60 percent by volume. The conversion runs through density. Take one gram of coating, divide the non-volatile mass by the non-volatile average density and the solvent mass by the solvent density, then take the ratio. The non-volatile average density is itself the mass-weighted harmonic mean of the individual pigment and resin densities. This is why a single assumed density cannot recover volume solids reliably. When a data sheet gives only mass solids, request the measured volume solids or calculate it from a full density breakdown. Guesswork here propagates directly into spreading rate, wet film setting and consumption estimates. Keep every density input visible in the working table so the assumption can be checked later.

---

本文只讨论公开文献与标准中的通用原理，不涉及任何具体工程项目的方案、选型与数据。
