import json
import os

# 1. Define the path and load the variable that was causing the NameError
TRANS_PATH = "translations.json"

def load_translations_internal():
    if not os.path.exists(TRANS_PATH):
        return {}
    try:
        with open(TRANS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

# This defines TRANSLATIONS globally within this file
TRANSLATIONS = load_translations_internal()

def score_numeric(qkey, option_text, lang='en'):
    if option_text is None:
        return 0
    
    s = str(option_text).strip()
    
    # Handle direct numeric strings (e.g., "1", "2")
    if s.isdigit():
        return int(s)
    
    # 2. Use the TRANSLATIONS variable defined above
    lang_code = lang if lang in TRANSLATIONS else 'en'
    opts = TRANSLATIONS.get(lang_code, {}).get('Q', {}).get(qkey, {}).get('opts')
    
    if not opts:
        opts = TRANSLATIONS.get('en', {}).get('Q', {}).get(qkey, {}).get('opts')
    
    if isinstance(opts, list):
        try:
            return opts.index(s) + 1
        except ValueError:
            return None
    return None

def compute_scores(res, lang='en'):
    # Convert all responses to numeric safely
    num = {k: score_numeric(k, v, lang) for k, v in res.items()}

    # List of keys required for your calculation logic
    required_keys = ['B6','B7','F4','C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C12']
    
    for req in required_keys:
        if num.get(req) is None:
            num[req] = 3 # Safe default fallback

    # --- YOUR CALCULATION LOGIC ---
    refresh_rev = 6 - num['B6']
    difficulty_rev = 6 - num['B7']
    env_rev = 6 - num['F4']
    sleep_quality = refresh_rev + difficulty_rev + env_rev

    who_items = [num['C1'], num['C2'], num['C3'], num['C4'], num['C5']]
    who_rev = [6 - x for x in who_items]
    WHO_total = sum(who_rev) * 4

    distress_total = num['C6'] + num['C7'] + num['C8'] + num['C9'] + num['C10'] + num['C12']

    cog_keys = ['D1','D2','D3','D4','D5','D6','D7','D8']
    cog_efficiency = sum(num.get(k, 0) or 0 for k in cog_keys)

    lifestyle_risk = (
        (num.get('F1') or 0) + 
        (num.get('F2') or 0) + 
        (5 - (num.get('F3') or 3)) + 
        (6 - (num.get('F4') or 3)) + 
        (num.get('F5') or 0) + 
        (num.get('F6') or 0)
    )

    return {
        'sleep_quality': int(sleep_quality),
        'WHO_total': int(WHO_total),
        'distress_total': int(distress_total),
        'cognitive_efficiency': int(cog_efficiency),
        'lifestyle_risk': int(lifestyle_risk)
    }
