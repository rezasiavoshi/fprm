# QC Chemical Laboratory — Test Lead-Time Catalogue

Source: `data/Leadtime.xlsx` (28 sheets). Converted with `tools/leadtime_to_md.py`. All times are analyst hands-on/elapsed minutes per sample as recorded in the workbook.

## 1. Analysis summary

| Metric | Value |
|---|---|
| Materials listed (Premix + A–Z sheets) | 550 |
| Materials with a time estimate | 174 (31%) |
| Materials without data (`-` or blank) | 376 |
| Total time per material — median | 308 min (5.1 h) |
| Total time per material — mean | 478 min (8.0 h) |
| Total time per material — min / max | 1 / 2608 min |
| Sum over all timed materials (one sample each) | 83,181 min (1,386 h) |
| Share of time in general vs specific tests | 28% general / 72% specific |
| General test types catalogued | 50 |

### 1.1 Coverage by sheet

| Sheet | Materials | With time | Coverage | Median total (min) | Max total (min) |
|---|---:|---:|---:|---:|---:|
| Permix | 21 | 16 | 76% | 608 | 2608 |
| A | 32 | 9 | 28% | 366 | 1003 |
| B | 36 | 8 | 22% | 364 | 821 |
| C | 48 | 17 | 35% | 311 | 1086 |
| D | 15 | 5 | 33% | 486 | 1001 |
| E | 18 | 10 | 55% | 664 | 1106 |
| F | 16 | 3 | 18% | 1161 | 1176 |
| G | 23 | 6 | 26% | 412 | 854 |
| H | 24 | 7 | 29% | 251 | 861 |
| I | 10 | 0 | 0% | – | – |
| J | 1 | 1 | 100% | 213 | 213 |
| L | 50 | 13 | 26% | 276 | 1606 |
| K | 5 | 1 | 20% | 766 | 766 |
| M | 42 | 14 | 33% | 226 | 956 |
| N | 6 | 2 | 33% | 696 | 1061 |
| O | 10 | 3 | 30% | 22 | 166 |
| Q | 1 | 0 | 0% | – | – |
| P | 48 | 10 | 20% | 218 | 883 |
| R | 16 | 1 | 6% | 319 | 319 |
| S | 58 | 18 | 31% | 278 | 1249 |
| T | 19 | 8 | 42% | 220 | 716 |
| U | 2 | 1 | 50% | 611 | 611 |
| V | 31 | 16 | 51% | 484 | 1186 |
| W | 6 | 0 | 0% | – | – |
| X | 3 | 1 | 33% | 166 | 166 |
| Y | 4 | 1 | 25% | 16 | 16 |
| Z | 5 | 3 | 60% | 214 | 236 |

### 1.2 Time-band distribution (timed materials)

| Band | Materials |
|---|---:|
| ≤ 2 h | 22 |
| 2–8 h (≤ 1 shift) | 86 |
| 8–24 h | 62 |
| 1–2 days | 4 |
| > 2 days | 0 |

### 1.3 Longest 15 materials (main capacity drivers)

| # | Sheet | Material | Specific tests | Total (min) | Total (h) |
|---:|---|---|---|---:|---:|
| 1 | Permix | Premix Xade | Assay E,Siberian Ginseng,Tribulus,Epimedium,Panax Ginseng,Viamin B Group | 2608 | 43.5 |
| 2 | Permix | Premix EnergeX | Assay E, Assay Silymarin,Tribulus,Ginkgo biloba,Damiana,Viamin B Group,Vitamin B12, Vitamin B5 | 2506 | 41.8 |
| 3 | Permix | Premix PregnaLife | Assay E,Vitamin B1,Vitamin B2,Vitamin B5,Vitamin B7,Vitamin B12,Ubidecarenone, Vitamin C | 1981 | 33.0 |
| 4 | L | L-Menthol | Limit of nonvolatile residue- Readly oxidizable substance in dl-menthol-Congealing range of dl-menthol | 1606 | 26.8 |
| 5 | Permix | Premix Optiwoman | Assay E,Vitamin B Group,Siberian Ginseng,Panax Ginseng,Biotin | 1378 | 23.0 |
| 6 | Permix | Premix Healthy Liver | Assay Artichoke-Assay milk thistle | 1306 | 21.8 |
| 7 | S | Silybum Marianum (Milk Thistle Ext.) Dry Conc 70:1 | Identification-Assay | 1249 | 20.8 |
| 8 | S | Sodium Citrate | Identification A- Identification B- Identification C- Assay- Tartrate- | 1226 | 20.4 |
| 9 | V | Vitamin B1 (Thiamin HCL) | Identification B- Assay- Limit on nitrate- Related compound- Absorbance of solution | 1186 | 19.8 |
| 10 | F | Ferrous Fumarate | Identifiction B-Assay-Sulfate- Limit of ferric Iron | 1176 | 19.6 |
| 11 | Permix | Premix Burning Fat | Assay Garcinia Quaesita Fruit-TLCGymnema Sylvestre-Coleus Forskohlii- Vitamin B6 | 1171 | 19.5 |
| 12 | L | Linagliptin (Morepen) | Assay-Related compounds | 1171 | 19.5 |
| 13 | F | Fluticasone Propionate Micronized | Assay-Impurity | 1161 | 19.4 |
| 14 | Permix | Premix Kamasotra | Assay Siberian ginseng-Korean ginseng | 1153 | 19.2 |
| 15 | E | Empagliflozin (Alborz Pharmed) | Assay-Related substance | 1106 | 18.4 |

### 1.4 Data-quality observations

- 376 of 550 materials (68%) have no time estimate — the catalogue cannot yet support a full workload model.
- Duplicate entries in the General Test list with different times: Acid value.
- 7 materials list specific tests but no specific-test time, so their total is understated: Premix Sleep Care (Permix), Honey Flovour (H), Methyl Sulphonyl Methan 99.4% (MSM) (M), Mannitol (M), Omega 3 (Flaxed Oil) (O), Orange Flavour Powder (Firmenich 05605TP0551) (O), Xanthan Gum (X).
- Sheet W has no Total column; totals were computed as General + Specific.
- Times are per test set, not per analyst-hour: long items (LOD 24 h, water absorption 48 h, multi-assay HPLC premixes) include unattended instrument/oven time, so hands-on vs elapsed time must be separated before FTE calculations.
- Spelling variants (e.g. ‘Apperance’, ‘Soluibility’, ‘Mangnesium’) kept as in the source.

## 2. General test time catalogue

| # | Test | Time (min) |
|---:|---|---:|
| 1 | Description | 1 |
| 2 | Soluibility | 15 |
| 3 | Saponification | 140 |
| 4 | Acid value | 30 |
| 5 | Acidity/Alkalinity | 30 |
| 6 | Optical rotation | 15 |
| 7 | LOD (60 min) | 70 |
| 8 | LOD (24 h) | 1450 |
| 9 | Water absortion (48 h) | 2890 |
| 10 | Ash | 80 |
| 11 | Sulfate | 15 |
| 12 | Chloride | 15 |
| 13 | Sodium | 25 |
| 14 | Conductivity | 10 |
| 15 | Phosphate | 15 |
| 16 | Zinc | 30 |
| 17 | Calcium | 30 |
| 18 | Mangnesium | 10 |
| 19 | Sulfate/chloride limit | 20 |
| 20 | Hydroxyl value | 70 |
| 21 | Peroxide value | 15 |
| 22 | Ester value | 5 |
| 23 | Dissolution | 30 |
| 24 | Water content | 20 |
| 25 | Melting point | 15 |
| 26 | Density Bulk | 10 |
| 27 | Density Tapped | 45 |
| 28 | Particle size | 30 |
| 29 | TLC (herbal) | 30 |
| 30 | TLC (drug) | 30 |
| 31 | Residue on evaporation | 105 |
| 32 | Water in soluble, soluble | 90 |
| 33 | Acid in soluble, soluble | 90 |
| 34 | Settling volume | 30 |
| 35 | Iodine | 10 |
| 36 | Iron | 10 |
| 37 | Carbonate | 10 |
| 38 | Copper | 15 |
| 39 | Manganese | 10 |
| 40 | Ogxalate | 10 |
| 41 | Potassium | 30 |
| 42 | Desnsity | 10 |
| 43 | Wash early | 60 |
| 44 | final wash | 120 |
| 45 | pH | 15 |
| 46 | Mercury | 25 |
| 47 | Clarity of solution | 60 |
| 48 | Color of Solution | 60 |
| 49 | SPECIFIC GRAVITY | 15 |
| 50 | Acid value | 25 |

