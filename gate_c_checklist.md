# Gate C — Submission Readiness Check
## Wearable MNA Electrochemical Sensing Systems Review
## Generated: 2026-05-14 | SCI-writer v3.0.0

---

## Gate C Scorecard

| Check | Requirement | Status | Notes |
|-------|-------------|--------|-------|
| Abstract word count | ≤300 words | ✅ PASS | 300 words after Stage 8 trim |
| Highlights count | 3–5 highlights | ✅ PASS | 5 highlights |
| Highlights length | Each ≤85 chars | ✅ PASS | All verified |
| Journal declaration | `\journal{Biosensors and Bioelectronics}` | ✅ PASS | In main.tex |
| Bibliography style | `elsarticle-num` | ✅ PASS | In main.tex |
| Document class | `review,1p` | ✅ PASS | In main.tex |
| Line numbers | `\linenumbers` enabled | ✅ PASS | In main.tex |
| CRediT statement | Present | ✅ PASS | In main.tex |
| Competing interests | Declared | ✅ PASS | In main.tex |
| Data availability | Stated | ✅ PASS | In main.tex |
| Table 1 | Performance comparison table | ✅ PASS | Added Stage 8 (21 rows) |
| Search methodology | §1.4 PRISMA-lite | ✅ PASS | Added Stage 8 |
| Chain-linking sentences | §2.5, §3.5, §5.4 | ✅ PASS | Added Stage 8 |
| CGM MARD comparison | Dexcom G7, FreeStyle Libre 2 | ✅ PASS | Added Stage 8 |
| Data flow §6.1 | ADC→ML pipeline | ✅ PASS | Added Stage 8 |
| ISO 10993 mention | §7.3 regulatory | ✅ PASS | Added Stage 9 |
| Wang/Gao attribution | §2.3 | ✅ PASS | Added Stage 9 |
| Cover letter | Declaration included | ✅ PASS | cover_letter.md |
| Figures | 6 placeholders | ⚠️ PARTIAL | Placeholders only — need actual images |
| Author names | Real names | ❌ FAIL | Must replace `[Author One]` etc. |
| Funding | Grant number | ❌ FAIL | Must replace `[grant number]` |
| Graphical abstract | 400×300 px image | ❌ FAIL | Placeholder — need actual image |
| BibTeX completeness | ≥130 entries | ⚠️ PARTIAL | ~90 entries; target 130 |
| Gate B citation audit | 0 unverified [N] claims | ⚠️ PARTIAL | 6 high-priority [N] remaining |

---

## Critical Blockers Before Submission

### Must Fix (Cannot Submit Without These):
1. **Author names and affiliations** — Replace `[Author One]`, `[Author Two]`, etc. with real names and ORCID IDs
2. **Corresponding author email** — Required by Editorial Manager
3. **Funding statement** — Fill in grant numbers and funding agency names
4. **Graphical abstract** — Generate 400×300 px image (no text overlay) from Fig. 1 concept

### Should Fix (High Priority):
5. **Gate B citation verification** — Verify Chen2022CNT (87% claim), Fan2026EdgeAI (DOI year), Son2014 foundational attribution
6. **BibTeX expansion** — Reach ≥130 entries; currently ~90
7. **Figure images** — Generate or source actual figure images for Figs. 1–6

---

## Projected Reviewer Scores (Post Stage 8)

| Reviewer | Pre-Stage 8 | Post-Stage 8 | Change |
|----------|------------|--------------|--------|
| R1 Domain Expert | 74/100 | ~81/100 | +7 |
| R2 Adjacent Field | 77/100 | ~82/100 | +5 |
| R3 Methods/Rigor | 72/100 | ~79/100 | +7 |
| EIC | 82/100 | ~86/100 | +4 |
| DA Devil's Advocate | 71/100 | ~82/100 | +11 |
| **Average** | **75.2** | **~82.0** | **+6.8** |

**Gate C threshold: avg ≥80/100, all reviewers ≥60/100 → PROJECTED PASS**

---

## File Manifest (Submission Package)

| File | Status | Notes |
|------|--------|-------|
| `main.tex` | ✅ Ready | ~640 lines; 8 sections; all P0/P1 revisions applied |
| `references.bib` | ⚠️ Partial | ~90 entries; expand to 130 |
| `elsarticle.cls` | ℹ️ Required | Download from Elsevier; place in root |
| `elsarticle-num.bst` | ℹ️ Required | Download from Elsevier; place in root |
| `highlights.txt` | ✅ Ready | 5 highlights ≤85 chars each |
| `cover_letter.md` | ✅ Template | Fill in author names, grant numbers |
| `fig_01_system_chain.png` | ❌ Missing | Generate from figure_plan.md spec |
| `fig_02_fabrication.png` | ❌ Missing | Generate or adapt |
| `fig_03_sensing_modalities.png` | ❌ Missing | Generate or adapt |
| `fig_04_biomarkers.png` | ❌ Missing | Generate |
| `fig_05_circuits.png` | ❌ Missing | Generate from block diagram spec |
| `fig_06_intelligence.png` | ❌ Missing | Generate |
| `graphical_abstract.png` | ❌ Missing | 400×300 px, crop of Fig. 1 |

---

## LaTeX Compilation Instructions

```bash
# Standard 4-pass compilation sequence for elsarticle + bibtex:
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

**Expected compilation warnings (acceptable):**
- "Citation `XXX' on page X undefined" → fixed after bibtex pass
- "Overfull \\hbox" for Table 1 → acceptable in review mode; use `\resizebox`
- "Package siunitx Warning" → update siunitx package if persistent

**Blockers that will prevent compilation:**
- Missing `elsarticle.cls` → download from CTAN or Elsevier author tools
- Undefined citation keys → verify all `\cite{KEY}` have matching bib entries

---

*Gate C status: PROJECTED PASS (subject to author info, figures, Gate B verification)*
*Next: Stage 10 — Final assembly and submission package zip*
