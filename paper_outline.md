# Paper Outline — Detailed Section Plan
## Wearable Electrochemical Sensing Systems Based on Microneedle Arrays:
## A Full-Chain Review from Sensor Fabrication to Intelligent Embedded Terminals
### SCI-writer Stage 1 Output | Generated 2026-05-14

---

## Narrative Architecture Validation

**Problem → Solution arc:**
§1 establishes the clinical urgency of continuous biomarker monitoring and the failure modes of conventional methods → §2-3 build the transducer foundation (fabrication + sensing physics) → §4 maps transducers to clinical applications → §5-6 close the system chain (circuits → intelligence) → §7 identifies the remaining barriers.

**Unique contribution visible:** The "full-chain" framing is introduced in §1.4, repeated as section transitions, and synthesized in §6.5 and §7.5 — ensuring the paper's differentiation is unmistakable to reviewers.

**Journal scope fit:** B&B scope: "from research to clinical practice" — our arc follows exactly this trajectory.

---

## Section 1: Introduction
**Word target:** 2,000 | **Planned citations:** 18-22 | **Key claim:** MNA-based wearable electrochemical sensing is the enabling technology for a new paradigm of continuous, non-laboratory health monitoring.

### 1.1 Clinical and Societal Motivation (~500 words)
**Topic sentence:** The global burden of metabolic, cardiovascular, and stress-related conditions creates an urgent need for continuous, ambulatory biomarker monitoring that conventional laboratory methods cannot fulfill.
- Diabetes prevalence: 537 million adults (IDF 2021), projected 783 million by 2045 [NEEDS_REF: IDF Diabetes Atlas 2021]
- Limitations: fingerstick compliance ~4 tests/day; glucose variability missed between measurements
- Beyond glucose: lactate as sepsis biomarker, cortisol for stress/inflammation, electrolytes for cardiac risk
- Wearable continuous monitoring paradigm: from episodic measurement to data-rich continuous streams
- **Key paper:** Tehrani et al. 2022 Nat Biomed Eng [V] — first fully integrated wearable MNA system as motivating example

### 1.2 Limitations of Conventional Monitoring Approaches (~400 words)
**Topic sentence:** Existing monitoring technologies — venipuncture, CGM implants, and sweat sensors — each fail a critical requirement for universal continuous health monitoring.
- Blood sampling: invasive, requires clinical setting, no continuous capability
- Implantable CGM (Dexcom G7, Abbott FreeStyle Libre): skin trauma from insertion trocar, foreign body response, 7-14 day replacement cycle, limited to glucose
- Sweat sensors: non-invasive but low biomarker concentrations, sweat gland activation required (exercise-dependent), poor correlation with blood levels for many analytes
- The ISF gap: ISF contains >99% of blood biomarkers at ~25-50% blood concentration; directly accessible via minimally invasive MNA without implant trauma

### 1.3 Microneedle Arrays as the Minimally Invasive Bridge (~500 words)
**Topic sentence:** Microneedle arrays with integrated electrochemical transducers uniquely bridge the gap between non-invasive sweat sensors and invasive implants, accessing ISF without skin trauma.
- MNA definition: 200-1000 μm needles penetrating epidermis to papillary dermis, accessing ISF
- Minimally invasive: penetrates stratum corneum (20-100 μm thick), stops before sensory nerve endings and blood vessels
- ISF biomarker fidelity: glucose/lactate ISF-blood ratio 0.7-1.0 during stable conditions
- Historical context: MNA technology from transdermal drug delivery (1990s) → electrochemical sensing (2010s) → fully integrated wearable systems (2020s)
- The fabrication-sensing-intelligence chain: why all three layers must be reviewed together
- **Key paper:** Dervisevic et al. 2021 Adv Funct Mater [V] — high-density Si MNA demonstrating ISF access at scale