## 3. Material test-time tables

### Sheet Permix

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Premix Optiwoman | Apperance | Assay E,Vitamin B Group,Siberian Ginseng,Panax Ginseng,Biotin | 1 | 1377 | 1378 |
| Premix Uromax | Apperance | Assay cranberry,Assay Vitamin C, | 1 | 210 | 211 |
| Premix Sleep Care | Apperance | Valeriana officinalis- Passiflora incammate | 1 | - | 1 |
| Premix EnergeX | Apperance | Assay E, Assay Silymarin,Tribulus,Ginkgo biloba,Damiana,Viamin B Group,Vitamin B12, Vitamin B5 | 1 | 2505 | 2506 |
| Premix Xade | Apperance | Assay E,Siberian Ginseng,Tribulus,Epimedium,Panax Ginseng,Viamin B Group | 1 | 2607 | 2608 |
| Premix Burning Fat | Apperance | Assay Garcinia Quaesita Fruit-TLCGymnema Sylvestre-Coleus Forskohlii- Vitamin B6 | 1 | 1170 | 1171 |
| Premix PregnaLife | Apperance | Assay E,Vitamin B1,Vitamin B2,Vitamin B5,Vitamin B7,Vitamin B12,Ubidecarenone, Vitamin C | 1 | 1980 | 1981 |
| Premix Prostica | Apperance | - | - | - | - |
| Premix Painlys | Apperance | - | - | - | - |
| Premix Ginc Active | Apperance | Assay Ginkgo biloba | 1 | 405 | 406 |
| Premix Digestive Aid | Apperance | TLC Ginger-Gentian- marshmellow-Liquorice | 1 | 615 | 616 |
| Premix DermoBella | Apperance | Assay Vitamin C- Vitamin E- Biotin | 1 | 600 | 601 |
| Premix CelerX Forte | Apperance | Assay Apium- TLC juniper | 1 | 465 | 466 |
| Premix Feroral | Apperance | Assay Ferrous fumarate- Folic Acid | 1 | 450 | 451 |
| Premix Kamasotra | Apperance | Assay Siberian ginseng-Korean ginseng | 1 | 1152 | 1153 |
| Premix Co Enzyme Q10 30mg | - | - | - | - | - |
| Premix Co Enzyme Q10 100mg | - | - | - | - | - |
| Premix Maxi CareX | Apperance | Assay VitaminC- Assay zinc gluconate | 1 | 120 | 121 |
| Premix Healthy Liver | Apperance | Assay Artichoke-Assay milk thistle | 1 | 1305 | 1306 |
| Premix Vitacal Forte | Apperance | Assay K1-Copper gluconate | 1 | 330 | 331 |
| Premix Comfort Formula (Relaxation Formula) | - | - | - | - | - |

### Sheet A

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Acacia Gum | - | - | - | - | - |
| Acesulfate | - | - | - | - | - |
| Acetaminophen | Appearance- Solubility-LOSS ON DRYING | Assay- ROI-LIMIT OF FREE 4-AMINOPHENOL-ORGANIC IMPURITIES | 86 | 917 | 1003 |
| Acetaminphon DC (Temad) | - | - | - | - | - |
| Acetic Acid | - | - | - | - | - |
| Acetic Onhydride | - | - | - | - | - |
| Acetoxy Empagliflozin | - | - | - | - | - |
| Acorus Tatarinowii Dried Rhizome | - | - | - | - | - |
| Alginic Acid | - | - | - | - | - |
| Allura Red | Appearance-Solubility-MERCURY | ASSAY-WATER-SOLUBLE SUBSTANCES-ACID-INSOLUBLE SUBSTANCES-ORGANIC COLORS AND LAKES | 41 | 325 | 366 |
| Aloevera Ext. | - | - | - | - | - |
| Alpha Lipoic Acid | - | - | - | - | - |
| Aluminium Hydroxid | - | - | - | - | - |
| Amlodipine Besylate | Appearance-Solubility-Water determination-Sulfate Ash-Optical rotation | - | - | 131 | 131 |
| Amomonium Dihydrogen Phosphate | - | - | - | - | - |
| Angelica Sinensis Dried Root | - | - | - | - | - |
| Apium Graveolens (Celery Seed Ext.) | Appearance-Particle size-Loss on Drying-Ash | Assay | 181 | 360 | 541 |
| Apixaban | - | - | - | - | - |
| Apixaban Granule Ready to Press(parsian) | Appearance- Solubility-LOSS ON DRYING-Water determination-Tap density- Bulk Density- | Identification-Assay- Dissolution | 161 | 495 | 656 |
| Apixaban Granule Ready to Press(tofigh Darou) | - | - | - | - | - |
| Apple Green | Appearance-Solubility | - | 16 | - | 16 |
| AshwagandhaExt. | - | - | - | - | - |
| Aspargine | - | - | - | - | - |
| Aspartam | - | - | - | - | - |
| Aspartic Acid | - | - | - | - | - |
| Astaxanthin | - | - | - | - | - |
| Astragalus Membranceus  Dried Root | - | - | - | - | - |
| Avacado Ext. | - | - | - | - | - |
| Avacado/Soy Bean Unsaponifiables Ext. | - | - | - | - | - |
| Azelastine HCL (MSN) | Appearance- Solubility-  ROI- LOD-Acidity or alkalinity | Identification B- Identification C- ORGANIC IMPURITIE | 196 | 240 | 436 |
| Avicel RC 591 | Appearance- Solubility-ROI-pH- LOD- Bulk density- PARTICLE SIZE DISTRIBUTION-WATER-SOLUBLE SUBSTANCES-ETHER SOLUBLE SUBSTANCES- | Identification B- Identification c- Conductivity- | 241 | 65 | 306 |
| Avicel CE15 | Appearance- Solubility-ROI-pH- LOD- Bulk density- PARTICLE SIZE DISTRIBUTION-WATER-SOLUBLE SUBSTANCES-ETHER SOLUBLE SUBSTANCES- | Identification B- Identification c- Conductivity- | 241 | 65 | 306 |

### Sheet B

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Bacopa Ext. | - | - | - | - | - |
| B-Alanine | Appearance- Solubility-ROI- Chloride- Sulfate- pH- LOD | Assay-OPTICAL ROTATION | 141 | 45 | 186 |
| Banana Flovour | - | - | - | - | - |
| Beta Carotene 10% | Appearance- Solubility-LOD- ROI | Identification A-Identification B-CONTENT OF TOTAL CAROTENOIDS- | 336 | 60 | 396 |
| Black Currant Ext. | - | - | - | - | - |
| Black Elderberry Ext. | - | - | - | - | - |
| Bee Propolis | - | - | - | - | - |
| Broccoli Ext. | - | - | - | - | - |
| Black Pepper Ext. | - | - | - | - | - |
| Bioflavonoids | - | - | - | - | - |
| Black Cumim seed | - | - | - | - | - |
| Bitter Melon Ext. | - | - | - | - | - |
| Brich Leaf Ext. | - | - | - | - | - |
| Bromelain Ext. | - | - | - | - | - |
| Borax | Appearance- Solubility- | Sodium-Borate- Assay- CARBONATE AND BICARBONATE- | 16 | 75 | 91 |
| Bromelian | - | - | - | - | - |
| BCAA | - | - | - | - | - |
| Benfotiamine | - | - | - | - | - |
| Betadex Sulfobutyl Ether Sodium- | - | - | - | - | - |
| Bempedoic Acid | Appearance- Solubility- ROI-Water determination- | Related substance- Assay- | 116 | 705 | 821 |
| Budesonide Micronized | - | - | - | - | - |
| Bifidobacterium Lactis | - | - | - | - | - |
| Bifidobacterium Bifidum | - | - | - | - | - |
| Bifidobacterium Longum | - | - | - | - | - |
| Bifidobacterium Infantis | - | - | - | - | - |
| Beet Root | - | - | - | - | - |
| Berberine Hcl | - | - | - | - | - |
| Boswellia Flovour | - | - | - | - | - |
| Benzyl Alcohol | - | - | - | - | - |
| Benzalkonium Chloride | Appearance- Solubility- Identification A- Identificatin B- Chloride- ROI- Acidity or Alkalinity-Water determination- WATER-INSOLUBLE MATTER | Assay | 291 | 200 | 491 |
| Butylated Hydroxy Anisole (BHA) | - | - | - | - | - |
| Berry Flovour | - | - | - | - | - |
| Brilliant Blue | Appearance- Solubility- Water determination | - | 36 | - | 36 |
| Black Iron Oxide | Appearance-Solubility-WATER-SOLUBLE SUBSTANCES-ACID-INSOLUBLE SUBSTANCES-ORGANIC COLORS AND LAKES | Assay-Identification A | 246 | 90 | 336 |
| Brown  Color - Code 1005 | - | - | - | - | - |
| BurningFat Marketing Sachet | Appearance | Assay Garcinia- Assay Gymnema-Assay Coleus- | 1 | 390 | 391 |

