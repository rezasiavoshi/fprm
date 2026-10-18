"""Build the Raw-Material (RM) and Finished-Product (FP) analyst questionnaires (.xlsx + .md).

Pre-fills each questionnaire from:
  data/QC_Capacity_Study.xlsx  - item lists, tests and column layout (answers paste back 1:1)
  data/Leadtime.xlsx           - recorded RM test times (minutes), used as hints to confirm
Usage: python3 tools/build_analyst_questionnaires.py [repo_root]
"""
import re, sys, os, collections, openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
STUDY = os.path.join(ROOT, "data/QC_Capacity_Study.xlsx")
LEAD = os.path.join(ROOT, "data/Leadtime.xlsx")
OUT = os.path.join(ROOT, "questionnaires")

# Study material name -> Leadtime.xlsx name(s). Curated: automatic fuzzy matching gave false pairs
# (Sucrose/Sucralose, Selenate/Selenite, MCC grades), so every non-exact pair is listed here.
ALIASES = {
    "Apium Graveolens Seed Dry Extract 6:1": ["Apium Graveolens (Celery Seed Ext.)"],
    "Artichoke Dry Extract 25:1": ["Cynara Scolymus (Globe Artichoke Ext.) Dry Conc 25:1"],
    "Ascorbic Acid (Vitamin C)": ["Vitamin C (Ascorbic Acid)"],
    "Ascorbic Acid Coated 97%": ["Vitamin C Coated 97.5% (Ascorbic Acid Coated)"],
    "Azelastine Hydrochloride": ["Azelastine HCL (MSN)"],
    "Beta-Carotene": ["Beta Carotene 10%"],
    "Biotin (Vitamin B7)": ["D-Biotin"],
    "Calcium Carbonate Heavy": ["Calcium Carbonate (Heavy)"],
    "Calcium Pantothenate (Vitamin B5)": ["Vitamin B5 (Calcium Pantothenate)"],
    "Citicoline Sodium": ["Citicoline"],
    "Cyanocobalamin (Vitamin B12)": ["Vitamin B12 (Cyanocobalamine)"],
    "D-Alpha Tocopheryl Acetate 50% (Vitamin E)": ["Vitamin E (D-Alpha Tocopheryl Acetate)"],
    "Dapagliflozin Propanediol Monohydrate": ["Dapagliflozine Propanediol Monohydrate (Tofigh Darou)",
                                              "Dapagliflozine Propanediol Monohydrate (Alborz Darou)"],
    "Devil's Claw Dry Extract 6:1": ["Harpagophytum Procombens (Devils Claw Ext.) Dry Conc 6:1"],
    "Dextromethorphan HBr": ["Dextromethorphan"],
    "Diphenhydramine HCl": ["Diphenhydramine"],
    "Echinacea Purpurea Dry Extract": ["Echinacea"],
    "Epimedium Grandiflorum (Horny Goat Weed) Dry Extract 20:1": ["Epimedium Grandiflorum (Horny Goat Weed Ext.) Dry Conc 20:1"],
    "Fennel Dry Extract 5:1": ["Funiculum Vulgaris (Fennel Ext.) Dry Conc 5:1"],
    "Ferrous Bisglycinate": ["Ferrous BisGlycinate 20%"],
    "Fluticasone Propionate": ["Fluticasone Propionate Micronized"],
    "Folic Acid (Vitamin B9)": ["Folic Acid 10% Powder", "Folic Acid 10% with Maltodextrin"],
    "Garcinia Cambogia Fruit Dry Extract 6:1": ["Garcinia Quaesita (Garcinia Ext.) Dry Conc 6:1"],
    "Gentian Dry Extract 4:1": ["Gentiana Lutea (Gentian Ext.) Dry Conc 4:1"],
    "Ginger Dry Extract 5:1": ["Zingiber Officinals (Ginger Ext.) Dry Conc 5:1"],
    "Ginkgo Biloba Leaf Dry Extract 50:1": ["Gink Biloba (GinKgo Ext.) Dry Conc 50:1"],
    "Gymnema Sylvestre Leaf Dry Extract 10:1": ["Gymnema Sylvestre Leaf (Gymnema Ext.) Dry Conc 10:1"],
    "Inositol (Vitamin B8)": ["Vitamin B8 (Inositol)"],
    "Juniper Communis Fruit Dry Extract 2:1": ["Juniper"],
    "Liquorice Dry Extract 8:1": ["Glycyrrhiza Glabra (Liquorice Ext.) Dry Conc 8:1"],
    "Loperamide HCl": ["Lopromaide HCL"],
    "Magnesium Oxide Heavy": ["Magnesium Oxide (Heavy)"],
    "Methionine": ["L-Methionine"],
    "Methyl Sulphonyl Methane (MSM)": ["Methyl Sulphonyl Methan 99.4% (MSM)"],
    "Milk Thistle Dry Extract 70:1": ["Silybum Marianum (Milk Thistle Ext.) Dry Conc 70:1"],
    "Nicotinamide (Vitamin B3)": ["Vitamin B3 (Nicothinamide)"],
    "Nicotinamide Mononucleotide (NMN) Granule": ["Nicotinamide MonoNucleotide (NMN)"],
    "Omega 3 Powder (from Flax Seed Dry Extract)": ["Omega 3 (Flaxed Oil)"],
    "Ozanimod Hydrochloride": ["Ozanimod"],
    "Panax Ginseng (Asian Ginseng) Dry Extract 3:1": ["Panax Ginseng (Korean Ginseng Ext.) Dry Conc 3:1"],
    "Pyridoxine Hydrochloride (Vitamin B6)": ["Vitamin B6 (Pyridoxin Hydrochloride)"],
    "Riboflavin (Vitamin B2)": ["Vitamin B2 (Riboflavine)"],
    "Sacubitril/Valsartan 3Sodium 2.5H2O Co-crystal": ["Sacubitril Valsartan Sodium"],
    "Saw Palmetto Dry Extract 4:1": ["Serenoa Repens (Sawpalmetto Ext.) Dry Conc 4:1"],
    "Siberian Ginseng Dry Extract 5:1": ["Eleutherococuss Senticosus (Siberian Ginseng Ext.) Dry Conc 5:1"],
    "Sodium Selenite": ["Sodium Selenite Anhydrous"],
    "Thiamine Hydrochloride (Vitamin B1)": ["Vitamin B1 (Thiamin HCL)"],
    "Tribulus Terrestris Dry Extract 50:1": ["Tribulus Tresstriss Ext. Dry Conc 50:1"],
    "Ubidecarenone (Co-Q10)": ["Ubidecarenon (Co Enzyme Q10)"],
    "Vitamin D3": ["Vitamin D3 100 Dry (Cholecalciferol)", "Vitamin D3 Liquid"],
    "Apple Green Color": ["Apple Green"],
    "Brown Color": ["Brown  Color - Code 1005"],
    "Exacol Brown HT": ["Exacol Brown"],
    "Sunset Yellow": ["Sunset Yellow - FD&C Yelloe No.6"],
    "Ferric Oxide Black": ["Black Iron Oxide"],
    "Ferric Oxide Red": ["Red Iron Oxide"],
    "Ferric Oxide Yellow": ["Yellow Iron Oxide"],
    "Croscarmellose Sodium": ["Cross Carmellose Sodium"],
    "Crospovidone": ["Crosspovidone A"],
    "Lactose Monohydrate": ["Lactose Monohydrate 80", "Lactose Monohydrate 200", "Lactose monohydrate mesh 80 DC grade"],
    "Microcrystalline Cellulose PH 101": ["Micro Cryslaline Cellulose PH101 (Avicel PH101)"],
    "Microcrystalline Cellulose PH 102": ["Micro Cryslaline Cellulose PH102 (Avicel PH102)"],
    "Microcrystalline Cellulose RC591": ["Avicel RC 591"],
    "Pregelatinized Starch": ["Corn Starch 1500 Pregelatin"],
    "PVP K30": ["Poly Vinil Pyrolidone K30 (PVP K30)"],
    "PVP K90": ["Poly Vinil Pyrolidone K90 (PVP K90)"],
    "Colloidal Silicon Dioxide": ["Silica Colloidal Anhydrous (Aerosil)"],
    "Glyceryl Behenate (Compritol 888 ATO)": ["Compritol 888 ATO (Glyceryl Dibehenate)"],
    "HPMC K4M": ["Hypermellose (HPMC Benecel E4M)"],
    "Sodium Carboxymethyl Cellulose (Medium Viscosity)": ["Carboxymethyl Cellulose Sodium"],
    "Sucrose": ["Sacarose (Pharma Sugar)"],
    "Cola Flavour": ["Cola Flavour Powder"],
    "Honey Flavour": ["Honey Flovour"],
    "Lemon Flavour": ["Lemon Flovour"],
    "Mint Flavour": ["Mint Essence"],
    "Orange Flavour": ["Orange Flavour Liquid", "Orange Flavour Powder (Firmenich 05605TP0551)"],
    "Sour Cherry Flavour": ["Sour Cherry Flovour"],
    "Strawberry Flavour": ["Powder Strawberry Flovour (Firmenich)", "Strawberry Liquid Flovour",
                           "Strawberry Liquid Flovour (Firmenich 052311B)"],
    "Polyethylene Glycol 4000 (PEG 4000)": ["Poly Ethylen Glycol 4000 (PEG 4000)"],
    "Propylene Glycol": ["Propylen Glaycol"],
    "Methacrylic Acid Copolymer (Eudragit L100-55)": ["Metaacrylic Acid Copolymer (Type C) (Eudragit L100-55)"],
    "Ethanol 96%": ["Ethanol (Alcohol)"],
    "Sodium Citrate Dihydrate": ["Sodium Citrate"],
    "Benzalkonium Alcohol 50%": ["Benzalkonium Chloride"],
}

