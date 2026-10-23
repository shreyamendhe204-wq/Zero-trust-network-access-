# Zero Trust Network Access (ZTNA) — Educational Project

## Project description
This project demonstrates a small, explainable Zero Trust-style access policy simulator. It evaluates fictional access requests using role permissions, device management/compliance, multi-factor authentication (MFA) status, and an illustrative risk score. The result is `ALLOW`, `DENY`, or `STEP-UP MFA`.

## Files
- `ShreyaMendhe_ZTNA.ipynb` — executable Jupyter Notebook with code and sample data.
- `requirements.txt` — Python dependency list.
- `ShreyaMendhe_ProjectReport.docx` — project report.
- `ShreyaMendhe_ZTNA_Presentation.pptx` — presentation slides.
- `README.md` — project overview and setup guide.

## Technologies used
- Python 3
- Jupyter Notebook
- pandas (for displaying and summarizing sample decisions)

## Setup and run
1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (recommended).
4. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
5. Start Jupyter:
   ```bash
   python -m pip install notebook
   jupyter notebook
   ```
6. Open `ShreyaMendhe_ZTNA.ipynb` and choose **Run All**.

## Dataset
The notebook uses fictional sample access requests defined directly in the notebook. No external dataset is required, and no real personal or network data is collected.

## Expected outcome
The notebook produces a table containing each request, the decision, and the reason, plus a summary count of decisions.

## Important limitation
This is an educational policy simulation, not a production ZTNA implementation. It does not connect to a network, provide real authentication, enforce access to applications, or replace a commercial security platform. Risk thresholds and policy rules are examples only.