### Sheet C

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Cynara Scolymus (Globe Artichoke Ext.) Dry Conc 25:1 | Appearance- Odour- Colour- Taste- Particle size- LOD- Ash-Solubility | Assay | 184 | 480 | 664 |
| Choleus Forskohlii Ext. Dry Conc 110:1 | Appearance-Colour-Taste- Particle size-LOD- Ash- bulk denity- Tap density | Identifiction-Assay- | 238 | 525 | 763 |
| Carnaubawax | - | - | - | - | - |
| Citrous | - | - | - | - | - |
| Caviar Liquid | - | - | - | - | - |
| Carthamus Tinctorius Dried Flower | - | - | - | - | - |
| Coconut Oil Powder | - | - | - | - | - |
| Chromium Picolinate | Appearance- Solubility- Chloride- Sulfate-LOSS ON DRYING | Identification B | 281 | 30 | 311 |
| Choline Bitartrate | Appearance- Solubility-RESIDUE ON IGNITION-OPTICAL ROTATION- PH- WATER DETERMINATION | Identification B | 146 | 30 | 176 |
| Choline Chloride | - | - | - | - | - |
| Calcium Carbonate (Heavy) | Appearance- Solubility-ACID-INSOLUBLE SUBSTANCES- BARIUM- IRON- LEAD- LIMIT OF MAGNESIUM AND ALKALI SALTS-  LOSS ON DRYING | Identification- Assay | 436 | 90 | 526 |
| Copper Gluconate | Appearance- Solubility- Chloride- Sulfate- | Identification A- Identification B- Assay- REDUCING SUBSTANCES | 46 | 125 | 171 |
| Citric Acid Anhydrous | Appearance- Solubility- ROI- Sulfate-COLOR OF SOLUTION- CLARITY OF SOLUTION-CLARITY OF SOLUTION | Assay-LIMIT OF OXALIC ACID | 231 | 60 | 291 |
| Copper Sulfate | - | - | - | - | - |
| Calcium Palmitate | - | - | - | - | - |
| Carmoisime Lake | - | - | - | - | - |
| Calcium Carbonate | - | - | - | - | - |
| Calcium Stearate | - | - | - | - | - |
| Calcium Ascorbate | - | - | - | - | - |
| Caffeine | Appearance- Solubility- RESIDUE ON IGNITION-WATER DETERMINATION | Identification B- Assay-ORGANIC IMPURITIES | 356 | 730 | 1086 |
| Carbetosin | - | - | - | - | - |
| Citicoline | - | - | - | - | - |
| Chlorpheniramin Maleate | Appearance- Solubility- RESIDUE ON IGNITION-LOSS ON DRYING- OPTICAL ROTATION- | Assay- Identification B- ORGANIC IMPURITIES | 181 | 820 | 1001 |
| Corn Starch 1500 Pregelatin | Appearance- Solubility- RESIDUE ON IGNITION- LOD- pH | Identification B- Identification C-LIMIT OF IRON-LIMIT OF OXIDIZING SUBSTANCES | 111 | 95 | 206 |
| Citric Acid | - | - | - | - | - |
| Cross Carmellose Sodium | Appearance- Solubility- RESIDUE ON IGNITION- LOSS ON DRYING- SETTLING VOLUME- pH | Identification B- Identification C- SODIUM CHLORIDE AND SODIUM GLYCOLATE- CONTENT OF WATER-SOLUBLE MATERIAL- DEGREE OF SUBSTITUTION- | 181 | 385 | 566 |
| Crosspovidone A | Appearance- Solubility- RESIDUE ON IGNITION- LOD- pH- LOSS ON DRYING- WATER-SOLUBLE SUBSTANCES | Identification B- Identification C- Identification D-  NITROGEN DETERMINATION- | 271 | 90 | 361 |
| Carbomer 940 | - | - | - | - | - |
| Corn Starch | Appearance- Solubility- RESIDUE ON IGNITION- LOD- pH | Identification B- Identification C-LIMIT OF IRON-LIMIT OF OXIDIZING SUBSTANCES | 111 | 95 | 206 |
| Calcium Hydrogen Phosphate | Appearance- Solubility- Carbonate- Sulfate- Chloride- LIMIT OF ACID-INSOLUBLE SUBSTANCES-Barium-LOSS ON IGNITION | Identification A- Identification B- Assay- | 226 | 85 | 311 |
| Calcium Hydrogen Phosphate (DC Grade) | - | - | - | - | - |
| Chocolate Mint Flovour | - | - | - | - | - |
| Camphor Flovour | - | - | - | - | - |
| Conjugated Linoleic Acid | - | - | - | - | - |
| Cetyl Alcohol | - | - | - | - | - |
| Corn Syrup Solid | - | - | - | - | - |
| Chasteberry Powder | - | - | - | - | - |
| Condexsed Milk Flavour | - | - | - | - | - |
| Compritol 888 ATO (Glyceryl Dibehenate) | Appearance- Solubility- MELTING RANGE OR TEMPERATURE- RESIDUE ON IGNITION-WATER DETERMINATION | Acid Value | 111 | 45 | 156 |
| Calcium Carbonate Light | - | - | - | - | - |
| Carboxymethyl Cellulose Sodium | - | - | - | - | - |
| Chocolate Flavour | - | - | - | - | - |
| Cola Flavour Powder | - | - | - | - | - |
| Caramel Powder Essence | Appearance- Solubility-Water insoluble | - | 106 | - | 106 |
| Caraml | Appearance- Solubility-Water insoluble | - | 106 | - | 106 |
| Comfort Formula Marketing Sachet | - | - | - | - | - |
| Co Enzyme Q10 30mg Marketing Sachet | - | - | - | - | - |
| Co Enzyme Q10 100mg Marketing Sachet | - | - | - | - | - |

### Sheet D

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| D-Mannose | - | - | - | - | - |
| Digestive Enzyme Blended | - | - | - | - | - |
| D-Biotin | Appearance- Solubility- Identification B- Identification C- OPTICAL ROTATION-Melting range-Sulfated Ash- | Assay- RELATED COMPOUNDS-Solution color and clarity | 166 | 320 | 486 |
| Dapagliflozine Propanediol Monohydrate (Tofigh Darou) | Appearance- Solubility- melting point- Water determination- Residue on ignition | Assay- Related Substance | 131 | 600 | 731 |
| Dapagliflozine Propanediol Monohydrate (Alborz Darou) | - | - | - | - | - |
| Dapagliflozine Propanediol Monohydrate (Parsian) | Appearance- Solubility- melting point- Water determination- Residue on ignition | Assay- Related Compound | 131 | 300 | 431 |
| Dextromethorphan | Appearance- Solubility- Melting point- Optical rotation- Appearance of solution-Acidity or alkalinity-Water (KF)-Sulfated ash | Assay- Related Substane | 206 | 210 | 416 |
| Diphenhydramine | Appearance- Solubility- Identification B- Identification C- Residue on ignition- ACIDITY OR ALKALINITY- LOSS ON DRYING | Assay- Organic Impurities | 211 | 790 | 1001 |
| Divalproex sodium | - | - | - | - | - |
| Dulaglutide | - | - | - | - | - |
| Dexlansoprazole Pellets 22.5 % | - | - | - | - | - |
| DIsodium Phosphate Dihydrate | - | - | - | - | - |
| Dicalcium Phosphat Anhydrous | - | - | - | - | - |
| Digestive Aid Marketing Sachet | - | - | - | - | - |
| DermoBella Marketing Sachet | - | - | - | - | - |