HEAD = PatternFill("solid", fgColor="1F4E78")
INPUT = PatternFill("solid", fgColor="FFF2CC")   # yellow = you type (same as the study)
AUTO = PatternFill("solid", fgColor="E7E6E6")    # grey = pre-filled / reference
SEC = PatternFill("solid", fgColor="DDEBF7")
THIN = Side(style="thin", color="BFBFBF")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")


def norm(s):
    return re.sub(r"[^a-z0-9]", "", re.sub(r"\(.*?\)", "", str(s).lower()))


def num(v):
    return v if isinstance(v, (int, float)) else None


def cell(v):
    return "" if v is None else str(v).replace("\n", " ").strip()


def load_study():
    wb = openpyxl.load_workbook(STUDY, data_only=True)
    rows = lambda name: [r for r in wb[name].iter_rows(min_row=5, values_only=True) if r[0]]
    hdr = lambda name: [c.value for c in wb[name][4]]
    return dict(tt=rows("Test_Times"), tt_h=hdr("Test_Times")[:26],
                rm=rows("RM_Lots"), rm_h=hdr("RM_Lots")[:8],
                fp=rows("Products"), fp_h=hdr("Products")[:13],
                interview=[r for r in wb["Interview"].iter_rows(min_row=5, values_only=True) if r[0]])


