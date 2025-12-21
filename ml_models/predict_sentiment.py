import math
import pickle
import re
from collections import defaultdict
from pathlib import Path

# Load model only ONCE
BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "sentiment_model.pkl", "rb") as f:
    model = pickle.load(f)

word_counts = model["word_counts"]
label_counts = model["label_counts"]
vocab = model["vocab"]
total_docs = model["total_docs"]

def predict_sentiment(text):
    words = re.findall(r"\b\w+\b", text.lower())
    scores = {}

    for label in label_counts:
        score = math.log(label_counts[label] / total_docs)
        total_words = sum(word_counts[label].values())

        for word in words:
            word_freq = word_counts[label].get(word, 0)
            score += math.log((word_freq + 1) / (total_words + len(vocab)))

        scores[label] = score

    return max(scores, key=scores.get)
