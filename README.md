# 基于微针阵列的可穿戴电化学传感系统：全链路综述

> **Wearable Electrochemical Sensing Systems Based on Microneedle Arrays: A Full-Chain Review from Sensor Fabrication to Intelligent Embedded Terminals**

[![Journal](https://img.shields.io/badge/Journal-Biosensors%20%26%20Bioelectronics-blue)](https://www.sciencedirect.com/journal/biosensors-and-bioelectronics)
[![LaTeX](https://img.shields.io/badge/LaTeX-elsarticle-green)](https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions)
[![Coverage](https://img.shields.io/badge/Coverage-91%20Papers-brightgreen)]()
[![Affiliation](https://img.shields.io/badge/Affiliation-SJTU-blue)](https://www.sjtu.edu.cn)

---

## 论文概览

| 项目 | 内容 |
|------|------|
| **标题** | Wearable Electrochemical Sensing Systems Based on Microneedle Arrays: A Full-Chain Review from Sensor Fabrication to Intelligent Embedded Terminals |
| **作者** | 张元杰, 王侃 |
| **单位** | 上海交通大学 自动化与传感科学与工程学院 |
| **目标期刊** | *Biosensors and Bioelectronics* (中科院一区, IF > 10) |
| **覆盖文献** | 91 篇 (2021-2026) |

---

## 研究内容

本综述首次将微针传感系统的完整技术链路纳入统一工程框架，围绕五个相互依赖的层次展开：

```
微针制备 → 电化学传感 → 生物标志物识别 → 电路集成 → 嵌入式智能
  DRIE        DPV/EIS       代谢物/离子      AFE/PWB      边缘AI推理
  微模塑       电流法        激素/药代       BLE/NFC      闭环反馈
  水凝胶       电位型
  3D打印
```

### 核心贡献

- **全链路框架** — 从传感器制备到智能终端的系统性工程综述
- **定量对比** — MNA-WES 与商业 CGM (Dexcom G7, FreeStyle Libre 2) 的 MARD 差距分析
- **技术演进** — 2022 年 MARD >15% → 2023 年 10.2% 的改进路线
- **功耗约束** — AFE <10 mW 对片上 ML 模型复杂度的硬约束分析
- **临床应用** — 闭环人工胰腺、运动员乳酸监测、帕金森药物管理

---

## 快速开始

### 在线阅读

- [PDF 全文](./paper.pdf)
- [Overleaf 上传包](./overleaf_upload.zip)

### 本地编译

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

### Overleaf 编译

1. 下载 [overleaf_upload.zip](./overleaf_upload.zip)
2. Overleaf → New Project → Upload Project
3. 编译器选 **pdfLaTeX**，主文档选 `main.tex`

---

## 仓库结构

```
microneedle-review/
├── main.tex                    # 主文档 (elsarticle review 格式)
├── paper.pdf                   # 编译后 PDF 全文
├── references.bib              # 参考文献数据库 (91 篇)
├── overleaf_upload.zip         # Overleaf 一键上传包
├── elsarticle.cls              # Elsevier 文档类
├── elsarticle-num.bst          # 编号引用样式
├── graphical_abstract.png      # 图形摘要
├── fig_01_system_chain.png     # 图1: 系统全链路框架
├── fig_02_fabrication.png      # 图2: 微针制备工艺对比
├── fig_03_modality_radar.png   # 图3: 传感模态雷达图
├── fig_04_biomarkers.png       # 图4: 生物标志物概览
├── fig_05_circuits.png         # 图5: 可穿戴电路架构
├── fig_06_intelligence.png     # 图6: 嵌入式智能流程
├── fig5_circuit_tikz.tex       # 电路图 TikZ 源码
├── highlights.txt              # 投稿亮点 (5 条)
├── cover_letter.md             # 投稿信
├── submission_checklist.md     # 投稿检查清单
├── literature_matrix.csv       # 文献矩阵
├── generate_figures.py         # 图表生成脚本
├── bib_audit.py                # 参考文献审计
├── diagnose.py                 # LaTeX 诊断工具
├── paper_outline.md            # 论文大纲
├── review_gap_analysis.md      # 综述缺口分析
├── review_report.md            # 审稿报告
├── revision_log.md             # 修订日志
├── figure_plan.md              # 图表规划
└── gate_c_checklist.md         # 质量门检查
```

---

## 作者

| | 姓名 | 单位 | 联系方式 |
|---|---|---|---|
| **第一作者** | 张元杰 | 上海交通大学 自动化与传感科学与工程学院 硕士生 | [ORCID](https://orcid.org/0009-0001-0705-7793) |
| **通讯作者** | 王侃 | 上海交通大学 自动化与传感科学与工程学院 副教授 | wangkan@sjtu.edu.cn |

---

## 引用

```bibtex
@article{zhang2026microneedle,
  title   = {Wearable Electrochemical Sensing Systems Based on Microneedle Arrays:
             A Full-Chain Review from Sensor Fabrication to Intelligent Embedded Terminals},
  author  = {Zhang, Yuanjie and Wang, Kan},
  journal = {Biosensors and Bioelectronics},
  year    = {2026}
}
```

---

## 许可证

本仓库存储投稿前 LaTeX 源文件，版权归作者所有。论文发表后请以期刊版本为准。
