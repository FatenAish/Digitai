import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Digit ai | Intelligence Platform",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
/* Main background */
.stApp {
    background: linear-gradient(135deg, #030303 0%, #080f10 45%, #061d1b 100%);
    color: white;
}

/* Hide Streamlit default elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* General spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 1200px;
}

/* Hero section */
.hero {
    text-align: center;
    padding: 70px 20px 50px 20px;
}

.hero-logo {
    display: flex;
    justify-content: center;
    margin-bottom: 30px;
}

.hero-title {
    font-size: 64px;
    font-weight: 700;
    margin-bottom: 15px;
    color: #ffffff;
}

.hero-title span {
    color: #00d1c1;
}

.hero-subtitle {
    font-size: 22px;
    color: #b7b7b7;
    max-width: 760px;
    margin: auto;
    line-height: 1.6;
}

.hero-buttons {
    margin-top: 35px;
}

/* Section titles */
.section-title {
    font-size: 38px;
    font-weight: 700;
    text-align: center;
    margin-top: 70px;
    margin-bottom: 15px;
    color: #ffffff;
}

.section-subtitle {
    font-size: 18px;
    color: #b7b7b7;
    text-align: center;
    max-width: 760px;
    margin: 0 auto 45px auto;
    line-height: 1.6;
}

/* Cards */
.service-card {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(0, 209, 193, 0.25);
    border-radius: 24px;
    padding: 32px;
    min-height: 310px;
    transition: all 0.3s ease;
    box-shadow: 0 20px 50px rgba(0,0,0,0.25);
}

.service-card:hover {
    transform: translateY(-8px);
    border-color: #00d1c1;
    box-shadow: 0 25px 70px rgba(0,209,193,0.18);
}

.card-icon {
    font-size: 38px;
    margin-bottom: 18px;
}

.card-title {
    font-size: 24px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 14px;
}

.card-text {
    font-size: 16px;
    color: #c9c9c9;
    line-height: 1.7;
}

/* Why us section */
.why-box {
    background: rgba(0, 209, 193, 0.08);
    border: 1px solid rgba(0, 209, 193, 0.25);
    border-radius: 26px;
    padding: 40px;
    margin-top: 30px;
}

.why-item {
    font-size: 17px;
    color: #d8d8d8;
    margin-bottom: 16px;
}

/* Process cards */
.process-card {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 22px;
    padding: 26px;
    border: 1px solid rgba(255,255,255,0.08);
    min-height: 190px;
}

.step-number {
    color: #00d1c1;
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 8px;
}

.step-title {
    color: white;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 8px;
}

.step-text {
    color: #bdbdbd;
    font-size: 15px;
    line-height: 1.6;
}

/* CTA */
.cta {
    background: linear-gradient(135deg, rgba(0, 209, 193, 0.18), rgba(255,255,255,0.05));
    border: 1px solid rgba(0, 209, 193, 0.35);
    border-radius: 32px;
    padding: 55px 30px;
    text-align: center;
    margin-top: 80px;
}

.cta-title {
    font-size: 38px;
    font-weight: 700;
    color: white;
    margin-bottom: 16px;
}

.cta-text {
    font-size: 18px;
    color: #c9c9c9;
    max-width: 700px;
    margin: auto;
    line-height: 1.6;
}

/* Contact box */
.contact-box {
    background: rgba(255,255,255,0.06);
    border-radius: 22px;
    padding: 25px;
    border: 1px solid rgba(255,255,255,0.1);
}

/* Buttons */
.stButton > button {
    background: #00d1c1;
    color: #000000;
    border: none;
    border-radius: 40px;
    padding: 0.75rem 2rem;
    font-weight: 700;
    font-size: 16px;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    background: #ffffff;
    color: #000000;
    transform: translateY(-2px);
}

/* Inputs */
.stTextInput input, .stTextArea textarea {
    background-color: rgba(255,255,255,0.08);
    color: white;
    border-radius: 14px;
    border: 1px solid rgba(0,209,193,0.25);
}

.stTextInput label, .stTextArea label {
    color: white !important;
}

/* Mobile */
@media only screen and (max-width: 768px) {
    .hero-title {
        font-size: 42px;
    }

    .hero-subtitle {
        font-size: 18px;
    }

    .section-title {
        font-size: 30px;
    }
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Hero Section
# -----------------------------
st.markdown('<div class="hero">', unsafe_allow_html=True)

st.image("Digiti.png", width=520)

st.markdown("""
<div class="hero-title">Digit <span>ai</span></div>
<div class="hero-subtitle">
An intelligence platform helping businesses grow through AI solutions, 
strategic content marketing, and high-performing social media experiences.
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.button("Start Your AI Journey")

st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# Services Section
# -----------------------------
st.markdown("""
<div class="section-title">Our Services</div>
<div class="section-subtitle">
Digit ai combines technology, creativity, and marketing strategy to help brands work smarter, 
communicate better, and grow faster.
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="service-card">
        <div class="card-icon">⚙️</div>
        <div class="card-title">AI Solutions</div>
        <div class="card-text">
            We help companies adopt practical AI tools that improve productivity, automate workflows, 
            support decision-making, and simplify daily operations.
            <br><br>
            Services include AI assistants, internal knowledge search, automation tools, 
            AI-powered dashboards, and custom business solutions.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="service-card">
        <div class="card-icon">✍️</div>
        <div class="card-title">Content Marketing</div>
        <div class="card-text">
            We create content strategies that help brands attract the right audience, improve visibility, 
            and communicate with clarity.
            <br><br>
            Services include SEO content, blog strategy, website copy, landing pages, brand messaging, 
            content calendars, and editorial planning.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="service-card">
        <div class="card-icon">📱</div>
        <div class="card-title">Social Media</div>
        <div class="card-text">
            We build professional social media experiences that strengthen brand presence and increase engagement.
            <br><br>
            Services include social media strategy, post ideas, captions, campaign planning, performance review, 
            and platform-specific content direction.
        </div>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------
# Why Digit ai
# -----------------------------
st.markdown("""
<div class="section-title">Why Choose Digit ai?</div>
<div class="section-subtitle">
We do not just create content or build tools. We connect AI, strategy, and marketing into one clear growth system.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="why-box">
    <div class="why-item">✓ Smart AI solutions tailored to real business needs</div>
    <div class="why-item">✓ Clear content strategies built for visibility, trust, and conversion</div>
    <div class="why-item">✓ Professional social media planning aligned with your brand voice</div>
    <div class="why-item">✓ A balance between automation, creativity, and human quality control</div>
    <div class="why-item">✓ Practical execution, not complicated tech talk</div>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# Process Section
# -----------------------------
st.markdown("""
<div class="section-title">How We Work</div>
<div class="section-subtitle">
A simple, focused process designed to understand your business and deliver solutions that actually work.
</div>
""", unsafe_allow_html=True)

p1, p2, p3, p4 = st.columns(4)

with p1:
    st.markdown("""
    <div class="process-card">
        <div class="step-number">01</div>
        <div class="step-title">Discover</div>
        <div class="step-text">
            We understand your goals, audience, challenges, and current workflow.
        </div>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class="process-card">
        <div class="step-number">02</div>
        <div class="step-title">Plan</div>
        <div class="step-text">
            We create a clear AI, content, or social media strategy based on your needs.
        </div>
    </div>
    """, unsafe_allow_html=True)

with p3:
    st.markdown("""
    <div class="process-card">
        <div class="step-number">03</div>
        <div class="step-title">Build</div>
        <div class="step-text">
            We develop the tools, content, campaigns, or systems required for execution.
        </div>
    </div>
    """, unsafe_allow_html=True)

with p4:
    st.markdown("""
    <div class="process-card">
        <div class="step-number">04</div>
        <div class="step-title">Improve</div>
        <div class="step-text">
            We review performance, improve outputs, and optimize based on results.
        </div>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------
# CTA Section
# -----------------------------
st.markdown("""
<div class="cta">
    <div class="cta-title">Ready to Build Smarter?</div>
    <div class="cta-text">
        Whether you need AI automation, stronger content, or a better social media presence, 
        Digit ai helps you turn ideas into professional digital solutions.
    </div>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# Contact Section
# -----------------------------
st.markdown("""
<div class="section-title">Contact Us</div>
<div class="section-subtitle">
Tell us what you need, and we will help you find the right solution.
</div>
""", unsafe_allow_html=True)

left, right = st.columns([1, 1])

with left:
    st.markdown("""
    <div class="contact-box">
        <h3 style="color:white;">Let’s Talk</h3>
        <p style="color:#c9c9c9; line-height:1.7;">
        Use this space to introduce your contact details, booking link, email address, 
        or company social media accounts.
        </p>
        <p style="color:#00d1c1; font-weight:700;">Email: hello@digitai.com</p>
        <p style="color:#00d1c1; font-weight:700;">Location: UAE / GCC</p>
    </div>
    """, unsafe_allow_html=True)

with right:
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("How can we help?")
        submitted = st.form_submit_button("Send Message")

        if submitted:
            st.success("Thank you. Your message has been received.")


# -----------------------------
# Footer
# -----------------------------
st.markdown("""
<br><br>
<hr style="border: 0.5px solid rgba(255,255,255,0.1);">
<p style="text-align:center; color:#8f8f8f;">
© 2026 Digit ai. Intelligence Platform. All rights reserved.
</p>
""", unsafe_allow_html=True)
