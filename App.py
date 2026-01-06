import streamlit as st
from datetime import datetime
import uuid

from Utils import t, t_question, append_to_google_sheet, TRANSLATIONS, map_to_english
from UI import render_mcq_card
from test_compute_scores import compute_scores
from score_interpretations import interpret_score, get_interpretation_labels

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Chronotype & Brain Efficiency",
    layout="wide"
)

# --------------------------------------------------
# Global CSS
# --------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(
            to bottom right, 
            var(--background-color), 
            var(--secondary-background-color)
        );
    }

    div[data-testid="stWidgetLabel"] p,
    div[data-testid="stMarkdownContainer"] p {
        color: var(--text-color);
    }

    h1, h2, h3 {
        color: var(--text-color);
        font-family: 'Inter', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Session State Init
# --------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = 1

if "responses" not in st.session_state:
    st.session_state.responses = {}

if "lang_choice" not in st.session_state:
    st.session_state.lang_choice = "en"

if "locked_lang" not in st.session_state:
    st.session_state.locked_lang = None

if "survey_id" not in st.session_state:
    st.session_state.survey_id = str(uuid.uuid4())
    st.session_state.data_saved = False

# --------------------------------------------------
# Progress Bar
# --------------------------------------------------
TOTAL_PAGES = 2

def show_progress():
    if st.session_state.page > 1:
        st.progress((st.session_state.page - 1) / TOTAL_PAGES)

# --------------------------------------------------
# INTRO PAGE
# --------------------------------------------------
def show_intro():
    lang = st.session_state.lang_choice

    st.title(t(lang, "title", "Survey"))
    st.write(t(lang, "desc", ""))

    lang_options = ["en", "hi", "mr"]
    lang_labels = {"en": "English", "hi": "हिन्दी", "mr": "मराठी"}

    st.selectbox(
        "Select Language",
        options=lang_options,
        format_func=lambda x: lang_labels[x],
        key="lang_choice"
    )

    if st.button(t(lang, "start", "Start")):
        st.session_state.locked_lang = st.session_state.lang_choice
        st.session_state.page = 2
        st.session_state.responses = {}
        st.rerun()

# --------------------------------------------------
# SECTION RENDER HELPERS
# --------------------------------------------------
def render_section_block(section_id, q_list, lang):
    st.subheader(t(lang, f"sections.{section_id}", f"Section {section_id}"))

    for q in q_list:
        data = t_question(lang, q)
        choice = render_mcq_card(
            data["q"],
            data["opts"],
            key=f"ans_{q}",
            current_value=st.session_state.responses.get(q)
        )
        st.session_state.responses[q] = choice

def render_section_c_inline():
    lang = st.session_state.locked_lang
    st.subheader(t(lang, "sections.C"))

    qs = [f"C{i}" for i in range(1, 13)]

    st.markdown(f"**{t(lang, 'sections.C_sub_who')}**")
    for q in qs[:5]:
        data = t_question(lang, q)
        st.session_state.responses[q] = render_mcq_card(
            data["q"], data["opts"],
            key=f"ans_{q}",
            current_value=st.session_state.responses.get(q)
        )

    st.divider()

    for q in qs[5:]:
        data = t_question(lang, q)
        st.session_state.responses[q] = render_mcq_card(
            data["q"], data["opts"],
            key=f"ans_{q}",
            current_value=st.session_state.responses.get(q)
        )

# --------------------------------------------------
# ALL QUESTIONS PAGE
# --------------------------------------------------
def show_all_questions():
    lang = st.session_state.locked_lang
    st.title(t(lang, "title"))

    show_progress()

    render_section_block("A", ["A1","A2","A3","A4","A5","A6","A7"], lang)
    render_section_block("B", [f"B{i}" for i in range(1,14)], lang)
    render_section_c_inline()
    render_section_block("D", [f"D{i}" for i in range(1,10)], lang)
    render_section_block("E", ["E1","E2","E3","E4"], lang)
    render_section_block("F", ["F1","F2","F3","F4","F5","F6"], lang)

    all_questions = (
        ["A1","A2","A3","A4","A5","A6","A7"] +
        [f"B{i}" for i in range(1,14)] +
        [f"C{i}" for i in range(1,13)] +
        [f"D{i}" for i in range(1,10)] +
        ["E1","E2","E3","E4"] +
        ["F1","F2","F3","F4","F5","F6"]
    )

    unanswered = [q for q in all_questions if st.session_state.responses.get(q) is None]

    col1, col2 = st.columns(2)

    with col1:
        if st.button(t(lang, "back", "Back")):
            st.session_state.page = 1
            st.rerun()

    with col2:
        if st.button(t(lang, "submit", "Submit"), disabled=bool(unanswered)):
            st.session_state.page = 3
            st.rerun()

    if unanswered:
        st.info(t(lang, "answer_all", "Please answer all questions to continue."))

SCALE_ORDER = [
    ("sleep_quality", "🌙"),
    ("WHO_total", "🙂"),
    ("distress_total", "⚠️"),
    ("cognitive_efficiency", "🧠"),
    ("lifestyle_risk", "🔥")
]

# --------------------------------------------------
# Final Page
# --------------------------------------------------
def show_final():
    lang = st.session_state.locked_lang
    scores = compute_scores(st.session_state.responses, lang)
    st.title(t(lang, "title"))

    st.success(t(lang, "final_thanks", "Thank you for completing the assessment!"))
    st.subheader(t(lang, "final_scores", "Your Scores"))
    # Display metrics using translations
    metrics = TRANSLATIONS.get("final_metrics", {}).get(lang, {})
    col1, col2 = st.columns(2)

    with col1:
        st.metric(metrics.get("sleep_quality", "🌙 Sleep Quality (3–15)"), scores.get("sleep_quality", 0))
        st.metric(metrics.get("WHO_total", "🙂 WHO-5 Well-being (0–100)"), scores.get("WHO_total", 0))
        st.metric(metrics.get("distress_total", "⚠️ Mental Distress (6–30)"), scores.get("distress_total", 0))

    with col2:
        st.metric(metrics.get("cognitive_efficiency", "🧠 Cognitive Efficiency (8–40)"), scores.get("cognitive_efficiency", 0))
        st.metric(metrics.get("lifestyle_risk", "🔥 Lifestyle Risk (higher = worse)"), scores.get("lifestyle_risk", 0))

    labels = get_interpretation_labels(lang)
    st.subheader(labels["section_title"])
    
    for scale_key, icon in SCALE_ORDER:
        score_value = scores.get(scale_key)
    
        interp = interpret_score(scale_key, score_value, lang)
    
        if not interp:
            continue
    
        with st.container(border=True):
            st.markdown(
                f"""
                ### {icon} {interp['title']}
                **{labels['level']}:** {interp['level']}
    
                {interp['meaning']}
                """
            )
    
            if interp.get("what_it_reflects"):
                st.markdown(f"**{labels['reflects']}:**")
                for item in interp["what_it_reflects"]:
                    st.markdown(f"- {item}")
    
            if interp.get("what_to_change"):
                st.markdown(f"**{labels['change']}:**")
                for item in interp["what_to_change"]:
                    st.markdown(f"- {item}")

    st.balloons()

    # Convert all responses to English before saving
    english_responses = {}
    for q, ans in st.session_state.responses.items():
        english_responses[q] = map_to_english(q, ans, st.session_state.locked_lang)

    # Save data only once per session
    if not st.session_state.get("data_saved", False):
        save_data = {
            "survey_id": st.session_state.survey_id,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "lang": "en",
            **english_responses,
            **scores
        }

        # # Debug log to check data
        # st.write("Saving data to Google Sheets:", save_data)

        if append_to_google_sheet(save_data):
            st.success(t(lang, "final_saved"))
            st.write(t(lang, "done_message"))
            st.session_state.data_saved = True  # prevent duplicate saves
        else:
            st.error("Failed to save data to Google Sheets. Please contact admin.")

# --------------------------------------------------
# NAVIGATION
# --------------------------------------------------
if st.session_state.page == 1:
    show_intro()
elif st.session_state.page == 2:
    show_all_questions()
elif st.session_state.page == 3:
    show_final()
