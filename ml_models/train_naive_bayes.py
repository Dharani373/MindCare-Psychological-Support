import math,re
import pickle
from collections import defaultdict
from sentiment_data import training_data

# Split data
texts = [t for t, l in training_data]
labels = [l for t, l in training_data]

# Vocabulary & counts
word_counts = defaultdict(lambda: defaultdict(int))
label_counts = defaultdict(int)
vocab = set()

# Training
for text, label in training_data:
    label_counts[label] += 1
    words = re.findall(r"\b\w+\b", text.lower())
    for word in words:
        vocab.add(word)
        word_counts[label][word] += 1

total_docs = len(training_data)
labels_set = set(labels)

# Save model
model = {
    "word_counts": dict(word_counts),
    "label_counts": dict(label_counts),
    "vocab": list(vocab),
    "total_docs": total_docs
}

with open("sentiment_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Naive Bayes sentiment model trained & saved")