### Sheet E

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Epimedium Grandiflorum (Horny Goat Weed Ext.) Dry Conc 20:1 | Appearance- Odor- taste- Particle size-Moisture- Ash content- Slack Density-Tight Density | Assay | 238 | 585 | 823 |
| Eleutherococuss Senticosus (Siberian Ginseng Ext.) Dry Conc 5:1 | Appearance- Odor- taste-Colour- Particle Size-Ash content- Loss on Drying | Identification- Assay | 184 | 480 | 664 |
| Evening Primrose Oil | - | - | - | - | - |
| Echinacea | Appearance- Odour- Taste- Colour-Particle Size- Ash content- Loss on drying | Identification- Assay | 184 | 480 | 664 |
| Empagliflozin (Alborz Pharmed) | Appearance- Solubility-Melting point- Loss on drying- Residue on ignition- Optical rotation- Particle size | Assay-Related substance | 226 | 880 | 1106 |
| Empagliflozin (Morepen) | Appearance- Solubility- Water determination- Residue on ignition- Specific optical rotation | Identification B- Related Substances- Assay | 131 | 944 | 1075 |
| Empagliflozin (Parsian) | Appearance- solubility- Melting point- Water determination -Specific optical rotation-Residue on ignition | Related compound- Assay | 131 | 720 | 851 |
| Empagliflozin (Tofigh Darou) | - | - | - | - | - |
| Ertuglifluzin L-Pyroglutamin Acid | - | - | - | - | - |
| Ezetimibe (Chanyoo) | Appearance- Solubility- Residue on ignition- WATER DETERMINATION- OPTICAL ROTATION | - | 116 | - | 116 |
| Enzalutamide | - | - | - | - | - |
| Ethanol (Alcohol) | Appearance- Solubility- SPECIFIC GRAVITY- ULTRAVIOLET ABSORPTION-CLARITY OF SOLUTION- ACIDITY OR ALKALINITY-COLOR OF SOLUTION- | - | 201 | - | 201 |
| Eucalyptus Flovour | - | - | - | - | - |
| Ethyl Vanillin | - | - | - | - | - |
| Edetate Disodium | Appearance- Solubility- pH- Loss on drying | Identification B-Identification C- Assay-Calcium-Limitbof nitrilotriacetic acid - | 101 | 540 | 641 |
| Exacol Brown | Appearance- Solubility- Water Insoluble | - | 106 | - | 106 |
| Erythrosine Pink | - | - | - | - | - |
| EnergX Marketing Sachet | - | - | - | - | - |

### Sheet F

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Funiculum Vulgaris (Fennel Ext.) Dry Conc 5:1 | Appearance- Colour- Odour- Particle size- Loss on drying- Ash | Identification | 184 | 30 | 214 |
| Fucoidan Ext. (Brown Kelp) | - | - | - | - | - |
| Fish Collagen Powder | - | - | - | - | - |
| Fish Ext. | - | - | - | - | - |
| Fisetin | - | - | - | - | - |
| Ferrous Fumarate | Appearance- Solubility- Loss on drying | Identifiction B-Assay-Sulfate- Limit of ferric Iron | 86 | 1090 | 1176 |
| Fructooligosacaharides | - | - | - | - | - |
| Ferrous BisGlycinate 20% | - | - | - | - | - |
| Folic Acid 10% Powder | - | - | - | - | - |
| Folic Acid 10% with Maltodextrin | - | - | - | - | - |
| Fluticasone Valerate | - | - | - | - | - |
| Fluticasone Propionate Micronized | Appearance- Solubility- Water determination-Optical rotation- | Assay-Impurity | 51 | 1110 | 1161 |
| Famotidine | - | - | - | - | - |
| Ferrous Bisglycinate20 mg+Vitamin C90mg+Vitamin B12 0.0027mg+ Vitamin B6 1.3mg +Folic Acid0.4mg  Pellets | - | - | - | - | - |
| FD&C Blue dye No.1 | - | - | - | - | - |
| Feroral Marketing Sachet | - | - | - | - | - |

### Sheet G

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Gentiana Lutea (Gentian Ext.) Dry Conc 4:1 | Appearance- Colour- Odour- Particle size- Loss on drying- Ash content | Identification(TLC) | 184 | 30 | 214 |
| Gink Biloba (GinKgo Ext.) Dry Conc 50:1 | Appearance-Odour- Taste- Particle Size-Bulk density- Loss on Drying- Ash content | Identification- Assay | 194 | 660 | 854 |
| Glycyrrhiza Glabra (Liquorice Ext.) Dry Conc 8:1 | Appearance- Loss on drying- pH- Ash -Moisture- Particle Size- | Assay | 206 | 315 | 521 |
| Gymnema Sylvestre Leaf (Gymnema Ext.) Dry Conc 10:1 | Appearance- Colour- Odour- Particle Size- Loss on drying- Ash content-Acid Insoluble Ash | Identification | 274 | 30 | 304 |
| Garcinia Quaesita (Garcinia Ext.) Dry Conc 6:1 | Appearance-Colour-Odour-Taste-Particle Size- Water determination-Bulk density- Tap density | Assay | 109 | 450 | 559 |
| Garlic Powder | - | - | - | - | - |
| Green Tea Ext. | - | - | - | - | - |
| Green Coffee 50% Ext. | - | - | - | - | - |
| Guarana Caffein Ext. | - | - | - | - | - |
| Galanga Ext. | - | - | - | - | - |
| Genistein | - | - | - | - | - |
| Glutamine | - | - | - | - | - |
| Glimepride | - | - | - | - | - |
| Glycerine | Appearance- Solubility- Chloride- Sulfate-RESIDUE ON IGNITION-COLOR-SPECIFIC GRAVITY-Water determination | Assay- | 176 | 60 | 236 |
| Gelatin | - | - | - | - | - |
| Glucire 59/14 | - | - | - | - | - |
| Glucire 44.14 | - | - | - | - | - |
| Glucire 48/16 | - | - | - | - | - |
| Glucire 50/13 | - | - | - | - | - |
| Gold | - | - | - | - | - |
| Glyceryl Monocaprylocaprate | - | - | - | - | - |
| Green  Color - Code 611 | - | - | - | - | - |
| Ginc Active Marketing Sachet | - | - | - | - | - |

