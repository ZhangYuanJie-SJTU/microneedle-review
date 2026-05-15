# Figure Plan
## Wearable MNA Electrochemical Sensing Systems — Visual Narrative
### SCI-writer Stage 1 Output | Generated 2026-05-14

---

## Overview

| Figure | Title | Section | Type | Priority |
|--------|-------|---------|------|----------|
| Fig. 1 | Full-Chain System Architecture | §1.4 | Schematic | ★★★★★ |
| Fig. 2 | MNA Fabrication Materials and Processes | §2 | Comparison chart + SEM panels | ★★★★★ |
| Fig. 3 | Electrochemical Sensing Modalities | §3 | Multi-panel technical diagram | ★★★★★ |
| Fig. 4 | Biomarker Clinical Significance Map | §4 | Infographic + table | ★★★★ |
| Fig. 5 | Wearable Circuit Architecture | §5 | Block diagram + photos | ★★★★★ |
| Fig. 6 | Embedded Intelligence Pipeline | §6 | Flow diagram + performance curves | ★★★★ |
| Table 1 | MNA Sensor Performance Comparison | §3+4 | Quantitative comparison table | ★★★★★ |

---

## Fig. 1 — Full-Chain System Architecture (Graphical Abstract Quality)

**Section:** §1.4 Introduction
**Size:** 180 mm × 120 mm (two-column wide) | **Format:** PNG/PDF vector | **Resolution:** ≥300 DPI
**Style:** Clean schematic, no photograph backgrounds, consistent color palette (suggest: blue-to-orange gradient for the chain layers)
**B&B graphical abstract:** This figure should also serve as the 400×300 px graphical abstract (crop and simplify)

**Content layout (left to right, 5 layers):**

```
┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│   Layer 1   │ → │   Layer 2   │ → │   Layer 3   │ → │   Layer 4   │ → │   Layer 5   │
│  MNA Array  │   │ Electrochem │   │  Flexible   │   │   Embedded  │   │  Clinical   │
│ Fabrication │   │  Transducers│   │  Circuits   │   │    AI/MCU   │   │  Outcomes   │
│             │   │             │   │  + Wireless │   │   Terminal  │   │             │
│ • Silicon   │   │ • Amperom.  │   │ • AFE       │   │ • Signal    │   │ • Glucose   │
│ • Polymer   │   │ • Voltamm.  │   │ • BLE/NFC   │   │   process.  │   │ • Lactate   │
│ • Hydrogel  │   │ • EIS       │   │ • Power mgmt│   │ • ML calib. │   │ • Cortisol  │
│ • Carbon    │   │ • ISE/Poten.│   │ • Flex PCB  │   │ • Edge AI   │   │ • Ions      │
└─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘
```

**Key visual elements:**
1. Cross-section of skin showing MNA penetrating to ISF layer (epidermis ~100 μm, needles 300-600 μm)
2. Magnified needle tip showing enzyme/aptamer layer
3. ISF fluid extraction arrow
4. Miniaturized flexible patch illustration
5. Wireless transmission wave to smartphone
6. Cloud + health dashboard endpoint

**Caption:** "Fig. 1. Full-chain architecture of a wearable microneedle array-based electrochemical sensing system. The five engineering layers — (1) MNA fabrication, (2) electrochemical transduction, (3) signal conditioning and wireless transmission, (4) embedded intelligent processing, and (5) clinical output — are reviewed systematically in Sections 2–6, respectively."

**Source note:** Original figure. No permission required.
**Mermaid/SVG spec:** Generate as SVG schematic diagram with 5 colored boxes and connecting arrows. Use skin cross-section illustration in layer 1.

---

## Fig. 2 — MNA Fabrication Materials and Processes

**Section:** §2 (spans 2.1-2.4)
**Size:** 180 mm × 150 mm (two-column wide, tall) | **Format:** PNG composite | **Resolution:** ≥300 DPI
**Layout:** 3-row × 3-column panel grid + performance comparison bar chart

**Panel layout:**

```
Row 1 — Material categories (3 representative SEM/schematic images):
┌──────────────────┬──────────────────┬──────────────────┐
│ (a) Silicon MNA  │ (b) Polymer/PDMS │ (c) Hydrogel MNA │
│ DRIE-etched tips │ Molded array     │ Swelling tips    │
│ ~9500/cm² array  │ hollow geometry  │ core-shell struct│
└──────────────────┴──────────────────┴──────────────────┘

Row 2 — Fabrication process flowcharts (3 processes):
┌──────────────────┬──────────────────┬──────────────────┐
│ (d) Photolith+   │ (e) Micromolding │ (f) 3D Printing  │
│ DRIE process     │ process          │ DLP/SLA process  │
│ flow (5 steps)   │ flow (4 steps)   │ flow (4 steps)   │
└──────────────────┴──────────────────┴──────────────────┘

Row 3 — Tip functionalization + Performance comparison:
┌──────────────────┬───────────────────────────────────────┐
│ (g) Enzyme immo- │ (h) Sensitivity vs LOD comparison     │
│ bilization layer │ bar chart: 6 representative sensors   │
│ cross-section    │ grouped by fabrication method         │
└──────────────────┴───────────────────────────────────────┘
```