def load_leadtime():
    wb = openpyxl.load_workbook(LEAD, data_only=True)
    out = {}
    for ws in wb.worksheets[1:]:
        for r in ws.iter_rows(min_row=2, values_only=True):
            if not r[0]:
                continue
            g, s = num(r[12]), num(r[16])
            t = num(r[20]) if len(r) > 20 else None
            if t is None and (g is not None or s is not None):
                t = (g or 0) + (s or 0)
            out[cell(r[0])] = dict(sheet=ws.title, gt=cell(r[4]), st=cell(r[8]), g=g, s=s, t=t)
    return out


def match(study_names, lead):
    by_norm = collections.defaultdict(list)
    for n in lead:
        by_norm[norm(n)].append(n)
    res = {}
    for m in study_names:
        if m in ALIASES:
            res[m] = ("Alias - confirm", [n for n in ALIASES[m] if n in lead])
        elif by_norm.get(norm(m)):
            res[m] = ("Exact", by_norm[norm(m)])
        else:
            res[m] = ("Not in Leadtime.xlsx", [])
    return res


def agg(names, lead, key):
    vals = [lead[n][key] for n in names if lead[n][key] is not None]
    if not vals:
        return None
    return round(max(vals) / 60, 2)   # minutes -> hours; worst supplier variant


# ---------------------------------------------------------------- xlsx helpers
def title(ws, text, sub=None):
    ws["A1"] = text
    ws["A1"].font = Font(bold=True, size=14, color="1F4E78")
    if sub:
        ws["A2"] = sub
        ws["A2"].font = Font(italic=True, color="595959")


def table(ws, r0, headers, rows, input_cols, widths=None, dv=None):
    """Write a header row at r0 and data below; input_cols are 1-based column numbers to colour yellow."""
    for j, h in enumerate(headers, 1):
        c = ws.cell(r0, j, h)
        c.fill, c.font, c.alignment, c.border = HEAD, Font(bold=True, color="FFFFFF"), WRAP, BOX
    for i, row in enumerate(rows, r0 + 1):
        for j, v in enumerate(row, 1):
            c = ws.cell(i, j, v)
            c.border, c.alignment = BOX, WRAP
            c.fill = INPUT if j in input_cols else AUTO
    ws.row_dimensions[r0].height = 60
    ws.freeze_panes = ws.cell(r0 + 1, 3)
    if rows:
        ws.auto_filter.ref = f"A{r0}:{get_column_letter(len(headers))}{r0 + len(rows)}"
    for j, w in enumerate(widths or [], 1):
        ws.column_dimensions[get_column_letter(j)].width = w
    last = r0 + max(len(rows), 1)
    for col, formula in (dv or {}).items():
        v = DataValidation(type="list", formula1=formula, allow_blank=True)
        ws.add_data_validation(v)
        v.add(f"{col}{r0 + 1}:{col}{last}")