### Sheet H

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Harpagophytum Procombens (Devils Claw Ext.) Dry Conc 6:1 | Appearance- Colour- Odour-Particle Size-Loss on drying- Ash Content | Identification | 184 | 30 | 214 |
| Horehound | - | - | - | - | - |
| Horse Tail | - | - | - | - | - |
| Hiciscus Ext. | - | - | - | - | - |
| Histidine | - | - | - | - | - |
| Hydrolyzed Keratin | - | - | - | - | - |
| Hydrolized Gelatine | - | - | - | - | - |
| Hydroxy Trypto Phan (HTP) | - | - | - | - | - |
| Hyaluronic Acid | - | - | - | - | - |
| Hydrochlorothiazide | Appearance- Solubility- RESIDUE ON IGNITION -Chloride-LOSS ON DRYING | Assay-ORGANIC IMPURITIES | 181 | 680 | 861 |
| Honey Flovour | Appearance-Odor- Water content-Particle size | 52 | - | - | 52 |
| Hydrochlorid Acid | - | - | - | - | - |
| Hyrochloric Acid (for Injection) | - | - | - | - | - |
| Hydroxy Propyl Cellulose H | - | - | - | - | - |
| Hydroxy Propyl Cellulose VH | - | - | - | - | - |
| Hydroxy Propyl Methyl Cellulose 15000cps (K15M CR) | Appearance- Solubility- RESIDUE ON IGNITION-pH- LOSS ON DRYING-Particle size | Identification A- Identification  B- Identification  C- Identification D-Identification E | 211 | 40 | 251 |
| HCL Solution 37% | - | - | - | - | - |
| HPMC 6 CPS (Hydroxy Propyl Methyl Cellolose 6 CPS) | Appearance- Solubility- RESIDUE ON IGNITION-pH- LOSS ON DRYING-Particle size | Identification A- Identification  B- Identification  C- Identification D-Identification E | 211 | 40 | 251 |
| HPMC 15 CPS (Hydroxy Propyl Methyl Cellolose 15 CP) | Appearance- Solubility- RESIDUE ON IGNITION-pH- LOSS ON DRYING-Particle size | Identification A- Identification  B- Identification  C- Identification D-Identification E | 211 | 40 | 251 |
| Hydroxypropyl Methyl Cellulose K100M | Appearance- Solubility- RESIDUE ON IGNITION-pH- LOSS ON DRYING-Particle size | Identification A- Identification  B- Identification  C- Identification D-Identification E | 211 | 40 | 251 |
| Hydrolized Polyvinyl Alcohol (HPA) | - | - | - | - | - |
| Hypermellose (HPMC Benecel E4M) | - | - | - | - | - |
| Healthy Liver Marketing Sachet | - | - | - | - | - |
| Holder XAde 60pcs | - | - | - | - | - |

### Sheet I

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Isolucine | - | - | - | - | - |
| Inolin | - | - | - | - | - |
| Isotretinoin | - | - | - | - | - |
| Ibuprofen | - | - | - | - | - |
| Ibrutinib | - | - | - | - | - |
| Ibrutinib Granule Ready to Press | - | - | - | - | - |
| Iron Liposomal | - | - | - | - | - |
| Iodin Solution O.IN | - | - | - | - | - |
| Isopropyl Alcohol | - | - | - | - | - |
| Indigo Carmine, FD&C Blue No.2 | - | - | - | - | - |

### Sheet J

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Juniper | Appearance-Colour-Odour- Particle Size-Loss on Drying- Ash Content | Identification | 183 | 30 | 213 |

### Sheet L

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Liguisticum Sinensis Dried Root | - | - | - | - | - |
| Lutein Marigold Ext. | - | - | - | - | - |
| Liguisticum Sinensis Dried Root | - | - | - | - | - |
| Lutein Oil 20% | - | - | - | - | - |
| L-Arginine | Appearance-Solubility-Residue on Ignition- Chloride- Sulfate-OPTICAL ROTATION-LOSS ON DRYING | Assay-ORGANIC IMPURITIES | 131 | 90 | 221 |
| L-Argenine (Base) | - | - | - | - | - |
| L-Cysteine | Appearance- Solubility- Residue on Ignition- Sulfate-Optical rotation-Loss on drying | Assay-Related compounds | 196 | 90 | 286 |
| L-Carnetine Base | - | - | - | - | - |
| L-Carnetine Tartarate | - | - | - | - | - |
| L-Methionine | Appearance- Solubility-Chloride- Sulfate-pH- Loss on drying | Assay- Related compounds | 141 | 730 | 871 |
| L-Menthol | Appearance-Solubility- Melting range-Optical rotation | Limit of nonvolatile residue- Readly oxidizable substance in dl-menthol-Congealing range of dl-menthol | 46 | 1560 | 1606 |
| L-Glutathione Reduced | - | - | - | - | - |
| L-Theanine | - | - | - | - | - |
| Luteolin | - | - | - | - | - |
| Leucine | - | - | - | - | - |
| L-Arginine HCL | - | - | - | - | - |
| L-Cystine | Appearance- Solubility- Optical rotation-Residue on ignition- Chloride- Sulfate-Loss on drying | Assay-Organic impurities | 131 | 90 | 221 |
| L-Glutathion | - | - | - | - | - |
| L-Glutamine | - | - | - | - | - |
| Liposomal Ferrous | - | - | - | - | - |
| Lenalidomide | - | - | - | - | - |
| Linagliptin (Parsian) | Appearance- Solubility- Water content-Residue on ignition | Identification B-Related compound- Assay | 116 | 810 | 926 |
| Linagliptin (Morepen) | Appearance- Solubility- Water content-Residue on ignition-Particle size | Assay-Related compounds | 146 | 1025 | 1171 |
| Lysine | - | - | - | - | - |
| Lycopene | - | - | - | - | - |
| Liraglutide | - | - | - | - | - |
| Lopromaide HCL | Appearance- Solubility-Melting point- Loss on drying- Sulfated Ash | Assay-Related substance | 181 | 325 | 506 |
| Lactobacillus Acidophilus | - | - | - | - | - |
| Lactobacillus Casei | - | - | - | - | - |
| Lactobacillus Paracasei | - | - | - | - | - |
| Lactobacillus Rhamnosus | - | - | - | - | - |
| Lactobacillus Gasseri | - | - | - | - | - |
| Lactobacillus Roteri | - | - | - | - | - |
| Lactobacillus Fermentum | - | - | - | - | - |
| L-Citrulline | - | - | - | - | - |
| Lactose Flolac 90-100 | - | - | - | - | - |
| Lactose Monohydrate 80 | Appearance- Solubility- Residue on ignition-Clarity and color of solution- optical rotation-ACIDITY OR ALKALINITY-LOSS ON DRYING-WATER DETERMINATION | Identification B- PROTEIN AND LIGHT-ABSORBING IMPURITIES | 221 | 55 | 276 |
| Lactose Spray Dried 100 | - | - | - | - | - |
| Lactose Monohydrate 200 | Appearance- Solubility- Residue on ignition-Clarity and color of solution- optical rotation-ACIDITY OR ALKALINITY-LOSS ON DRYING-WATER DETERMINATION | Identification B- PROTEIN AND LIGHT-ABSORBING IMPURITIES | 221 | 55 | 276 |
| Lemon Flovour | Appearance- Colour- Odour-Water content-Particle Size | - | 54 | - | 54 |
| Light Substituted Hydroxy Propyl Cellulose 21 | - | - | - | - | - |
| Ludi Flash | - | - | - | - | - |
| Lactose DC 90 | - | - | - | - | - |
| Lactose DC 100 | Appearance- Solubility- Residue on ignition-Clarity and color of solution- optical rotation-ACIDITY OR ALKALINITY-LOSS ON DRYING-WATER DETERMINATION | Identification B- PROTEIN AND LIGHT-ABSORBING IMPURITIES | 221 | 55 | 276 |
| Lactulose | - | - | - | - | - |
| L-Methionin Liquid | - | - | - | - | - |
| Lecithin | - | - | - | - | - |
| Light Hydroxy Propyl Cellulose 22 | - | - | - | - | - |
| Lapermaide HCL | - | - | - | - | - |
| Lactose monohydrate mesh 80 DC grade | Appearance- Solubility- Residue on ignition-Clarity and color of solution- optical rotation-ACIDITY OR ALKALINITY-LOSS ON DRYING-WATER DETERMINATION | Identification B- PROTEIN AND LIGHT-ABSORBING IMPURITIES | 221 | 55 | 276 |

### Sheet K

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Kale (Cabbage Ext.) | - | - | - | - | - |
| Kelp Ext. | - | - | - | - | - |
| Kollidone VA 64 | Appearance- Solubility-Residue on ignition-pH- Water determination- | Identification B-Identification c- Identification D- Identification E-Nitrogen determination- LIMIT OF ALDEHYDES- LIMIT OF HYDRAZINELIMIT OF HYDRAZINE- PEROXIDES | 131 | 635 | 766 |
| Kolidon (BASF) CL-SF | - | - | - | - | - |
| Kamasutra Marketing Sachet | - | - | - | - | - |