**Panels (a)-(c):** Adapt from published SEM images with permission, or generate schematic equivalents.
- Panel (a): Si MNA, ~9500 needles/cm² (based on Dervisevic 2021 [V])
- Panel (b): Hollow PDMS MNA array (based on Parrilla 2022 [V])
- Panel (c): Core-shell hydrogel structure (based on Zhou 2024 [V])

**Panel (h) performance chart — data points (all [V] verified):**
| Sensor | Sensitivity (μA mM⁻¹ cm⁻²) | LOD (μM) |
|--------|---------------------------|----------|
| Si MNA (Dervisevic 2021) | [from paper] | [from paper] |
| Hollow PDMS (Parrilla 2022) | [from paper] | [from paper] |
| Hydrogel (Zhou 2024) | [from paper] | [from paper] |
| 3D-printed (Reynoso 2024) | [from paper] | [from paper] |
*NOTE: Exact values must be extracted from papers at Gate B before finalizing this figure.*

**Caption:** "Fig. 2. Microneedle array fabrication technologies. (a-c) Representative material categories: silicon DRIE, polymer micromolding, and hydrogel core-shell structures. (d-f) Schematic fabrication workflows for the three dominant processes. (g) Enzyme immobilization layer cross-section showing Nafion/BSA-crosslinked GOx layer. (h) Sensitivity and LOD comparison across fabrication methods."

---

## Fig. 3 — Electrochemical Sensing Modalities

**Section:** §3
**Size:** 180 mm × 140 mm | **Format:** Vector + data plots | **Resolution:** ≥300 DPI
**Layout:** 2-row × 3-column technical diagram

```
Row 1 — Sensing mode schematics (3 panels):
┌──────────────────┬──────────────────┬──────────────────┐
│ (a) Amperometry  │ (b) DPV/SWV      │ (c) EIS          │
│ i-t curve at     │ voltammogram     │ Nyquist plot     │
│ constant E_appl  │ with peaks for   │ Randles cell     │
│ Cottrell eq.     │ glucose/UA/dop.  │ pre/post binding │
└──────────────────┴──────────────────┴──────────────────┘

Row 2 — More sensing modes + comparison:
┌──────────────────┬──────────────────┬──────────────────┐
│ (d) Potentiometry│ (e) FSCV         │ (f) Summary:     │
│ Nernst response  │ color plot for   │ Modality vs.     │
│ for K+/Na+/pH    │ dopamine trans.  │ analyte matrix   │
│ slope 59.2 mV/d  │ at 400 V/s       │ (radar chart)    │
└──────────────────┴──────────────────┴──────────────────┘
```

**Panel (f) radar chart axes:** LOD capability | Selectivity | Continuous measurement | Miniaturization ease | Wearable power requirement
- Amperometry: high continuous, medium LOD, medium power
- DPV/SWV: excellent LOD, good selectivity, high power
- EIS: excellent selectivity (aptasensor), poor continuous, medium power
- Potentiometry: good continuous, limited to ions, lowest power
- FSCV: excellent time resolution, highest power, limited selectivity

**Caption:** "Fig. 3. Electrochemical sensing modalities for MNA-based wearable sensors. (a) Amperometric i-t response following Cottrell kinetics. (b) Differential pulse voltammogram showing analyte peak resolution. (c) Nyquist plot comparing pre- and post-target binding impedance spectra. (d) Nernstian potentiometric response for K⁺ with 59.2 mV/decade slope. (e) FSCV color plot for dopamine subsecond detection. (f) Multi-axis comparison of modalities across key performance dimensions."

---

## Fig. 4 — Biomarker Clinical Significance Map

**Section:** §4
**Size:** 180 mm × 100 mm | **Format:** Infographic | **Resolution:** ≥300 DPI
**Layout:** Horizontal timeline + bubble chart

```
Layout: Human body silhouette (left) + biomarker panels (right)

Left: Stylized human body with ISF sampling site indicated
      Annotation arrows pointing to:
      - Brain (neurotransmitters: dopamine)
      - Blood vessel (compare: glucose, lactate)
      - Skin/ISF (MNA sampling site)
      - Kidney (uric acid, creatinine)

Right: Table/visual of biomarkers organized by section:
      ┌─────────────────────────────────────────────────────────┐
      │ Metabolic    │ Glucose (2.8-22.2 mM) / Lactate / UA     │
      │ Electrolytes │ Na+ / K+ / Ca2+ / pH                     │
      │ Stress/Immune│ Cortisol (5-25 ng/mL) / IL-6             │
      │ Neuro        │ Dopamine (0.01-1 μM)                     │
      │ Drug PK      │ Vancomycin / Levodopa / MTX              │
      └─────────────────────────────────────────────────────────┘
```