### 1.4 Scope, Organization, and Unique Contribution of This Review (~600 words)
**Topic sentence:** This review is the first to systematically cover wearable MNA electrochemical sensing as a complete engineering system chain, from needle tip chemistry to intelligent embedded terminals.
- Explicit scope: 91 papers, 2021-2026, covering fabrication → sensing → biomarkers → circuits → intelligence
- What differentiates this review from prior art: [Reference to gap analysis — 5 existing reviews and their specific omissions]
- Organization roadmap: §2 (fabrication) → §3 (sensing) → §4 (biomarkers/clinical) → §5 (circuits) → §6 (intelligence) → §7 (challenges)
- Full-chain framework figure introduced here (→ Fig. 1)
- Explicit statement: "To our knowledge, this is the first review to treat MNA-based wearable electrochemical sensing as a complete engineering system from microneedle tip functionalization through analog front-end design to embedded terminal intelligence."

---

## Section 2: Microneedle Array Fabrication Technologies
**Word target:** 3,500 | **Planned citations:** 28-32 | **Key claim:** Material selection and fabrication process jointly determine the electrochemical performance, mechanical safety, and scalability of MNA-based sensors.

### 2.1 Material Selection Principles (~700 words)
**Topic sentence:** The choice of MNA material governs the trade-off between mechanical robustness, electrochemical inertness, biocompatibility, and manufacturing scalability.

**Sub-topic A: Silicon and metal-based MNAs**
- Silicon: high aspect ratio via DRIE, excellent dimensional control; brittle fracture risk; requires metal electrode coating
- Stainless steel: robust, laser-cut, low cost; surface oxide layer limits electrochemical performance without functionalization
- Titanium: biocompatible, corrosion-resistant; used as substrate for PtIr or gold electrode coatings
- Gold/Platinum: electrochemically inert, low background current; typically deposited as thin film on structured substrate
- **Key paper:** Dervisevic 2021 Adv Funct Mater [V] (Si, ~9500 needles/cm²)

**Sub-topic B: Polymer-based MNAs**
- PDMS (polydimethylsiloxane): flexible, biocompatible, conformal; requires conductive coating
- SU-8 epoxy: photopatternable, high aspect ratio; brittle at high aspect ratios
- PMMA, PC, PLA: injection-moldable, scalable; thermal processing may damage enzyme layers
- Polyimide (Kapton): flexible, chemically inert; used as flex substrate for electrode wiring
- **Key paper:** Parrilla 2022 Talanta [V] (hollow PDMS MNA glucose patches)

**Sub-topic C: Hydrogel-based MNAs**
- Swelling mechanism: hydrogel absorbs ISF, concentrates analytes at electrode surface
- Materials: PVA, GelMA, polyacrylamide; tuneable swelling ratio
- Advantage: ISF extraction without hollow needle hydraulic issues
- Limitation: mechanical weakness, slow response time during swelling equilibration
- **Key paper:** Zhou 2024 ACS Nano [V] (core-shell zwitterionic hydrogel MN)

**Sub-topic D: Carbon-based MNA electrodes**
- Glassy carbon: wide electrochemical window, low background
- Carbon nanotube (CNT): high surface area, fast electron transfer kinetics
- Graphene and rGO: tuneable functionalization, high conductivity
- Pyrolytic carbon: derived from SU-8 precursor, batch-compatible

### 2.2 Geometric Design: From Concept to ISF Access (~600 words)
**Topic sentence:** Needle geometry (height, diameter, tip angle, array pitch) determines ISF access depth, mechanical safety, and the available electrode area.

- Solid MNAs: coating-based sensing (enzyme/ion-selective membrane on outer surface)
- Hollow MNAs: ISF flows through lumen to internal reference electrode; higher flow rate but fabrication complexity
- Porous MNAs: ISF wicking through porous matrix; intermediate approach
- Coated/dissolving: sensing layer on tip, dissolves in ISF to release probe molecules
- Fracture mechanics: critical force per needle >0.1 N; tip sharpness affects skin penetration threshold
- Optimal insertion depth: 200-800 μm (penetrates viable epidermis; avoids dermis nerves and vasculature)
- Array pitch optimization: too close = needle-to-needle ISF competition; too sparse = insufficient signal
- **Key paper:** Heifler 2021 ACS Nano [V] ("clinic-on-a-needle" — geometry rationale for multi-electrode)

