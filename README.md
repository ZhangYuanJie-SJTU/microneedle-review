# 基于微针阵列的可穿戴电化学传感系统综述

**期刊投稿** | Biosensors and Bioelectronics（Elsevier）| ISSN 0956-5663

---

## 论文信息

| 项目 | 内容 |
|------|------|
| **标题** | Wearable Electrochemical Sensing Systems Based on Microneedle Arrays: A Full-Chain Review from Sensor Fabrication to Intelligent Embedded Terminals |
| **中文标题** | 基于微针阵列的可穿戴电化学传感系统：从传感器制备到智能嵌入式终端的全链路综述 |
| **作者** | 张元杰、王侃 |
| **通讯作者** | 王侃（wangkan@sjtu.edu.cn） |
| **单位** | 上海交通大学 自动化与传感科学与工程学院 |
| **目标期刊** | *Biosensors and Bioelectronics*（中科院一区，IF > 10） |
| **投稿状态** | 准备中 |

---

## 摘要

微针阵列（MNA）基可穿戴电化学传感系统是连接非侵入性汗液传感器与植入式器件之间的关键平台，可通过皮下组织间液（ISF）实现无痛、持续的生化指标监测。

本综述系统梳理了 **2021—2026 年**共 **91 篇**相关文献，围绕五个相互依赖的工程层次展开：

1. **微针制备工艺** — 硅深反应离子蚀刻（DRIE）、聚合物微模塑、水凝胶溶胀阵列、3D 打印
2. **电化学传感模态** — 电流法、差分脉冲伏安法（DPV）、电化学阻抗谱（EIS）、电位型离子选择电极
3. **目标生物标志物** — 代谢物（葡萄糖、乳酸、尿酸）、离子（Na⁺、K⁺、Ca²⁺）、激素（皮质醇）及药代动力学指标
4. **可穿戴电路集成** — 模拟前端恒电位仪、柔性印刷电路板、无线通信（BLE 5.0、NFC）
5. **嵌入式智能终端** — 片上信号处理、机器学习自适应校准、边缘 AI 推理、闭环治疗反馈

---

## 仓库结构

```
microneedle-review/
├── main.tex                  # 主文档（elsarticle review 格式）
├── references.bib            # 参考文献数据库（91 篇）
├── elsarticle.cls            # Elsevier 文档类
├── elsarticle-num.bst        # 编号引用样式
├── fig_01_system_chain.png   # 图1：系统全链路框架
├── fig_02_fabrication.png    # 图2：微针制备工艺对比
├── fig_03_modality_radar.png # 图3：传感模态雷达图
├── fig_04_biomarkers.png     # 图4：生物标志物概览
├── fig_05_circuits.png       # 图5：可穿戴电路架构
├── fig_06_intelligence.png   # 图6：嵌入式智能流程
├── graphical_abstract.png    # 图形摘要
└── highlights.txt            # 投稿亮点（5 条）
```

---

## 本地编译

### 前提条件

- TeX Live 2022+ 或 MiKTeX（含 `mhchem`、`siunitx`、`microtype` 宏包）
- 或直接在 [Overleaf](https://www.overleaf.com) 上传本项目 ZIP 编译

### 编译命令

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

### Overleaf 上传

1. 下载本仓库为 ZIP（Code → Download ZIP）
2. Overleaf → New Project → Upload Project
3. 编译器选 **pdfLaTeX**，主文档选 `main.tex`
4. 点击 **Recompile from scratch** 确保参考文献正确生成

---

## 核心创新点

- 首个将微针尖端化学 → 电化学信号转导 → 柔性电路集成 → 嵌入式智能终端纳入**统一工程框架**的综述
- 定量分析 MNA-WES 与商业 CGM 系统（Dexcom G7、Abbott FreeStyle Libre 2）的 MARD 差距
- 梳理从 2022 年 MARD > 15% 到 2023 年 10.2% 的技术演进路线
- 提出 AFE 功耗（< 10 mW 系统目标）对片上 ML 模型复杂度的硬约束
- 覆盖闭环人工胰腺、运动员实时乳酸监测、帕金森症药物管理等前沿临床应用

---

## 作者信息

**张元杰**
- 上海交通大学 自动化与传感科学与工程学院 硕士研究生
- ORCID：[0009-0001-0705-7793](https://orcid.org/0009-0001-0705-7793)
- Email：Zhangyuanjie_SJTU@163.com

**王侃**（通讯作者）
- 上海交通大学 自动化与传感科学与工程学院 副教授
- Email：wangkan@sjtu.edu.cn

---

## 引用格式

论文接受后将更新正式引用信息。预引用格式（APA）：

> Zhang, Y., & Wang, K. (2026). Wearable electrochemical sensing systems based on microneedle arrays: A full-chain review from sensor fabrication to intelligent embedded terminals. *Biosensors and Bioelectronics*.

---

## 许可证

本仓库仅存储投稿前 LaTeX 源文件，版权归作者所有。论文发表后请以期刊版本为准。
