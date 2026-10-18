"""Flatten each RM master-list material into its USP-NF compendial tests -> data/usp_tests.csv.

Reads the usp48 index read-only (section headings + chapter numbers; section text is only scanned by
regex for the technique, never printed). Materials without a monograph get no rows here; the
questionnaire keeps one 'In-house specification tests' row for them.
Usage: python3 tools/usp_tests.py [--usp48 ~/usp48]   (run from the repo root)
"""
import csv, os, re, sqlite3, sys, collections
sys.argv[1:1] = []  # builder reads ROOT from argv[1]; keep it '.'
import build_analyst_questionnaires as B

USP48 = os.path.expanduser(sys.argv[sys.argv.index("--usp48") + 1] if "--usp48" in sys.argv else "~/usp48")
OUT = os.path.join("data", "usp_tests.csv")

# Master-list material -> monograph title, where spelling/purchase matching fails or picks wrongly.
# Herbal dry extracts are mapped to the closest DS extract monograph; the extract ratio is not checked.
MANUAL = {
    "Dapagliflozin Propanediol Monohydrate": "Dapagliflozin Propanediol",
    "Dextromethorphan HBr": "Dextromethorphan Hydrobromide",
    "Loperamide HCl": "Loperamide Hydrochloride",
    "Phenylephrine HCl": "Phenylephrine Hydrochloride",
    "L-Citrulline": "Citrulline",
    "L-Carnitine (Base)": "Levocarnitine",
    "Borax": "Sodium Borate",
    "D-Alpha Tocopheryl Acetate 50% (Vitamin E)": "Vitamin E Preparation",
    "dl-Alpha Tocopheryl Acetate 50% (Vitamin E)": "Vitamin E Preparation",
    "Echinacea Purpurea Dry Extract": "Powdered Echinacea purpurea Extract",
    "Ginkgo Biloba Leaf Dry Extract 50:1": "Powdered Ginkgo Extract",
    "Milk Thistle Dry Extract 70:1": "Powdered Milk Thistle Extract",
    "Saw Palmetto Dry Extract 4:1": "Saw Palmetto Extract",
    "Panax Ginseng (Asian Ginseng) Dry Extract 3:1": "Asian Ginseng Root and Rhizome Dry Extract",
    "Siberian Ginseng Dry Extract 5:1": "Eleuthero Root and Rhizome Dry Extract",
    "Liquorice Dry Extract 8:1": "Powdered Licorice Extract",
    "Garcinia Cambogia Fruit Dry Extract 6:1": "Powdered Garcinia Hydroxycitrate Extract",
    "Coleus Forskohlii Root Dry Extract 10:1": "Powdered Forskohlii Extract",
    "Gymnema Sylvestre Leaf Dry Extract 10:1": "Native Gymnema Extract",
    "PVP K90": "Povidone",
    "HPMC 15cps (Hypromellose)": "Hypromellose",
    "HPMC K100M (100,000 cps CR)": "Hypromellose",
    "L-Menthol": "Menthol",
    "Glycerine": "Glycerin",
    "Benzalkonium Alcohol 50%": "Benzalkonium Chloride Solution",
    "Glyceryl Behenate (Compritol 888 ATO)": "Glyceryl Dibehenate",
    "Methacrylic Acid Copolymer (Eudragit L100-55)": "Methacrylic Acid and Ethyl Acrylate Copolymer",
    "Deionized Water": "Purified Water",
    "Water": "Purified Water",
    "Microcrystalline Cellulose RC591": "Microcrystalline Cellulose and Carboxymethylcellulose Sodium",
    "Sorbitol Solution 70%": "Sorbitol Solution",
    "Citric Acid": "Citric Acid Monohydrate",
    "Hydrochloric Acid Solution 37%": "Hydrochloric Acid",
    "Sodium Citrate Dihydrate": "Sodium Citrate",
}

SKIP_MAJOR = {"Header", "DEFINITION", "ADDITIONAL REQUIREMENTS"}


def monograph_titles(db):
    return {B.norm(t): t for (t,) in db.execute("select title from monographs where category in ('USP','NF','DS')")}