### 2.3 Electrode Tip Functionalization (~700 words)
**Topic sentence:** The electrochemical performance of an MNA sensor depends critically on the tip functionalization strategy — enzyme immobilization, nanostructuring, or molecular recognition layer design.

**Enzyme immobilization methods:**
- Physical entrapment in Nafion/BSA-crosslinked matrix: simple but limited stability
- Covalent attachment via EDC/NHS chemistry: stronger binding, retained enzyme activity
- Self-assembled monolayer (SAM) orientation control: enhances electron transfer rate
- PEDOT electropolymerization: conductive host matrix for enzyme entrapment
- Stability benchmark: >7 days in vivo without significant sensitivity loss

**Nanostructuring for sensitivity enhancement:**
- Gold nanoparticles (AuNPs) electrodeposition: increases effective surface area 5-10×
- Platinum black: high surface area, catalytic activity for H₂O₂ detection
- rGO composites: combines high surface area with electrocatalytic activity
- LOD improvement from nanostructuring: typical 3-5× reduction in LOD vs. flat electrode

**Aptasensor/MIP integration:**
- Aptamers: single-stranded DNA/RNA selected for target binding; used for cortisol, IL-6, vancomycin
- Molecularly imprinted polymers (MIPs): synthetic antibody mimics; suitable for small molecules
- EIS-based detection: binding event changes Rct → quantified via Nyquist plot analysis

### 2.4 Fabrication Processes (~900 words)
**Topic sentence:** Each fabrication process class offers distinct dimensional accuracy, throughput, and integration compatibility trade-offs.

**Photolithography and DRIE (Si MNA):**
- DRIE (Bosch process): alternating SF₆ etch and C₄F₈ passivation; enables >50:1 aspect ratio
- Photolithography resolution: sub-micron alignment; excellent dimensional control
- Post-processing: thermal oxidation, metal deposition (PVD), electroplating
- Scalability: CMOS-compatible, wafer-scale production; high capital cost

**Micromolding (polymer MNA):**
- Master mold fabrication: SU-8 negative tone photoresist → PDMS casting
- Multi-step molding: primary mold → secondary mold → final MNA
- Tip sharpness control via controlled peeling/demolding angle
- Low-cost, high throughput; limited to low-Tg polymers

**3D Printing (emerging):**
- DLP/SLA: 25-100 μm resolution; appropriate for hollow MNA fabrication
- Multi-material printing: structural polymer + conductive electrode in one print
- **Key paper:** Reynoso 2024 Biosens Bioelectron [V] (3D-printed aptamer MNA pharmacokinetics)
- Limitation: surface roughness, limited electrode material choices

**Electrodeposition:**
- Ni/Au hollow MNA via photoresist template electroforming
- PEDOT electropolymerization for enzyme entrapment directly on needle tip
- Advantage: conformal coating of complex 3D geometries

**Laser processing:**
- CO₂ and UV laser cutting of stainless steel for solid MNA
- Laser ablation for carbon fiber electrode exposure at needle tips
- Laser pyrolysis of polyimide → carbon electrode (no separate deposition step)

### 2.5 Scalability and Manufacturing Considerations (~600 words)
**Topic sentence:** Translating laboratory MNA fabrication to scalable manufacturing requires addressing process variability, batch-to-batch consistency, and cost-per-device targets.

- Roll-to-roll compatible approaches: screen-printed flexible electrodes on polymer substrate
- Sterilization compatibility: EtO gas sterilization (enzyme-compatible); gamma irradiation (damages enzyme activity)
- Shelf life requirements: >12 months dry storage; hydrogel MNA requires specialized packaging
- Regulatory manufacturing requirements: ISO 13485 QMS; FDA 21 CFR Part 820
- Cost benchmark: current MNA patch manufacturing cost ~$15-50/device; target for mass adoption <$5
- **Key paper:** Friedel 2023 Lab Chip [V] (scalability discussion for human ISF monitoring)

---

## Section 3: Electrochemical Sensing Modalities
**Word target:** 3,000 | **Planned citations:** 22-26 | **Key claim:** The choice of electrochemical sensing modality — not just electrode material — determines which biomarkers can be detected and at what clinical accuracy.

