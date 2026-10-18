"""Convert Leadtime.xlsx (QC chemical-lab test-time catalogue) to Markdown with summary analysis."""
import sys, statistics, openpyxl

def num(v):
    return v if isinstance(v, (int, float)) else None

def cell(v):
    if v is None: return ""
    return str(v).replace("|", "/").replace("\n", " ").strip()

def main(src, dst):
    wb = openpyxl.load_workbook(src, data_only=True)
    gen = wb["General Test"]
    general = [(cell(r[0]), r[1]) for r in gen.iter_rows(min_row=2, values_only=True) if r[0]]

    sheets = {}
    for ws in wb.worksheets[1:]:
        rows = []
        for r in ws.iter_rows(min_row=2, values_only=True):
            if not r[0]: continue
            g, s = num(r[12]), num(r[16])
            t = num(r[20]) if len(r) > 20 else None
            if t is None and (g is not None or s is not None):
                t = (g or 0) + (s or 0)
            rows.append(dict(mat=cell(r[0]), gt=cell(r[4]), st=cell(r[8]), g=g, s=s, t=t,
                             gtxt=cell(r[12]), stxt=cell(r[16]),
                             ttxt=cell(r[20]) if len(r) > 20 else ""))
        sheets[ws.title] = rows

    allrows = [(sh, r) for sh, rs in sheets.items() for r in rs]
    timed = [(sh, r) for sh, r in allrows if r["t"]]
    blank = [(sh, r) for sh, r in allrows if not r["t"]]
    totals = [r["t"] for _, r in timed]
    mismatch = [(sh, r) for sh, r in timed
                if r["g"] is not None and r["s"] is not None and len(str(r["ttxt"])) and num_eq(r) is False]
    dup_general = sorted({n for n, _ in general if [x for x, _ in general].count(n) > 1})

    o = []
    w = o.append
    w("# QC Chemical Laboratory — Test Lead-Time Catalogue\n")
    w(f"Source: `data/Leadtime.xlsx` ({len(wb.worksheets)} sheets). Converted with `tools/leadtime_to_md.py`. "
      "All times are analyst hands-on/elapsed minutes per sample as recorded in the workbook.\n")
    w("## 1. Analysis summary\n")
    w("| Metric | Value |\n|---|---|")
    w(f"| Materials listed (Premix + A–Z sheets) | {len(allrows)} |")
    w(f"| Materials with a time estimate | {len(timed)} ({len(timed)*100//max(1,len(allrows))}%) |")
    w(f"| Materials without data (`-` or blank) | {len(blank)} |")
    if totals:
        w(f"| Total time per material — median | {statistics.median(totals):.0f} min ({statistics.median(totals)/60:.1f} h) |")
        w(f"| Total time per material — mean | {statistics.mean(totals):.0f} min ({statistics.mean(totals)/60:.1f} h) |")
        w(f"| Total time per material — min / max | {min(totals):.0f} / {max(totals):.0f} min |")
        w(f"| Sum over all timed materials (one sample each) | {sum(totals):,.0f} min ({sum(totals)/60:,.0f} h) |")
        sg = sum(r['g'] or 0 for _, r in timed); ss = sum(r['s'] or 0 for _, r in timed)
        w(f"| Share of time in general vs specific tests | {sg*100/(sg+ss):.0f}% general / {ss*100/(sg+ss):.0f}% specific |")
    w(f"| General test types catalogued | {len(general)} |")
    w("")
    w("### 1.1 Coverage by sheet\n")
    w("| Sheet | Materials | With time | Coverage | Median total (min) | Max total (min) |\n|---|---:|---:|---:|---:|---:|")
    for sh, rs in sheets.items():
        ts = [r["t"] for r in rs if r["t"]]
        w(f"| {sh} | {len(rs)} | {len(ts)} | {len(ts)*100//max(1,len(rs))}% | "
          f"{statistics.median(ts):.0f} | {max(ts):.0f} |" if ts else f"| {sh} | {len(rs)} | 0 | 0% | – | – |")
    w("\n### 1.2 Time-band distribution (timed materials)\n")
    bands = [(0, 120, "≤ 2 h"), (120, 480, "2–8 h (≤ 1 shift)"), (480, 1440, "8–24 h"), (1440, 2880, "1–2 days"), (2880, 1e9, "> 2 days")]
    w("| Band | Materials |\n|---|---:|")
    for lo, hi, lab in bands:
        w(f"| {lab} | {sum(1 for t in totals if lo < t <= hi or (lo == 0 and t <= hi))} |")
    w("\n### 1.3 Longest 15 materials (main capacity drivers)\n")
    w("| # | Sheet | Material | Specific tests | Total (min) | Total (h) |\n|---:|---|---|---|---:|---:|")
    for i, (sh, r) in enumerate(sorted(timed, key=lambda x: -x[1]["t"])[:15], 1):
        w(f"| {i} | {sh} | {r['mat']} | {r['st']} | {r['t']:.0f} | {r['t']/60:.1f} |")
    w("\n### 1.4 Data-quality observations\n")
    w(f"- {len(blank)} of {len(allrows)} materials ({len(blank)*100//max(1,len(allrows))}%) have no time estimate — the catalogue cannot yet support a full workload model.")
    if mismatch:
        w(f"- {len(mismatch)} rows where Total ≠ General + Specific: " + ", ".join(f"{r['mat']} ({sh})" for sh, r in mismatch[:10]) + ".")
    if dup_general:
        w(f"- Duplicate entries in the General Test list with different times: {', '.join(dup_general)}.")
    partial = [(sh, r) for sh, r in timed if r["st"] not in ("", "-") and r["s"] is None]
    if partial:
        w(f"- {len(partial)} materials list specific tests but no specific-test time, so their total is understated: "
          + ", ".join(f"{r['mat']} ({sh})" for sh, r in partial) + ".")
    w("- Sheet W has no Total column; totals were computed as General + Specific.")
    w("- Times are per test set, not per analyst-hour: long items (LOD 24 h, water absorption 48 h, multi-assay HPLC premixes) include unattended instrument/oven time, so hands-on vs elapsed time must be separated before FTE calculations.")
    w("- Spelling variants (e.g. ‘Apperance’, ‘Soluibility’, ‘Mangnesium’) kept as in the source.")
    w("")
    w("## 2. General test time catalogue\n")
    w("| # | Test | Time (min) |\n|---:|---|---:|")
    for i, (n, t) in enumerate(general, 1):
        w(f"| {i} | {n} | {cell(t)} |")
    w("")
    w("## 3. Material test-time tables\n")
    for sh, rs in sheets.items():
        w(f"### Sheet {sh}\n")
        w("| Material | General tests | Specific tests | General (min) | Specific (min) | Total (min) |\n|---|---|---|---:|---:|---:|")
        for r in rs:
            tot = f"{r['t']:.0f}" if r["t"] else (r["ttxt"] or "-")
            w(f"| {r['mat']} | {r['gt'] or '-'} | {r['st'] or '-'} | {r['gtxt'] or '-'} | {r['stxt'] or '-'} | {tot} |")
        w("")
    open(dst, "w").write("\n".join(o) + "\n")

def num_eq(r):
    try:
        return abs(float(r["ttxt"]) - ((r["g"] or 0) + (r["s"] or 0))) < 0.5
    except ValueError:
        return None

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