**Data annotation:** Each biomarker annotated with: ISF concentration range | Clinical alarm threshold | Detection method | Best reported LOD

**Caption:** "Fig. 4. Target biomarkers for MNA-based wearable electrochemical monitoring. Clinical ISF concentration ranges, alarm thresholds, and applicable detection modalities are indicated for each analyte category."

---

## Fig. 5 — Wearable Circuit Architecture and System Integration

**Section:** §5
**Size:** 180 mm × 130 mm | **Format:** Block diagram + photograph | **Resolution:** ≥300 DPI
**Layout:** 2-panel (block diagram left, representative photograph right)

```
Panel (a) — System block diagram:
┌─────────────────────────────────────────────────────┐
│                  MNA Patch                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────┐   │
│  │  WE1-N   │→ │  AFE     │→ │    MCU           │   │
│  │  CE, RE  │  │ 3-el.    │  │ ARM Cortex-M4    │   │
│  │ (MNA)    │  │ potentio.│  │ ADC 16-bit       │   │
│  └──────────┘  │ TIA gain │  │ Signal process.  │   │
│                │ MUX/ADC  │  │ ML inference     │   │
│                └──────────┘  └──────┬───────────┘   │
│                                     │               │
│  ┌──────────────────────────────────▼─────────────┐ │
│  │  Wireless Module: BLE 5.0 / NFC 13.56 MHz      │ │
│  └──────────────────────────────────┬─────────────┘ │
│                                     │               │
│  ┌─────────────────────────────────▼──────────────┐ │
│  │  Power: LiPo + PMIC + optional TENG/BFC        │ │
│  └────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────┘
          ↕ BLE / NFC ↕
┌────────────────────────┐     ┌──────────────┐
│ Smartphone App         │────▶│ Cloud/EHR    │
│ Real-time display      │     │ Data storage │
└────────────────────────┘     └──────────────┘

Panel (b) — Photograph placeholder:
Representative wearable MNA patch on wrist skin
(Source: Tehrani 2022 Nat Biomed Eng [V] — with permission; or generate schematic)
```

**Caption:** "Fig. 5. Wearable circuit architecture for MNA electrochemical sensing systems. (a) Complete system block diagram showing the signal path from MNA transducer through analog front-end, MCU, and wireless module to the cloud. (b) Representative photograph of a fully integrated wearable MNA patch (adapted from [Tehrani 2022 [V]] with permission)."

---

## Fig. 6 — Embedded Intelligence Pipeline

**Section:** §6
**Size:** 180 mm × 120 mm | **Format:** Flow diagram + performance curves | **Resolution:** ≥300 DPI
**Layout:** Top row flow diagram + bottom row performance benchmarks

```
Top row — Pipeline flow (left to right):
Raw signal → Noise filter → Drift correction → Calibration → Anomaly detection → Clinical alert
   ↑              (LMS)      (Kalman filter)   (ML-based)    (LSTM model)        (BLE push)
 motion
 artifact
 model

Bottom row — Performance benchmarks (3 panels):
┌──────────────────┬──────────────────┬──────────────────┐
│ (a) MARD vs.     │ (b) Prediction   │ (c) Power        │
│ wear day         │ accuracy vs.     │ consumption      │
│ (factory calib   │ model complexity │ breakdown        │
│  vs. ML-adapted) │ (logistic/LSTM/  │ (AFE/MCU/BLE/    │
│                  │ transformer)     │ sensor)          │
└──────────────────┴──────────────────┴──────────────────┘
```

**Panel (a) data:** MARD trending from Day 1 (~8%) to Day 7+ (factory: rises to ~15-20%; ML-adapted: stays <10%)
- Based on: Yang J 2023 ACS Sensors [V] (14-day, MARD 10.2%); Liu Y 2025 Adv Sci [V]

**Panel (b) data:** Prediction accuracy for hypoglycemia 30-min ahead
- Logistic regression: ~75% sensitivity; LSTM: ~85%; Transformer: ~88%
- Data: Fan P 2026 Nat Commun [V]

**Panel (c) power breakdown pie chart:**
- AFE (potentiostat): ~30%
- MCU (ARM Cortex): ~25%
- BLE module: ~35%
- Sensor/electrochemical: ~10%
- Target total: <10 mW

