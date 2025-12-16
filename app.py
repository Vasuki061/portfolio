import streamlit as st
from streamlit_option_menu import option_menu
import urllib.parse

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Vasuki - AI/ML Developer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CUSTOM CSS STYLING (Midnight Blue & Lime Green with FINAL VISIBILITY FIXES) ---
CUSTOM_CSS = """
    <style>
    /* Setting Streamlit's internal variables for theme control */
    :root {
        --st-body-background: #0D1117; /* Midnight Blue */
        --st-sidebar-background: #161B22; /* Dark Slate Blue (Target Color) */
        --st-primary-color: #39FF14; /* Lime Green */
        --st-text-color: #C9D1D9; /* Light Gray Text */
        --st-font: sans-serif;
    }

    /* Main application background */
    .stApp {
        background-color: #0D1117;
        color: #C9D1D9; 
    }

    /* ULTIMATE SIDEBAR FIX: SOLID BACKGROUND ON ALL LAYERS */
    section.main {
        background-color: #0D1117 !important;
    }

    [data-testid="stSidebar"] {
        background: #161B22 !important;
        border-right: 1px solid #39FF14; /* Add a thin accent line */
    }

    [data-testid="stSidebarContent"] {
        background-color: #161B22 !important;
    }

    .profile-card {
        background: #161B22; 
        padding: 30px;
        border-radius: 10px;
        border: 1px solid #39FF14; 
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(57, 255, 20, 0.4);
    }

    h1, h2, h3 {
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }

    /* --- INPUT FIELD FIXES (Labels and Inputs) --- */
    .stTextInput label, .stTextArea label {
        color: #FFFFFF !important; /* Bright White text for labels */
        font-weight: 600 !important;
    }

    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: #21262D !important;
        color: #FFFFFF !important;
        border: 1px solid #C9D1D9 !important;
        border-radius: 6px !important;
        padding: 12px !important;
    }

    /* --- FINAL UNIVERSAL BUTTON VISIBILITY FIX (Lime Green Background / Dark Text & Icon) --- */

    /* 1. TARGET ALL BUTTON BACKGROUNDS: st.button, st.link_button, and st.form_submit_button */
    div.stButton > button, 
    div.stLinkButton > a,
    [data-testid="stForm"] button {
        background-color: #39FF14 !important; /* FORCE LIME GREEN BACKGROUND */
        border: 2px solid #39FF14 !important;
        padding: 10px 25px !important;
        border-radius: 6px !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 15px rgba(57, 255, 20, 0.6) !important;
        width: 100%; 
        margin: 5px 0;
        transition: all 0.3s ease !important;
    }

    /* 2. FORCE DARK TEXT and ICON COLOR on all buttons (Crucial for Visibility) */
    div.stButton > button, 
    div.stLinkButton > a,
    [data-testid="stForm"] button,
    div.stButton > button *,
    div.stLinkButton > a *,
    [data-testid="stForm"] button * {
        color: #0D1117 !important; /* FORCE DARK TEXT */
        fill: #0D1117 !important; /* FORCE DARK ICON COLOR */
    }

    /* Universal Hover Style for all buttons */
    div.stButton > button:hover, 
    div.stLinkButton > a:hover, 
    [data-testid="stForm"] button:hover {
        background: #21262D !important; 
        border-color: #FFFFFF !important;
        box-shadow: 0 6px 20px rgba(57, 255, 20, 1.0) !important;
        transform: translateY(-2px) !important;
    }

    /* Ensure hover text/icon is white */
    div.stButton > button:hover *, 
    div.stLinkButton > a:hover *,
    [data-testid="stForm"] button:hover * {
        color: #FFFFFF !important; /* White text on hover */
        fill: #FFFFFF !important; /* White icon on hover */
    }


    /* 3. Target the final SEND EMAIL NOW button by its ID */
    #send_email_button {
        background: #39FF14 !important; 
        color: #0D1117 !important; 
        border: 2px solid #39FF14 !important;
        padding: 15px 25px !important; 
        font-size: 18px !important;
        box-shadow: 0 4px 15px rgba(57, 255, 20, 0.6) !important;
        display: inline-block;
        text-align: center;
        text-decoration: none;
        width: 100%;
        border-radius: 6px;
        font-weight: 700;
        transition: all 0.3s ease;
    }

    #send_email_button:hover {
        background: #21262D !important; 
        border-color: #FFFFFF !important;
        color: #FFFFFF !important; 
        box-shadow: 0 6px 20px rgba(57, 255, 20, 1.0) !important;
        transform: translateY(-2px) !important;
    }

    .stSuccess {
        background-color: #39FF14 !important;
        color: #0D1117 !important;
        padding: 15px !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }

    .skill-badge {
        background: #39FF14;
        color: #000000; 
        padding: 8px 16px;
        border-radius: 20px;
        display: inline-block;
        margin: 5px;
        font-size: 14px;
        font-weight: 700;
        box-shadow: 0 2px 10px rgba(57, 255, 20, 0.8);
        border: 1px solid #39FF14; 
    }

    .project-card {
        background: #161B22; 
        padding: 30px;
        border-radius: 10px;
        border-left: 4px solid #39FF14; 
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(57, 255, 20, 0.4); 
        transition: all 0.3s ease;
    }

    .project-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(57, 255, 20, 0.8);
        border-left-color: #C9D1D9; 
    }

    /* FIX FOR METRIC TEXT VISIBILITY */
    /* Target the main metric value */
    [data-testid="stMetricValue"] {
        color: #FFFFFF !important; /* Bright White for the main number */
        text-shadow: 0 0 5px #39FF14; /* Slight glow for emphasis */
    }

    /* Target the metric labels (The small text above the number) */
    [data-testid="stMetricLabel"] {
        color: #39FF14 !important; /* Lime Green for the labels */
    }
    </style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION (Minimalist) ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)

    # Small branding placeholder (VASUKI) - FIX APPLIED HERE
    st.markdown(
        "<p style='text-align: center; color: #39FF14; font-size: 20px; font-weight: 700;'>VASUKI</p>",
        unsafe_allow_html=True)
    st.markdown("---", unsafe_allow_html=True)

    # Streamlit Option Menu
    selected = option_menu(
        menu_title=None,
        options=["Home", "About", "Skills", "Projects", "Experience", "Contact"],
        icons=["house-fill", "person-fill", "code-square", "folder-fill", "briefcase-fill", "envelope-fill"],
        menu_icon=None,
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#161B22"},
            "icon": {"color": "#39FF14", "font-size": "22px"},
            "nav-link": {
                "font-size": "18px",
                "text-align": "left",
                "margin": "8px 5px",
                "padding": "12px 15px",
                "color": "#C9D1D9",
                "font-weight": "600",
                "--hover-color": "#21262D",
                "transition": "all 0.3s ease",
            },
            "nav-link-selected": {
                "background-color": "#21262D",
                "color": "#39FF14",
                "font-weight": "700",
                "border-radius": "4px",
            },
        }
    )

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Sidebar Footer/Quick Contact (Optional)
    st.markdown("""
        <div style='padding: 10px; border-top: 1px solid #21262D;'>
        <p style='font-size: 14px; color: #C9D1D9;'>
        <strong style='color: #39FF14;'>Contact:</strong><br>
        <a href='mailto:vasukiadiga9036@gmail.com'>Email</a> | 
        <a href='https://www.linkedin.com/in/vasuki-adiga'>LinkedIn</a>
        </p>
        </div>
    """, unsafe_allow_html=True)

# --- 4. PAGE CONTENT LOGIC ---
# HOME SECTION
if selected == "Home":
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("# 👋 Hi, I'm **VASUKI**")
        st.markdown("## 🎓 AI/ML Engineering Student | Aspiring Data Scientist")
        st.markdown("""
        <div class='profile-card'>
        <p style='font-size: 19px; line-height: 2;'>
        🎓 Pursuing <strong style='color: #F0F0F0;'>BE in AI & ML Engineering</strong> with strong programming and data structures foundation<br>
        💻 Learning and working with <strong style='color: #F0F0F0;'>Python, C, TensorFlow</strong>, and web development<br>
        ☁️ Exploring <strong style='color: #F0F0F0;'>cloud technologies</strong> and AI model deployment<br>
        🚀 Looking for <strong style='color: #F0F0F0;'>internships and projects</strong> in AI/ML, Data Science, Software, Web or Cloud domains
        </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            # Home button 1 (Styled Green/Dark)
            st.link_button("📧 Email Me", "mailto:vasukiadiga9036@gmail.com", use_container_width=True)
        with col_btn2:
            # Home button 2 (Styled Green/Dark)
            st.link_button("💼 LinkedIn", "https://www.linkedin.com/in/vasuki-adiga", use_container_width=True)

    with col2:
        # Accent box uses Lime Green scheme
        st.markdown("""
        <div style='background: #39FF14; 
        padding: 60px 40px; border-radius: 10px; text-align: center; margin-top: 40px;
        box-shadow: 0 10px 40px rgba(57, 255, 20, 0.9);
        border: 2px solid #FFFFFF;'>
        <h1 style='font-size: 100px; margin: 0; color: #0D1117;'>🎓</h1>
        <h2 style='margin-top: 20px; font-size: 28px; color: #0D1117;'>AI/ML</h2>
        <h2 style='margin-top: 5px; font-size: 28px; color: #0D1117;'>Student</h2>
        </div>
        """, unsafe_allow_html=True)

    # Quick Stats
    st.markdown("---")
    st.markdown("## 📊 Quick Stats")
    col1, col2, col3, col4 = st.columns(4)

    # The metric values should now be bright white and the labels lime green
    with col1:
        st.metric("🎓 CGPA", "8.76")
    with col2:
        st.metric("💼 Projects", "3+")
    with col3:
        st.metric("⚡ Skills", "15+")
    with col4:
        st.metric("🏆 Courses", "3")

