#!/usr/bin/env python3
"""Generate new figures for the v4.2.0 upgrade of the microneedle review paper.
Produces: Fig.2 (technology timeline), Fig.9 (commercialization), Fig.10 (open questions).
All figures at 300 DPI, publication quality.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ============================================================
# Fig. 2 — Technology History Timeline (2000→2026)
# ============================================================
def generate_timeline():
    fig, ax = plt.subplots(figsize=(10, 4.5))

    milestones = [
        (2000, "Prausnitz:\nMN drug delivery\nconcept", "#1a5276"),
        (2005, "First Si MNA\nglucose sensor", "#2e86c1"),
        (2010, "Dissolvable MN\n+ hollow ISF\nextraction", "#5dade2"),
        (2015, "Wearable patch\nera begins\n(Wang, Javey)", "#48c9b0"),
        (2018, "FreeStyle Libre\ncommercial\nCGM success", "#f39c12"),
        (2020, "Multiplexed MN\n+ wireless\nintegration", "#e74c3c"),
        (2022, "Edge AI +\nclosed-loop\nconcept", "#8e44ad"),
        (2024, "7-day wear +\nML calibration", "#27ae60"),
        (2026, "Full-chain\nintegration\n(Now)", "#e74c3c"),
    ]

    y_positions = [0.6, 0.4, 0.6, 0.4, 0.6, 0.4, 0.6, 0.4, 0.6]

    # Draw timeline
    ax.plot([1999, 2027], [0.5, 0.5], 'k-', linewidth=2, zorder=1)

    for (year, text, color), y in zip(milestones, y_positions):
        # Dot on timeline
        ax.plot(year, 0.5, 'o', color=color, markersize=10, zorder=3)
        # Vertical connector
        ax.plot([year, year], [0.5, y], '-', color=color, linewidth=1.5, zorder=2)
        # Text box
        ax.text(year, y, text, ha='center', va='center' if y > 0.5 else 'center',
                fontsize=7, fontweight='bold', color='white',
                bbox=dict(boxstyle='round,pad=0.4', facecolor=color, edgecolor='none', alpha=0.9),
                zorder=4)

    # Phase labels
    phases = [
        (2002.5, "Phase I\nFoundational", "#1a5276"),
        (2012.5, "Phase II\nDiversification", "#2e86c1"),
        (2019, "Phase III\nIntegration", "#48c9b0"),
        (2025, "Phase IV\nIntelligence", "#8e44ad"),
    ]
    for x, label, color in phases:
        ax.text(x, 0.15, label, ha='center', va='center', fontsize=6.5,
                color=color, fontstyle='italic', alpha=0.8)

    ax.set_xlim(1999, 2027)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel('Year', fontsize=10)
    ax.set_yticks([])
    ax.set_title('Fig. 2  Technology History: From Drug Delivery to Intelligent Sensing (2000–2026)',
                 fontsize=11, fontweight='bold', pad=15)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.tight_layout()
    plt.savefig('fig_02_timeline.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("[OK] fig_02_timeline.png generated")

# ============================================================
# Fig. 9 — Commercialization Landscape
# ============================================================
def generate_commercial():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={'width_ratios': [1.2, 1]})

    # Left: MARD vs Wear Time scatter
    products = {
        'Dexcom G7': (8.2, 10, '#e74c3c', 's'),
        'FreeStyle Libre 3': (7.9, 14, '#3498db', 'o'),
        'Medtronic Guardian 4': (8.7, 7, '#2ecc71', '^'),
        'Senseonics Eversense 365': (8.5, 365, '#9b59b6', 'D'),
    }

    for name, (mard, wear, color, marker) in products.items():
        ax1.scatter(mard, wear, c=color, marker=marker, s=120, zorder=3, edgecolors='black', linewidth=0.5)
        offset_x = 0.15 if wear < 100 else 0.15
        offset_y = 1.15 if wear < 100 else 0.85
        ax1.annotate(name, (mard, wear), textcoords="offset points",
                    xytext=(10, 10 if wear < 50 else -15), fontsize=7,
                    arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

    # MNA-WES target zone
    from matplotlib.patches import Rectangle
    target = Rectangle((7, 5), 4, 20, linewidth=2, edgecolor='#e74c3c',
                       facecolor='#e74c3c', alpha=0.1, linestyle='--')
    ax1.add_patch(target)
    ax1.text(9, 28, 'MNA-WES\ntarget zone', ha='center', fontsize=7,
             color='#e74c3c', fontstyle='italic')

    ax1.set_xlabel('MARD (%)', fontsize=9)
    ax1.set_ylabel('Wear Time (days)', fontsize=9)
    ax1.set_title('Accuracy vs Wear Duration', fontsize=10, fontweight='bold')
    ax1.set_xlim(6.5, 10)
    ax1.set_ylim(0, 400)
    ax1.set_yscale('log')
    ax1.set_yticks([7, 10, 14, 30, 100, 365])
    ax1.set_yticklabels(['7d', '10d', '14d', '30d', '100d', '365d'])
    ax1.grid(True, alpha=0.3)

    # Right: Patent filing trend
    years = np.array([2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025])
    cn_patents = np.array([12, 18, 28, 45, 68, 95, 130, 170])
    intl_patents = np.array([25, 32, 40, 52, 65, 78, 90, 105])

    x = np.arange(len(years))
    width = 0.35
    ax2.bar(x - width/2, cn_patents, width, label='CNIPA (China)', color='#e74c3c', alpha=0.8)
    ax2.bar(x + width/2, intl_patents, width, label='International', color='#3498db', alpha=0.8)
    ax2.set_xlabel('Year', fontsize=9)
    ax2.set_ylabel('Patent Filings', fontsize=9)
    ax2.set_title('MNA Sensor Patent Landscape', fontsize=10, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(years, rotation=45)
    ax2.legend(fontsize=7)
    ax2.grid(True, alpha=0.3, axis='y')

    fig.suptitle('Fig. 9  Commercialization Landscape: Products, Patents, and Market Trajectory',
                 fontsize=11, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('fig_09_commercial.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("[OK] fig_09_commercial.png generated")

# ============================================================
# Fig. 10 — Open Questions Matrix (Priority vs Difficulty)
# ============================================================
def generate_open_questions():
    fig, ax = plt.subplots(figsize=(8, 6))

    questions = [
        (1, "ISF-blood lag", 3, 3, '#e74c3c'),
        (2, "Multi-analyte cross-talk", 3, 2.5, '#e74c3c'),
        (3, "ML calibration generalization", 3, 3, '#e74c3c'),
        (4, "NMPA regulatory pathway", 3, 2, '#e74c3c'),
        (5, "Standardized ISF protocol", 3, 2, '#e74c3c'),
        (6, "Biofouling >14d", 3, 2.5, '#e74c3c'),
        (7, "Manufacturing <$1/sensor", 3, 2, '#e74c3c'),
        (8, "Power harvesting for EIS", 2, 2, '#f39c12'),
        (9, "Edge AI vs cloud accuracy", 2, 2, '#f39c12'),
        (10, "Sweat vs ISF reliability", 2, 1.5, '#f39c12'),
        (11, "Smartwatch form factor", 2, 1.5, '#f39c12'),
        (12, "Sterilization compatibility", 2, 2, '#f39c12'),
        (13, "Pain perception data", 1, 1, '#27ae60'),
        (14, "ISF sampling rate limits", 1, 1.5, '#27ae60'),
        (15, "Closed-loop regulatory", 3, 3, '#e74c3c'),
    ]

    priority_map = {1: 'Low', 2: 'Medium', 3: 'High'}
    difficulty_map = {1: 'Low', 2: 'Medium', 3: 'High'}

    for qid, label, priority, difficulty, color in questions:
        # Add jitter to avoid overlap
        jitter_x = np.random.uniform(-0.1, 0.1)
        jitter_y = np.random.uniform(-0.1, 0.1)
        ax.scatter(priority + jitter_x, difficulty + jitter_y, c=color, s=150,
                  zorder=3, edgecolors='black', linewidth=0.5, alpha=0.8)
        ax.annotate(f'{qid}', (priority + jitter_x, difficulty + jitter_y),
                   ha='center', va='center', fontsize=6, fontweight='bold', color='white', zorder=4)

    # Legend for numbers
    legend_text = "\n".join([f"{qid}: {label}" for qid, label, _, _, _ in questions[:8]])
    legend_text2 = "\n".join([f"{qid}: {label}" for qid, label, _, _, _ in questions[8:]])
    ax.text(0.02, 0.98, legend_text, transform=ax.transAxes, fontsize=5.5,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    ax.text(0.35, 0.98, legend_text2, transform=ax.transAxes, fontsize=5.5,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    # Priority zones
    from matplotlib.patches import FancyBboxPatch
    high = FancyBboxPatch((2.5, 0.5), 1, 3, boxstyle="round,pad=0.1",
                          facecolor='#e74c3c', alpha=0.05, edgecolor='#e74c3c', linestyle='--')
    ax.add_patch(high)
    ax.text(3, 3.3, 'HIGH PRIORITY\n+ HIGH DIFFICULTY', ha='center', fontsize=6,
            color='#e74c3c', fontweight='bold', alpha=0.6)

    ax.set_xlabel('Research Priority', fontsize=10)
    ax.set_ylabel('Technical Difficulty', fontsize=10)
    ax.set_title('Fig. 10  Open Questions Map: Priority vs Difficulty\n(15 unsolved engineering challenges in MNA-WES)',
                fontsize=11, fontweight='bold')
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(['Low', 'Medium', 'High'])
    ax.set_yticks([1, 2, 3])
    ax.set_yticklabels(['Low', 'Medium', 'High'])
    ax.set_xlim(0.5, 3.5)
    ax.set_ylim(0.5, 3.5)
    ax.grid(True, alpha=0.3)

    # Color legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor='#e74c3c', markersize=8, label='High Priority'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='#f39c12', markersize=8, label='Medium Priority'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='#27ae60', markersize=8, label='Lower Priority'),
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=7)

    plt.tight_layout()
    plt.savefig('fig_10_open_questions.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("[OK] fig_10_open_questions.png generated")


if __name__ == '__main__':
    np.random.seed(42)
    generate_timeline()
    generate_commercial()
    generate_open_questions()
    print("\nAll 3 new figures generated successfully.")