### 3.1 Amperometry and Chronoamperometry (~700 words)
**Topic sentence:** Amperometric detection via enzyme-mediated H₂O₂ oxidation is the dominant modality for metabolite monitoring (glucose, lactate) due to its simplicity, selectivity, and continuous measurement capability.

- Working principle: E_applied = 0.6-0.7 V vs. Ag/AgCl; H₂O₂ generated by GOx/LOx oxidized at Pt/Au electrode
- Cottrell equation: i(t) = nFAD^{1/2}C / (π^{1/2}t^{1/2}) — governs transient current response
- Sensitivity optimization: electrode surface area, enzyme loading, membrane permeability
- Differential measurement: working minus inactive reference needle eliminates background drift
- **Key paper:** Yang Y 2024 Biosens Bioelectron [V] (differential MNA CGM, sensitivity details)
- Interference rejection: Nafion outer membrane (exclusion of AA, UA, acetaminophen by charge/size)
- Calibration: one-point vs. two-point vs. ML-based (see §6.2)

### 3.2 Voltammetry: CV, DPV, SWV, FSCV (~700 words)
**Topic sentence:** Pulse and scan voltammetric techniques enable selective detection of electroactive biomarkers (uric acid, dopamine, catecholamines) directly without enzymes, using electrochemical fingerprinting.

- Cyclic Voltammetry (CV): characterization tool; peak separation ΔEp diagnostic of kinetics; Randles-Ševčík: i_p = 0.4463·nFAC·(nFvD/RT)^{1/2}
- Differential Pulse Voltammetry (DPV): pulse superposition eliminates charging current; LOD improvement ~10× vs. CV
- Square Wave Voltammetry (SWV): faster than DPV; suitable for time-resolved measurements
- Fast-Scan CV (FSCV): 400 V/s scan rate; resolves subsecond dopamine transients in vivo
- Application: UA detection via DPV at +0.33 V; dopamine at +0.2 V; AA interference separation
- Wearable SWV implementation: requires precise waveform generation (DAC + op-amp AFE)

### 3.3 Electrochemical Impedance Spectroscopy (EIS) (~500 words)
**Topic sentence:** EIS-based aptasensors enable label-free detection of large biomolecules (proteins, hormones) that enzyme-based methods cannot address, using impedance changes upon target binding.

- Randles cell model: Z = R_s + 1/(jωC_dl + 1/(R_ct + Z_W))
- R_ct as the detection signal: binding of cortisol/protein increases R_ct measurably
- Frequency range: 0.1 Hz – 100 kHz; diagnostic frequency depends on analyte-aptamer pair
- LOD benchmark: cortisol aptasensor LOD <1 ng/mL required for clinical stress monitoring
- **Key paper:** Bakhshandeh 2024 Adv Mater [V] (Aptalyzer — aptasensor in vivo glucose+lactate via EIS)
- Wearable EIS challenge: impedance analyzer chip (AD5941) integration; power consumption

### 3.4 Potentiometry and Ion-Selective Electrodes (~600 words)
**Topic sentence:** Potentiometric ISEs with Nernstian response are uniquely suited for ion monitoring (Na⁺, K⁺, Ca²⁺, pH) — applications where amperometric and voltammetric methods fail.

- Nernst equation: E = E⁰ + (RT/z_iF)·ln(a_i); Nernstian slope at 25°C = 59.2/z_i mV/decade
- Ion-selective membrane design: ionophore selection (valinomycin for K⁺, monensin for Na⁺)
- Reference electrode: all-solid-state Ag/AgCl with inner reference layer
- Selectivity: Nikolsky-Eisenman equation; log k_{ij} < -2 required for clinical selectivity
- pH monitoring: iridium oxide (IrOx) sub-Nernstian sensors; polyaniline-based
- **Key paper:** Molinero-Fernández 2023 ACS Sensors [V] (7-electrode in vivo multi-ion potentiometric)
- **Key paper:** García-Guzmán 2021 ACS Sensors [V] (MNA ISE pH clinical validation)
- Clinical target: Na⁺ 135-145 mM, K⁺ 3.5-5.0 mM, pH 7.35-7.45 in ISF

