import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Meridian Forward | Problem → Output", page_icon="🎯", layout="wide")

st.markdown("""
<style>
.stApp { background:#F4F7FB; }
.block-container { max-width:1200px; padding-top:2rem; padding-bottom:3rem; }
.hero { background:linear-gradient(115deg,#14243A,#244A70,#3567D4); color:white; padding:2.3rem; border-radius:22px; margin-bottom:1.2rem; }
.hero h1 {color:white; font-size:2.6rem; margin:.3rem 0;}
.hero p {color:#E7EEF8; font-size:1.08rem;}
.tag {color:#B9D1FF; font-size:.8rem; font-weight:800; letter-spacing:.12em;}
.panel {background:white; padding:1.2rem; border-radius:16px; border:1px solid #E2E8F0; min-height:155px;}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("## Meridian Forward")
st.sidebar.caption("HCM AS2 • Team 02")
page = st.sidebar.radio("Portfolio", ["Problem", "Output"])

st.markdown('<div class="hero"><div class="tag">HUMAN CAPITAL MANAGEMENT • AS2</div><h1>Meridian Forward</h1><p>From workforce capability problem to a practical HR solution</p></div>', unsafe_allow_html=True)

if page == "Problem":
    st.markdown("## 01 / The Problem")
    st.write("Meridian Forward wants to move towards shorter product cycles and more original design while maintaining reliable existing services. However, slow decision-making, coordination challenges and shortages in specialist capabilities may prevent the organisation from delivering the proposed four-week pilot safely.")
    c1,c2,c3 = st.columns(3)
    c1.metric("Available capacity", "1,984 hours")
    c2.metric("Pilot demand", "1,868 hours")
    c3.metric("Role-specific gaps", "216 hours")
    st.markdown("### What is going wrong?")
    a,b,c = st.columns(3)
    with a:
        st.markdown('<div class="panel"><h3>⚙️ Capability mismatch</h3><p>Total capacity looks sufficient, but the right specialist skills are not available in the right roles.</p></div>', unsafe_allow_html=True)
    with b:
        st.markdown('<div class="panel"><h3>🔁 Workload uncertainty</h3><p>The baseline relies on removing 60 duplicate customer packs, equivalent to 240 hours, without harming service.</p></div>', unsafe_allow_html=True)
    with c:
        st.markdown('<div class="panel"><h3>⏱️ Decision delays</h3><p>Unclear decision rights and escalation routes can slow delivery while existing service commitments continue.</p></div>', unsafe_allow_html=True)
    st.markdown("### Evidence: specialist capability gaps")
    gaps = pd.DataFrame({"Capability":["Data preparation","Quality assurance","Legacy expertise"],"Shortage (hours)":[80,72,64]})
    fig = px.bar(gaps, x="Capability", y="Shortage (hours)", text="Shortage (hours)", title="216 hours of role-specific shortages")
    fig.update_layout(showlegend=False, plot_bgcolor="white", paper_bgcolor="white", yaxis_title="Hours", xaxis_title="")
    st.plotly_chart(fig, use_container_width=True)
    st.warning("Key risk: an overall surplus of 116 hours does not mean the pilot has all the specialist capabilities it needs.")
    st.caption("Planning figures are from the team's current working model. Validate against the final case exhibits and calculation sheet.")

else:
    st.markdown("## 02 / The Output")
    st.write("**Recommended output:** a capability-led HR action plan that protects existing services, improves decision speed and fills validated specialist gaps without committing to permanent hires that cannot arrive within the four-week pilot.")
    st.markdown("### Proposed solution")
    x,y,z = st.columns(3)
    with x:
        st.markdown('<div class="panel"><h3>1. Redesign work</h3><p>Validate duplicate work, retain essential service tasks and redeploy suitable internal capacity.</p></div>', unsafe_allow_html=True)
    with y:
        st.markdown('<div class="panel"><h3>2. Fill skill gaps</h3><p>Use internal development first; source temporary specialists only for confirmed residual gaps.</p></div>', unsafe_allow_html=True)
    with z:
        st.markdown('<div class="panel"><h3>3. Clarify decisions</h3><p>Delegate low-risk operational choices locally, with clear escalation for high-risk or cross-functional decisions.</p></div>', unsafe_allow_html=True)
    st.markdown("### Expected decision metrics")
    a,b,c = st.columns(3)
    a.metric("Baseline net balance", "+116 hours")
    b.metric("Conditional vendor option", "₹3.76 lakh")
    c.metric("Four-week budget cap", "₹6.00 lakh")
    st.markdown("### What if the assumption fails?")
    d,e = st.columns(2)
    d.metric("Demand if 240 duplicate-work hours remain", "2,108 hours")
    e.metric("Downside vendor estimate", "₹6.40 lakh", delta="₹0.40 lakh above cap", delta_color="inverse")
    st.error("Decision gate: do not proceed on the baseline case until the duplicate-work assumption, role-level capacity, vendor quote and service impact are validated. If the assumption fails, revise scope, timeline or budget.")
    st.markdown("### Final output in one line")
    st.success("Proceed conditionally: protect existing services, validate the workload reduction, redeploy and train where feasible, use approved temporary specialist support for confirmed gaps, and apply selective decentralisation with clear escalation.")
    st.caption("The vendor option is a proposal, not an approved purchase. Replace assumptions with verified team evidence before submission.")

st.sidebar.divider()
st.sidebar.caption("Keep the portfolio focused on the problem and the output.")
