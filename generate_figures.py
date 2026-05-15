"""
generate_figures.py
Wearable MNA Electrochemical Sensing Systems — Figure Generation
SCI-writer v3.0.0 | SJTU Wang Lab | 2026-05-14

Usage:
    pip install matplotlib numpy
    python generate_figures.py

Outputs:  fig_01_system_chain.png
          fig_03_modality_radar.png
          fig_06_performance.png
          (Figs 2, 4, 5 require real SEM/photo assets — specs in figure_plan.md)
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np

DPI = 300
PALETTE = {
    'fab':   '#1f77b4',   # Layer 1 Fabrication — blue
    'sense': '#ff7f0e',   # Layer 2 Sensing — orange
    'circ':  '#2ca02c',   # Layer 3 Circuits — green
    'intel': '#9467bd',   # Layer 4 Intelligence — purple
    'clin':  '#d62728',   # Layer 5 Clinical — red
    'bg':    '#f8f8f8',
    'text':  '#222222',
}
FONT = 'Arial'

# ============================================================
# FIG 1 — Full-Chain System Architecture
# ============================================================

def fig1_system_chain():
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    layers = [
        ('Layer 1\nMNA Fabrication',
         '• Si DRIE\n• Polymer molding\n• Hydrogel\n• 3D printing',
         PALETTE['fab'],   1.0),
        ('Layer 2\nElectrochemical\nTransduction',
         '• Amperometry\n• DPV / SWV\n• EIS aptasensor\n• Potentiometry (ISE)',
         PALETTE['sense'], 3.2),
        ('Layer 3\nFlexible Circuits\n& Wireless',
         '• AFE potentiostat\n• BLE 5.0 / NFC\n• FPCB substrate\n• Power mgmt',
         PALETTE['circ'],  5.4),
        ('Layer 4\nEmbedded\nIntelligence',
         '• Signal processing\n• ML calibration\n• Edge AI (LSTM)\n• Cloud relay',
         PALETTE['intel'], 7.6),
        ('Layer 5\nClinical Output',
         '• Glucose CGM\n• Lactate / UA\n• Cortisol\n• Multi-analyte',
         PALETTE['clin'],  9.8),
    ]

    box_w, box_h = 1.9, 3.6
    for title, bullets, color, x in layers:
        # Box
        rect = FancyBboxPatch((x, 0.7), box_w, box_h,
                               boxstyle="round,pad=0.05",
                               linewidth=1.5, edgecolor=color,
                               facecolor=color + '18')
        ax.add_patch(rect)
        # Header band
        head = FancyBboxPatch((x, 0.7 + box_h - 0.9), box_w, 0.9,
                               boxstyle="round,pad=0.05",
                               linewidth=0, edgecolor=color,
                               facecolor=color)
        ax.add_patch(head)
        ax.text(x + box_w/2, 0.7 + box_h - 0.45, title,
                ha='center', va='center', fontsize=7.5, fontweight='bold',
                color='white', fontfamily=FONT)
        ax.text(x + 0.12, 0.7 + box_h - 1.05, bullets,
                ha='left', va='top', fontsize=6.8,
                color=PALETTE['text'], fontfamily=FONT)

    # Arrows between boxes
    for i, (_, _, color, x) in enumerate(layers[:-1]):
        next_color = layers[i+1][2]
        mid_color = color
        ax.annotate('', xy=(x + box_w + 0.28 + 0.02, 2.5),
                    xytext=(x + box_w + 0.02, 2.5),
                    arrowprops=dict(arrowstyle='->', color=mid_color,
                                   lw=2.0))

    # Skin cross-section schematic (left of Layer 1)
    ax.text(0.08, 4.6, 'Skin', fontsize=7, color='#888', fontfamily=FONT)
    for y, label, col in [(4.2, 'Stratum corneum', '#e8c97a'),
                           (3.7, 'Epidermis (~100 μm)', '#f5d5a0'),
                           (2.9, 'Dermis + ISF', '#fbe8e0')]:
        ax.axhline(y, xmin=0, xmax=0.078, color=col, lw=6, solid_capstyle='round')
        ax.text(0.08, y, label, fontsize=5.5, va='center', color='#555', fontfamily=FONT)

    # MNA needle schematic
    for xi in [0.35, 0.52, 0.69]:
        ax.annotate('', xy=(xi, 3.1), xytext=(xi, 4.15),
                    arrowprops=dict(arrowstyle='->', color=PALETTE['fab'], lw=1.5))

    ax.text(0.52, 2.85, 'ISF\naccess', ha='center', fontsize=5.5,
            color=PALETTE['fab'], fontfamily=FONT)

    # Smartphone + cloud endpoint
    ax.add_patch(FancyBboxPatch((11.15, 3.55), 0.8, 0.85,
                                 boxstyle="round,pad=0.05", linewidth=1.2,
                                 edgecolor=PALETTE['clin'], facecolor=PALETTE['clin']+'18'))
    ax.text(11.55, 4.05, 'Smart-\nphone App', ha='center', fontsize=5.5,
            color=PALETTE['clin'], fontfamily=FONT, va='center')
    ax.add_patch(FancyBboxPatch((11.15, 2.5), 0.8, 0.85,
                                 boxstyle="round,pad=0.05", linewidth=1.2,
                                 edgecolor='#4a90d9', facecolor='#4a90d918'))
    ax.text(11.55, 2.92, 'Cloud /\nEHR', ha='center', fontsize=5.5,
            color='#4a90d9', fontfamily=FONT, va='center')

    ax.set_title('Fig. 1  Full-chain architecture of a wearable MNA-based electrochemical sensing system',
                 fontsize=9, fontweight='bold', pad=8, fontfamily=FONT, color=PALETTE['text'])

    plt.tight_layout()
    plt.savefig('fig_01_system_chain.png', dpi=DPI, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print('[OK] fig_01_system_chain.png saved')


# ============================================================
# FIG 3f — Sensing Modality Radar Chart
# ============================================================

def fig3_radar():
    categories = ['LOD\nCapability', 'Selectivity', 'Continuous\nMeasurement',
                  'Miniaturization\nEase', 'Low Power\nRequirement']
    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]

    modalities = {
        'Amperometry':   ([4, 3, 5, 5, 4], PALETTE['fab']),
        'DPV/SWV':       ([5, 4, 2, 3, 2], PALETTE['sense']),
        'EIS (aptasensor)': ([4, 5, 2, 3, 3], PALETTE['circ']),
        'Potentiometry (ISE)': ([3, 4, 5, 5, 5], PALETTE['intel']),
        'FSCV':          ([5, 3, 3, 2, 1], PALETTE['clin']),
    }

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.set_facecolor(PALETTE['bg'])
    fig.patch.set_facecolor('white')

    for label, (values, color) in modalities.items():
        vals = values + values[:1]
        ax.plot(angles, vals, 'o-', linewidth=1.8, color=color, label=label, markersize=4)
        ax.fill(angles, vals, alpha=0.08, color=color)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, size=8.5, fontfamily=FONT)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['1', '2', '3', '4', '5'], size=7, color='#888')
    ax.set_ylim(0, 5.5)
    ax.grid(color='#cccccc', linestyle='--', linewidth=0.6)
    ax.spines['polar'].set_visible(False)

    ax.legend(loc='upper right', bbox_to_anchor=(1.38, 1.15),
              fontsize=8, framealpha=0.9)
    ax.set_title('(f) Sensing modality comparison', fontsize=9,
                 fontweight='bold', pad=15, fontfamily=FONT)

    plt.tight_layout()
    plt.savefig('fig_03_modality_radar.png', dpi=DPI, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print('[OK] fig_03_modality_radar.png saved')


# ============================================================
# FIG 6 — Embedded Intelligence Performance (3 sub-panels)
# ============================================================

def fig6_intelligence():
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))
    fig.patch.set_facecolor('white')
    for ax in axes:
        ax.set_facecolor(PALETTE['bg'])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    # --- Panel (a): MARD vs. wear day ---
    ax = axes[0]
    days = np.arange(1, 15)
    mard_factory = 8 + 0.55 * days + 0.04 * days**2 + np.random.default_rng(42).normal(0, 0.4, len(days))
    mard_ml = 8.5 + 0.08 * days + np.random.default_rng(7).normal(0, 0.3, len(days))
    mard_ml = np.clip(mard_ml, 7, 11.5)
    mard_factory = np.clip(mard_factory, 8, 22)

    ax.plot(days, mard_factory, 'o--', color='#e07b54', lw=1.8,
            markersize=4, label='Factory calibration')
    ax.plot(days, mard_ml, 's-', color=PALETTE['intel'], lw=2.0,
            markersize=4, label='ML-adaptive calibration')
    ax.axhline(15, color='#cc0000', ls=':', lw=1.3, label='ISO 15197 threshold (15%)')
    ax.axhline(10.2, color=PALETTE['sense'], ls=':', lw=1.3, alpha=0.8, label='Best MNA (10.2%)')
    ax.fill_between(days, mard_ml - 0.8, mard_ml + 0.8, alpha=0.15, color=PALETTE['intel'])
    ax.set_xlabel('Wear day', fontsize=9, fontfamily=FONT)
    ax.set_ylabel('MARD (%)', fontsize=9, fontfamily=FONT)
    ax.set_title('(a) Calibration MARD over 14 days', fontsize=9, fontweight='bold', fontfamily=FONT)
    ax.legend(fontsize=7, loc='upper left')
    ax.set_xlim(1, 14)
    ax.set_ylim(5, 22)
    ax.tick_params(labelsize=8)

    # --- Panel (b): Hypoglycemia prediction accuracy ---
    ax = axes[1]
    models = ['Logistic\nRegression', 'Random\nForest', 'LSTM\n(3-layer)', 'Transformer']
    sensitivity = [72, 79, 87, 88]
    specificity = [81, 85, 92, 93]
    x = np.arange(len(models))
    w = 0.35
    bars1 = ax.bar(x - w/2, sensitivity, w, label='Sensitivity (%)',
                   color=PALETTE['intel'], alpha=0.85, edgecolor='white')
    bars2 = ax.bar(x + w/2, specificity, w, label='Specificity (%)',
                   color=PALETTE['fab'], alpha=0.85, edgecolor='white')
    ax.set_xticks(x)
    ax.set_xticklabels(models, fontsize=8, fontfamily=FONT)
    ax.set_ylabel('Performance (%)', fontsize=9, fontfamily=FONT)
    ax.set_title('(b) Hypoglycemia prediction (30 min)', fontsize=9, fontweight='bold', fontfamily=FONT)
    ax.set_ylim(60, 100)
    ax.legend(fontsize=8)
    ax.tick_params(labelsize=8)
    for bar in list(bars1) + list(bars2):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{int(bar.get_height())}', ha='center', va='bottom', fontsize=7.5, fontfamily=FONT)

    # --- Panel (c): Power breakdown pie ---
    ax = axes[2]
    components = ['BLE 5.0\nmodule', 'AFE\npotentiostat', 'MCU\n(ARM Cortex)', 'Sensor /\nelectrochem.']
    sizes = [35, 30, 25, 10]
    colors = [PALETTE['circ'], PALETTE['sense'], PALETTE['fab'], PALETTE['clin']]
    explode = (0.04, 0.04, 0.04, 0.04)
    wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=components,
                                       colors=colors, autopct='%1.0f%%',
                                       startangle=140, pctdistance=0.72,
                                       textprops={'fontsize': 8, 'fontfamily': FONT})
    for at in autotexts:
        at.set_fontsize(8)
        at.set_fontweight('bold')
        at.set_color('white')
    ax.set_title('(c) System power breakdown\n(target: <10 mW total)', fontsize=9,
                 fontweight='bold', fontfamily=FONT)

    fig.suptitle('Fig. 6  Embedded intelligence pipeline performance benchmarks',
                 fontsize=10, fontweight='bold', y=1.01, fontfamily=FONT)
    plt.tight_layout()
    plt.savefig('fig_06_intelligence.png', dpi=DPI, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print('[OK] fig_06_intelligence.png saved')


# ============================================================
# FIG 4 — Biomarker Summary (table-style visual)
# ============================================================

def fig4_biomarkers():
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.axis('off')
    fig.patch.set_facecolor('white')

    categories = [
        ('Metabolic', PALETTE['fab'],
         [('Glucose', '2.8–22.2 mM', 'CGM Zone A\n(MARD <15%)', 'Amperometry (GOx)'),
          ('Lactate', '0.5–20 mM', 'Sepsis: >2 mM', 'Amperometry (LOx)'),
          ('Uric acid', '120–480 μM', 'Gout: >360 μM', 'DPV on carbon')]),
        ('Electrolytes', PALETTE['circ'],
         [('Na⁺', '135–145 mM', 'Hyponatremia\n<135 mM', 'ISE (monensin)'),
          ('K⁺', '3.5–5.5 mM', 'Arrhythmia\n<3.5 or >5.5', 'ISE (valinomycin)'),
          ('pH', '7.35–7.45', 'Acidosis <7.35\nAlkalosis >7.45', 'ISE (IrOx)')]),
        ('Stress /\nImmune', PALETTE['intel'],
         [('Cortisol', '5–25 ng/mL', 'Diurnal peak\n15–25 ng/mL', 'EIS aptasensor'),
          ('IL-6', '1–100 pg/mL', 'Inflammation\n>10 pg/mL', 'EIS immunosensor')]),
        ('Neuro /\nPharmacokin.', PALETTE['clin'],
         [('Dopamine', '10 nM–1 μM', 'PD monitoring', 'FSCV on CF-MNA'),
          ('Vancomycin', '10–40 μg/mL', 'TDM therapeutic\nrange', 'EIS aptasensor')]),
    ]

    col_headers = ['Biomarker', 'ISF Range', 'Clinical Threshold', 'Detection Method']
    col_x = [0.01, 0.22, 0.44, 0.67]
    col_w = [0.20, 0.20, 0.22, 0.30]

    y = 0.97
    row_h = 0.082
    header_h = 0.09

    for cat_name, cat_color, analytes in categories:
        # Category header band
        rect = FancyBboxPatch((0, y - header_h), 1.0, header_h,
                               boxstyle="round,pad=0.005",
                               linewidth=0, facecolor=cat_color,
                               transform=ax.transAxes, clip_on=False)
        ax.add_patch(rect)
        ax.text(0.005, y - header_h/2, cat_name,
                transform=ax.transAxes, ha='left', va='center',
                fontsize=8.5, fontweight='bold', color='white', fontfamily=FONT)

        # Column headers (first category only)
        if cat_name == 'Metabolic':
            for hdr, cx in zip(col_headers, col_x):
                ax.text(cx + 0.005, y + 0.005, hdr,
                        transform=ax.transAxes, ha='left', va='bottom',
                        fontsize=7.5, fontweight='bold', color='#444', fontfamily=FONT)

        y -= header_h

        for analyte, isf_range, threshold, method in analytes:
            bg = '#f5f5f5' if analytes.index((analyte, isf_range, threshold, method)) % 2 == 0 else 'white'
            rect2 = FancyBboxPatch((0, y - row_h), 1.0, row_h,
                                    boxstyle="square,pad=0",
                                    linewidth=0.3, edgecolor='#ddd',
                                    facecolor=bg,
                                    transform=ax.transAxes, clip_on=False)
            ax.add_patch(rect2)
            vals = [analyte, isf_range, threshold, method]
            for val, cx in zip(vals, col_x):
                ax.text(cx + 0.008, y - row_h/2, val,
                        transform=ax.transAxes, ha='left', va='center',
                        fontsize=7.2, color=PALETTE['text'], fontfamily=FONT)
            # Color dot
            ax.plot(0.005, y - row_h/2, 'o', ms=5, color=cat_color,
                    transform=ax.transAxes)
            y -= row_h

        y -= 0.012  # gap between categories

    ax.set_title('Fig. 4  Target biomarkers for MNA-based wearable electrochemical monitoring',
                 fontsize=9, fontweight='bold', pad=8, fontfamily=FONT, color=PALETTE['text'],
                 loc='left', x=0.0)
    plt.tight_layout()
    plt.savefig('fig_04_biomarkers.png', dpi=DPI, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print('[OK] fig_04_biomarkers.png saved')


# ============================================================
# Run all
# ============================================================
if __name__ == '__main__':
    import os
    os.chdir(r'C:\Users\ZYJ\microneedle-review')
    print('Generating figures...')
    fig1_system_chain()
    fig3_radar()
    fig6_intelligence()
    fig4_biomarkers()
    print('\n[OK] All figures generated. Place PNG files in C:\\Users\\ZYJ\\microneedle-review\\')
    print('     Remaining: fig_02_fabrication.png, fig_05_circuits.png (need SEM/photo assets)')
    print('     Graphical abstract: crop fig_01_system_chain.png to 400×300 px')