### 3.5 Multi-Analyte Multiplexed Arrays (~500 words)
**Topic sentence:** The full clinical value of MNA-based monitoring is realized only in multiplexed systems that simultaneously detect multiple biomarkers from a single ISF sample.

- Electrode addressing: spatially separated working electrodes on a single MNA patch
- Crosstalk prevention: differential electrical shielding; spatial separation >500 μm
- Simultaneous amperometry + potentiometry: shared reference electrode design challenges
- Data fusion: multi-analyte correlation (glucose-lactate-pH triangulation for metabolic state)
- **Key paper:** Li X 2025 Innovation [V] (9-analyte self-calibrating array — current state-of-the-art)
- **Key paper:** Heifler 2021 ACS Nano [V] (glucose + lactate + insulin simultaneous)
- Circuit requirement: multi-channel potentiostat AFE (see §5.2)

---

## Section 4: Target Biomarkers and Clinical Applications
**Word target:** 3,000 | **Planned citations:** 24-28 | **Key claim:** The clinical utility of MNA sensors depends on matching sensor specifications (LOD, linear range, selectivity) to physiological target concentrations and clinical decision thresholds.

### 4.1 Metabolic Markers: Glucose, Lactate, Uric Acid, Creatinine (~900 words)
- **Glucose:** ISF 2.8-22.2 mM clinical range; MARD <10% target; CGM accuracy: ISO 15197:2015; Clarke EGA zone A/B acceptable
  - Key paper: Yang J 2023 ACS Sensors [V] (14-day CGM, MARD 10.2%)
  - Key paper: Tehrani 2022 Nat Biomed Eng [V] (human validation, Clarke EGA analysis)
- **Lactate:** ISF 0.5-20 mM during exercise; >4 mM: anaerobic threshold; clinical sepsis threshold 2 mM
  - Key paper: Djassemi 2026 ACS Sensors [V] (21-patient, 14-day lactate monitoring)
  - Key paper: Djassemi 2026 Biosens Bioelectron [N] (baseball pitcher exercise validation)
- **Uric Acid:** ISF 0.2-0.6 mM baseline; >0.36 mM: hyperuricemia; DPV at RRDE/carbon electrode
- **Creatinine:** ISF 44-97 μM; kidney function biomarker; non-enzymatic detection challenges

### 4.2 Electrolytes: Na⁺, K⁺, Ca²⁺, NH₄⁺, pH (~700 words)
- Na⁺: 120-160 mM (ISF); hyponatremia/hypernatremia diagnosis; ISE with monensin ionophore
- K⁺: 3.5-5.5 mM; cardiac arrhythmia risk at >6 mM; valinomycin-based ISE
- Ca²⁺: 1.0-1.35 mM ionized; muscle function, coagulation; calcium ionophore II
- pH: 7.35-7.45; metabolic acidosis indicator; IrOx potentiometric sensor
- Sweat vs. ISF comparison: ISF electrolytes better correlate with blood; sweat prone to contamination
- Key paper: Molinero-Fernández 2023 ACS Sensors [V]

### 4.3 Stress and Immune Markers: Cortisol, Cytokines (~500 words)
- Cortisol: 5-25 ng/mL (ISF); diurnal rhythm; stress/HPA axis; EIS aptasensor detection
- IL-6: 0-10 pg/mL; infection/inflammation; ultra-low LOD required (<0.1 pg/mL)
- TNF-α: sepsis biomarker; MNA aptasensor proof-of-concept
- Key paper: Bakhshandeh 2024 Adv Mater [V] (Aptalyzer — cortisol in vivo)

### 4.4 Neurotransmitters: Dopamine, Serotonin (~400 words)
- Dopamine: 0.01-1 μM (ISF); Parkinson's, reward pathway; FSCV detection
- Serotonin: gut-brain axis; depression monitoring
- FSCV 400 V/s scan rate requirement: wearable implementation challenges
- Key paper: Yu Z 2022 Anal Chem [V] (ANN-guided drug monitoring, neurotransmitter context)