**Caption:** "Fig. 6. Embedded intelligence pipeline for wearable MNA sensor systems. The top panel illustrates the signal processing chain from raw electrochemical measurement to clinical alert generation. Bottom panels show: (a) MARD comparison between factory calibration and ML-adaptive calibration over wear duration; (b) hypoglycemia prediction accuracy as a function of model complexity; (c) system power consumption breakdown by component."

---

## Table 1 — MNA Sensor Performance Comparison

**Section:** §3 + §4 (spans both; placed at end of §4)
**Format:** Multi-column LaTeX table (booktabs style) | **Width:** Full page (both columns if double-column)
**Rows:** ~25-30 representative sensors from corpus

**Column structure:**

| Column | Content | Unit |
|--------|---------|------|
| Ref | [citation number] | — |
| Year | Publication year | — |
| MNA material | Si/Metal/Polymer/Hydrogel/3D-printed | — |
| Target analyte | Glucose/Lactate/UA/Cortisol/Na⁺/etc. | — |
| Detection method | Amperometry/DPV/EIS/ISE | — |
| Linear range | Min–Max | mM or μM |
| Sensitivity | Value | μA mM⁻¹ cm⁻² |
| LOD | Value | μM or ng/mL |
| Selectivity | Tested interferents | — |
| In vivo/Human | Y/N | — |
| Wear time | Duration | days |
| Wireless | BLE/NFC/None | — |

**Selected rows (all [V] from sub-agents — values to be filled at Gate B):**

| Ref | Year | Material | Analyte | Method | Linear range | LOD | In vivo |
|-----|------|----------|---------|--------|-------------|-----|---------|
| [Dervisevic 2021] | 2021 | Silicon | Glucose | Amp | [Gate B] | [Gate B] | Yes |
| [Heifler 2021] | 2021 | Si/Au | Glu+Lac+Ins | Amp | [Gate B] | [Gate B] | Yes |
| [Parrilla 2022] | 2022 | Hollow PDMS | Glucose | Amp | [Gate B] | [Gate B] | Partial |
| [García-Guzmán 2021] | 2021 | MNA | pH | ISE | pH 4-9 | 0.01 pH | Human |
| [Molinero-Fernández 2023] | 2023 | — | Multi-ion | ISE | [Gate B] | [Gate B] | In vivo |
| [Yang Y 2024] | 2024 | — | Glucose | Amp | [Gate B] | [Gate B] | Human |
| [Yang J 2023] | 2023 | — | Glucose | Amp | 2.2-22.2 mM | <0.5 mM | Human |
| [Bakhshandeh 2024] | 2024 | — | Glu+Lac | EIS | [Gate B] | [Gate B] | In vivo |
| [Li X 2025] | 2025 | — | 9-analyte | Multi | [Gate B] | [Gate B] | Yes |
| [Tehrani 2022] | 2022 | — | Glucose | Amp | [Gate B] | [Gate B] | Human |
| [Reynoso 2024] | 2024 | 3D-printed | Drug | Apt/EIS | [Gate B] | [Gate B] | In vivo |
| [Zhou 2024] | 2024 | Hydrogel | Glucose | Amp | [Gate B] | [Gate B] | In vivo |
| [Friedel 2023] | 2023 | — | Multi | Multi | [Gate B] | [Gate B] | Human |

**Note:** [Gate B] = exact values to be extracted from full text and verified at Gate B citation audit.

**Caption:** "Table 1. Performance comparison of representative MNA-based wearable electrochemical sensors (2021–2026). Sensitivity values normalized to electrode area. LOD calculated by 3σ/slope method (IUPAC). 'Human' denotes validated in clinical human subjects study."

---

## Production Notes

**Color scheme:**
- Layer 1 (Fabrication): Blue (#1f77b4)
- Layer 2 (Sensing): Orange (#ff7f0e)
- Layer 3 (Circuits): Green (#2ca02c)
- Layer 4 (Intelligence): Purple (#9467bd)
- Layer 5 (Clinical): Red (#d62728)
- Consistent across all figures

**Font:** Arial or Helvetica; minimum 8 pt in figures; axis labels 10 pt

**Generation method:**
- Figs. 1, 5, 6: SVG schematic via `scientific-visualization` skill or manual Mermaid/Inkscape
- Figs. 2, 3: Composite from (a) adapted SEM/published images + (b-h) generated schematic panels
- Fig. 4: Infographic — pure vector generation
- Table 1: LaTeX `booktabs` in `main.tex`

**Permission requirements:**
- All SEM images from published papers require written permission (Creative Commons CC-BY articles: free)
- Alternative: generate all figures as schematics (no permission needed)
- Preferred: original schematic figures throughout (eliminates permission delays)

---

*SCI-writer Stage 1 | figure_plan.md | 6 figures + 1 table specified*
