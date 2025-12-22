import math
import os
import re
import pickle
from django.conf import settings

# Load model only ONCE (safe absolute path)
MODEL_PATH = os.path.join(
    settings.BASE_DIR,
    "ml_models",
    "sentiment_model.pkl"
)

sentiment_model = None

if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, "rb") as f:
        sentiment_model = pickle.load(f)
else:
    print("sentiment_model.pkl not found — ML disabled")


# Extract trained data
word_counts = sentiment_model["word_counts"]
label_counts = sentiment_model["label_counts"]
vocab = sentiment_model["vocab"]
total_docs = sentiment_model["total_docs"]


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
