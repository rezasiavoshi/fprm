# QC Laboratory Capacity, Staffing Gap and CAPEX Assessment

| Folder | Contents |
|---|---|
| `brief/` | Original task brief (`capex.md`) |
| `reports/` | Deliverable 1 — assessment report (illustrative values only) |
| `questionnaires/` | Deliverable 2 — unit-head questionnaire (`Chemical_Lab_*`) and analyst questionnaires: Chemical lab raw materials (`RM_Analyst_*`) and finished products (`FP_Analyst_*`), Physical lab (`Physical_Analyst_*`) and Micro lab (`Micro_Analyst_*`) |
| `data/` | Source workbooks, the purchasing raw-material list (`rawmaterials.md`, from usp48), the generated lead-time catalogue (`Leadtime.md`) and USP–NF tests per material (`usp_tests.csv`, micro: `usp_micro.csv`) |
| `tools/` | Conversion scripts (need `openpyxl`) |

## Regenerating outputs

```bash
python3 tools/leadtime_to_md.py data/Leadtime.xlsx data/Leadtime.md
python3 tools/questionnaire_to_xlsx.py questionnaires/Chemical_Lab_Questionnaire.md questionnaires/Chemical_Lab_Questionnaire.xlsx
PYTHONPATH=tools python3 tools/usp_tests.py     # data/usp_tests.csv + usp_micro.csv: RM tests per material from ~/usp48 (USP-NF index)
python3 tools/build_analyst_questionnaires.py   # RM, FP, Physical and Micro analyst questionnaires (.xlsx + .md)
```
