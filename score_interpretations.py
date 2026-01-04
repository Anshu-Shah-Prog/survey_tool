# score_interpretations.py

# ======================================================
# VERIFIED SCORE RANGES (from compute_scores.py)
#
# sleep_quality        : 3 – 15   (higher = better)
# WHO_total            : 20 – 100 (higher = better)
# distress_total       : 6 – 30   (higher = worse)
# cognitive_efficiency : 8 – 40   (higher = better)
# lifestyle_risk       : 5 – 29   (higher = worse)
# ======================================================
INTERPRETATION_LABELS = {
    "en": {
        "section_title": "Score Interpretation",
        "level": "Level",
        "reflects": "What this reflects",
        "change": "What you can improve"
    },
    "hi": {
        "section_title": "स्कोर की व्याख्या",
        "level": "स्तर",
        "reflects": "यह क्या दर्शाता है",
        "change": "आप क्या सुधार सकते हैं"
    },
    "mr": {
        "section_title": "गुणांकनाचे स्पष्टीकरण",
        "level": "पातळी",
        "reflects": "हे काय दर्शवते",
        "change": "आपण काय सुधारू शकता"
    }
}

SCORE_INTERPRETATIONS = {

    # ==================================================
    # 1. SLEEP QUALITY (3–15)
    # ==================================================
    "sleep_quality": {

        "en": [
            {
                "range": (3, 7),
                "level": "Low",
                "title": "Poor sleep quality",
                "meaning": "Your sleep is insufficient or disturbed and may be affecting your energy, mood, and ability to focus during the day.",
                "what_it_reflects": [
                    "Inadequate physical and mental recovery",
                    "Irregular or disrupted sleep routine"
                ],
                "what_to_change": [
                    "Fix a consistent sleep and wake-up time",
                    "Reduce screen exposure before bedtime",
                    "Create a calm pre-sleep routine"
                ]
            },
            {
                "range": (8, 11),
                "level": "Moderate",
                "title": "Fair sleep quality",
                "meaning": "Your sleep supports basic daily functioning but may not be fully restorative.",
                "what_it_reflects": [
                    "Partial recovery during sleep",
                    "Occasional sleep disturbances"
                ],
                "what_to_change": [
                    "Improve sleep consistency",
                    "Focus on sleep hygiene and relaxation"
                ]
            },
            {
                "range": (12, 15),
                "level": "High",
                "title": "Good sleep quality",
                "meaning": "Your sleep pattern effectively supports emotional stability, attention, and overall well-being.",
                "what_it_reflects": [
                    "Healthy sleep regulation",
                    "Effective night-time recovery"
                ],
                "what_to_change": [
                    "Maintain current healthy sleep habits"
                ]
            }
        ],

        "hi": [
            {
                "range": (3, 7),
                "level": "Low",
                "title": "खराब नींद गुणवत्ता",
                "meaning": "आपकी नींद पर्याप्त या स्थिर नहीं है, जिससे ऊर्जा, मनोदशा और एकाग्रता प्रभावित हो सकती है।",
                "what_it_reflects": [
                    "शारीरिक और मानसिक विश्राम की कमी",
                    "अनियमित नींद दिनचर्या"
                ],
                "what_to_change": [
                    "सोने और जागने का समय नियमित करें",
                    "सोने से पहले स्क्रीन का उपयोग कम करें",
                    "शांत सोने की दिनचर्या अपनाएँ"
                ]
            },
            {
                "range": (8, 11),
                "level": "Moderate",
                "title": "सामान्य नींद गुणवत्ता",
                "meaning": "नींद दैनिक कार्यों के लिए पर्याप्त है लेकिन पूरी तरह से तरोताजा नहीं करती।",
                "what_it_reflects": [
                    "आंशिक विश्राम",
                    "कभी-कभी नींद में बाधा"
                ],
                "what_to_change": [
                    "नींद की नियमितता बढ़ाएँ",
                    "नींद स्वच्छता पर ध्यान दें"
                ]
            },
            {
                "range": (12, 15),
                "level": "High",
                "title": "अच्छी नींद गुणवत्ता",
                "meaning": "आपकी नींद मानसिक संतुलन और ध्यान को अच्छी तरह समर्थन देती है।",
                "what_it_reflects": [
                    "स्वस्थ नींद नियंत्रण",
                    "अच्छा विश्राम"
                ],
                "what_to_change": [
                    "वर्तमान आदतें बनाए रखें"
                ]
            }
        ],

        "mr": [
            {
                "range": (3, 7),
                "level": "Low",
                "title": "खराब झोप गुणवत्ता",
                "meaning": "तुमची झोप अपुरी किंवा विस्कळीत असून त्यामुळे ऊर्जा, मनःस्थिती आणि लक्षावर परिणाम होऊ शकतो.",
                "what_it_reflects": [
                    "अपुरा शारीरिक व मानसिक विश्रांती",
                    "अनियमित झोपेची सवय"
                ],
                "what_to_change": [
                    "झोपेची व उठण्याची वेळ निश्चित ठेवा",
                    "झोपण्यापूर्वी स्क्रीन वापर कमी करा",
                    "शांत झोपेची सवय लावा"
                ]
            },
            {
                "range": (8, 11),
                "level": "Moderate",
                "title": "मध्यम झोप गुणवत्ता",
                "meaning": "झोप पुरेशी आहे पण पूर्णपणे ताजेतवानी करत नाही.",
                "what_it_reflects": [
                    "अर्धवट विश्रांती",
                    "कधीकधी झोपेत अडथळे"
                ],
                "what_to_change": [
                    "झोपेची नियमितता वाढवा",
                    "झोपेपूर्वी विश्रांती घ्या"
                ]
            },
            {
                "range": (12, 15),
                "level": "High",
                "title": "चांगली झोप गुणवत्ता",
                "meaning": "तुमची झोप मानसिक व भावनिक आरोग्यास पोषक आहे.",
                "what_it_reflects": [
                    "संतुलित झोप नियंत्रण",
                    "योग्य विश्रांती"
                ],
                "what_to_change": [
                    "सध्याच्या सवयी टिकवा"
                ]
            }
        ]
    },

    # ==================================================
    # 2. WHO-5 WELL-BEING (20–100)
    # ==================================================
    "WHO_total": {

        "en": [
            {
                "range": (20, 44),
                "level": "Low",
                "title": "Low well-being",
                "meaning": "Your responses suggest reduced emotional well-being and limited positive mood.",
                "what_it_reflects": [
                    "Low vitality",
                    "Reduced enjoyment in daily life"
                ],
                "what_to_change": [
                    "Increase pleasant and restorative activities",
                    "Seek emotional support if low mood continues"
                ]
            },
            {
                "range": (45, 69),
                "level": "Moderate",
                "title": "Moderate well-being",
                "meaning": "Your well-being is present but not consistently positive.",
                "what_it_reflects": [
                    "Fluctuating emotional balance"
                ],
                "what_to_change": [
                    "Strengthen self-care routines",
                    "Improve work–life balance"
                ]
            },
            {
                "range": (70, 100),
                "level": "High",
                "title": "High well-being",
                "meaning": "You report strong emotional well-being and positive mental health.",
                "what_it_reflects": [
                    "Positive mood",
                    "Psychological resilience"
                ],
                "what_to_change": [
                    "Maintain current supportive habits"
                ]
            }
        ],

        "hi": [
            {
                "range": (20, 44),
                "level": "Low",
                "title": "कम मानसिक कल्याण",
                "meaning": "आपके उत्तर भावनात्मक भलाई में कमी और कम सकारात्मक मनोदशा दर्शाते हैं।",
                "what_it_reflects": [
                    "कम ऊर्जा",
                    "दैनिक जीवन में आनंद की कमी"
                ],
                "what_to_change": [
                    "सकारात्मक गतिविधियाँ बढ़ाएँ",
                    "ज़रूरत हो तो भावनात्मक सहायता लें"
                ]
            },
            {
                "range": (45, 69),
                "level": "Moderate",
                "title": "मध्यम मानसिक कल्याण",
                "meaning": "मानसिक कल्याण मौजूद है लेकिन लगातार सकारात्मक नहीं है।",
                "what_it_reflects": [
                    "भावनात्मक अस्थिरता"
                ],
                "what_to_change": [
                    "स्व-देखभाल की आदतें मज़बूत करें",
                    "कार्य–जीवन संतुलन सुधारें"
                ]
            },
            {
                "range": (70, 100),
                "level": "High",
                "title": "उच्च मानसिक कल्याण",
                "meaning": "आपका मानसिक और भावनात्मक स्वास्थ्य अच्छा है।",
                "what_it_reflects": [
                    "सकारात्मक सोच",
                    "मानसिक मजबूती"
                ],
                "what_to_change": [
                    "स्वस्थ आदतें बनाए रखें"
                ]
            }
        ],

        "mr": [
            {
                "range": (20, 44),
                "level": "Low",
                "title": "कमी मानसिक कल्याण",
                "meaning": "तुमच्या भावनिक आरोग्यात घट दिसून येते.",
                "what_it_reflects": [
                    "कमी ऊर्जा",
                    "दैनंदिन जीवनातील आनंद कमी होणे"
                ],
                "what_to_change": [
                    "आनंददायी व विश्रांती देणाऱ्या क्रिया वाढवा",
                    "गरज असल्यास भावनिक मदत घ्या"
                ]
            },
            {
                "range": (45, 69),
                "level": "Moderate",
                "title": "मध्यम मानसिक कल्याण",
                "meaning": "मानसिक कल्याण आहे पण सातत्याने सकारात्मक नाही.",
                "what_it_reflects": [
                    "भावनिक चढ-उतार"
                ],
                "what_to_change": [
                    "स्व-देखभाल सवयी बळकट करा",
                    "काम–जीवन संतुलन सुधारा"
                ]
            },
            {
                "range": (70, 100),
                "level": "High",
                "title": "उच्च मानसिक कल्याण",
                "meaning": "तुमचे मानसिक व भावनिक आरोग्य चांगले आहे.",
                "what_it_reflects": [
                    "सकारात्मक मनःस्थिती",
                    "मानसिक लवचिकता"
                ],
                "what_to_change": [
                    "सध्याच्या चांगल्या सवयी टिकवा"
                ]
            }
        ]
    },

    # ==================================================
    # 3. DISTRESS TOTAL (6–30)
    # ==================================================
    "distress_total": {

        "en": [
            {
                "range": (6, 13),
                "level": "Low",
                "title": "Low psychological distress",
                "meaning": "You are managing emotional demands effectively.",
                "what_it_reflects": [
                    "Healthy stress coping"
                ],
                "what_to_change": [
                    "Maintain current coping strategies"
                ]
            },
            {
                "range": (14, 21),
                "level": "Moderate",
                "title": "Moderate psychological distress",
                "meaning": "Emotional strain is present and may affect daily functioning.",
                "what_it_reflects": [
                    "Accumulated stress"
                ],
                "what_to_change": [
                    "Reduce workload",
                    "Increase recovery time"
                ]
            },
            {
                "range": (22, 30),
                "level": "High",
                "title": "High psychological distress",
                "meaning": "Emotional strain is significantly impacting well-being.",
                "what_it_reflects": [
                    "Persistent stress exposure"
                ],
                "what_to_change": [
                    "Seek professional or social support"
                ]
            }
        ],

        "hi": [
            {
                "range": (6, 13),
                "level": "Low",
                "title": "कम मानसिक तनाव",
                "meaning": "आप भावनात्मक दबाव को अच्छी तरह संभाल रहे हैं।",
                "what_it_reflects": [
                    "स्वस्थ तनाव प्रबंधन"
                ],
                "what_to_change": [
                    "वर्तमान तरीकों को बनाए रखें"
                ]
            },
            {
                "range": (14, 21),
                "level": "Moderate",
                "title": "मध्यम मानसिक तनाव",
                "meaning": "तनाव मौजूद है और कार्यक्षमता को प्रभावित कर सकता है।",
                "what_it_reflects": [
                    "जमा हुआ तनाव"
                ],
                "what_to_change": [
                    "काम का बोझ कम करें",
                    "विश्राम बढ़ाएँ"
                ]
            },
            {
                "range": (22, 30),
                "level": "High",
                "title": "अधिक मानसिक तनाव",
                "meaning": "मानसिक तनाव आपके स्वास्थ्य पर प्रभाव डाल रहा है।",
                "what_it_reflects": [
                    "लगातार तनाव"
                ],
                "what_to_change": [
                    "पेशेवर या सामाजिक सहायता लें"
                ]
            }
        ],

        "mr": [
            {
                "range": (6, 13),
                "level": "Low",
                "title": "कमी मानसिक ताण",
                "meaning": "तुम्ही मानसिक ताण योग्य प्रकारे हाताळत आहात.",
                "what_it_reflects": [
                    "चांगले ताण व्यवस्थापन"
                ],
                "what_to_change": [
                    "सध्याच्या उपाययोजना सुरू ठेवा"
                ]
            },
            {
                "range": (14, 21),
                "level": "Moderate",
                "title": "मध्यम मानसिक ताण",
                "meaning": "ताण जाणवत असून दैनंदिन कार्यावर परिणाम होऊ शकतो.",
                "what_it_reflects": [
                    "साचलेला ताण"
                ],
                "what_to_change": [
                    "कामाचा ताण कमी करा",
                    "विश्रांती वाढवा"
                ]
            },
            {
                "range": (22, 30),
                "level": "High",
                "title": "उच्च मानसिक ताण",
                "meaning": "मानसिक ताण आरोग्यावर गंभीर परिणाम करत आहे.",
                "what_it_reflects": [
                    "सततचा ताण"
                ],
                "what_to_change": [
                    "व्यावसायिक किंवा सामाजिक मदत घ्या"
                ]
            }
        ]
    },

    # ==================================================
    # 4. COGNITIVE EFFICIENCY (8–40)
    # ==================================================
    "cognitive_efficiency": {

        "en": [
            {
                "range": (8, 18),
                "level": "Low",
                "title": "Reduced cognitive efficiency",
                "meaning": "You may have difficulty focusing or sustaining mental effort.",
                "what_it_reflects": [
                    "Mental fatigue",
                    "Reduced attention"
                ],
                "what_to_change": [
                    "Improve sleep quality",
                    "Avoid multitasking"
                ]
            },
            {
                "range": (19, 29),
                "level": "Moderate",
                "title": "Average cognitive efficiency",
                "meaning": "Mental performance is adequate but inconsistent.",
                "what_it_reflects": [
                    "Variable focus"
                ],
                "what_to_change": [
                    "Organize tasks",
                    "Take regular breaks"
                ]
            },
            {
                "range": (30, 40),
                "level": "High",
                "title": "High cognitive efficiency",
                "meaning": "You are able to think clearly and focus effectively.",
                "what_it_reflects": [
                    "Strong mental clarity"
                ],
                "what_to_change": [
                    "Maintain current habits"
                ]
            }
        ],

        "hi": [
            {
                "range": (8, 18),
                "level": "Low",
                "title": "कम संज्ञानात्मक दक्षता",
                "meaning": "ध्यान केंद्रित करने में कठिनाई हो सकती है।",
                "what_it_reflects": [
                    "मानसिक थकान"
                ],
                "what_to_change": [
                    "नींद सुधारें",
                    "एक साथ कई काम न करें"
                ]
            },
            {
                "range": (19, 29),
                "level": "Moderate",
                "title": "औसत संज्ञानात्मक दक्षता",
                "meaning": "मानसिक कार्यक्षमता पर्याप्त है लेकिन स्थिर नहीं।",
                "what_it_reflects": [
                    "ध्यान में उतार-चढ़ाव"
                ],
                "what_to_change": [
                    "काम व्यवस्थित करें",
                    "नियमित ब्रेक लें"
                ]
            },
            {
                "range": (30, 40),
                "level": "High",
                "title": "उच्च संज्ञानात्मक दक्षता",
                "meaning": "आप स्पष्ट रूप से सोचने और ध्यान बनाए रखने में सक्षम हैं।",
                "what_it_reflects": [
                    "अच्छी मानसिक स्पष्टता"
                ],
                "what_to_change": [
                    "अच्छी आदतें बनाए रखें"
                ]
            }
        ],

        "mr": [
            {
                "range": (8, 18),
                "level": "Low",
                "title": "कमी संज्ञानात्मक कार्यक्षमता",
                "meaning": "लक्ष केंद्रित ठेवण्यात अडचण येऊ शकते.",
                "what_it_reflects": [
                    "मानसिक थकवा"
                ],
                "what_to_change": [
                    "झोप सुधार करा",
                    "मल्टीटास्किंग टाळा"
                ]
            },
            {
                "range": (19, 29),
                "level": "Moderate",
                "title": "मध्यम संज्ञानात्मक कार्यक्षमता",
                "meaning": "मानसिक कार्यक्षमता पुरेशी आहे पण स्थिर नाही.",
                "what_it_reflects": [
                    "लक्षातील चढ-उतार"
                ],
                "what_to_change": [
                    "कामांची मांडणी करा",
                    "नियमित विश्रांती घ्या"
                ]
            },
            {
                "range": (30, 40),
                "level": "High",
                "title": "उच्च संज्ञानात्मक कार्यक्षमता",
                "meaning": "तुम्ही स्पष्टपणे विचार करू शकता आणि लक्ष टिकवू शकता.",
                "what_it_reflects": [
                    "मजबूत मानसिक स्पष्टता"
                ],
                "what_to_change": [
                    "सध्याच्या सवयी टिकवा"
                ]
            }
        ]
    },

    # ==================================================
    # 5. LIFESTYLE RISK (5–29)
    # ==================================================
    "lifestyle_risk": {

        "en": [
            {
                "range": (5, 11),
                "level": "Low",
                "title": "Low lifestyle risk",
                "meaning": "Your lifestyle habits support long-term physical and mental health.",
                "what_it_reflects": [
                    "Balanced routines"
                ],
                "what_to_change": [
                    "Maintain healthy habits"
                ]
            },
            {
                "range": (12, 20),
                "level": "Moderate",
                "title": "Moderate lifestyle risk",
                "meaning": "Some habits may negatively affect health over time.",
                "what_it_reflects": [
                    "Inconsistent health behaviors"
                ],
                "what_to_change": [
                    "Improve sleep, diet, or activity"
                ]
            },
            {
                "range": (21, 29),
                "level": "High",
                "title": "High lifestyle risk",
                "meaning": "Lifestyle patterns may significantly impact health and well-being.",
                "what_it_reflects": [
                    "Elevated behavioral risk"
                ],
                "what_to_change": [
                    "Adopt structured, health-supportive routines"
                ]
            }
        ],

        "hi": [
            {
                "range": (5, 11),
                "level": "Low",
                "title": "कम जीवनशैली जोखिम",
                "meaning": "आपकी जीवनशैली शारीरिक और मानसिक स्वास्थ्य को समर्थन देती है।",
                "what_it_reflects": [
                    "संतुलित दिनचर्या"
                ],
                "what_to_change": [
                    "स्वस्थ आदतें बनाए रखें"
                ]
            },
            {
                "range": (12, 20),
                "level": "Moderate",
                "title": "मध्यम जीवनशैली जोखिम",
                "meaning": "कुछ आदतें समय के साथ स्वास्थ्य को प्रभावित कर सकती हैं।",
                "what_it_reflects": [
                    "अनियमित स्वास्थ्य व्यवहार"
                ],
                "what_to_change": [
                    "नींद, आहार या व्यायाम सुधारें"
                ]
            },
            {
                "range": (21, 29),
                "level": "High",
                "title": "अधिक जीवनशैली जोखिम",
                "meaning": "जीवनशैली स्वास्थ्य पर नकारात्मक प्रभाव डाल सकती है।",
                "what_it_reflects": [
                    "उच्च व्यवहारिक जोखिम"
                ],
                "what_to_change": [
                    "संरचित और स्वस्थ दिनचर्या अपनाएँ"
                ]
            }
        ],

        "mr": [
            {
                "range": (5, 11),
                "level": "Low",
                "title": "कमी जीवनशैली धोका",
                "meaning": "तुमची जीवनशैली शारीरिक व मानसिक आरोग्यास पोषक आहे.",
                "what_it_reflects": [
                    "संतुलित दिनक्रम"
                ],
                "what_to_change": [
                    "चांगल्या सवयी टिकवा"
                ]
            },
            {
                "range": (12, 20),
                "level": "Moderate",
                "title": "मध्यम जीवनशैली धोका",
                "meaning": "काही सवयी कालांतराने आरोग्यावर परिणाम करू शकतात.",
                "what_it_reflects": [
                    "अनियमित आरोग्यविषयक सवयी"
                ],
                "what_to_change": [
                    "झोप, आहार किंवा व्यायाम सुधार करा"
                ]
            },
            {
                "range": (21, 29),
                "level": "High",
                "title": "उच्च जीवनशैली धोका",
                "meaning": "जीवनशैली आरोग्यावर लक्षणीय नकारात्मक परिणाम करू शकते.",
                "what_it_reflects": [
                    "उच्च वर्तनात्मक धोका"
                ],
                "what_to_change": [
                    "संरचित व आरोग्यपूरक दिनक्रम स्वीकारा"
                ]
            }
        ]
    }
}


def interpret_score(scale_name, score_value, lang="en"):
    """
    Returns the interpretation dictionary for a given scale and score.
    Automatically falls back to English if the selected language is unavailable.
    """
    scale = SCORE_INTERPRETATIONS.get(scale_name)
    if not scale:
        return None

    entries = scale.get(lang) or scale.get("en")
    if not entries:
        return None

    for item in entries:
        low, high = item["range"]
        if low <= score_value <= high:
            return item

    return None

def get_interpretation_labels(lang="en"):
    """
    Returns language-specific labels for interpretation sections.
    Falls back to English if language is missing.
    """
    return INTERPRETATION_LABELS.get(lang) or INTERPRETATION_LABELS["en"]