def map_materials(mats, db):
    titles = monograph_titles(db)
    raw = B.load_raw()
    pairs = B.match_raw(raw, mats, B.load_leadtime(), B.load_db_mapping())
    by_purchase = {}
    for r in csv.DictReader(open(os.path.join(USP48, "output/master_by_row.csv"), encoding="utf-8-sig")):
        if r["monograph_title"] and r["monograph_title"] != "NO_MONOGRAPH":
            by_purchase[B.norm(re.sub(r"\s+", " ", r["original"].strip()))] = r["monograph_title"]
    via = collections.defaultdict(collections.Counter)
    for name, _, st, m in pairs:
        if m and st.startswith("On master list") and B.norm(name) in by_purchase:
            via[m][by_purchase[B.norm(name)]] += 1
    res = {}
    for m in mats:
        if m in MANUAL:
            res[m] = (MANUAL[m], "manual")
        elif B.norm(m) in titles:
            res[m] = (titles[B.norm(m)], "title")
        elif via.get(m):
            t, _ = via[m].most_common(1)[0]
            res[m] = (t, "purchase list" + (" (several)" if len(via[m]) > 1 else ""))
        else:
            res[m] = (None, "none")
    return res


SPECIFIC = {"HPLC", "GC"}   # techniques timed per material, not from the catalog
ELEMENTS = r"\b(lead|nickel|cadmium|aluminum|iron|arsenic|mercury|copper|zinc|calcium|potassium|sodium|magnesium|barium|selenium)\b"
MICRO = {"61", "62", "71", "85", "2021", "2022", "2023"}
CHAPTER_CODE = {"197": "ID_IR", "191": "ID_CHEM", "201": "TLC", "203": "TLC", "731": "LOD", "281": "ROI", "733": "LOI",
                "561": "ASH", "791": "PH", "781": "OR", "741": "MP", "841": "SG", "831": "RI", "911": "VISC", "912": "VISC",
                "913": "VISC", "645": "COND", "643": "TOC", "221": "LIMIT", "211": "LIMIT", "241": "LIMIT", "231": "LIMIT",
                "271": "LIMIT", "206": "LIMIT", "401": "FATS", "616": "PHYS", "846": "PHYS", "467": "RS_GC", "541": "TITR",
                "857": "UV", "233": "AAS", "251": "LIMIT", "261": "LIMIT", "611": "GC"}


def clean_name(minor, text):
    n = re.sub(r"[⧫◆▲▼•]|\((?:USP|NF|CN)[^)]*\)", "", minor)
    n = re.sub(r"\s+", " ", n).strip(" :")
    if not n or re.fullmatch(r"[A-Z]\.?", n):
        t = re.sub(r"[⧫◆▲▼•]|\((?:USP|NF|CN)[^)]*\)", "", text).strip()
        t = re.sub(r"^[A-Z]\.\s*", "", t)
        t = re.split(r"\s(?:Sample|Standard|Analysis|Solution|Buffer|Mobile|Diluent)\b|:|〈|\[", t)[0].strip()
        n = (minor.strip(" .⧫◆") + ". " if minor.strip(" .⧫◆") else "") + (t[:50] or "test")
    return n[:90]


