"""Africa Skills Bridge: conference demonstration from executed notebook figures."""
from pathlib import Path
import streamlit as st

st.set_page_config(page_title='Africa Skills Bridge | Research Prototype',page_icon='🌍',layout='wide')
ROOT=Path(__file__).parent
st.title('Africa Skills Bridge')
st.caption('From labour-market intelligence to evidence-informed TVET transformation | Conference research prototype, 13 November 2026')
st.warning('Demonstration based on saved outputs of an executed research notebook. ESCO is a reference taxonomy, not evidence of African employer demand. The ILO STED/SPEED diagnostic has NOT been completed or formally endorsed.')
page=st.sidebar.radio('Explore the prototype',['Overview','Labour-market context','Occupations and competencies','Cross-sector exploration','ILO STED/SPEED pathway','Evidence and next steps','Research provenance and deployment'])
st.sidebar.caption('Offline-ready: figures bundled from the uploaded executed notebook. No live API calls.')

def load_manifest():
 p=ROOT/'data'/'release_manifest.json'
 if p.exists():
  try:
   import json
   obj=json.loads(p.read_text(encoding='utf-8'))
   return obj if isinstance(obj,dict) else None
  except (OSError,ValueError):return None
 return None

def fig(n,caption):
 p=ROOT/'assets'/f'figure_{n}.png'
 if p.exists():st.image(str(p),caption=caption,use_container_width=True)
 else:st.error(f'Figure {n} not bundled')

if page=='Overview':
 st.subheader('What has been demonstrated')
 st.info('The figures are an archived research snapshot. Dataset totals and verification status are shown only when supported by an exported release manifest. No labour-market shortage estimate is implied.')
 manifest=load_manifest()
 if manifest:
  st.json({k:manifest.get(k) for k in ('version','generated_utc','world_bank_rows','esco_profile_rows','esco_relation_rows','research_claim') if k in manifest})
 else:st.caption('A verified release manifest has not yet been imported. Run the notebook export section to populate one.')
 fig(10,'ESCO discovery: selected occupations and retrieval coverage')
 st.markdown('**Presentation message:** We connect official aggregate indicators, occupational reference concepts and a transparent evidence-to-decision framework. The prototype identifies what remains to be validated before policy decisions.')
elif page=='Labour-market context':
 st.subheader('Official aggregate labour-market indicators')
 fig(16,'Figure 16 — World Bank country-indicator trends from the executed notebook')
 fig(17,'Figure 17 — latest common-year comparisons, where observations permit')
 with st.expander('Interpretation and limits',expanded=True):
  st.write('The figures provide descriptive macroeconomic context. Compare countries only within the same indicator definition and observation year. They cannot establish occupation-level vacancies, shortages, or training gaps. Check country coverage and observation years before interpreting differences.')
 fig(14,'Figure 14 — World Bank evidence coverage')
elif page=='Occupations and competencies':
 st.subheader('ESCO occupational reference intelligence')
 fig(11,'Figure 11 — essential and optional occupation–skill relationships')
 fig(12,'Figure 12 — occupation relationship coverage in the sampled profiles')
 fig(18,'Figure 18 — selected occupation–skill reference matrix')
 st.info('ESCO relationship frequencies reflect taxonomy structure and the selected sample. They do not quantify skill demand, skill proficiency, or shortages in Uganda.')
elif page=='Cross-sector exploration':
 st.subheader('Digital competencies across economic-sector search themes')
 fig(13,'Figure 13 — exploratory cross-sector skill search')
 fig(19,'Figure 19 — overlap of retrieved skill URIs between search themes')
 st.write('Search-term overlap is a discovery aid, not proof of sector requirements. Proposed use cases in agriculture, manufacturing, tourism and minerals require employer and occupational-task validation.')
elif page=='ILO STED/SPEED pathway':
 st.subheader('Seven-stage evidence-to-decision diagnostic')
 stages=[('0','Sector selection','PARTIAL','Agree sector priorities with employers and public stakeholders'),('1','Sector position and outlook','PARTIAL','Add sector output, trade, investment and value-chain evidence'),('2','Business capabilities','PARTIAL','Interview enterprises and map work processes'),('3','Types of skills','REFERENCE ONLY','Validate ESCO references against national standards and tasks'),('4','Numbers of workers by skill type','EVIDENCE GAP','Obtain occupational employment and demand data'),('5','Skills supply and gaps','EVIDENCE GAP','Collect provider, graduate, tracer and employer evidence'),('6','Proposed responses','FRAMEWORK','Validate interventions, financing, responsibilities and indicators')]
 for number,name,status,action in stages:
  with st.expander(f'Stage {number}: {name} — {status}',expanded=number in ('3','4','5')):
   st.write('Next evidence/action:',action)
 fig(15,'Figure 15 — methodological readiness from the earlier executed section')
 st.caption('Stage categories are qualitative research assessments, not numerical scores or ILO certification.')
elif page=='Evidence and next steps':
 st.subheader('Research integrity and what remains')
 st.table({'Workstream':['Live/verified source provenance','Sector economic and value-chain evidence','Employer skills-demand assessment','Occupational employment estimates','TVET capacity and graduate outcomes','Stakeholder validation','Formal SSEC/Council decisions'], 'Current position':['Check against executed notebook and saved source manifests','Pending','Pending','Pending','Pending','Pending','Not claimed']})
 st.success('Tomorrow’s defensible claim: an evidence-organising and visual decision-support prototype has been demonstrated; formal sector skills assessment is the next phase.')
 st.markdown('**Suggested 5-minute demo:** Overview (45 sec) → Labour-market context (60 sec) → Occupations and competencies (75 sec) → ILO pathway (75 sec) → Evidence gaps and invitation for collaboration (45 sec).')

else:
 st.subheader('Provenance, release artifacts and deployment')
 m=load_manifest()
 if m:st.json(m)
 else:st.warning('No exported notebook release manifest installed. Displayed figures are a static conference snapshot, not a verified current release.')
 for filename in ['evidence_inventory.csv','sted_speed_alignment.csv','consultation_action_register.csv','sector_screening.csv']:
  p=ROOT/'data'/filename
  if p.is_file():
   st.markdown('**'+filename.replace('_',' ').replace('.csv','').title()+'**')
   import pandas as pd
   df=pd.read_csv(p);st.dataframe(df,use_container_width=True)
   st.download_button('Download '+filename,df.to_csv(index=False).encode('utf-8'),filename,mime='text/csv',key=filename)
 st.caption('Deployment URL is configured after publication. GitHub and hosting are not automatically created by the notebook.')
