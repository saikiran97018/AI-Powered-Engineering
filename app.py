# Import libraries
import streamlit as st
import google.generativeai as genai
import time  # For unique timestamp

# Set your Google Gemini API key
genai.configure(api_key="AIzaSyBChtpfxdTTuHGV_UY1-i6EpBhC03-1K1M")

# Predefined data
branches = [
    "CSE", "Mech", "EE", "Chemical Engineering", 
    "Civil Engineering", "Aerospace Engineering", 
    "Biotechnology", "Environmental Engineering"
]
semesters = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th"]

# YouTube resources for each department
youtube_resources = {
    "CSE": [
        "freeCodeCamp - Programming tutorials",
        "CodeWithHarry - Python and web development",
        "GeeksforGeeks - Data Structures and Algorithms"
    ],
    "Mech": [
        "Engineer4Free - Mechanics and thermodynamics",
        "Learn Engineering - Fluid mechanics and robotics",
        "The Efficient Engineer - Engineering concepts"
    ],
    "EE": [
        "ElectroBOOM - Circuits and electronics",
        "GreatScott! - DIY electronics projects",
        "All About Electronics - Signal processing"
    ],
    "Chemical Engineering": [
        "LearnChemE - Thermodynamics and process control",
        "Chemical Engineering Guy - Aspen HYSYS tutorials",
        "The ChemEng Student - Study tips and resources"
    ],
    "Civil Engineering": [
        "Practical Engineering - Structural analysis",
        "Civil Engineering Academy - Exam preparation",
        "Structurefree - Structural engineering concepts"
    ],
    "Aerospace Engineering": [
        "AIAA - Aerospace concepts and news",
        "Real Engineering - Aerospace technology",
        "Everyday Astronaut - Space exploration"
    ],
    "Biotechnology": [
        "Biotech Review - Biotechnology concepts",
        "Khan Academy - Biology and biochemistry",
        "iBiology - Research and applications"
    ],
    "Environmental Engineering": [
        "Practical Engineering - Environmental systems",
        "CrashCourse - Environmental science",
        "The Water Channel - Water management"
    ]
}

# Dynamic response generator using Gemini API
def generate_dynamic_response(query_type, branch, semester, user_input):
    if not user_input:
        return "Please provide an input to get started!"

    # Add timestamp to ensure unique prompt (avoids caching)
    timestamp = str(time.time())
    prompt = (
        f"You are an AI tutor for a {branch} engineering student in {semester} semester. "
        f"Request: '{user_input}'. Feature: '{query_type}'. Timestamp: {timestamp}. "
        f"Generate a unique, tailored response specific to this input: "
        f"- Study Plan: A 7-day plan with topic, explanation (1-2 sentences), video (e.g., 'YouTube: freeCodeCamp - [topic]'), and problem. "
        f"Format each day as: 'Day X: Topic - [t], Explanation - [e], Video - [v], Problem - [p]'.\n"
        f"- Project Idea: A project with name, description (1-2 sentences), 3 steps, and 1 resource. "
        f"Format as: 'Name: [n]\nDescription: [d]\nSteps: 1) [s1], 2) [s2], 3) [s3]\nResource: [r]'.\n"
        f"- Code Help: Identify the error in the code, explain it (1-2 sentences), suggest a fix, and provide an example. "
        f"Format as: 'Error: [e]\nExplanation: [exp]\nFix: [f]\nCorrected Example: [ex]'.\n"
        f"- Career Prep: 2 unique interview questions with answers and 1 tip, tailored to the goal. "
        f"Format as: 'Q1: [q1], A1: [a1], Q2: [q2], A2: [a2], Tip: [t]'.\n"
        f"Ensure the response is specific to {branch} and '{user_input}'."
    )
    
    # Call Gemini API
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")  # Free tier model
        response = model.generate_content(prompt)
        raw_output = response.text.strip()
    except Exception as e:
        raw_output = f"Error: Could not connect to Gemini API. Details: {str(e)}"

    return f"**{query_type} Response ({branch})**\n{raw_output}"

