CRISIS_KEYWORDS = [
    "suicide",
    "kill myself",
    "end my life",
    "want to die",
    "no reason to live",
    "hurt myself",
    "self harm",
    "can't go on",
    "give up on life"
]

def is_crisis_message(text):
    text = text.lower()
    return any(keyword in text for keyword in CRISIS_KEYWORDS)