### 4.5 Pharmacokinetic Monitoring (~500 words)
- Therapeutic drug monitoring: vancomycin, methotrexate, levodopa; tight therapeutic windows
- ISF-plasma ratio for drugs: typically 0.7-1.0 for unbound fraction
- Aptasensor approach: sequence-specific binding for drug molecules
- Key paper: Reynoso 2024 Biosens Bioelectron [V] (3D-printed aptamer MNA pharmacokinetics)
- Closed-loop implications: real-time drug level → dosing adjustment (§6.4)

---

## Section 5: Signal Conditioning and Wearable Circuit Integration
**Word target:** 2,500 | **Planned citations:** 18-22 | **Key claim:** The mechanical and electrical co-design of flexible circuits and wireless modules is the rate-limiting engineering challenge in transitioning MNA sensors from laboratory to wearable devices.

### 5.1 Flexible Substrate Engineering and Skin-Conformal Design (~600 words)
- Substrate materials: PI (Kapton), PET, PDMS; Young's modulus matching to skin (~130 kPa)
- Serpentine trace design: strain relief under 30% elongation
- Multi-layer stack: substrate / adhesive / electrode metal / dielectric / top encapsulation
- Key considerations: thermal expansion mismatch, delamination under sweat exposure
- Skin adhesive: acrylic medical adhesive; wear time >7 days without irritation
- Key paper: Tehrani 2022 Nat Biomed Eng [V] (FPCB integration in first complete system)

### 5.2 Analog Front-End: Potentiostat Circuits and Low-Noise Design (~700 words)
- Three-electrode potentiostat: working, counter, reference; control amplifier maintains E_WE-RE = V_applied
- Transimpedance amplifier (TIA): converts current → voltage; gain = R_f; noise floor: i_noise = √(4kT/R_f + i_n²)
- Multi-channel AFE: time-division multiplexing vs. simultaneous multi-channel readout; TDM: 1 ADC, multiple mux; simultaneous: N ADCs required
- ASIC integration: custom IC for sub-nW per channel; AD5941 (ADI) as commercial reference
- Key paper: Akram 2024 IEEE ISSCC [V] (3.7 nW potentiostat IC — state-of-the-art power figure)
- Dynamic range: 1 nA – 10 μA for typical MNA sensors; 16-bit ADC resolution target
- EMI shielding: essential for worn device (body-noise pickup, motion artifact)

### 5.3 Wireless Communication Protocols (~600 words)
- BLE 5.0: 1-2 Mbps, <10 mW, >10 m range; dominant protocol for CGM (Dexcom, Abbott)
- NFC: 13.56 MHz, passive operation (zero power for sensor), <10 cm range; suitable for infrequent reads
- WiFi 802.11n: high bandwidth but >100 mW — unsuitable for continuous wearable
- LoRa: >1 km range, <100 mW; suitable for agricultural/industrial, not personal health
- Protocol selection guide: continuous monitoring → BLE; implant → NFC or IMD band; remote area → LoRa
- Antenna design on flex substrate: meandered dipole; SAR compliance (FCC 47 CFR Part 15)

### 5.4 Power Management and Energy Harvesting (~600 words)
- Battery options: LiPo (high energy density, rechargeable), primary lithium (long shelf life)
- Target: <10 mW continuous for CGM patch (7-day battery life from coin cell)
- Energy harvesting: TENG (triboelectric nanogenerator) — motion-powered; OCV 100-400 V, but low average power
- BFC (biofuel cell): glucose/O₂ in ISF → up to 1 mW/cm²; self-powered sensor concept
- Wireless charging: Qi standard (5 W) at 100-200 kHz; coil integration in patch
- Power states: active measurement → BLE transmit → deep sleep; duty cycle optimization
- Key paper: Liu Y 2025 Adv Sci [V] (power management in closed-loop pancreas patch)

---

## Section 6: Embedded Intelligence and Terminal Systems
**Word target:** 2,500 | **Planned citations:** 16-20 | **Key claim:** Embedded intelligence — from on-device signal processing to edge AI inference — is the differentiating layer that elevates raw electrochemical signals into clinically actionable health insights.