# Custom CSS for DeepSeek-like UI
st.markdown(
    """
    <style>
    /* Main background and text */
    .main {background-color: #0e1117; color: #ffffff; padding: 20px; border-radius: 10px;}
    h1, h2, h3, h4, h5, h6 {color: #ffffff;}
    p, div, span, label {color: #ffffff !important;}
    
    /* Sidebar */
    .sidebar .sidebar-content {background-color: #1e1e1e; color: #ffffff;}
    .sidebar .sidebar-content .stSelectbox label {color: #ffffff;}
    
    /* Buttons */
    .stButton>button {background-color: #4CAF50; color: white; border-radius: 5px; padding: 10px 20px; font-size: 16px; border: none;}
    .stButton>button:hover {background-color: #45a049;}
    
    /* Input fields */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {background-color: #1e1e1e; color: #ffffff; border: 1px solid #444;}
    .stTextInput>label, .stTextArea>label {color: #ffffff;}
    
    /* Tabs */
    .stTabs>div>div>button {background-color: #1e1e1e; color: #ffffff; border: 1px solid #444; border-radius: 5px; margin: 5px;}
    .stTabs>div>div>button:hover {background-color: #333;}
    .stTabs>div>div>button[aria-selected="true"] {background-color: #4CAF50; color: white;}
    
    /* Code block styling */
    pre {background-color: #1e1e1e; color: #ffffff; padding: 10px; border-radius: 5px; border: 1px solid #444;}
    
    /* Alignment and spacing */
    .stTextInput, .stTextArea, .stButton {margin-bottom: 20px;}
    .stTabs {margin-top: 20px;}
    .stMarkdown {margin-top: 10px;}
    </style>
    """, unsafe_allow_html=True
)

# Streamlit UI
def main():
    st.title(" KIRAN AI-Powered Engineering Learning Assistant 🚀")
    st.markdown("Your dynamic companion for study, projects, coding, and career success! Built by [Your Name] | March 2025", unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.header("Settings ⚙️")
        
        # Branch and semester selection
        branch = st.selectbox("Your Branch 🎓", options=branches, index=0)
        semester = st.selectbox("Your Semester 📅", options=semesters, index=2)
        st.markdown("---")

        # YouTube resources dropdown
        st.subheader("YouTube Resources")
        if branch in youtube_resources:
            st.write(f"Recommended YouTube resources for {branch}:")
            for resource in youtube_resources[branch]:
                st.write(f"- {resource}")
        else:
            st.write("No YouTube resources available for this branch.")
        
        st.markdown("---")
        st.write("Select a feature below to get started!")

    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📚 Study Plan", "💻 Code Help", "💡 Project Idea", "🎯 Career Prep"])

    with tab1:
        st.header("Personalized Study Plan 📅")
        st.write("Get a tailored 7-day plan for your weak topics.")
        study_input = st.text_input("Weak Topic", placeholder="E.g., 'I struggle with data structures'", key="study")
        if st.button("Generate Study Plan", key="study_btn"):
            with st.spinner("Crafting your plan..."):
                response = generate_dynamic_response("Study Plan", branch, semester, study_input)
                st.markdown(response)

    with tab3:
        st.header("Project Idea Generator 💡")
        st.write("Request a creative project idea with steps.")
        project_input = st.text_input("Project Request", placeholder="E.g., 'Suggest a project for IoT in mechanical engineering'", key="project")
        if st.button("Generate Project Idea", key="project_btn"):
            with st.spinner("Designing your project..."):
                response = generate_dynamic_response("Project Idea", branch, semester, project_input)
                st.markdown(response)

    with tab2:
        st.header("Code Helper 🐛")
        st.write("Paste your buggy code, and I’ll debug it!")
        code_input = st.text_area("Your Code", placeholder="E.g., 'def sort(arr): arr.sort[", height=150, key="code")
        if st.button("Debug Code", key="code_btn"):
            with st.spinner("Debugging your code..."):
                response = generate_dynamic_response("Code Help", branch, semester, code_input)
                st.markdown(response)

    with tab4:
        st.header("Career Prep 🎯")
        st.write("Prepare for interviews or career goals.")
        career_input = st.text_input("Career Goal", placeholder="E.g., 'Prepare me for a software engineering interview'", key="career")
        if st.button("Prepare Me", key="career_btn"):
            with st.spinner("Preparing your career advice..."):
                response = generate_dynamic_response("Career Prep", branch, semester, career_input)
                st.markdown(response)

    st.markdown("---")
    st.header("Explore Examples 🧩")
    col1, col2 = st.columns(2)
    examples = {
        "Study Plan": "I struggle with data structures",
        "Project Idea": "Suggest a project for IoT in mechanical engineering",
        "Code Help": "def sort(arr): arr.sort[",
        "Career Prep": "Prepare me for a software engineering interview"
    }
    with col1:
        for ex_type, ex_input in list(examples.items())[:2]:
            if st.button(f"{ex_type}: '{ex_input}'", key=f"ex_{ex_type}_1"):
                response = generate_dynamic_response(ex_type, branch, semester, ex_input)
                st.markdown(f"**{ex_type} Example**:\n{response}")
    with col2:
        for ex_type, ex_input in list(examples.items())[2:]:
            if st.button(f"{ex_type}: '{ex_input}'", key=f"ex_{ex_type}_2"):
                response = generate_dynamic_response(ex_type, branch, semester, ex_input)
                st.markdown(f"**{ex_type} Example**:\n{response}")

if __name__ == "__main__":
    main()