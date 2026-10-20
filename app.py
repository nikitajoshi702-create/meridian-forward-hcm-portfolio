import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Meridian Forward | Problem & Output", page_icon="🎯", layout="wide")

# Consistent, high-contrast visual system
st.markdown("""
<style>
:root {
  --navy:#14243A;
  --navy2:#203B5A;
  --blue:#3567D4;
  --teal:#138A80;
  --ink:#172B43;
  --muted:#53657A;
  --paper:#F3F6FA;
  --white:#FFFFFF;
  --line:#DCE4EE;
}
.stApp { background:var(--paper); color:var(--ink); }
[data-testid="stAppViewContainer"] { background:var(--paper); }
.block-container { max-width:1240px; padding-top:1.7rem; padding-bottom:3rem; }
[data-testid="stSidebar"] { background:var(--navy); }
[data-testid="stSidebar"] * { color:#F8FAFC !important; }
[data-testid="stSidebar"] [data-testid="stRadio"] label { background:transparent; border-radius:8px; padding:5px 7px; }
[data-testid="stSidebar"] [data-testid="stRadio"] label p { color:#F8FAFC !important; font-weight:600; }
[data-testid="stSidebar"] hr { border-color:#3C5068; }
.hero {
  background:linear-gradient(115deg,var(--navy) 0%,var(--navy2) 62%,var(--blue) 100%);
  padding:2.1rem 2.25rem; border-radius:20px; margin-bottom:1.35rem;
  box-shadow:0 8px 24px rgba(20,36,58,.12);
}
.hero .eyebrow { color:#BBD0FF; font-size:.78rem; font-weight:800; letter-spacing:.14em; }
.hero h1 { color:#FFFFFF !important; font-size:2.55rem; line-height:1.12; margin:.45rem 0 .6rem; }
.hero p { color:#EAF1FF !important; font-size:1.08rem; margin:0; }
h1,h2,h3,h4,p,li,label { color:var(--ink); }
h2 { font-weight:750; letter-spacing:-.02em; }
h3 { font-weight:700; }
.stMarkdown, .stMarkdown p, .stMarkdown li { color:var(--ink); }
.panel {
  background:#FFFFFF; padding:1.2rem 1.2rem 1.15rem; border:1px solid var(--line);
  border-radius:16px; min-height:160px; box-shadow:0 4px 14px rgba(20,36,58,.045);
}
.panel h3 { color:var(--navy) !important; font-size:1.13rem; margin:.2rem 0 .7rem; }
.panel p { color:var(--muted) !important; line-height:1.55; margin:0; }
div[data-testid="stMetric"] {
  background:#FFFFFF; border:1px solid var(--line); border-radius:15px;
  padding:1rem 1.1rem; box-shadow:0 4px 14px rgba(20,36,58,.04);
}
div[data-testid="stMetricLabel"] p { color:var(--muted) !important; font-weight:650; }
div[data-testid="stMetricValue"] { color:var(--navy) !important; font-weight:800; }
div[data-testid="stMetricDelta"] { font-weight:650; }
.stAlert { border-radius:12px; }
[data-testid="stDataFrame"], [data-testid="stTable"] { background:#FFFFFF; }
.stCaption, [data-testid="stCaptionContainer"] { color:var(--muted) !important; }
div.stButton > button { border-radius:9px; font-weight:650; }
hr { border-color:var(--line); }
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("## 🧭 Meridian Forward")
st.sidebar.caption("HCM AS2 • Team 02")
page = st.sidebar.radio("Portfolio", ["Problem", "Output"])
st.sidebar.divider()
st.sidebar.caption("Problem → evidence → recommended output")

st.markdown("""
<div class="hero">
  <div class="eyebrow">HUMAN CAPITAL MANAGEMENT • AS2</div>
  <h1>Meridian Forward</h1>
  <p>From workforce capability problem to a practical HR solution</p>
</div>
""", unsafe_allow_html=True)

if page == "Problem":
    st.markdown("## 01 / The Problem")
    st.write("Meridian Forward wants shorter product cycles and more original design while maintaining reliable existing services. Slow decision-making, coordination challenges and specialist skill shortages may prevent the proposed four-week pilot from being delivered safely.")
    c1,c2,c3 = st.columns(3)
    c1.metric("Available capacity", "1,984 hours")
    c2.metric("Pilot demand", "1,868 hours")
    c3.metric("Specialist gaps", "216 hours")
    st.markdown("### The three challenges")
    a,b,c = st.columns(3)
    with a:
        st.markdown('<div class="panel"><h3>⚙️ Capability mismatch</h3><p>Total capacity appears sufficient, but the right specialist skills are not available in the right roles.</p></div>', unsafe_allow_html=True)
    with b:
        st.markdown('<div class="panel"><h3>↔️ Workload uncertainty</h3><p>The baseline assumes 60 duplicate customer packs—240 hours of work—can be removed without harming service.</p></div>', unsafe_allow_html=True)
    with c:
        st.markdown('<div class="panel"><h3>⏱️ Decision delays</h3><p>Unclear decision rights and escalation routes can slow delivery while existing service commitments continue.</p></div>', unsafe_allow_html=True)
    st.markdown("### Evidence: specialist capability gaps")
    gaps = pd.DataFrame({"Capability":["Data preparation","Quality assurance","Legacy expertise"],"Shortage (hours)":[80,72,64]})
    fig = px.bar(gaps, x="Capability", y="Shortage (hours)", text="Shortage (hours)", title="216 hours of role-specific shortages",
                 color="Capability", color_discrete_sequence=["#3567D4","#138A80","#7295D9"])
    fig.update_traces(textposition="outside", marker_line_width=0)
    fig.update_layout(showlegend=False, plot_bgcolor="#FFFFFF", paper_bgcolor="#FFFFFF",
                      font=dict(color="#172B43"), title_font=dict(color="#14243A", size=18),
                      yaxis_title="Hours", xaxis_title="", margin=dict(l=10,r=10,t=60,b=10))
    st.plotly_chart(fig, use_container_width=True)
    st.warning("An overall surplus of 116 hours does not mean the pilot has all the specialist capabilities it needs.")
    st.caption("Planning figures are from the team's current working model. Validate against the final case exhibits and calculation sheet.")

else:
    st.markdown("## 02 / The Output")
    st.write("**Recommended output:** a capability-led HR action plan that protects existing services, improves decision speed and fills validated specialist gaps without relying on permanent hires that cannot arrive within the four-week pilot.")
    st.markdown("### The proposed solution")
    x,y,z = st.columns(3)
    with x:
        st.markdown('<div class="panel"><h3>01 · Redesign work</h3><p>Validate duplicate work, retain essential service tasks and redeploy suitable internal capacity.</p></div>', unsafe_allow_html=True)
    with y:
        st.markdown('<div class="panel"><h3>02 · Fill skill gaps</h3><p>Develop internal talent first; use temporary specialists only for confirmed residual gaps.</p></div>', unsafe_allow_html=True)
    with z:
        st.markdown('<div class="panel"><h3>03 · Clarify decisions</h3><p>Delegate low-risk operational choices locally, with clear escalation for high-risk or cross-functional decisions.</p></div>', unsafe_allow_html=True)
    st.markdown("### Decision metrics")
    a,b,c = st.columns(3)
    a.metric("Baseline net balance", "+116 hours")
    b.metric("Conditional vendor option", "₹3.76 lakh")
    c.metric("Four-week budget cap", "₹6.00 lakh")
    st.markdown("### Downside scenario")
    d,e = st.columns(2)
    d.metric("Demand if 240 hours remain", "2,108 hours")
    e.metric("Downside vendor estimate", "₹6.40 lakh", delta="₹0.40 lakh above cap", delta_color="inverse")
    st.error("Decision gate: do not proceed on the baseline until duplicate-work removal, role-level capacity, vendor quote and service impact are validated. If the assumption fails, revise scope, timeline or budget.")
    st.markdown("### Final recommendation")
    st.success("Proceed conditionally: protect existing services, validate workload reduction, redeploy and train where feasible, source approved temporary specialist support for confirmed gaps, and apply selective decentralisation with clear escalation.")
    st.caption("The vendor option is a proposal, not an approved purchase. Replace assumptions with verified team evidence before submission.")

st.sidebar.divider()
st.sidebar.caption("Problem • evidence • output")
