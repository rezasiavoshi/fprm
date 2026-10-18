# QC Laboratory Capacity, Staffing Gap and CAPEX Assessment

| Folder | Contents |
|---|---|
| `brief/` | Original task brief (`capex.md`) |
| `reports/` | Deliverable 1 — assessment report (illustrative values only) |
| `questionnaires/` | Deliverable 2 — unit head questionnaires (`.md` source, `.xlsx` generated) |
| `data/` | Source workbooks and the generated lead-time catalogue (`Leadtime.md`) |
| `tools/` | Conversion scripts (need `openpyxl`) |

## Regenerating outputs

```bash
python3 tools/leadtime_to_md.py data/Leadtime.xlsx data/Leadtime.md
python3 tools/questionnaire_to_xlsx.py questionnaires/Chemical_Lab_Questionnaire.md questionnaires/Chemical_Lab_Questionnaire.xlsx
```
