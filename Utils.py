import streamlit as st
import json
import os
import gspread
from google.oauth2.service_account import Credentials

TRANS_PATH = "translations.json"

@st.cache_data
def load_translations():
    if not os.path.exists(TRANS_PATH):
        st.error("Missing translations.json file!")
        return {}
    try:
        with open(TRANS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        st.error(f"Error in translations.json syntax: {e}")
        return {}

TRANSLATIONS = load_translations()

def t(lang_code, key, default=None):
    """Translation lookup that works for nested questions or top-level keys."""
    if not TRANSLATIONS:
        return default or key

    # 1. First, check if key exists as top-level
    top_val = TRANSLATIONS.get(key)
    if isinstance(top_val, dict) and lang_code in top_val:
        return top_val[lang_code]

    # 2. Otherwise, check inside lang_code block (like questions)
    lang_block = TRANSLATIONS.get(lang_code, {})
    cur = lang_block
    if key:
        parts = key.split(".")
        for p in parts:
            if isinstance(cur, dict) and p in cur:
                cur = cur[p]
            else:
                cur = None
                break
        if cur is not None:
            return cur

    return default or key

def t_question(lang_code, q_id):
    """Specific helper to get question data safely"""
    # Force check the Q block directly
    lang_block = TRANSLATIONS.get(lang_code, {})
    q_dict = lang_block.get("Q", {})
    q_data = q_dict.get(q_id)
    
    if q_data and isinstance(q_data, dict):
        return q_data
    
    # Fallback if ID is missing
    return {"q": f"Question {q_id} missing", "opts": ["Error: Options not found"]}
    
def map_to_english(q_id, selected_option, lang_code):
    """
    Convert the user's selected option in any language to English.
    """
    if lang_code == "en":
        return selected_option  # Already English

    # Get English options
    en_opts = TRANSLATIONS.get("en", {}).get("Q", {}).get(q_id, {}).get("opts", [])
    # Get selected language options
    lang_opts = TRANSLATIONS.get(lang_code, {}).get("Q", {}).get(q_id, {}).get("opts", [])

    if not en_opts or not lang_opts:
        return selected_option  # fallback

    try:
        idx = lang_opts.index(selected_option)  # find index in user language
        return en_opts[idx]  # return English version
    except ValueError:
        return selected_option  # fallback if not found


def append_to_google_sheet(data_dict, sheet_name="Database"):
    """
    Appends data to Google Sheets using Streamlit secrets service account.
    Automatically creates 'Responses' worksheet if missing and adds headers if sheet is empty.
    """
    try:
        import gspread
        from google.oauth2.service_account import Credentials
        import streamlit as st

        # Load credentials from Streamlit secrets
        creds_info = st.secrets["gcp_service_account"]
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = Credentials.from_service_account_info(creds_info, scopes=scopes)
        client = gspread.authorize(creds)

        # Open sheet, create worksheet if missing
        try:
            sheet = client.open(sheet_name).worksheet("Responses")
        except gspread.exceptions.WorksheetNotFound:
            sh = client.open(sheet_name)
            sheet = sh.add_worksheet(title="Responses", rows=1000, cols=20)

        # Get existing rows to check if headers exist
        existing = sheet.get_all_values()
        if not existing:
            # Append headers first
            sheet.append_row(list(data_dict.keys()))

        # Append data
        sheet.append_row(list(data_dict.values()))
        return True

    except Exception as e:
        st.error(f"Google Sheets error: {e}")
        return False
