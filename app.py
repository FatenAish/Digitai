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
/* Hide Streamlit default UI */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(168, 85, 247, 0.28), transparent 35%),
        radial-gradient(circle at top right, rgba(124, 58, 237, 0.22), transparent 35%),
        linear-gradient(135deg, #070014 0%, #120024 45%, #070014 100%);
    color: #ffffff;
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Navbar */
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
    width: 38px;
    height: 38px;
    border-radius: 12px;
    background: linear-gradient(135deg, #a855f7, #7c3aed);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 30px rgba(168, 85, 247, 0.55);
    font-size: 20px;
    font-weight: 800;
}

.logo-text {
    font-size: 24px;
    font-weight: 800;
    letter-spacing: -0.5px;
}

.logo-text span {
    color: #c084fc;
}

.nav-links {
    color: #c9b8dd;
    font-size: 14px;
}

/* Hero */
.hero {
    text-align: center;
    padding: 70px 20px 45px 20px;
}

.badge {
    display: inline-block;
    padding: 10px 18px;
    border-radius: 999px;
    border: 1px solid rgba(192, 132, 252, 0.4);
    background: rgba(168, 85, 247, 0.13);
    color: #e9d5ff;
    font-size: 14px;
    margin-bottom: 24px;
}

.hero-title {
    font-size: 72px;
    line-height: 1.05;
    font-weight: 850;
    letter-spacing: -3px;
    max-width: 980px;
    margin: auto;
}

.hero-title span {
    background: linear-gradient(90deg, #d8b4fe, #a855f7, #f0abfc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    max-width: 780px;
    margin: 24px auto 0 auto;
    color: #d8c8ea;
    font-size: 21px;
    line-height: 1.7;
}

.hero-actions {
    margin-top: 34px;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #a855f7, #7c3aed);
    color: white;
    border: 0;
    border-radius: 999px;
    padding: 0.85rem 2.1rem;
    font-size: 16px;
    font-weight: 700;
    box-shadow: 0 18px 45px rgba(124, 58, 237, 0.35);
    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 22px 55px rgba(168, 85, 247, 0.45);
    color: white;
}

/* Section */
.section {
    margin-top: 75px;
}

.section-title {
    text-align: center;
    font-size: 42px;
    font-weight: 820;
    letter-spacing: -1.5px;
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

/* Cards */
.card {
    background: rgba(255, 255, 255, 0.065);
    border: 1px solid rgba(216, 180, 254, 0.18);
    border-radius: 28px;
    padding: 32px;
    min-height: 285px;
    box-shadow: 0 24px 70px rgba(0,0,0,0.28);
    backdrop-filter: blur(14px);
    transition: all 0.25s ease;
}

.card:hover {
    transform: translateY(-7px);
    border-color: rgba(216, 180, 254, 0.55);
    box-shadow: 0 28px 80px rgba(168, 85, 247, 0.18);
}

.card-icon {
    width: 52px;
    height: 52px;
    border-radius: 18px;
    background: rgba(168, 85, 247, 0.18);
    border: 1px solid rgba(216, 180, 254, 0.28);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #e9d5ff;
    font-size: 24px;
    font-weight: 800;
    margin-bottom: 22px;
}

.card-title {
    color: #ffffff;
    font-size: 23px;
    font-weight: 780;
    margin-bottom: 13px;
}

.card-text {
    color: #d6c7e7;
    font-size: 16px;
    line-height: 1.75;
}

/* Problem / opportunity */
.split-box {
    background: rgba(255,255,255,0.055);
    border: 1px solid rgba(216, 180, 254, 0.16);
    border-radius: 30px;
    padding: 36px;
    min-height: 310px;
}

.problem-item {
    color: #d8c8ea;
    font-size: 17px;
    margin-bottom: 15px;
    line-height: 1.5;
}

.highlight {
    color: #d8b4fe;
    font-weight: 800;
}

/* Workflow */
.workflow {
    background: linear-gradient(135deg, rgba(168, 85, 247, 0.16), rgba(255,255,255,0.045));
    border: 1px solid rgba(216, 180, 254, 0.24);
    border-radius: 32px;
    padding: 38px;
    text-align: center;
}

.workflow-line {
    color: #ffffff;
    font-size: 25px;
    font-weight: 750;
    line-height: 1.8;
}

.workflow-line span {
    color: #c084fc;
}

/* Stats */
.stat-card {
    background: rgba(168, 85, 247, 0.12);
    border: 1px solid rgba(216, 180, 254, 0.24);
    border-radius: 28px;
    padding: 35px 25px;
    text-align: center;
    min-height: 170px;
}

.stat-number {
    font-size: 44px;
    font-weight: 850;
    color: #d8b4fe;
    margin-bottom: 8px;
}

.stat-label {
    color: #d8c8ea;
    font-size: 16px;
    line-height: 1.5;
}

/* CTA */
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
    font-weight: 850;
    margin-bottom: 15px;
}

.cta-text {
    max-width: 720px;
    margin: auto;
    color: #ddcbed;
    font-size: 18px;
    line-height: 1.7;
}

/* Contact form */
.stTextInput input,
.stTextArea textarea {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(216, 180, 254, 0.24);
    color: white;
    border-radius: 16px;
}

.stTextInput label,
.stTextArea label {
    color: #ffffff !important;
}

/* Responsive */
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

    .workflow-line {
        font-size: 18px;
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
        We help businesses execute faster with <span>AI, content, and digital strategy.</span>
    </div>
    <div class="hero-subtitle">
        Digit ai builds practical AI systems and marketing solutions that reduce manual work, 
        improve consistency, and turn strategy into measurable execution.
    </div>
</div>
""", unsafe_allow_html=True)

btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])
with btn_col2:
    st.button("Book a Consultation")


# -----------------------------
# Problem / Opportunity
# -----------------------------
st.markdown("""
<div class="section">
    <div class="section-title">The Problem We Solve</div>
    <div class="section-subtitle">
        Many businesses have strong strategies, but execution becomes slow, manual, and inconsistent.
    </div>
</div>
""", unsafe_allow_html=True)

left, right = st.columns(2)

with left:
    st.markdown("""
    <div class="split-box">
        <div class="card-title">Common Business Challenges</div>
        <div class="problem-item">◆ Strategies fail because execution is not structured.</div>
        <div class="problem-item">◆ Reporting takes too much manual effort.</div>
        <div class="problem-item">◆ Decisions become slow because data is scattered.</div>
        <div class="problem-item">◆ Outputs are inconsistent across teams, projects, and campaigns.</div>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div class="split-box">
        <div class="card-title">Our Opportunity</div>
        <div class="card-text">
            Digit ai adds an AI-powered execution layer inside your projects, workflows, 
            and marketing operations.
            <br><br>
            This helps teams move from manual coordination to faster, smarter, and more consistent delivery.
            <br><br>
            <span class="highlight">The goal is simple: less manual work, better execution, and clearer results.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------
# Services
# -----------------------------
st.markdown("""
<div class="section">
    <div class="section-title">Our Services</div>
    <div class="section-subtitle">
        We combine AI implementation with content and social media expertise to support business growth from planning to execution.
    </div>
</div>
""", unsafe_allow_html=True)

s1, s2, s3 = st.columns(3)

with s1:
    st.markdown("""
    <div class="card">
        <div class="card-icon">AI</div>
        <div class="card-title">AI Execution Systems</div>
        <div class="card-text">
            We design AI-powered systems that help teams automate workflows, validate outputs, 
            generate reports, track KPIs, and improve project execution.
            <br><br>
            This includes AI PMO systems, QA engines, workflow automation, and dashboard-ready outputs.
        </div>
    </div>
    """, unsafe_allow_html=True)

with s2:
    st.markdown("""
    <div class="card">
        <div class="card-icon">CM</div>
        <div class="card-title">Content Marketing</div>
        <div class="card-text">
            We create strategic content that improves brand visibility, supports SEO, 
            and communicates your message clearly.
            <br><br>
            This includes website copy, blogs, landing pages, campaign content, content planning, 
            and editorial quality checks.
        </div>
    </div>
    """, unsafe_allow_html=True)

with s3:
    st.markdown("""
    <div class="card">
        <div class="card-icon">SM</div>
        <div class="card-title">Social Media Strategy</div>
        <div class="card-text">
            We help brands build a stronger social media presence through clear planning, 
            creative content ideas, and consistent execution.
            <br><br>
            This includes content calendars, captions, campaign concepts, performance reviews, 
            and platform-specific direction.
        </div>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------
# AI Use Cases
# -----------------------------
st.markdown("""
<div class="section">
    <div class="section-title">AI Use Cases</div>
    <div class="section-subtitle">
        Our AI systems are built around practical business needs, not abstract technology.
    </div>
</div>
""", unsafe_allow_html=True)

u1, u2, u3, u4 = st.columns(4)

with u1:
    st.markdown("""
    <div class="card">
        <div class="card-icon">01</div>
        <div class="card-title">PMO Automation</div>
        <div class="card-text">
            Automate project tracking, task follow-ups, status updates, and delivery documentation.
        </div>
    </div>
    """, unsafe_allow_html=True)

with u2:
    st.markdown("""
    <div class="card">
        <div class="card-icon">02</div>
        <div class="card-title">KPI Tracking</div>
        <div class="card-text">
            Turn scattered project data into clear indicators that help teams make faster decisions.
        </div>
    </div>
    """, unsafe_allow_html=True)

with u3:
    st.markdown("""
    <div class="card">
        <div class="card-icon">03</div>
        <div class="card-title">Report Generation</div>
        <div class="card-text">
            Generate structured reports faster with consistent formatting, language, and insights.
        </div>
    </div>
    """, unsafe_allow_html=True)

with u4:
    st.markdown("""
    <div class="card">
        <div class="card-icon">04</div>
        <div class="card-title">Compliance Validation</div>
        <div class="card-text">
            Review outputs against rules, guidelines, requirements, or internal quality standards.
        </div>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------
# Workflow
# -----------------------------
st.markdown("""
<div class="section">
    <div class="section-title">How It Works</div>
    <div class="section-subtitle">
        A simple execution workflow that converts inputs into reviewed, structured, and usable outputs.
    </div>
</div>

<div class="workflow">
    <div class="workflow-line">
        Input <span>→</span> AI Processing <span>→</span> QA <span>→</span> Output <span>→</span> Dashboard
    </div>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# Impact
# -----------------------------
st.markdown("""
<div class="section">
    <div class="section-title">Expected Impact</div>
    <div class="section-subtitle">
        Digit ai is built to help teams reduce repetitive work and improve execution quality.
    </div>
</div>
""", unsafe_allow_html=True)

i1, i2, i3 = st.columns(3)

with i1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">60–80%</div>
        <div class="stat-label">Potential reduction in manual work</div>
    </div>
    """, unsafe_allow_html=True)

with i2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">Faster</div>
        <div class="stat-label">Execution, reporting, and decision-making</div>
    </div>
    """, unsafe_allow_html=True)

with i3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">Higher</div>
        <div class="stat-label">Consistency across content, reports, and workflows</div>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------
# Engagement Model
# -----------------------------
st.markdown("""
<div class="section">
    <div class="section-title">Engagement Model</div>
    <div class="section-subtitle">
        Flexible ways to work with Digit ai depending on your business needs.
    </div>
</div>
""", unsafe_allow_html=True)

e1, e2, e3 = st.columns(3)

with e1:
    st.markdown("""
    <div class="card">
        <div class="card-icon">P</div>
        <div class="card-title">Project-Based</div>
        <div class="card-text">
            Ideal for companies that need one specific AI system, campaign, content project, or automation workflow.
        </div>
    </div>
    """, unsafe_allow_html=True)

with e2:
    st.markdown("""
    <div class="card">
        <div class="card-icon">E</div>
        <div class="card-title">Embedded Partner</div>
        <div class="card-text">
            We work closely with your team as an execution partner across AI, content, and digital operations.
        </div>
    </div>
    """, unsafe_allow_html=True)

with e3:
    st.markdown("""
    <div class="card">
        <div class="card-icon">W</div>
        <div class="card-title">White-Label</div>
        <div class="card-text">
            We support agencies, consultants, and partners with AI and content execution under their own brand.
        </div>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------
# Pilot CTA
# -----------------------------
st.markdown("""
<div class="cta">
    <div class="cta-title">Start with a 2–3 Week Proof of Concept</div>
    <div class="cta-text">
        The best way to test Digit ai is on a real project. We identify one workflow, build a focused AI-powered solution, 
        validate the output, and show the impact before scaling.
    </div>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# Contact
# -----------------------------
st.markdown("""
<div class="section">
    <div class="section-title">Let’s Build Your AI Execution Layer</div>
    <div class="section-subtitle">
        Tell us what you want to improve: reporting, content, social media, workflow automation, or project execution.
    </div>
</div>
""", unsafe_allow_html=True)

contact_left, contact_right = st.columns([1, 1])

with contact_left:
    st.markdown("""
    <div class="split-box">
        <div class="card-title">Contact Digit ai</div>
        <div class="card-text">
            Replace the details below with your real email, phone number, or booking link.
            <br><br>
            <span class="highlight">Email:</span> hello@digitai.com<br>
            <span class="highlight">Location:</span> UAE / GCC<br>
            <span class="highlight">Services:</span> AI systems, content marketing, and social media
        </div>
    </div>
    """, unsafe_allow_html=True)

with contact_right:
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        service = st.text_input("What service are you interested in?")
        message = st.text_area("Tell us about your project")
        submitted = st.form_submit_button("Send Message")

        if submitted:
            st.success("Thank you. Your message has been received.")


# -----------------------------
# Footer
# -----------------------------
st.markdown("""
<br><br>
<hr style="border: 0.5px solid rgba(255,255,255,0.12);">
<p style="text-align:center; color:#a99abc;">
© 2026 Digit ai. AI-Powered Execution Systems.
</p>
""", unsafe_allow_html=True)