### Sheet M

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Mentha Pipperita (Peppermint) | Appearance-Colour- Odour- Particle Size-Loss on drying- Ash content | Identification | 184 | 30 | 214 |
| Mullien | - | - | - | - | - |
| Maitake Ext. | - | - | - | - | - |
| Mashroom Shiitake Ext. | - | - | - | - | - |
| Maca Ext. | - | - | - | - | - |
| Myricetin | - | - | - | - | - |
| Manganese Sulfate Monohydrate | Appearance-Solubility- LOSS ON IGNITION-Identification A- Identification B | Assay-SUBSTANCES NOT PRECIPITATED BY AMMONIUM SULFIDE- | 121 | 120 | 241 |
| Methyl Sulphonyl Methan 99.4% (MSM) | Appearance-Solubility- Melting range-Water determination | 51 | - | - | 51 |
| Magnesium Oxide (Heavy) | Appearance-Solubility- Free alkali soluble salts- Loss on ignition- Substance insoluble in acetic acid-Chloride- Sulfate- Bulk density | Assay- | 246 | 45 | 291 |
| Melatonin | Appearance- Solubility- Residue on ignition- Chloride- Loss on drying | Identification B- Identification C- Assay- Related compounds- | 126 | 830 | 956 |
| Magnesium Carbonate Heavy | - | - | - | - | - |
| Methylfolate | - | - | - | - | - |
| Macrogol 20000 | - | - | - | - | - |
| Methylred | - | - | - | - | - |
| Methanamine | - | - | - | - | - |
| Metformin Hydrochloride (Kimiagaran Emrouz) | Appearance- Solubility- Loss on drying -Ash | Assay- Related compounds- Identification | 166 | 780 | 946 |
| Metformin Hydrochloride (Mahban Chemi) | Appearance- Solubility- Loss on drying -Ash | Assay- Related compounds- Identification | 166 | 780 | 946 |
| Metformin DC Extended Release | - | - | - | - | - |
| Moxifloxacin HCL | - | - | - | - | - |
| Mirabegron | - | - | - | - | - |
| Molnupiravir | - | - | - | - | - |
| Macitentan | - | - | - | - | - |
| Mesalazine | - | - | - | - | - |
| Mannitol | Appearance- Solubility- Loss on drying- Conductivity- melting point- Appearance of solution | 141 | - | - | 141 |
| Micro Cryslaline Cellulose PH101 (Avicel PH101) | Appearance- Solubility- Residue on ignition-Conductivity- pH- Loss on drying- Bulk density | Identification B- Identification C | 201 | 25 | 226 |
| Micro Cryslaline Cellulose PH102 (Avicel PH102) | Appearance- Solubility- Residue on ignition-Conductivity- pH- Loss on drying- Bulk density | Identification B- Identification C | 201 | 25 | 226 |
| Magnesium Stearate | Appearance- Solubility- Chloride- Sulfate- Alkanitiy and acidity- Bulk density- Loss on drying | Identification A- Assay | 156 | 55 | 211 |
| Methyl Paraben | Appearance- Solubility- Melting point- Residue on ignition- Colour of solution- Acidity | Organic impurities | 166 | 405 | 571 |
| Magnesium Aspartate | - | - | - | - | - |
| Mannitol DC 400 | - | - | - | - | - |
| MCT OIL (Medium Chain Triglycride) | - | - | - | - | - |
| Maltodextrin | Appearance- Solubility- Residue on ignition- pH- Loss on drying | - | 181 | - | 181 |
| Micro Crystalline Cellulose Neo-C91SD  Colloidal | Appearance- Solubility- Residue on ignition-Conductivity- pH- Loss on drying- Bulk density | Identification B- Identification C | 201 | 25 | 226 |
| Mannitol Liquid | - | - | - | - | - |
| MonoAmmonium Glycyrrhizinate | - | - | - | - | - |
| Metaacrylic Acid Copolymer (Type C) (Eudragit L100-55) | - | - | - | - | - |
| MicroCrystaline Cellulose PH112 (Avicel PH112) | - | - | - | - | - |
| Meglumine | - | - | - | - | - |
| Mint Essence | - | - | - | - | - |
| Mango Flavour Powder | - | - | - | - | - |
| Micronized HPMC | - | - | - | - | - |
| Maxi CareX Marketing Sachet | - | - | - | - | - |

### Sheet N

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Nettel Ext. | - | - | - | - | - |
| N-Acetyle L-Cysteene | - | - | - | - | - |
| Nicotinamide MonoNucleotide (NMN) | - | - | - | - | - |
| Naproxen | Appearance- Solubility- Loss on drying | Identification- Assay- chromatograohic purity | 196 | 135 | 331 |
| Nebivolol Hydrochloride Micronized | - | - | - | - | - |
| Neotame | Appearance- Solubility- RESIDUE ON IGNITION-OPTICAL ROTATION- WATER DETERMINATION | Assay-RELATED COMPOUNDS- | 131 | 930 | 1061 |

### Sheet O

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Omega 3 (Flaxed Oil) | Appearance-Solubility- Loss on drying-Ash content | 166 | - | - | 166 |
| Orlistat | - | - | - | - | - |
| Ozanimod | - | - | - | - | - |
| Omega 3 (Flaxed Oil) | - | - | - | - | - |
| Ondansetron Base | - | - | - | - | - |
| Orange Flovour Powder Olbrichtarom | Appearance- Odour- Water Content | - | 22 | - | 22 |
| Orange Flavour Liquid | - | - | - | - | - |
| Orange Flavour Powder (Firmenich 05605TP0551) | Appearance- Odour- Water Content | 22 | - | - | 22 |
| Opadry White (85F18422) | - | - | - | - | - |
| Opadry Yellow | - | - | - | - | - |

### Sheet Q

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Quercetin | - | - | - | - | - |

### Sheet P

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Panax Ginseng (Korean Ginseng Ext.) Dry Conc 3:1 | Appearance- Particle size- Loss on Drying-Ash content | Identification- Assay- | 181 | 702 | 883 |
| Passiflora Incarnata (Passion Flower Ext.) Dry Conc 4:1 | Appearance-Colour- Odour-Particle Size- Loss on Drying-Ash content | Identification | 183 | 30 | 213 |
| Pollen (Aqueous Pollen Ext.) | - | - | - | - | - |
| Paeoniae Rubra Dried Root | - | - | - | - | - |
| Polygala Tenuifolia Dried Root | - | - | - | - | - |
| Prunus Persica Dried Ripe Seed | - | - | - | - | - |
| Pumpkin Ext. | - | - | - | - | - |
| Pygeum Africanum Ext. | - | - | - | - | - |
| Polygala Tenuifolia Dried Root | - | - | - | - | - |
| Prunus Persica Dried Ripe Seed | - | - | - | - | - |
| Paeonia Rubra Dried Root | - | - | - | - | - |
| Picrorhiza kurroa | - | - | - | - | - |
| Peppermint Oil | - | - | - | - | - |
| Phenylalanine | - | - | - | - | - |
| Proline | - | - | - | - | - |
| Potassium Iodide | Appearance- Solubility-Alkalinity-Loss on drying | Assay-Iodate-Thiosulfate & barium- Identification A-Identification B | 116 | 105 | 221 |
| Potasium Nitrate | - | - | - | - | - |
| Potassium Sorbate | Appearance- Solubility-Loss on drying-Acidity and alkalinity- | Identification A- Assay- | 116 | 510 | 626 |
| Pyroglutamic Acid | - | - | - | - | - |
| Phosphatidylserine | - | - | - | - | - |
| P-Aminobenzoic Acid (Paba) | - | - | - | - | - |
| Potassium Aluminium Silicate | - | - | - | - | - |
| Para Omino Benzoic Acid | - | - | - | - | - |
| Propyl Paraben | - | - | - | - | - |
| Propyl Glaycol | - | - | - | - | - |
| Polysorbate 80 | Appearance- Solubility- Specific Gravity-Water determination- Residue on ignition | Acid Value-Saponification Value- Peroxide Value | 131 | 80 | 211 |
| Poly Vinil Pyrolidone K25 (PVP K25) | - | - | - | - | - |
| Poly Vinil Pyrolidone K30 (PVP K30) | Appearance- Solubility-Water determination- Residue on ignition- pH- | Identification B- Identification C- Identification D- Identification E- Nitrogen determination- LIMIT OF HYDRAZINE- 2-PYRROLIDONE- PEROXIDES- | 131 | 535 | 666 |
| Poly Vinil Pyrolidone K90 (PVP K90) | Appearance- Solubility-Water determination- Residue on ignition- pH- | Identification B- Identification C- Identification D- Identification E- Nitrogen determination- LIMIT OF HYDRAZINE- 2-PYRROLIDONE- PEROXIDES- | 131 | 535 | 666 |
| Powder Strawberry Flovour (Firmenich) | Appearance -Particle size- Water content | - | 51 | - | 51 |
| Phenol | - | - | - | - | - |
| Propyylen Glycol Apyrogen (for Injection) | - | - | - | - | - |
| Phytosterol | - | - | - | - | - |
| Pantothenic Acid | - | - | - | - | - |
| Propylen Glaycol | - | - | - | - | - |
| Poloxamer 188 | - | - | - | - | - |
| Precirol ATO5 | - | - | - | - | - |
| Phenylethyl Alcohol | - | - | - | - | - |
| Purified Water (for HPLC) | - | - | - | - | - |
| Phloral | - | - | - | - | - |
| Propyl Gallate | - | - | - | - | - |
| Potassiun Hydroxide Liquid 50% | - | - | - | - | - |
| Pink Iron Oxide | - | - | - | - | - |
| Poly Ethylen Glycol 400 (PEG 400) | Appearance- Solubility- Residue on ignition- pH-  COMPLETENESS AND COLOR OF SOLUTION | LIMIT OF ETHYLENE GLYCOL AND DIETHYLENE GLYCOL | 171 | 45 | 216 |
| Poly Ethylen Glycol 4000 (PEG 4000) | Appearance- Solubility- Residue on ignition- pH-  COMPLETENESS AND COLOR OF SOLUTION | LIMIT OF ETHYLENE GLYCOL AND DIETHYLENE GLYCOL | 171 | 45 | 216 |
| Poly Ethylen Glycol 3000 (PEG 3000) | - | - | - | - | - |
| Pink Color - Code 313 | - | - | - | - | - |
| Purple  Color - Code 807 | - | - | - | - | - |

