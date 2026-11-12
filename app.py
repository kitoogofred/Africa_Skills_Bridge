"""Africa Skills Bridge: conference demonstration from executed notebook figures."""
from pathlib import Path
import streamlit as st

st.set_page_config(page_title='Africa Skills Bridge | Research Prototype',page_icon='🌍',layout='wide')
ROOT=Path(__file__).parent
st.markdown("""<style>
:root {--asb-navy:#102B45;--asb-teal:#13705B;--asb-ink:#203449}
.block-container {padding-top:1.7rem;max-width:1250px}
.asb-hero {background:linear-gradient(110deg,#102B45 0%,#174A59 100%);color:#fff;padding:2.1rem 2.3rem;border-radius:15px;margin-bottom:1.2rem}
.asb-kicker {color:#A9D8CF;font-size:.78rem;letter-spacing:.12em;font-weight:700}
.asb-hero h1 {color:#fff;font-size:2.55rem;margin:.45rem 0 .3rem 0;line-height:1.15}
.asb-subtitle {font-size:1.16rem;color:#E0ECF4;line-height:1.55;margin:.2rem 0 1.15rem}
.asb-author {font-size:1.02rem;color:#fff;font-weight:650;margin:.3rem 0}
.asb-role {font-size:.88rem;color:#D0E3ED;margin:.18rem 0}
.asb-motto {border-left:3px solid #8BD7C6;padding-left:1rem;color:#E6F1F4;font-style:italic;margin-top:1.3rem;line-height:1.55}
.asb-footer {margin-top:2.5rem;padding:1.1rem 0;border-top:1px solid #D9E2E8;color:#546678;font-size:.83rem}
</style>""",unsafe_allow_html=True)
st.markdown("""<section class='asb-hero'>
<div class='asb-kicker'>AI-ENABLED · HUMAN-GOVERNED · EVIDENCE-BASED</div>
<h1>Africa Skills Bridge</h1>
<div class='asb-subtitle'>From Labour-Market Intelligence to Evidence-Based TVET Transformation</div>
<div class='asb-author'>Developed by Dr. Fredrick Edward Kitoogo</div>
<div class='asb-role'>Principal, Uganda Institute of Information and Communications Technology (UICT)</div>
<div class='asb-role'>Chairperson, ICT–STI Sector Skills Expert Committee</div>
<div class='asb-motto'>Bridging Africa’s skills intelligence gap by connecting evidence, emerging occupational competencies, education and training pathways, and informed decisions for a future-ready workforce.</div>
</section>""",unsafe_allow_html=True)
st.caption('Research and decision-support prototype | November 2026 | Portal version 1.5.6')
st.warning('Demonstration based on saved outputs of an executed research notebook. ESCO is a reference taxonomy, not evidence of African employer demand. The ILO STED/SPEED diagnostic has NOT been completed or formally endorsed.')
page=st.sidebar.radio('Explore the prototype',['Overview','Labour-market context','Occupations and competencies','Cross-sector exploration','ILO STED/SPEED pathway','Evidence and next steps','Research provenance and deployment'])
st.sidebar.caption('Offline-ready: figures bundled from the uploaded executed notebook. No live API calls.')
st.sidebar.divider()
st.sidebar.markdown('**About the developer**')
st.sidebar.caption('Dr. Fredrick Edward Kitoogo | ICT–STI skills development and digital transformation')
st.sidebar.caption('Version 1.5.6 · Research prototype')

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
 st.subheader('Welcome to Africa Skills Bridge')
 st.write('Africa’s digital transformation requires stronger connections between labour-market evidence, emerging technologies, occupational competencies and responsive education and training systems.')
 st.write('Africa Skills Bridge is an AI-enabled, human-governed research and decision-support prototype. It brings together selected international labour-market indicators, occupational and skills reference data, and an ILO-informed diagnostic pathway to support structured exploration and stakeholder dialogue.')
 st.markdown('**Our vision:** An Africa where education and training systems anticipate changing skills needs, strengthen employability and contribute to inclusive economic transformation.')
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

st.markdown("""<div class='asb-footer'><strong>Africa Skills Bridge · Version 1.5.6</strong><br>Developed by Dr. Fredrick Edward Kitoogo · Research and decision-support prototype.<br>Institutional roles identify the developer; they do not imply institutional or regulatory endorsement. ESCO is a reference taxonomy, not African employer-demand evidence. Outputs require country-specific validation before policy decisions.</div>""",unsafe_allow_html=True)