### 6.1 On-Device Signal Processing: Noise Filtering and Drift Correction (~500 words)
- Motion artifact: accelerometer-coupled adaptive filter; LMS algorithm for artifact subtraction
- Baseline drift: polynomial baseline subtraction; Kalman filter for slow drift tracking
- Biofouling-induced drift: exponential decay model; compensated by periodic reference re-baseline
- DSP implementation: ARM Cortex-M4 FPU for IIR/FIR filter; 50 Hz sampling adequate for metabolites
- Key paper: Fan P 2026 Nat Commun [V] (in-sensor edge computing with integrated signal processing)

### 6.2 Calibration Algorithms: Factory, In-Situ, and Personalized ML (~600 words)
- Factory calibration: lot-specific calibration curve stored in MCU EEPROM; valid 7-14 days
- Two-point in-situ calibration: pre-wear blood glucose + 2-hour post-wear; reduces MARD by ~30%
- Adaptive calibration: continuous Bayesian update using blood reference measurements
- ML personalization: LSTM/transformer on individual metabolic pattern → personalized calibration curve
- Key paper: Yang J 2023 ACS Sensors [V] (14-day CGM MARD 10.2% — factory calibration benchmark)
- Key paper: Li X 2025 Innovation [V] (self-calibrating 9-analyte array)
- Target MARD: <10% (Class III CGM standard); <15% acceptable for non-glucose analytes