### Sheet R

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Rhubarb Ext. | - | - | - | - | - |
| Rhodiola Rosea Ext. | - | - | - | - | - |
| Rutin | - | - | - | - | - |
| Reishi Polysaccharides 30% | - | - | - | - | - |
| Resveratrol | - | - | - | - | - |
| Remdesevir | - | - | - | - | - |
| Rivaroxaban | - | - | - | - | - |
| Ranolazine | - | - | - | - | - |
| Ramipril | - | - | - | - | - |
| Rosuvastatin Calcium | - | - | - | - | - |
| Royal Jelly | - | - | - | - | - |
| Retinyl Acetate | - | - | - | - | - |
| Raspberry Flavour | - | - | - | - | - |
| Red Iron Oxide | Appearance- Solubility-Water soluble substance-Acid insoluble substance | Assay-organic colour and lakes | 196 | 123 | 319 |
| Red Color - Code 219 | - | - | - | - | - |
| Rober Stopper | - | - | - | - | - |

### Sheet S

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Serenoa Repens (Sawpalmetto Ext.) Dry Conc 4:1 | Appearance-Residue on ignition-Particle size-Loss on drying- | Identification | 181 | 30 | 211 |
| Silybum Marianum (Milk Thistle Ext.) Dry Conc 70:1 | Appearance- Colour- Odour- Taste-Particle Size- Loss on Drying- Sulphated Ash | Identification-Assay | 184 | 1065 | 1249 |
| Soybean Lecithin | - | - | - | - | - |
| Salvia Miltiorrhiza Dried Root | - | - | - | - | - |
| Soybean Ext. | - | - | - | - | - |
| Shiitake Ext. | - | - | - | - | - |
| Spirulina Ext. | - | - | - | - | - |
| Stevia Ext. | - | - | - | - | - |
| Spinach Powder | - | - | - | - | - |
| Sophora Japonica Ext. | - | - | - | - | - |
| Star Flower Oil | - | - | - | - | - |
| Salvia Miltiorrhiza Dried Root | - | - | - | - | - |
| Senna Ext. | - | - | - | - | - |
| Sarsaparilla Ext. | - | - | - | - | - |
| Soy Isoflavones | - | - | - | - | - |
| Selenomethionin | - | - | - | - | - |
| Serine | - | - | - | - | - |
| Saccharomces Cerevisiae | - | - | - | - | - |
| Sodium Alginate | - | - | - | - | - |
| Sodium Bicarbonate | Appearance- Solubility- Insoluble substance- Chloride- Loss on drying | Identification A- Identification  B- Assay- Normal carbonate- Limit of sulfur compound-Iron- Limit of organics | 176 | 410 | 586 |
| Sodium Selenite Anhydrous | Appearance- Solubility- Appearance of solution- pH- Chloride- Sulfate- Loss on drying | Identification A- Identification  B- Identification C- Identification D- Assay | 201 | 100 | 301 |
| Sodium Ascorbate | - | - | - | - | - |
| Selenium Glycinate | - | - | - | - | - |
| Sodium Nitrite | - | - | - | - | - |
| Sodium Molybdate | - | - | - | - | - |
| Safinamide Mesylate | - | - | - | - | - |
| Sitagliptin Phosphate Monohydrate | Appearance- Solubility- Water determination | Identification B- Identification C- Assay- Organic Impurities- | 36 | 855 | 891 |
| Saproptrin Dihydrochloride | - | - | - | - | - |
| Semaglutide | - | - | - | - | - |
| Sacubitril Valsartan Sodium | Appearance-Solubility- Water determination | Sodium content | 36 | 35 | 71 |
| Sucrosomial | - | - | - | - | - |
| Sorbitol | - | - | - | - | - |
| Sodium Lauryl Sulfate (SLS) | Appearance- Solubility- Alkalinity- | Sodium- Sulfate- Content of sodium alkyl sulfates- Sodium chloride- Unsulfated alcohols | 46 | 180 | 226 |
| Silica Colloidal Anhydrous (Aerosil) | Appearance- Solubility- pH- Chloride- Loss on ignition | - | 111 | - | 111 |
| Stearic Acid | Appearance- Solubility- Residue on ignition | Acid Value | 96 | 30 | 126 |
| Sodium Starch Glycolate | Appearance- Solubility- pH -Loss on drying | Identification B -Identification C- Assay-LIMIT OF SODIUM CHLORIDE | 101 | 195 | 296 |
| Sodium Citrate | Appearance- Solubility- pH -Alkalinity- Water determination | Identification A- Identification B- Identification C- Assay- Tartrate- | 81 | 1145 | 1226 |
| Sodium Chloride | Appearance- Solubiity- Loss on drying | Identification A- Identification B-Assay-Barium-Ferrocyanides- Iodides-Iron- Limit of bromides- Appearance of Solution | 86 | 275 | 361 |
| Sodium Stearyl Fumarate | Appearance- Solubility- WATER DETERMINATION | Assay-  Limt of sodium stearyl maleate and stearyl alcohol - Saponification Value- | 36 | 225 | 261 |
| Sucralose | Appearance- Solubility- Residue on ignition- Optical rotation- Water determination | Assay- Related compounds-Limit of hydrolysis products- | 131 | 435 | 566 |
| Sorbitol 70% | - | - | - | - | - |
| Sour Cherry Flovour | Appearance-Water determination | - | 21 | - | 21 |
| Strawberry Liquid Flovour | - | 7 | - | - | - |
| Strawberry Liquid Flovour (Firmenich 052311B) | - | - | - | - | - |
| Silicone Oil | - | - | - | - | - |
| Sodium Sacharine | - | - | - | - | - |
| Sun Flower Oil | - | - | - | - | - |
| Sodium Hydroxide | Appearance- Solubility- pH- Insoluble substance and organic matter | Identification A- Assay- | 101 | 75 | 176 |
| Salcaprozate Sodium | - | - | - | - | - |
| Sodium Hydroxide (for Injection) | - | - | - | - | - |
| Suceinic Acid (for Injection) | - | - | - | - | - |
| Sodium Carbonate | Appearance- Solubility- Water determination | Identification A-Identification B- Assay | 36 | 100 | 136 |
| Simethicon Emulsion | - | - | - | - | - |
| Sodium Bitartarat | - | - | - | - | - |
| Sodium Louryl Sulfate (SLS) Fine | - | - | - | - | - |
| Sodium Benzoate | Appearance- Solubility-Alkalinity- Water determination-Appearance of solution | Assay | 76 | 360 | 436 |
| Sacarose (Pharma Sugar) | - | - | - | - | - |
| Sunset Yellow - FD&C Yelloe No.6 | - | - | - | - | - |