def classify(major, name, text):
    """-> (code or None, technique, applicable, note). code None = material-specific (HPLC/GC/other)."""
    t = text
    chs = re.findall(r"〈(\d+)[A-Z]?〉", t[:400])
    low = (name + " " + t).lower()
    if any(c in MICRO for c in chs) or re.search(r"microbial|sterility|endotoxin|specified microorganisms", name.lower()):
        return "MICRO", "Micro lab", "drop", ""
    if major == "IDENTIFICATION" and re.search(r"retention times?|as obtained in|corresponds to th", name.lower()):
        return "SHARED", "from another test", "drop", ""
    if len(t) < 500 and re.search(r"retention times?|as obtained in|corresponds to that of|chromatogram", low) \
            and not re.search(r"mobile phase|column:", low):
        return "SHARED", "from another test", "drop", ""
    if re.search(r"^(packaging|labeling|usp reference)", name.lower()):
        return "SKIP", "", "drop", ""
    note = ""
    appl = "Y"
    if re.search(r"where (it is labeled|the label states)|\(where it is labeled|intended for use in the manufacture of (injectable|peritoneal|hemodialysis)", low[:600]):
        appl, note = "N", "Only for some grades/labels - check your supplier grade"
    if re.search(ELEMENTS, name.lower()) and re.search(r"^(limit of )?\w+$", name.lower()):
        tech = "AAS" if re.search(r"atomic absorption|inductively coupled|matrix modifier|graphite furnace", low) else ""
    elif re.search(r"mode:\s*gc|gas chromatograph|carrier gas|column:.{0,150}?\bg\d+\b|headspace", low):
        tech = "GC"
    elif re.search(r"mode:\s*(lc|hplc|ic)|\bhplc\b|column:.{0,150}?\bl\d+\b|ion chromatograph", low):
        tech = "HPLC"
    elif re.search(r"thin-layer|mode:\s*(tlc|hptlc)|\brf value", low):
        tech = "TLC"
    elif re.search(r"atomic absorption|inductively coupled|matrix modifier|mode:\s*(aa|icp)|graphite furnace|hollow-cathode", low):
        tech = "AAS"
    elif re.search(r"chromatographic system|mobile phase|relative retention|system suitability solution", low) \
            or (major == "ASSAY" and "as directed in the assay for" in low):
        tech = "" if re.search(ELEMENTS, name.lower()) else "CHROM"
    else:
        tech = ""
    code = None
    if "565" in chs or "561" in chs:
        code = "PEST" if "pesticide" in low else ("RS_GC" if "solvent" in low else ("ASH" if "ash" in low else None))
    if code is None and tech == "GC" and re.search(r"residual solvent|〈467〉", low):
        code = "RS_GC"
    if code is None and tech in SPECIFIC | {"CHROM"}:
        return None, tech, appl, note
    if code is None:
        for c in chs:
            if c in CHAPTER_CODE:
                code = CHAPTER_CODE[c]
                break
    if code == "LIMIT" and tech == "AAS":
        code = "AAS"
    if code == "GC":
        return None, "GC", appl, note
    if code is None:
        if "921" in chs or re.search(r"water determination", low):
            code = "KF" if re.search(r"method i\b|method ia|method ic|titrimetric", low) else "LOD"
        elif tech == "TLC":
            code = "TLC"
        elif tech == "AAS":
            code = "AAS"
        elif re.search(r"infrared", low):
            code = "ID_IR"
        elif re.search(r"optical rotation|specific rotation", low):
            code = "OR"
        elif re.search(r"(clarity|color|colour|appearance|completeness) (and colou?r )?of solution", name.lower()):
            code = "CLAR"
        elif re.search(r"\bacidity|alkalinity", name.lower()):
            code = "ACID"
        elif re.search(r"acid value|iodine value|peroxide value|saponification|hydroxyl value|ester value", low):
            code = "FATS"
        elif re.search(r"titrat|kjeldahl|nitrogen determination", low):
            code = "TITR"
        elif re.search(r"fluoresc|ultraviolet|〈857〉|absorbance|spectrophotomet|wavelength", low):
            code = "ID_UV" if major == "IDENTIFICATION" else "UV"
        elif re.search(r"water-soluble|insoluble|residue on evaporation|nonvolatile residue|weigh the residue", low):
            code = "GRAV"
        elif re.search(r"conductivity", name.lower()):
            code = "COND"
        elif re.search(r"settling volume|bulk density|surface area|particle size|k-value", low):
            code = "PHYS" if "k-value" not in low else "VISC"
        elif major == "IDENTIFICATION":
            code = "ID_CHEM"
        else:
            code = "LIMIT"
    if code == "ID_IR" and major != "IDENTIFICATION":
        code = "UV" if "ultraviolet" in low else code
    return code, B.USP_CATALOG[code][1], appl, note