### 6.3 Edge AI: Anomaly Detection and Predictive Analytics (~600 words)
- Hypoglycemia prediction: LSTM on CGM time series; 30-minute prediction horizon; sensitivity >85%
- Sepsis early warning: multi-analyte anomaly score (lactate + pH + Na⁺); ROC AUC target >0.90
- Atrial fibrillation-like detection from electrochemical rhythm patterns
- TinyML deployment: TensorFlow Lite for Microcontrollers (TFLM); ARM Cortex-M7 capable
- Memory budget: <512 KB SRAM for inference; quantized INT8 models
- Key paper: Fan P 2026 Nat Commun [V] (in-sensor edge computing)
- Key paper: Yu Z 2022 Anal Chem [V] (ANN for Parkinson's drug management)

### 6.4 Cloud Connectivity and Digital Health Platforms (~400 words)
- Architecture: BLE → smartphone → cloud; or direct LTE-M/NB-IoT for independent devices
- Data security: AES-128 encryption; HIPAA/GDPR compliance for patient data
- Digital twin concept: cloud model updated with individual wear data for long-term health tracking
- Key paper: Liu Y 2025 Adv Sci [V] (cloud-connected closed-loop insulin delivery)
- Key paper: Huang X 2024 Theranostics [V] (cloud-enabled electronic/fluidic MNA insulin delivery)

### 6.5 Clinical-Grade Data Quality Assurance (~400 words)
- CGM accuracy standard: ISO 15197:2015 — 95% of readings within ±15 mg/dL or ±15%
- Clarke Error Grid Analysis: Zone A + B acceptable; Zone D/E unacceptable for closed-loop
- Data completeness: >90% uptime required for clinical CGM approval
- Sensor failure detection: anomaly flag when signal-to-noise drops below threshold
- Post-market surveillance requirement: real-world performance data collection

---

## Section 7: Challenges and Future Perspectives
**Word target:** 2,000 | **Planned citations:** 16-20 | **Key claim:** The translation of MNA electrochemical sensors from research demonstrations to cleared wearable medical devices requires resolving three interconnected challenges: biofouling, calibration accuracy, and regulatory compliance.

### 7.1 Biofouling, Protein Adsorption, and Long-Term Stability (~500 words)
- Protein adsorption on electrode surface: fibrinogen, albumin — blocks enzyme access, reduces sensitivity by 30-70% within 24h
- Anti-biofouling strategies: zwitterionic polymers (MPC, SBMA), PEG brushes, lubricin coating
- ISF capsule formation: implant-type fibrous encapsulation from day 3-7; less severe for MNA (daily replacement)
- Enzyme stability in ISF environment: GOx half-life in vivo 7-14 days; LOx more labile
- Key paper: Zhou 2024 ACS Nano [V] (zwitterionic hydrogel anti-biofouling)
- Future direction: stimuli-responsive anti-fouling coatings; self-cleaning electrode surfaces

### 7.2 ISF-Blood Glucose Lag and Calibration Accuracy (~400 words)
- Physiological lag: glucose diffusion from capillaries to ISF → 5-15 min lag during rapid glucose changes
- Algorithmic compensation: predictive algorithms using glucose rate-of-change (dG/dt)
- MARD during meals (rapid glucose rise): significantly higher than fasting MARD
- Factory vs. individual calibration: inter-individual variability in ISF-blood ratio (0.7-1.1)
- Future direction: wearable blood reference integration; AI-based lag compensation

### 7.3 Regulatory Pathways: FDA 510(k) and CE Marking (~400 words)
- FDA: Class III CGM device under 21 CFR Part 870; De Novo pathway for novel MNA-based sensors
- 510(k) predicate: Dexcom G7, Abbott FreeStyle Libre for glucose; no cleared predicate for multi-analyte
- CE marking: EU IVDR 2022/746 (replaced IVD Directive 98/79/EC from May 2022)
- Notified Body assessment: clinical evidence requirements significantly increased under IVDR
- Timeline benchmark: typical FDA CGM clearance timeline 18-24 months from submission
- Key challenge: multi-analyte MNA systems have no cleared predicate → De Novo required

### 7.4 Manufacturing Scalability and Cost Reduction (~300 words)
- Current bottleneck: enzyme immobilization step is manual and low-throughput
- Roll-to-roll FPCB: scalable to 1000s of patches/day; electrode deposition included
- Target cost: <$5/device for disposable daily-replacement patch
- Quality control: impedance spectroscopy as 100% inline QC for electrode integrity

### 7.5 Future Directions (~400 words)
- Closed-loop therapy integration: MNA glucose sensor → insulin pump actuator (artificial pancreas)
- Multi-modal sensing: combine electrochemical + optical (PPG, SpO₂) + mechanical (pulse wave)
- Autonomous health AI: continuous multi-analyte data → personalized health score → proactive intervention
- Synthetic biology integration: engineered cells on MNA surface as ultra-selective biosensors
- In-body power generation: BFC powered by ISF glucose + O₂ for self-powered sensing
- Single-patient longitudinal monitoring: weeks-to-months of continuous data enabling new physiology insights

---

## Section 8: Conclusion
**Word target:** 500 | **Planned citations:** 3-5

**Structure:**
1. Three key takeaways (not a section summary):
   - The full-chain integration of fabrication, electrochemistry, circuit design, and embedded intelligence has enabled the first generation of clinically-validated wearable MNA sensors
   - Multi-analyte multiplexed MNA systems with edge AI represent the frontier capability, with Li et al. 2025 [V] demonstrating 9-analyte self-calibrating operation
   - The field is converging toward closed-loop therapeutic devices, but clinical translation requires resolving biofouling, calibration accuracy, and regulatory pathway challenges

2. Future vision: "The next decade will likely see wearable MNA-based sensing systems transition from single-analyte research tools to multi-modal, AI-augmented clinical devices capable of continuous, personalized health management — provided the engineering community addresses the remaining full-chain integration challenges identified in this review."

---

## Appendix: Logical Flow Validation

| Check | Result |
|-------|--------|
| §1 establishes problem solved by §2-6 | ✓ |
| Each section has ≥2 forward-looking sentences to next section | Plan: yes |
| §2 (fabrication) directly enables §3 (sensing) | ✓ |
| §3 (sensing) directly enables §4 (biomarkers) | ✓ |
| §4 (biomarkers) motivates §5 (circuit requirements) | ✓ |
| §5 (circuits) provides foundation for §6 (intelligence) | ✓ |
| §7 (challenges) references all prior sections | ✓ |
| Unique contribution claim in §1.4 is reflected in section structure | ✓ |
| Target journal scope match (B&B: "research to clinical practice") | ✓ |

---

*SCI-writer Stage 1 | paper_outline.md | Word budget total: 17,000 planned (buffer for compression)*