# ABOUT SECTION
elif selected == "About":
    st.markdown("# 👤 About Me")
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='profile-card'>
        <h3>🎓 Education</h3>
        <p style='line-height: 2;'>
        <strong style='font-size: 18px;'>B.E. Artificial Intelligence and Machine Learning Engineering</strong><br>
        <span style='color: #C9D1D9;'>Mangalore Institute of Technology & Engineering</span><br>
        CGPA: <strong style='color: #39FF14;'>8.76</strong> | 2022 - Present</p>

        <p style='line-height: 2; margin-top: 20px;'>
        <strong style='font-size: 18px;'>Senior Secondary (12th)</strong><br>
        <span style='color: #C9D1D9;'>Government PU College Byndoor</span><br>
        Percentage: <strong style='color: #39FF14;'>95%</strong> | 2021 - 2022</p>

        <p style='line-height: 2; margin-top: 20px;'>
        <strong style='font-size: 18px;'>Secondary School (SSLC)</strong><br>
        <span style='color: #C9D1D9;'>Government Junior college Byndoor</span><br>
        Percentage: <strong style='color: #39FF14;'>91.52%</strong> | 2019 - 2020</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='profile-card'>
        <h3>📚 Courses & Certifications</h3>
        <ul style='line-height: 2.5;'>
        <li><strong>Introduction to Cybersecurity</strong><br>
        <span style='color: #C9D1D9;'>Cisco Networking Academy</span></li>
        <li><strong>Postman API Fundamentals Student Expert</strong><br>
        <span style='color: #C9D1D9;'>Postman</span></li>
        <li><strong>HTML Web Development Crash Course</strong><br>
        <span style='color: #C9D1D9;'>Infosys Springboard</span></li>
        </ul>
        </div>

        <div class='profile-card' style='margin-top: 20px;'>
        <h3>📍 Contact Information</h3>
        <p style='line-height: 2.5;'>
        <strong>📱 Phone:</strong> +91-9110475701<br>
        <strong>📧 Email:</strong> vasukiadiga9036@gmail.com<br>
        <strong>📍 Location:</strong> Trasi, India
        </p>
        </div>
        """, unsafe_allow_html=True)

# SKILLS SECTION
elif selected == "Skills":
    st.markdown("# 💻 Technical Skills")
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='profile-card'>
        <h3>👨‍💻 Programming Languages</h3>
        <div style='margin-top: 15px;'>
        """, unsafe_allow_html=True)
        st.markdown('<span class="skill-badge">C</span> <span class="skill-badge">Python</span>',
                    unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

        st.markdown("""
        <div class='profile-card'>
        <h3>🧠 AI/ML Frameworks</h3>
        <div style='margin-top: 15px;'>
        """, unsafe_allow_html=True)
        st.markdown(
            '<span class="skill-badge">TensorFlow</span> <span class="skill-badge">Scikit-learn</span> <span class="skill-badge">NumPy</span> <span class="skill-badge">Pandas</span>',
            unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

        st.markdown("""
        <div class='profile-card'>
        <h3>🗄️ Database</h3>
        <div style='margin-top: 15px;'>
        """, unsafe_allow_html=True)
        st.markdown('<span class="skill-badge">MongoDB</span> <span class="skill-badge">SQL</span>',
                    unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='profile-card'>
        <h3>🌐 Interface & Web Technologies</h3>
        <div style='margin-top: 15px;'>
        """, unsafe_allow_html=True)
        st.markdown(
            '<span class="skill-badge">HTML</span> <span class="skill-badge">CSS</span> <span class="skill-badge">Flask</span> <span class="skill-badge">Streamlit</span>',
            unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

        st.markdown("""
        <div class='profile-card'>
        <h3>🔧 Tools</h3>
        <div style='margin-top: 15px;'>
        """, unsafe_allow_html=True)
        st.markdown(
            '<span class="skill-badge">Visual Studio</span> <span class="skill-badge">GitHub</span> <span class="skill-badge">Python</span>',
            unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

        st.markdown("""
        <div class='profile-card'>
        <h3>☁️ Cloud & Development Areas</h3>
        <div style='margin-top: 15px;'>
        """, unsafe_allow_html=True)
        st.markdown(
            '<span class="skill-badge">Cloud (Basics)</span> <span class="skill-badge">Web Development</span>',
            unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

# PROJECTS SECTION
elif selected == "Projects":
    st.markdown("# 📂 Featured Projects")
    st.markdown("<br>", unsafe_allow_html=True)

    # Project 1: Al Image Generation and Refinement (Detailed)
    st.markdown("""
    <div class='project-card'>
    <h3 style='font-size: 24px;'>🎨 AI Image Generation and Refinement</h3>
    <p style='font-size: 17px; line-height: 2; margin-top: 15px;'>
    Developed an AI-powered fashion platform implementing 3 core features: outfit classification, 
    personalised recommendations, and AI-based image generation, achieving 91% classification accuracy.
    Implemented CNN models for clothing quality analysis and diffusion models for realistic image generation, deployed using TensorFlow, Streamlit, and Flask.
    </p>
    <p style='margin-top: 20px;'><strong>Technologies Used:</strong></p>
    <div style='margin-top: 10px;'>
    """, unsafe_allow_html=True)
    st.markdown(
        '<span class="skill-badge">TensorFlow</span> <span class="skill-badge">CNN</span> <span class="skill-badge">Diffusion Models</span> <span class="skill-badge">Streamlit</span> <span class="skill-badge">Flask</span>',
        unsafe_allow_html=True)
    st.markdown("""
    <p style='margin-top: 20px;'><strong>Key Features:</strong></p>
    <ul style='line-height: 2;'>
    <li>Outfit classification system</li>
    <li>Personalised fashion recommendations</li>
    <li>AI-based realistic image generation</li>
    <li>CNN models for clothing quality analysis</li>
    </ul>
    </div>
    </div>
    """, unsafe_allow_html=True)

    # Project 2: Inventory Management (UPDATED with full description and features)
    st.markdown("""
    <div class='project-card'>
    <h3 style='font-size: 24px;'>📦 Inventory Management System</h3>
    <p style='font-size: 17px; line-height: 2; margin-top: 15px;'>
    Inventory Management Project is a simple and efficient system designed to help users manage various items 
    by storing key details such as item name, manufacturer, quantity, and expiry date. This project is especially 
    useful for applications like medical supplies, groceries, or warehouse stock management, helping users 
    in organizing items properly, avoiding waste, and making informed decisions.
    </p>
    <p style='margin-top: 20px;'><strong>Technologies Used:</strong></p>
    <div style='margin-top: 10px;'>
    """, unsafe_allow_html=True)
    # Using general programming and database tools from your skills section for context
    st.markdown(
        '<span class="skill-badge">Python</span> <span class="skill-badge">SQL/MongoDB</span> <span class="skill-badge">Web Development</span>',
        unsafe_allow_html=True)
    st.markdown("""
    <p style='margin-top: 20px;'><strong>Key Features:</strong></p>
    <ul style='line-height: 2;'>
    <li>Comprehensive Item Detail Storage (Name, Manufacturer, Quantity, Expiry Date).</li>
    <li>Functionality to add new items and view a full inventory list.</li>
    <li>Advanced filtering based on imminent expiry duration (e.g., within 1 month or 2 months).</li>
    <li>Automated expiry alerts (To proactively avoid stock waste).</li>
    <li>Smart price prediction (Aids in making informed stock and pricing decisions).</li>
    </ul>
    </div>
    </div>
    """, unsafe_allow_html=True)

    # Project 3: Student Learning App (Detailed)
    st.markdown("""
    <div class='project-card'>
    <h3 style='font-size: 24px;'>📚 Student Learning App</h3>
    <p style='font-size: 17px; line-height: 2; margin-top: 15px;'>
    Created a full-stack educational platform with quizzes, calculators, and learning tools to boost engagement.
    Built using Python for the backend and HTML/CSS for the frontend, providing a responsive user experience.
    </p>
    <p style='margin-top: 20px;'><strong>Technologies Used:</strong></p>
    <div style='margin-top: 10px;'>
    """, unsafe_allow_html=True)
    st.markdown(
        '<span class="skill-badge">Python</span> <span class="skill-badge">HTML</span> <span class="skill-badge">CSS</span>',
        unsafe_allow_html=True)
    st.markdown("""
    <p style='margin-top: 20px;'><strong>Features:</strong></p>
    <ul style='line-height: 2;'>
    <li>Interactive quizzes for learning assessment</li>
    <li>Built-in calculators and learning tools</li>
    <li>Responsive user experience</li>
    <li>Full-stack implementation</li>
    </ul>
    </div>
    </div>
    """, unsafe_allow_html=True)

# EXPERIENCE SECTION
elif selected == "Experience":
    st.markdown("# 💼 Professional Experience")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class='project-card'>
    <h2>☁️ AI & Cloud Internship</h2>
    <h3 style='color: #39FF14; font-size: 22px; margin-top: 10px;'>IBM</h3>
    <br>
    <p style='font-size: 17px; line-height: 2;'>
    <strong style='color: #C9D1D9;'>Key Responsibilities & Learning:</strong>
    </p>
    <ul style='font-size: 16px; line-height: 2.5;'>
    <li>Worked with IBM Cloud services and basic AI model deployment.</li>
    <li>Gained hands-on experience with cloud storage, service deployment, and AI workflow automation.</li>
    </ul>

    <p style='margin-top: 25px;'><strong>Technologies & Tools:</strong></p>
    <div style='margin-top: 10px;'>
    """, unsafe_allow_html=True)
    st.markdown(
        '<span class="skill-badge">IBM Cloud</span> <span class="skill-badge">AI Model Deployment</span> <span class="skill-badge">Cloud Storage</span> <span class="skill-badge">AI Workflow Automation</span>',
        unsafe_allow_html=True)
    st.markdown("</div></div>", unsafe_allow_html=True)

# CONTACT SECTION
elif selected == "Contact":
    st.markdown("# 📬 Get In Touch")
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <div class='profile-card'>
        <h3>Let's Connect Directly!</h3>
        <p style='font-size: 17px; line-height: 2;'>
        Fill out this quick form, and the <strong>SEND EMAIL NOW</strong> button will directly open your default email client with your message pre-filled.
        </p>
        </div>
        """, unsafe_allow_html=True)

        # Contact Form
        with st.form("contact_form", clear_on_submit=False):
            st.markdown("### 📝 Your Inquiry Details")
            name = st.text_input("Your Name *", placeholder="Enter your full name", key="contact_name")
            email = st.text_input("Your Email *", placeholder="your.email@example.com", key="contact_email")
            subject = st.text_input("Subject *", placeholder="What's this about?", key="contact_subject")
            message = st.text_area("Message *", height=150, placeholder="Tell me about your inquiry...",
                                   key="contact_message")

            # This button is now styled with the lime green theme and dark text
            submitted = st.form_submit_button("Prepare Email Content 🚀", use_container_width=True)

            feedback_placeholder = st.empty()
            mailto_link_placeholder = st.empty()

            if submitted:
                if name and email and subject and message:
                    # Construct the mailto link content
                    mailto_body = f"Hello Vasuki,\n\n{message}\n\n---\nSender Details:\nName: {name}\nEmail: {email}"
                    encoded_body = urllib.parse.quote(mailto_body)
                    encoded_subject = urllib.parse.quote(f"[Portfolio Contact] {subject}")

                    mailto_link = f"mailto:vasukiadiga9036@gmail.com?subject={encoded_subject}&body={encoded_body}"

                    feedback_placeholder.success(
                        "✅ Success! Click the **SEND EMAIL NOW** button below to finalize your message in your email client.")
                    st.balloons()

                    # Display the final, large, directly clickable mailto button
                    mailto_link_placeholder.markdown(f("""
                    <a id="send_email_button" href="{mailto_link}" target="_blank">
                        SEND EMAIL NOW (Opens Client)
                    </a>
                    """), unsafe_allow_html=True)

                else:
                    feedback_placeholder.error("❌ Please fill in all required fields (*)")

            st.markdown("<br>", unsafe_allow_html=True)
            st.info("💡 **Alternatively, email directly:** vasukiadiga9036@gmail.com")

    with col2:
        st.markdown("""
        <div class='profile-card'>
        <h3>📞 Contact Details</h3>
        <p style='line-height: 2.5;'>
        <strong>📱 Phone:</strong><br>
        <span style='color: #C9D1D9;'>+91-9110475701</span><br><br>

        <strong>📧 Email:</strong><br>
        <a href='mailto:vasukiadiga9036@gmail.com'>vasukiadiga9036@gmail.com</a><br><br>

        <strong>📍 Location:</strong><br>
        <span style='color: #C9D1D9;'>Trasi, India</span><br><br>

        <strong>💼 LinkedIn:</strong><br>
        <a href='https://www.linkedin.com/in/vasuki-adiga' target='_blank'>
        linkedin.com/in/vasuki-adiga
        </a>
        </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Quick action buttons
        st.markdown("""
        <div class='profile-card'>
        <h3>🚀 Quick Actions</h3>
        </div>
        """, unsafe_allow_html=True)

        # Both quick action buttons are now styled as Lime Green/Dark Text
        st.link_button("📧 Email Me Directly", "mailto:vasukiadiga9036@gmail.com", use_container_width=True)
        st.link_button("💼 View LinkedIn Profile", "https://www.linkedin.com/in/vasuki-adiga", use_container_width=True)

# --- 5. FOOTER ---
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #C9D1D9; padding: 20px;'>
    <p style='font-size: 16px;'>© 2024 Vasuki | Built with ❤️ using Streamlit & Python</p>
    <p style='font-size: 14px; color: #6A737D;'>Trasi, India</p>
    </div>
""", unsafe_allow_html=True)