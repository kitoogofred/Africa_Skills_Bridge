# Africa Skills Bridge — Portal V1.2

**Status:** deployable conference demonstration source, not yet a live hosted service. Figures 10–19 are archived notebook outputs. No occupation-level shortage, worker-demand forecast or SSEC endorsement is claimed.

## Launch locally

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Notebook integration

Run the final **Part XI — Portal integration and deployment** of the companion notebook after Part X. Download the generated `asb_portal_release.zip`, then copy its `data/` files into this repository's `data/` directory. If new figures are generated and validated, replace the corresponding `assets/figure_10.png` ... `figure_19.png`. Commit the changes and confirm the GitHub Actions quality gate.

## Deploy on Streamlit Community Cloud

1. Create a GitHub repository (e.g. `Africa_Skills_Bridge`) and upload the **contents of this folder** to its root. Do not upload credentials, restricted surveys or private datasets.
2. Verify `.github/workflows/quality.yml` succeeds under the repository Actions tab.
3. Sign in to Streamlit Community Cloud, choose **Create app → Deploy a public app from GitHub**, select your repository, branch `main`, and entrypoint `app.py`.
4. Wait for deployment, open the generated `*.streamlit.app` URL and verify all seven pages, 10 figures, provenance page and downloads. Copy the actual URL into the notebook deployment configuration cell and presentation.
5. Keep a local offline copy and screenshots for the conference. Public Streamlit hosting can be unavailable or require wake-up time.

## Optional Docker deployment

```bash
docker build -t africa-skills-bridge .
docker run --rm -p 8501:8501 africa-skills-bridge
```

## Governance

This is **not** a production LMIS or a completed ILO STED/SPEED assessment. ESCO is a reference taxonomy, and World Bank macro indicators are not evidence of occupational shortages. Before institutional use, add permissioned employer/provider data, source licensing, consultation and validation, governance decisions, access controls and monitoring. No automatic publishing of notebook exports is enabled.