def display_name(major, name, code, tech):
    """Short test label: 'Assay (HPLC)', 'ID A - IR', 'Organic Impurities (HPLC)'."""
    what = tech if not code else B.USP_CATALOG[code][0].split(" (")[0].replace("Identification - ", "")
    if major == "IDENTIFICATION":
        m = re.match(r"([A-Z])\.", name)
        return f"ID {m.group(1)} - {what}" if m else f"ID - {what}"
    if major == "ASSAY" and re.fullmatch(r"(Procedure|Assay)?\s*\d*", name):
        name = "Assay"
    elif major == "ASSAY" and code in ("", None, "TITR", "UV", "AAS") and not name.lower().startswith(("assay", "content")):
        name = "Assay - " + name
    return f"{name} ({tech})" if not code else name


def extract(db, titles):
    """monograph title -> [dict(section, test, chapter, code, technique, applicable, note)] (dropped rows excluded)."""
    q = ",".join("?" * len(titles))
    rows = db.execute(f"select m.title, s.major, s.minor, s.text from sections s join monographs m on m.id=s.monograph_id "
                      f"where m.category in ('USP','NF','DS') and m.title in ({q}) order by m.title, s.ord", titles).fetchall()
    tests = collections.defaultdict(list)
    for title, major, minor, text in rows:
        if major in SKIP_MAJOR:
            continue
        text = re.sub(r"\s+", " ", text or "").strip()
        if not text.startswith("•"):
            if tests[title]:
                tests[title][-1]["text"] += " " + text
            continue
        tests[title].append(dict(major=major, minor=minor, text=text))
    out = {}
    for title, ts in tests.items():
        seen, lst = set(), []
        for i, t in enumerate(ts):   # index artefact: a cut-short bullet whose body sits in the next section
            if len(t["text"]) < 60 and "〈" not in t["text"] and ":" not in t["text"] and i + 1 < len(ts) and ts[i + 1]["major"] == t["major"]:
                t["text"] += " " + ts[i + 1]["text"]
            if t["major"] != "IDENTIFICATION" and re.match(r"[⧫◆▲\s]*[A-H]\.\s", t["minor"]):
                t["major"] = "IDENTIFICATION"
        cls = [(t, clean_name(t["minor"], t["text"][1:].strip())) for t in ts]
        cls = [(t, name, classify(t["major"], name, t["text"])) for t, name in cls]
        assay = next((c[1] for t, _, c in cls if t["major"] == "ASSAY" and c[1] in SPECIFIC), "HPLC")
        for t, name, (code, tech, appl, note) in cls:
            if appl == "drop":
                continue
            tech = assay if tech == "CHROM" else tech
            name = display_name(t["major"], name, code, tech)
            key = (code, name.split(",")[0]) if code else name
            if key in seen:
                continue
            seen.add(key)
            name = name.split(",")[0] if code == "LIMIT" else name
            ch = ",".join(dict.fromkeys(re.findall(r"〈(\d+)[A-Z]?〉", t["text"][:400])))
            lst.append(dict(section=t["major"].title(), test=name, chapter=ch, code=code or "", technique=tech,
                            applicable=appl, note=note))
        if sum(x["section"] == "Assay" for x in lst) > 1:
            for x in lst:
                if x["section"] == "Assay":
                    x["note"] = x["note"] or "Alternative assays - keep only the one you run"
        out[title] = lst
    return out


def main():
    s = B.load_study()
    mats = [(r[0], r[1]) for r in s["rm"]]
    db = sqlite3.connect(os.path.join(USP48, "output/usp.sqlite"))
    mp = map_materials([m for m, _ in mats], db)
    tests = extract(db, sorted({t for t, _ in mp.values() if t}))
    cols = ["material", "category", "monograph", "mapped_by", "section", "test", "chapter", "code", "technique", "applicable", "note"]
    n = 0
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for m, cat in mats:
            t, how = mp[m]
            for x in tests.get(t, []) if t else [{}]:
                w.writerow([m, cat, t or "", how] + [x.get(k, "") for k in cols[4:]])
                n += 1
    by = collections.Counter(how for _, how in mp.values())
    print(f"{OUT}: {n} rows; materials mapped {sum(v for k, v in by.items() if k != 'none')}/{len(mats)} {dict(by)}")
    flat = [x for t in tests.values() for x in t]
    print("by code:", dict(collections.Counter(x["code"] or x["technique"] for x in flat).most_common()))


if __name__ == "__main__":
    main()