### Sheet T

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Tribulus Tresstriss Ext. Dry Conc 50:1 | Appearance- Colour- Odour- particle size- Loss on drying- Ash content | Assay | 184 | 30 | 214 |
| Turnera Diffusa (Damiana Ext.) Dry 5:1 | Appearance- Colour- Odour- particle size- Loss on drying- Ash conten | Identification | 184 | 30 | 214 |
| Tomato Ext. | - | - | - | - | - |
| Tumeric Ext. | - | - | - | - | - |
| Tongkat Ali Ext. | - | - | - | - | - |
| Taraxacam | - | - | - | - | - |
| Taurine | Appearance- Solubility- Residue on ignition- Chloride- Sulfate- Loss on drying | Related compounds | 196 | 30 | 226 |
| Thereonine | - | - | - | - | - |
| Tryptophan | - | - | - | - | - |
| Tyrosine | - | - | - | - | - |
| Tofacitinib Citrate | - | - | - | - | - |
| Trisodium Citrate (for Injection) | - | - | - | - | - |
| Tin (II) Chloride | Appearance- Solubility- Appearance of Solution | Identification A- Identification B- Identification C- Assay- Limit of sulfate- Limit of Lead- Substance not precipited by thioacetamide | 26 | 170 | 196 |
| Tadalafil | - | - | - | - | - |
| Ticagrelor Base | - | - | - | - | - |
| Telmisartan | Appearance- Solubility- Residue on ignition- Loss on drying | Assay- Organic impurity | 166 | 550 | 716 |
| Triacetin | Appearance- Solubility- Water determination- Acidity | - | 66 | - | 66 |
| Talc | Appearance- Solubility-WATER-SOLUBLE SUBSTANCES- ACIDITY AND ALKALINITY- LOSS ON IGNITION | Identification B- Identification C- | 216 | 40 | 256 |
| Titanium Dioxide | Appearance- Solubility- Loss on drying- Loss on ignition- Water soluble substance- Acid insoluble substance | Identification A- Assay- | 346 | 65 | 411 |

### Sheet U

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Ubidecarenon (Co Enzyme Q10) | Appearance- Solubility- Colour reaction- Melting point- Residue on ignition- Particle size- | Assay | 161 | 450 | 611 |
| Uromax Marketing Sachet | - | - | - | - | - |

### Sheet V

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Vitamin A Acetate 500000 Dry | - | - | - | - | - |
| Vitamin A Acetate 1000000 Dry | - | - | - | - | - |
| Vitamin A Palmitate | - | - | - | - | - |
| Vitamin B1 (Thiamin HCL) | Appearance- Solubility- Residue on ignition- pH- Water determination- | Identification B- Assay- Limit on nitrate- Related compound- Absorbance of solution | 131 | 1055 | 1186 |
| Vitamin B1 (Thiamin Monohydrate) | - | - | - | - | - |
| Vitamin B2 (Riboflavine) | Appearance- Solubility-  Residue on ignition- Optical rotation- Loss on drying | Identification A- Assay- Limit of lumiflavin | 181 | 495 | 676 |
| Vitamin B3 (Nicothinamide) | Appearance- Solubility- Optical rotation- Water determination+ melting point- | Assay- Ultravilot absorption- | 66 | 515 | 581 |
| Vitamin B5 (Calcium Pantothenate) | Appearance- Solubility- Specific optical rotation- Alkalinity- Loss on drying | Assay | 131 | 495 | 626 |
| Vitamin B6 (Pyridoxin Hydrochloride) | Appearance- Solubility- Appearance of solution- Residue on ignition- Chloride | Identification B- Assay | 131 | 510 | 641 |
| Vitamin B7 (Biotin) | Appearance- Solubility- Opticalrotation- Residue on gnition | Identification B- Identification C- Assay-Related compounds | 101 | 660 | 761 |
| Vitamin B8 (Inositol) | Appearance- Solubility- Clarity of solution- Colour of solution- Water determination | Conductivity | 156 | 20 | 176 |
| Vitamin B9 (Folic Acid) | Appearance- Solubility- Loss on drying- Residue on ignition | Identification- Assay | 166 | 515 | 681 |
| Vitamin B12 (Cyanocobalamine) | Appearance- Solubility- Loss on drying | Identification B- Assay- Related compounds | 86 | 585 | 671 |
| Vitamin C (Ascorbic Acid) | - | - | - | - | - |
| Vitamin C Coated 97.5% (Ascorbic Acid Coated) | Appearance- Loss on drying-Reidue on ignition- | Assay | 151 | 35 | 186 |
| Vitamin C Coated Lipid | - | - | - | - | - |
| Vitamin D3 100 Dry (Cholecalciferol) | Appearance- Particle Size- | - | 31 | 31 | 62 |
| Vitamin D3 Liquid | - | - | - | - | - |
| Vitamin E (D-Alpha Tocopheryl Acetate) | Appearance- Solubility- Loss on drying- Particle size | Assay | 116 | 270 | 386 |
| Vitamin K1 | Appearance- Solubility- Loss on drying- Particle size | Assay | 116 | 270 | 386 |
| Vitamin K2 Fermentation | - | - | - | - | - |
| Vitamin K2 Synthesis | - | - | - | - | - |
| Valeriana Officinals (Valerian Ext.) Dry Conc 5:1 | Appearance- Colour- Odour- Particle size- Loss on drying- Ash | Identification- | 184 | 30 | 214 |
| Valine | - | - | - | - | - |
| Vanadium (III) Sulfate | - | - | - | - | - |
| Valsartan | Appearance- Solubility- Water determination- Ash- | - | 116 | - | 116 |
| Vildagliptin | - | - | - | - | - |
| Vitamin E (demoxinate E) liquid | - | - | - | - | - |
| Vanila & Toffie Liquid Flovour | - | - | - | - | - |
| Vanilla Flovour | Appearance- Solubility- Particle size- Loss on drying | - | 116 | - | 116 |
| Vitacal Forte Marketing Sachet | - | - | - | - | - |

### Sheet W

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Wine Tea Extract | - | - | - | - | - |
| Wild Cherry Ext. | - | - | - | - | - |
| Wattle Ext. | - | - | - | - | - |
| Working Standard Colchicine | - | - | - | - | - |
| Wrapper Triplex (PUC/PE/PVDC) | - | - | - | - | - |
| Water | - | - | - | - | - |

### Sheet X

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Xanthan Gum | Appearance- Solubility- Loss on drying- Ash | Assay | 166 | - | 166 |
| Xylitol | - | - | - | - | - |
| Xylene | - | - | - | - | - |

### Sheet Y

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Yohembine | - | - | - | - | - |
| Yeast | - | - | - | - | - |
| Yellow Iron Oxide | Appearance- Solubility | - | 16 | - | 16 |
| Yellow Cap Probiotic Drop | - | - | - | - | - |

### Sheet Z

| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |
|---|---|---|---:|---:|---:|
| Zingiber Officinals (Ginger Ext.) Dry Conc 5:1 | Appearance- Colour- Odour- Particle Size- Loss on drying- Ash content | Identification | 184 | 30 | 214 |
| Zeaxanthin Marigold Ext. | - | - | - | - | - |
| Zinc Gluconate | Appearance-Solubility- Particle Size- pH- Water determination- Chloride- Sulfate | Assay-Identification | 161 | 75 | 236 |
| Zinc Sulfate Solution Titrisol | - | - | - | - | - |
| Zinc Sulfate | Appearance- Solubility- ACIDITY- Loss on drying | Identification-ALKALIES AND ALKALINE EARTHS- | 116 | 40 | 156 |