def qsheet(ws, sections, sub):
    """Question sheet: sections = [(section title, [(id, question, maps-to)])]."""
    title(ws, ws.title, sub)
    r = 4
    for j, (h, w) in enumerate([("#", 7), ("Question", 70), ("Answer", 60), ("Feeds study sheet / column", 26)], 1):
        c = ws.cell(r, j, h)
        c.fill, c.font, c.border = HEAD, Font(bold=True, color="FFFFFF"), BOX
        ws.column_dimensions[get_column_letter(j)].width = w
    for sec, qs in sections:
        r += 1
        ws.cell(r, 1, sec).font = Font(bold=True)
        for j in range(1, 5):
            ws.cell(r, j).fill = SEC
        for qid, q, maps in qs:
            r += 1
            for j, v in enumerate([qid, q, None, maps], 1):
                c = ws.cell(r, j, v)
                c.alignment, c.border = WRAP, BOX
                c.fill = INPUT if j == 3 else AUTO
            ws.row_dimensions[r].height = max(30, 15 * (len(q) // 80 + 1))
    ws.freeze_panes = "A5"


RESPONDENT = ("A. Respondent", [
    ("A1", "Name / ID, role, years of QC experience.", "Personnel A, B, D"),
    ("A2", "Which techniques/instruments are you qualified on (HPLC, GC, UV-Vis, AAS/ICP, KF, dissolution, titration)?", "Personnel C; Test_Times X"),
    ("A3", "Contract hours per week and annual leave weeks.", "Personnel E, F"),
    ("A4", "In a normal week, what % of your time is: testing / reviewing others' data / documentation & LIMS / "
           "meetings & training / cleaning & housekeeping / investigations? (should add to 100%)", "Personnel G, H"),
    ("A5", "Average overtime hours per month over the last 6 months, and the main reason.", "Personnel J; Evidence H"),
    ("A6", "Is any method or instrument in your area done by only one qualified person? Which?", "Report: key-person risk"),
])

TIMES_HELP = [
    "Times are in HOURS per sample unless the header says per sequence. Give MIN / MOST LIKELY / MAX for preparation - "
    "a realistic range is more useful than one exact number.",
    "Analyst time = hands-on time only. Instrument run time, oven/LOD time and dissolution bath time are recorded "
    "separately because the instrument works unattended.",
    "Set 'Applicable' = N for tests you never do on that item. Add tests that are missing on the 'Extra tests' sheet.",
    "Grey columns are pre-filled. Columns AA onward are reference only (e.g. times recorded in Leadtime.xlsx) - "
    "confirm or correct them in the yellow columns.",
    "Columns A-Z are in the same order as the Test_Times sheet of QC_Capacity_Study.xlsx: answers are pasted back 1:1.",
]

TT_WIDTHS = [26, 6, 34, 26, 1, 9, 13, 10, 9, 10, 10, 10, 10, 10, 10, 1, 10, 10, 10, 10, 10, 9, 10, 16, 11, 30]
TT_INPUT = set(range(6, 27)) - {16}   # F..Z editable, P (PERT) is computed in the study
TT_DV = {"F": '"Y,N"', "G": '"HPLC,GC,UV-Vis,AAS / ICP,KF titrator,Other / bench,None"',
         "H": '"Low,Medium,High"', "W": '"Y,N"', "Y": '"High,Medium,Low"'}


def tt_rows(rows):
    # Keep study columns A..Z; blank the computed lookup (E) and PERT (P) columns.
    return [[v if j not in (4, 15) else None for j, v in enumerate(r[:26])] for r in rows]


def extra_tests_sheet(wb, s, kind, examples):
    ws = wb.create_sheet("Extra tests")
    title(ws, "Extra tests (not listed on the Test times sheet)",
          "One row per item x test. Same columns as Test times. " + examples)
    table(ws, 4, s["tt_h"], [[None, kind] + [None] * 24 for _ in range(40)], set(range(1, 27)) - {2, 5, 16},
          TT_WIDTHS, TT_DV)


def overview(wb, name, area, scope_lines, sheets, stats):
    ws = wb.active
    ws.title = "Overview"
    title(ws, name, "Deliverable 2 - analyst edition. Part of the QC Laboratory Capacity, Staffing Gap and CAPEX Assessment.")
    lines = [("Area", area)] + scope_lines + [("", "")] + [("Sheet: " + a, b) for a, b in sheets] + [("", "")] \
        + [("Colour code", "Yellow = you type. Grey = pre-filled from company records - correct it if it is wrong.")] \
        + [("Data basis", t) for t in stats] + [("", ""), ("Respondent", None), ("Date", None), ("Reviewed by (unit head)", None)]
    for i, (a, b) in enumerate(lines, 4):
        ws.cell(i, 1, a).font = Font(bold=True)
        c = ws.cell(i, 2, b)
        c.alignment = WRAP
        if a in ("Respondent", "Date", "Reviewed by (unit head)"):
            c.fill, c.border = INPUT, BOX
    ws.column_dimensions["A"].width = 28
    ws.column_dimensions["B"].width = 110


def help_rows(ws, r, lines):
    for t in lines:
        ws.cell(r, 1, "• " + t).font = Font(italic=True, color="595959")
        r += 1
    return r


# ---------------------------------------------------------------- RM
RM_QUESTIONS = [RESPONDENT,
    ("B. Receipt and sampling", [
        ("B1", "Who samples incoming materials in the warehouse (QC analyst, sampler, warehouse)? Hours per week of QC time spent on sampling and walking to the warehouse.", "Capacity C (non-routine)"),
        ("B2", "How many lots arrive in a typical month, and in the peak month? Are receipts bunched (e.g. end of quarter)?", "RM_Lots D; Evidence B"),
        ("B3", "Is reduced testing used for qualified suppliers (ID only + CoA, skip-lot)? For which materials/categories?", "Test_Times F (Applicable)"),
        ("B4", "How many supplier qualifications (full testing of 3 lots of a new supplier) per year? Hours each?", "Capacity C"),
        ("B5", "Which materials are re-tested at re-test date / expiry extension? Lots per year?", "RM_Lots H; Capacity C"),
    ]),
    ("C. Methods and instruments", [
        ("C1", "Which RM tests use GC (residual solvents, assay)? Lots/yr and instrument hours per sample.", "Extra tests; Instruments"),
        ("C2", "KF / LOD / titration: how many samples per day can one analyst handle? Is the KF titrator a bottleneck?", "Test_Times K-T"),
        ("C3", "Herbal extracts and premixes (multi-assay): how many separate HPLC methods does one lot need, and can they share a sequence?", "Test_Times I, J"),
        ("C4", "When the pharmacopoeia changes a monograph, how many hours to update and verify the method? How often per year?", "Capacity C"),
        ("C5", "How many days per month is each instrument you use down (breakdown, calibration, waiting for parts/columns/reagents)?", "Settings downtime"),
        ("C6", "Do you wait for a free HPLC/GC? How often per week and for how long?", "Evidence; Notes"),
    ]),
    ("D. Workload and service level", [
        ("D1", "Target turnaround from receipt to release (days) and actual typical turnaround. Has production ever waited for a raw material release?", "Evidence E, F, G"),
        ("D2", "How many lots are typically waiting (in quarantine, not yet tested) at month end?", "Evidence D"),
        ("D3", "Which materials are new or will be added in the next 2-3 years (new products, new suppliers)?", "RM_Lots E; Settings growth"),
        ("D4", "Non-routine work: OOS investigations, supplier complaints, method verification, R&D samples. Hours per year?", "Capacity C"),
    ]),
    ("E. Closing", [
        ("E1", "If you had one more analyst or one more instrument, what would change first?", "Report_Outline"),
        ("E2", "What is the biggest risk to on-time raw material release today?", "Report_Outline"),
    ]),
]

FP_QUESTIONS = [RESPONDENT,
    ("B. Batches and stability", [
        ("B1", "How many release batches does each family produce per year now, and per the production plan in 2-3 years? (enter on 'Volumes')", "Products F, I"),
        ("B2", "Stability: which conditions and time points are on the protocol (e.g. 0/3/6/9/12/18/24/36 months, 25/60 and 40/75)? How many stability samples tested per year?", "Products G, J"),
        ("B3", "Are in-process controls (blend uniformity, core weight, hardness, LOD) done by QC or by production? Samples per batch and hours?", "Extra tests"),
        ("B4", "How many process/cleaning validation and swab samples per year? Analyst and HPLC hours each?", "Capacity C"),
    ]),
    ("C. Methods and instruments", [
        ("C1", "Which families can be run in the same HPLC sequence (same column and mobile phase)? Use the 'Campaign groups' sheet.", "Test_Times J"),
        ("C2", "Dissolution: 6 or 12 vessels? Single point or profile? HPLC or UV finish? How long is the bath occupied per sample?", "Test_Times G, R"),
        ("C3", "Content uniformity: 10 or 30 units? Is it run on the same sequence as assay?", "Test_Times U, J"),
        ("C4", "Fixed-dose combinations: does each active need its own method (e.g. ezetimibe + rosuvastatin)? Which families?", "Test_Times I"),
        ("C5", "How many days per month is each HPLC/dissolution bath down (breakdown, calibration, waiting for parts/columns)?", "Settings downtime"),
        ("C6", "Do you run HPLC overnight or at weekends unattended? What prevents it?", "Settings hours/day"),
        ("C7", "Do you wait for a free HPLC or dissolution bath? How often per week and for how long?", "Evidence; Notes"),
    ]),
    ("D. Workload and service level", [
        ("D1", "Target turnaround from sample receipt to batch release (days) and actual typical turnaround. Batches released late last year?", "Evidence E, F, G"),
        ("D2", "How many samples (release + stability) are typically waiting at month end? Stability pulls tested late?", "Evidence D, K"),
        ("D3", "Non-routine work: method validation/transfer for new products, OOS/OOT investigations, complaint samples, R&D support. Hours per year?", "Capacity C"),
        ("D4", "Which new products or line extensions arrive in the next 2-3 years?", "Products; Settings growth"),
    ]),
    ("E. Closing", [
        ("E1", "If you had one more analyst or one more HPLC, what would change first?", "Report_Outline"),
        ("E2", "What is the biggest risk to on-time batch release today?", "Report_Outline"),
    ]),
]


def build_rm(s, lead):
    mats = [r[0] for r in s["rm"]]
    m = match(mats, lead)
    used = {n for _, names in m.values() for n in names}
    wb = Workbook()
    n_exact = sum(1 for k, _ in m.values() if k == "Exact")
    n_alias = sum(1 for k, _ in m.values() if k.startswith("Alias"))
    n_timed = sum(1 for _, names in m.values() if agg(names, lead, "t"))
    unlisted = [n for n in lead if n not in used]
    stats = [f"{len(mats)} materials and {sum(1 for r in s['tt'] if r[1] == 'RM')} material x test rows from QC_Capacity_Study.xlsx (RM_Lots, Test_Times).",
             f"Leadtime.xlsx: {n_exact} exact + {n_alias} alias name matches; {n_timed} materials have a recorded time to confirm.",
             f"{len(unlisted)} materials appear in Leadtime.xlsx but not in the study list - see 'Other materials'."]
    overview(wb, "Raw Material Analyst Questionnaire", "QC Chemical Laboratory - raw materials (APIs, excipients, colorants, flavours, solvents)",
             [("Who fills it", "Each analyst who tests incoming raw materials (2-3 people). Each person fills a separate copy."),
              ("Time needed", "About 2 hours, plus reviewing the pre-filled tables.")],
             [("Questions", "Respondent profile, receipt & sampling, methods, workload."),
              ("Volumes", "Lots received per year for each material."),
              ("Test times", "Time per test for each material - the core input."),
              ("Extra tests", "Tests missing from the list (GC residual solvents, KF as separate test, etc.)."),
              ("Other materials", "Materials in Leadtime.xlsx that are not in the study list - still tested?")], stats)

    qsheet(wb.create_sheet("Questions"), RM_QUESTIONS, "Answer in the yellow column. Short answers are fine.")

    ws = wb.create_sheet("Volumes")
    title(ws, "Lots received and tested per year", "Columns A-H = RM_Lots sheet of the study. Sorted as in the study; use the filter.")
    rows = []
    for r in s["rm"]:
        k, names = m[r[0]]
        rows.append(list(r[:5]) + [None] + list(r[6:8]) + [None, None, k, "; ".join(names), agg(names, lead, "t")])
    hdr = s["rm_h"] + ["Suppliers (number)", "Reduced testing? (none / ID+CoA / skip-lot)",
                       "Match to Leadtime.xlsx", "Leadtime.xlsx name(s)", "Recorded total h/lot (Leadtime, worst variant)"]
    table(ws, 4, hdr, rows, {4, 5, 7, 8, 9, 10}, [34, 18, 10, 10, 12, 1, 22, 30, 10, 18, 16, 40, 12],
          {"J": '"None,ID + CoA,Skip-lot"'})

    ws = wb.create_sheet("Test times")
    title(ws, "Test times per material (hours)")
    r0 = help_rows(ws, 2, TIMES_HELP) + 1
    rows = []
    for r in tt_rows([r for r in s["tt"] if r[1] == "RM"]):
        k, names = m[r[0]]
        test = r[3]
        if test.startswith("Assay"):
            hint, src = agg(names, lead, "s"), "specific tests"
        elif test.startswith("Other compendial"):
            hint, src = agg(names, lead, "g"), "general tests"
        else:
            hint, src = agg(names, lead, "t"), "all tests"
        tests = "; ".join(sorted({lead[n]["st" if src == "specific tests" else "gt"] for n in names} - {"", "-"}))[:250] if src != "all tests" \
            else "; ".join(sorted({lead[n]["gt"] + " | " + lead[n]["st"] for n in names}))[:250]
        rows.append(r + [hint, src if hint is not None else None, tests or None, k])
    table(ws, r0, s["tt_h"] + ["Recorded h/sample (Leadtime)", "Covers", "Recorded test list", "Match"],
          rows, TT_INPUT, TT_WIDTHS + [11, 12, 50, 14], TT_DV)

    extra_tests_sheet(wb, s, "RM", "Examples: residual solvents by GC, KF water as a separate test, microbial limits if done in this lab, heavy metals by ICP.")

    ws = wb.create_sheet("Other materials")
    title(ws, "Materials in Leadtime.xlsx that are not in the study list",
          "Is it still purchased and tested? If Y, give lots/yr - it will be added to the study.")
    rows = [[n, lead[n]["sheet"], round(lead[n]["t"] / 60, 2) if lead[n]["t"] else None, None, None, None, None]
            for n in sorted(unlisted, key=str.lower)]
    table(ws, 4, ["Material (as in Leadtime.xlsx)", "Leadtime sheet", "Recorded total h/lot", "Still tested? (Y/N)",
                  "Lots / yr", "Same material as (study name, if a duplicate)", "Notes"],
          rows, {4, 5, 6, 7}, [50, 10, 12, 12, 10, 36, 30], {"D": '"Y,N"'})
    return wb, dict(mats=len(mats), exact=n_exact, alias=n_alias, timed=n_timed, unlisted=len(unlisted),
                    rows=sum(1 for r in s["tt"] if r[1] == "RM"), m=m,
                    cats=collections.Counter(r[1] for r in s["rm"]))


# ---------------------------------------------------------------- FP
def campaign_candidates(fp):
    fams = collections.OrderedDict()
    for r in fp:
        if r[4]:
            f = fams.setdefault(r[4], dict(products=[], actives=set(), form=set()))
            f["products"].append(r[0])
            f["actives"].update(a.strip() for a in str(r[1] or "").split(",") if a.strip() and not a.startswith("Not in source"))
            f["form"].add(r[3] or "?")
    by_active = collections.defaultdict(list)
    for fid, f in fams.items():
        for a in f["actives"]:
            by_active[a].append(fid)
    rows = [[a, len(fids), ", ".join(fids), None, None, None]
            for a, fids in sorted(by_active.items(), key=lambda x: (-len(x[1]), x[0])) if len(fids) > 1]
    no_active = [fid for fid, f in fams.items() if not f["actives"]]
    return fams, rows, no_active


def build_fp(s):
    wb = Workbook()
    fams, camp, no_active = campaign_candidates(s["fp"])
    fp_rows = [r for r in s["tt"] if r[1] == "FP"]
    stats = [f"{len(s['fp'])} products in {len(fams)} method families and {len(fp_rows)} family x test rows from QC_Capacity_Study.xlsx (Products, Test_Times).",
             f"{len(camp)} active ingredients appear in more than one family - candidates for shared HPLC sequences ('Campaign groups').",
             f"{len(no_active)} families have no active ingredient in the formula database ({', '.join(no_active)}) - name the actives in Test times Notes.",
             "No recorded finished-product test times exist yet (Leadtime.xlsx covers raw materials only), so all times are new estimates."]
    overview(wb, "Finished Product Analyst Questionnaire", "QC Chemical Laboratory - finished products (release, stability, in-process)",
             [("Who fills it", "Each analyst who tests finished products (2-3 people). Each person fills a separate copy."),
              ("Time needed", "About 3 hours. Start with the families you test most often.")],
             [("Questions", "Respondent profile, batches & stability, methods, workload."),
              ("Volumes", "Release batches and stability samples per year for each product."),
              ("Test times", "Time per test for each method family - the core input."),
              ("Campaign groups", "Families sharing an active ingredient - can they share an HPLC sequence?"),
              ("Extra tests", "Tests missing from the list (IPC, blend uniformity, water content, preservative assay, etc.).")], stats)

    qsheet(wb.create_sheet("Questions"), FP_QUESTIONS, "Answer in the yellow column. Short answers are fine.")

    ws = wb.create_sheet("Volumes")
    title(ws, "Release batches and stability samples per year", "Columns A-M = Products sheet of the study. Grey columns K-L are calculated in the study.")
    rows = [list(r[:10]) + [None, None, r[12], None, None] for r in s["fp"]]
    table(ws, 4, s["fp_h"] + ["Stability time points / yr per batch on study", "IPC samples tested by QC per batch"],
          rows, {4, 5, 6, 7, 8, 9, 10, 13, 14, 15}, [30, 30, 8, 12, 8, 10, 10, 12, 12, 12, 1, 1, 30, 14, 14],
          {"H": '"Marketed,Pipeline / no formula,Discontinued"'})

    ws = wb.create_sheet("Test times")
    title(ws, "Test times per method family (hours)")
    r0 = help_rows(ws, 2, TIMES_HELP[:3] + [TIMES_HELP[4],
                   "A family = all strengths tested with the same methods. If one strength needs a different method, say so in Notes."]) + 1
    table(ws, r0, s["tt_h"], tt_rows(fp_rows), TT_INPUT, TT_WIDTHS, TT_DV)

    ws = wb.create_sheet("Campaign groups")
    title(ws, "Families that share an active ingredient",
          "If they use the same column and mobile phase, give them one group code (e.g. G1). The code goes into Test times column J.")
    table(ws, 4, ["Active ingredient", "# families", "Families", "Same column + mobile phase? (Y/N/partly)",
                  "Group code", "Notes"], camp, {4, 5, 6}, [36, 10, 40, 16, 10, 40], {"D": '"Y,N,Partly"'})

    extra_tests_sheet(wb, s, "FP", "Examples: blend uniformity, water content (KF), preservative assay, residual solvents, nasal spray delivered dose.")
    return wb, dict(products=len(s["fp"]), fams=len(fams), no_active=no_active, rows=len(fp_rows), camp=camp,
                    forms=collections.Counter(r[3] or "not stated" for r in s["fp"]))


# ---------------------------------------------------------------- Markdown
def md_questions(sections):
    o = []
    for sec, qs in sections:
        o += [f"### {sec}", "", "| # | Question | Answer |", "|---|---|---|"]
        o += [f"| {q} | {t} | |" for q, t, _ in qs]
        o.append("")
    return o


def write_md(path, title_, area, who, sheets, facts, sections, extra):
    o = [f"# {title_}", "",
         "**Deliverable 2 — analyst edition** of the *QC Laboratory Capacity, Staffing Gap and CAPEX Assessment* "
         "(see `reports/QC_Lab_Capacity_Staffing_CAPEX_Report.md`). The unit-head edition is "
         "`questionnaires/Chemical_Lab_Questionnaire.md`.", "",
         f"- **Area:** {area}", f"- **Who fills it:** {who}",
         f"- **Working file:** `{os.path.basename(path)[:-3]}.xlsx` — the tables are only in the workbook; this page lists the questions and explains the sheets.",
         "- **Generated by:** `tools/build_analyst_questionnaires.py` from `data/QC_Capacity_Study.xlsx` and `data/Leadtime.xlsx`. Re-run it after the source workbooks change.", "",
         "## How the answers are used", "",
         "Every table keeps the column order of the matching sheet in `QC_Capacity_Study.xlsx`, so answers are pasted back "
         "without re-typing, and the study's `Capacity` sheet then shows utilisation and the staffing/instrument gap. "
         "Times are asked as minimum / most likely / maximum, and hands-on analyst time is kept apart from unattended instrument time.", "",
         "## Workbook sheets", "", "| Sheet | What to do |", "|---|---|"]
    o += [f"| {a} | {b} |" for a, b in sheets]
    o += ["", "## Pre-filled data", ""] + [f"- {f}" for f in facts] + [""] + extra
    o += ["## Questions", ""] + md_questions(sections)
    o += ["## Declaration", "", "| | |", "|---|---|", "| Respondent | |", "| Date | |", "| Reviewed by (unit head) | |", ""]
    open(path, "w", encoding="utf-8").write("\n".join(o))


def main():
    s, lead = load_study(), load_leadtime()
    rm_wb, rm = build_rm(s, lead)
    fp_wb, fp = build_fp(s)
    rm_wb.save(os.path.join(OUT, "RM_Analyst_Questionnaire.xlsx"))
    fp_wb.save(os.path.join(OUT, "FP_Analyst_Questionnaire.xlsx"))

    no_match = sorted(k for k, (st, _) in rm["m"].items() if st.startswith("Not"))
    write_md(os.path.join(OUT, "RM_Analyst_Questionnaire.md"), "Raw Material Analyst Questionnaire",
             "QC Chemical Laboratory — raw materials", "each analyst testing incoming materials (2–3 people, one copy each)",
             [("Questions", "Answer sections A–E below."),
              ("Volumes", "Lots/yr now and future, supplier/pharmacopoeia, number of suppliers, reduced-testing status per material."),
              ("Test times", f"{rm['rows']} material × test rows. Confirm or correct the recorded Leadtime.xlsx time shown on the right."),
              ("Extra tests", "Add tests that are missing (GC residual solvents, KF as a separate test, ICP)."),
              ("Other materials", f"{rm['unlisted']} materials in Leadtime.xlsx not in the study list: still tested? lots/yr?")],
             [f"{rm['mats']} materials: " + ", ".join(f"{c} {n}" for n, c in rm["cats"].most_common()) + ".",
              f"Names matched to `Leadtime.xlsx`: {rm['exact']} exact, {rm['alias']} via a curated alias list (marked *Alias – confirm*), "
              f"{len(no_match)} not found. {rm['timed']} materials carry a recorded time.",
              "Recorded times are per test set in minutes and include unattended oven/instrument time; they are shown in hours as a "
              "starting point only. Where a material has several supplier variants, the longest time is shown.",
              "Leadtime.xlsx specific-test time is shown on the *Assay + related substances* row; general-test time on the "
              "*Other compendial tests* row; excipients show the total on their single *Compendial tests* row."],
             RM_QUESTIONS,
             ["### Materials with no match in Leadtime.xlsx", "",
              "These need a fresh time estimate (or the Leadtime.xlsx name, if it exists under another name):", "",
              ", ".join(no_match) + ".", ""])

    write_md(os.path.join(OUT, "FP_Analyst_Questionnaire.md"), "Finished Product Analyst Questionnaire",
             "QC Chemical Laboratory — finished products", "each analyst testing release and stability samples (2–3 people, one copy each)",
             [("Questions", "Answer sections A–E below."),
              ("Volumes", "Release batches/yr and stability samples/yr per product, now and future; stability time points; IPC samples."),
              ("Test times", f"{fp['rows']} family × test rows (assay, related substances, dissolution, CU, ID, other)."),
              ("Campaign groups", f"{len(fp['camp'])} actives shared by more than one family: can they share an HPLC sequence?"),
              ("Extra tests", "Add tests that are missing (blend uniformity, KF, preservative assay, delivered dose).")],
             [f"{fp['products']} products in {fp['fams']} method families; dosage forms: "
              + ", ".join(f"{c} {n}" for n, c in fp["forms"].most_common()) + ".",
              f"{len(fp['no_active'])} families have no active ingredient in the formula database ({', '.join(fp['no_active'])}); the analyst is asked to name them.",
              "Families group strengths that share methods, so times are asked once per family, not per product.",
              "There is no recorded time catalogue for finished products; every time on this questionnaire is a new estimate."],
             FP_QUESTIONS,
             ["### Most-shared actives (campaign candidates)", "", "| Active | Families |", "|---|---|"]
             + [f"| {a} | {f} |" for a, _, f, *_ in fp["camp"][:12]] + [""])
    print(f"RM: {rm['mats']} materials, {rm['rows']} test rows, exact {rm['exact']}, alias {rm['alias']}, "
          f"none {len(no_match)}, timed {rm['timed']}, other {rm['unlisted']}")
    print(f"FP: {fp['products']} products, {fp['fams']} families, {fp['rows']} test rows, {len(fp['camp'])} shared actives")
    missing = [(k, n) for k, ns in ALIASES.items() for n in ns if n not in lead]
    if missing:
        print("WARNING alias targets not found:", missing)


if __name__ == "__main__":
    main()
