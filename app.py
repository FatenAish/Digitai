import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Digit ai | AI-Powered Execution Systems",
    page_icon="◆",
    layout="wide"
)

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(168, 85, 247, 0.30), transparent 35%),
        radial-gradient(circle at top right, rgba(147, 51, 234, 0.25), transparent 38%),
        linear-gradient(135deg, #070014 0%, #130026 50%, #070014 100%);
    color: #ffffff;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 18px 0 35px 0;
}

.logo-wrap {
    display: flex;
    align-items: center;
    gap: 12px;
}

.logo-mark {
    width: 42px;
    height: 42px;
    border-radius: 14px;
    background: linear-gradient(135deg, #c084fc, #7c3aed);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 35px rgba(168, 85, 247, 0.65);
    font-size: 21px;
    font-weight: 900;
}

.logo-text {
    font-size: 26px;
    font-weight: 850;
    letter-spacing: -0.5px;
}

.logo-text span {
    color: #c084fc;
}

.nav-links {
    color: #d8c8ea;
    font-size: 14px;
}

.hero {
    text-align: center;
    padding: 70px 20px 45px 20px;
}

.badge {
    display: inline-block;
    padding: 10px 18px;
    border-radius: 999px;
    border: 1px solid rgba(216, 180, 254, 0.42);
    background: rgba(168, 85, 247, 0.14);
    color: #f3e8ff;
    font-size: 14px;
    margin-bottom: 24px;
}

.hero-title {
    font-size: 72px;
    line-height: 1.05;
    font-weight: 900;
    letter-spacing: -3px;
    max-width: 980px;
    margin: auto;
}

.hero-title span {
    background: linear-gradient(90deg, #f3e8ff, #c084fc, #a855f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    max-width: 800px;
    margin: 24px auto 0 auto;
    color: #dcccef;
    font-size: 21px;
    line-height: 1.7;
}

.section {
    margin-top: 75px;
}

.section-title {
    text-align: center;
    font-size: 42px;
    font-weight: 850;
    letter-spacing: -1.4px;
    margin-bottom: 14px;
}

.section-subtitle {
    text-align: center;
    max-width: 760px;
    margin: 0 auto 42px auto;
    color: #cbb9df;
    font-size: 18px;
    line-height: 1.7;
}

.card {
    background: rgba(255, 255, 255, 0.065);
    border: 1px solid rgba(216, 180, 254, 0.18);
    border-radius: 28px;
    padding: 30px;
    min-height: 270px;
    box-shadow: 0 24px 70px rgba(0,0,0,0.28);
    backdrop-filter: blur(14px);
    transition: all 0.25s ease;
}

.card:hover {
    transform: translateY(-7px);
    border-color: rgba(216, 180, 254, 0.55);
    box-shadow: 0 28px 80px rgba(168, 85, 247, 0.20);
}

.card-icon {
    width: 54px;
    height: 54px;
    border-radius: 18px;
    background: rgba(168, 85, 247, 0.18);
    border: 1px solid rgba(216, 180, 254, 0.28);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #f3e8ff;
    font-size: 20px;
    font-weight: 900;
    margin-bottom: 22px;
}

.card-title {
    color: #ffffff;
    font-size: 23px;
    font-weight: 800;
    margin-bottom: 13px;
}

.card-text {
    color: #d9cae8;
    font-size: 16px;
    line-height: 1.75;
}

.highlight {
    color: #d8b4fe;
    font-weight: 850;
}

.metric-box {
    background: rgba(168, 85, 247, 0.13);
    border: 1px solid rgba(216, 180, 254, 0.25);
    border-radius: 26px;
    padding: 28px;
    text-align: center;
    min-height: 150px;
}

.metric-number {
    font-size: 40px;
    font-weight: 900;
    color: #d8b4fe;
}

.metric-label {
    color: #dcccef;
    font-size: 15px;
    margin-top: 8px;
}

.interactive-box {
    background: rgba(255,255,255,0.065);
    border: 1px solid rgba(216, 180, 254, 0.20);
    border-radius: 30px;
    padding: 34px;
    box-shadow: 0 25px 70px rgba(0,0,0,0.25);
}

.workflow {
    background: linear-gradient(135deg, rgba(168, 85, 247, 0.18), rgba(255,255,255,0.055));
    border: 1px solid rgba(216, 180, 254, 0.28);
    border-radius: 32px;
    padding: 38px;
    text-align: center;
}

.workflow-step {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(216, 180, 254, 0.16);
    border-radius: 20px;
    padding: 18px;
    text-align: center;
    color: #ffffff;
    font-weight: 750;
}

.cta {
    margin-top: 85px;
    background:
        radial-gradient(circle at center, rgba(168, 85, 247, 0.28), transparent 65%),
        linear-gradient(135deg, rgba(124, 58, 237, 0.28), rgba(255,255,255,0.06));
    border: 1px solid rgba(216, 180, 254, 0.32);
    border-radius: 36px;
    padding: 58px 35px;
    text-align: center;
}

.cta-title {
    font-size: 42px;
    font-weight: 900;
    margin-bottom: 15px;
}

.cta-text {
    max-width: 720px;
    margin: auto;
    color: #ddcbed;
    font-size: 18px;
    line-height: 1.7;
}

.stButton > button {
    background: linear-gradient(135deg, #a855f7, #7c3aed);
    color: white;
    border: 0;
    border-radius: 999px;
    padding: 0.85rem 2.1rem;
    font-size: 16px;
    font-weight: 750;
    box-shadow: 0 18px 45px rgba(124, 58, 237, 0.35);
    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 22px 55px rgba(168, 85, 247, 0.45);
    color: white;
}

.stSelectbox label,
.stSlider label,
.stTextInput label,
.stTextArea label,
.stRadio label,
.stMultiSelect label {
    color: #ffffff !important;
}

.stTextInput input,
.stTextArea textarea {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(216, 180, 254, 0.24);
    color: white;
    border-radius: 16px;
}

div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.08);
    border-color: rgba(216, 180, 254, 0.24);
    color: white;
    border-radius: 16px;
}

[data-testid="stMetric"] {
    background: rgba(168, 85, 247, 0.12);
    border: 1px solid rgba(216, 180, 254, 0.22);
    padding: 20px;
    border-radius: 22px;
}

hr {
    border: 0.5px solid rgba(255,255,255,0.12);
}

@media only screen and (max-width: 768px) {
    .hero-title {
        font-size: 43px;
        letter-spacing: -1.5px;
    }

    .hero-subtitle {
        font-size: 17px;
    }

    .section-title {
        font-size: 31px;
    }

    .navbar {
        display: block;
        text-align: center;
    }

    .logo-wrap {
        justify-content: center;
        margin-bottom: 12px;
    }
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Data
# -----------------------------
services = {
    "AI Execution Systems": {
        "headline": "Build AI systems that reduce manual work and improve execution.",
        "description": "Best for companies that need workflow automation, reporting automation, QA engines, KPI tracking, and internal AI tools.",
        "outputs": [
            "AI PMO system",
            "QA and validation engine",
            "Automated reporting workflow",
            "KPI tracking dashboard",
            "Workflow automation system"
        ],
        "best_for": "Project teams, operations teams, consultancies, agencies, and companies managing repeated reporting or execution workflows."
    },
    "Content Marketing": {
        "headline": "Turn your brand message into clear, strategic content.",
        "description": "Best for businesses that need SEO content, landing pages, website copy, blogs, campaign messaging, and editorial planning.",
        "outputs": [
            "Website copy",
            "SEO blogs",
            "Landing pages",
            "Content calendars",
            "Editorial guidelines"
        ],
        "best_for": "Brands that want better visibility, clearer messaging, and content that supports business growth."
    },
    "Social Media Strategy": {
        "headline": "Build a stronger and more consistent social media presence.",
        "description": "Best for brands that need platform-specific content, campaign ideas, captions, content calendars, and performance direction.",
        "outputs": [
            "Social media strategy",
            "Monthly content calendar",
            "Campaign concepts",
            "Captions and post ideas",
            "Performance review"
        ],
        "best_for": "Brands that want to improve consistency, engagement, and storytelling across social platforms."
    }
}

use_cases = {
    "PMO Automation": "Automate project updates, task tracking, status reports, and follow-up workflows.",
    "KPI Tracking": "Convert scattered data into simple performance indicators and dashboard-ready insights.",
    "Report Generation": "Generate structured reports faster with consistent formatting, language, and quality.",
    "Compliance Validation": "Check outputs against internal standards, rules, requirements, or brand guidelines.",
    "Content QA": "Review content for accuracy, tone, structure, SEO, and consistency before publishing.",
    "Workflow Automation": "Reduce repetitive operational tasks through AI-supported processes."
}


# -----------------------------
# Navbar
# -----------------------------
st.markdown("""
<div class="navbar">
    <div class="logo-wrap">
        <div class="logo-mark">◆</div>
        <div class="logo-text">Digit <span>ai</span></div>
    </div>
    <div class="nav-links">AI Systems · Content Marketing · Social Media</div>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# Hero
# -----------------------------
st.markdown("""
<div class="hero">
    <div class="badge">AI-Powered Execution Systems</div>
    <div class="hero-title">
        We turn strategy into <span>faster, smarter execution.</span>
    </div>
    <div class="hero-subtitle">
        Digit ai helps businesses reduce manual work, automate workflows, improve content quality, 
        and build stronger digital execution across AI, content marketing, and social media.
    </div>
</div>
""", unsafe_allow_html=True)

hero_col1, hero_col2, hero_col3 = st.columns([1, 1, 1])
with hero_col2:
    if st.button("Explore Services"):
        st.session_state["explore_clicked"] = True

if st.session_state.get("explore_clicked"):
    st.success("Great. Start by choosing a service below.")


# -----------------------------
# Interactive Service Selector
# -----------------------------
st.markdown("""
<div class="section">
    <div class="section-title">Choose What You Need</div>
    <div class="section-subtitle">
        Select a service and see how Digit ai can support your business.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="interactive-box">', unsafe_allow_html=True)

selected_service = st.selectbox(
    "Which service are you most interested in?",
    list(services.keys())
)

service = services[selected_service]

st.markdown(f"""
<div class="card-title">{service["headline"]}</div>
<div class="card-text">{service["description"]}</div>
<br>
<div class="highlight">Best for:</div>
<div class="card-text">{service["best_for"]}</div>
""", unsafe_allow_html=True)

st.write("")

output_cols = st.columns(len(service["outputs"]))

for col, output in zip(output_cols, service["outputs"]):
    with col:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-label">{output}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# Tabs
# -----------------------------
st.markdown("""
<div class="section">
    <div class="section-title">Explore Digit ai Services</div>
    <div class="section-subtitle">
        Use the tabs below to explore each service area in more detail.
    </div>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["AI Systems", "Content Marketing", "Social Media"])

with tab1:
    st.markdown("### AI Systems")
    st.write(
        "We build AI-powered execution systems that help teams automate work, validate outputs, "
        "generate reports, track KPIs, and improve project delivery."
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Manual Work Reduction", "60–80%")
    with c2:
        st.metric("Pilot Duration", "2–3 Weeks")
    with c3:
        st.metric("Core Focus", "Execution")

    with st.expander("What AI systems can Digit ai build?"):
        st.write("""
        - AI PMO systems  
        - QA and validation engines  
        - Automated reporting systems  
        - Workflow automation tools  
        - KPI tracking dashboards  
        - Internal AI assistants  
        """)

    with st.expander("Best AI project to start with"):
        st.write("""
        Start with one real workflow that is repetitive, manual, and easy to measure. 
        For example: weekly reporting, project status tracking, compliance checking, or content QA.
        """)

with tab2:
    st.markdown("### Content Marketing")
    st.write(
        "We help brands create content that is clear, searchable, useful, and aligned with their business goals."
    )

    with st.expander("Content services"):
        st.write("""
        - Website copy  
        - SEO blogs  
        - Landing pages  
        - Content calendars  
        - Campaign content  
        - Editorial review and QA  
        """)

    with st.expander("What makes the content stronger?"):
        st.write("""
        The content should be structured around search intent, brand positioning, user needs, 
        and clear calls to action. The goal is not just to publish more content, but to publish content that performs.
        """)

with tab3:
    st.markdown("### Social Media")
    st.write(
        "We help brands plan, structure, and improve their social media presence with consistent messaging and better execution."
    )

    with st.expander("Social media services"):
        st.write("""
        - Social media strategy  
        - Monthly content calendars  
        - Caption writing  
        - Campaign ideas  
        - Platform-specific content direction  
        - Performance review  
        """)

    with st.expander("Best social media starting point"):
        st.write("""
        Start by defining your content pillars, target audience, tone of voice, and monthly campaign priorities. 
        Then turn that into a practical content calendar.
        """)


# -----------------------------
# Interactive Use Cases
# -----------------------------
st.markdown("""
<div class="section">
    <div class="section-title">AI Use Case Finder</div>
    <div class="section-subtitle">
        Choose a use case and see how Digit ai can apply it inside a real business workflow.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="interactive-box">', unsafe_allow_html=True)

selected_use_case = st.radio(
    "Select a use case:",
    list(use_cases.keys()),
    horizontal=True
)

st.markdown(f"""
<div class="card-title">{selected_use_case}</div>
<div class="card-text">{use_cases[selected_use_case]}</div>
""", unsafe_allow_html=True)

if selected_use_case == "PMO Automation":
    st.info("Example: Turn project updates, owner comments, and task progress into an automated weekly status report.")
elif selected_use_case == "KPI Tracking":
    st.info("Example: Convert weekly project data into dashboard-ready KPIs for faster decision-making.")
elif selected_use_case == "Report Generation":
    st.info("Example: Generate clean reports from raw notes, sheets, meeting updates, or project inputs.")
elif selected_use_case == "Compliance Validation":
    st.info("Example: Check outputs against required rules, client standards, or internal guidelines.")
elif selected_use_case == "Content QA":
    st.info("Example: Review content for tone, missing information, structure, SEO, and consistency.")
elif selected_use_case == "Workflow Automation":
    st.info("Example: Automate repetitive steps between input, review, output, and reporting.")

st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# Work Reduction Calculator
# -----------------------------
st.markdown("""
<div class="section">
    <div class="section-title">Manual Work Reduction Calculator</div>
    <div class="section-subtitle">
        Estimate how many hours your team could save by automating repetitive work.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="interactive-box">', unsafe_allow_html=True)

calc_col1, calc_col2, calc_col3 = st.columns(3)

with calc_col1:
    weekly_hours = st.slider("Current manual hours per week", 1, 100, 25)

with calc_col2:
    reduction = st.slider("Expected automation reduction", 10, 80, 60)

with calc_col3:
    team_members = st.slider("Number of team members affected", 1, 30, 3)

weekly_saved = weekly_hours * (reduction / 100) * team_members
monthly_saved = weekly_saved * 4
yearly_saved = weekly_saved * 52

m1, m2, m3 = st.columns(3)

with m1:
    st.metric("Weekly Hours Saved", f"{weekly_saved:.0f}")
with m2:
    st.metric("Monthly Hours Saved", f"{monthly_saved:.0f}")
with m3:
    st.metric("Yearly Hours Saved", f"{yearly_saved:.0f}")

st.caption("This is an estimate based on the selected manual workload and expected automation reduction.")

st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# Workflow
# -----------------------------
st.markdown("""
<div class="section">
    <div class="section-title">How Our AI Workflow Works</div>
    <div class="section-subtitle">
        A clear execution flow from raw input to reviewed output and dashboard-ready results.
    </div>
</div>
""", unsafe_allow_html=True)

w1, w2, w3, w4, w5 = st.columns(5)

workflow_steps = [
    ("Input", "Documents, sheets, notes, project data, or content requests."),
    ("AI Processing", "AI structures, analyzes, drafts, or automates the required output."),
    ("QA", "Outputs are validated against rules, standards, and quality checks."),
    ("Output", "The final result is formatted, reviewed, and ready to use."),
    ("Dashboard", "Results can be tracked through reports, metrics, or dashboards.")
]

for col, step in zip([w1, w2, w3, w4, w5], workflow_steps):
    with col:
        st.markdown(f"""
        <div class="workflow-step">
            {step[0]}
        </div>
        """, unsafe_allow_html=True)
        st.caption(step[1])


# -----------------------------
# Project Fit Assessment
# -----------------------------
st.markdown("""
<div class="section">
    <div class="section-title">Is Your Project a Good Fit?</div>
    <div class="section-subtitle">
        Answer a few questions and get a quick recommendation.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="interactive-box">', unsafe_allow_html=True)

q1 = st.checkbox("The workflow is repetitive or manual.")
q2 = st.checkbox("The output needs consistent formatting or quality.")
q3 = st.checkbox("The team spends time preparing reports or updates.")
q4 = st.checkbox("There are rules, guidelines, or standards that need to be checked.")
q5 = st.checkbox("The work can be tested on one real project first.")

score = sum([q1, q2, q3, q4, q5])

st.progress(score / 5)

if score == 0:
    st.warning("Your project may need more definition before starting.")
elif score <= 2:
    st.info("This could be a fit, but the workflow should be clarified first.")
elif score <= 4:
    st.success("This looks like a good fit for a Digit ai pilot.")
else:
    st.success("Strong fit. This is a great candidate for a 2–3 week Proof of Concept.")

st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# Engagement Model
# -----------------------------
st.markdown("""
<div class="section">
    <div class="section-title">Engagement Model</div>
    <div class="section-subtitle">
        Choose the model that best fits how you want to work with Digit ai.
    </div>
</div>
""", unsafe_allow_html=True)

model = st.selectbox(
    "Choose an engagement model:",
    ["Project-Based", "Embedded Partner", "White-Label"]
)

if model == "Project-Based":
    st.markdown("""
    <div class="interactive-box">
        <div class="card-title">Project-Based</div>
        <div class="card-text">
            Best for one clear AI system, content project, campaign, or workflow automation need.
            This model works well when the scope and output are already defined.
        </div>
    </div>
    """, unsafe_allow_html=True)

elif model == "Embedded Partner":
    st.markdown("""
    <div class="interactive-box">
        <div class="card-title">Embedded Partner</div>
        <div class="card-text">
            Best for companies that need ongoing support across AI, content, marketing, and digital execution.
            Digit ai works closely with your team as an execution partner.
        </div>
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
    <div class="interactive-box">
        <div class="card-title">White-Label</div>
        <div class="card-text">
            Best for agencies, consultants, or partners that want AI and content execution delivered under their own brand.
        </div>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------
# CTA
# -----------------------------
st.markdown("""
<div class="cta">
    <div class="cta-title">Start with a 2–3 Week Proof of Concept</div>
    <div class="cta-text">
        The best way to test Digit ai is on a real project. We identify one workflow, build a focused AI-powered solution, 
        validate the output, and measure the impact before scaling.
    </div>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# Contact
# -----------------------------
st.markdown("""
<div class="section">
    <div class="section-title">Let’s Build Your Execution Layer</div>
    <div class="section-subtitle">
        Tell us what you want to improve, and Digit ai will help shape the right starting point.
    </div>
</div>
""", unsafe_allow_html=True)

contact_left, contact_right = st.columns([1, 1])

with contact_left:
    st.markdown("""
    <div class="interactive-box">
        <div class="card-title">Contact Digit ai</div>
        <div class="card-text">
            Replace these details with your real contact information.
            <br><br>
            <span class="highlight">Email:</span> hello@digitai.com<br>
            <span class="highlight">Services:</span> AI systems, content marketing, and social media<br>
            <span class="highlight">Pilot:</span> 2–3 week Proof of Concept
        </div>
    </div>
    """, unsafe_allow_html=True)

with contact_right:
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        selected_contact_service = st.selectbox(
            "Service needed",
            ["AI Execution Systems", "Content Marketing", "Social Media Strategy", "Not sure yet"]
        )
        message = st.text_area("Tell us about your project")
        submitted = st.form_submit_button("Send Message")

        if submitted:
            st.success(f"Thank you, {name if name else 'there'}. Your request for {selected_contact_service} has been received.")


# -----------------------------
# Footer
# -----------------------------
st.markdown("""
<br><br>
<hr>
<p style="text-align:center; color:#a99abc;">
© 2026 Digit ai. AI-Powered Execution Systems.
</p>
""", unsafe_allow_html=True)
