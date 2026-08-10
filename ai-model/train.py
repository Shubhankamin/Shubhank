import json
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# ============================================================
# 1. LOAD TRAINING DATA
# ============================================================

with open(
    "data/intents.json",
    "r",
    encoding="utf-8"
) as file:

    data = json.load(file)


sentences = []
labels = []


for intent in data["intents"]:

    for pattern in intent["patterns"]:

        sentences.append(pattern)
        labels.append(intent["tag"])


print("=" * 50)
print("SHUBHANK AI - MODEL TRAINING")
print("=" * 50)

print(
    f"Training examples: {len(sentences)}"
)

print(
    f"Number of intents: {len(set(labels))}"
)


# ============================================================
# 2. TEXT → TF-IDF
# ============================================================

vectorizer = TfidfVectorizer(
    lowercase=True,
    ngram_range=(1, 2)
)


X = vectorizer.fit_transform(
    sentences
)


print(
    f"Vocabulary size: {X.shape[1]}"
)


# ============================================================
# 3. ENCODE INTENTS
# ============================================================

encoder = LabelEncoder()

y = encoder.fit_transform(
    labels
)


print("\nIntent classes:")

for index, intent in enumerate(
    encoder.classes_
):

    print(
        f"{index}: {intent}"
    )


# ============================================================
# 4. TRAIN / VALIDATION SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print("\nDataset split:")

print(
    f"Training samples: {X_train.shape[0]}"
)

print(
    f"Testing samples: {X_test.shape[0]}"
)


# ============================================================
# 5. LOGISTIC REGRESSION CLASSIFIER
# ============================================================

classifier = LogisticRegression(
    max_iter=1000
)


# ============================================================
# 6. TRAIN
# ============================================================

print("\nStarting training...\n")


classifier.fit(
    X_train,
    y_train
)


# ============================================================
# 7. EVALUATE
# ============================================================

predictions = classifier.predict(
    X_test
)


accuracy = accuracy_score(
    y_test,
    predictions
)


print("=" * 50)
print("MODEL EVALUATION")
print("=" * 50)

print(
    f"Test accuracy: {accuracy:.4f}"
)


# ============================================================
# 8. SAVE CLASSIFIER
# ============================================================

with open(
    "model/resume_model.pkl",
    "wb"
) as file:

    pickle.dump(
        classifier,
        file
    )


# ============================================================
# 9. SAVE TF-IDF VECTORIZER
# ============================================================

with open(
    "model/vectorizer.pkl",
    "wb"
) as file:

    pickle.dump(
        vectorizer,
        file
    )


# ============================================================
# 10. SAVE LABEL ENCODER
# ============================================================

with open(
    "model/encoder.pkl",
    "wb"
) as file:

    pickle.dump(
        encoder,
        file
    )


print("\nModel saved successfully!")

print("\nGenerated files:")

print(
    "model/resume_model.pkl"
)

print(
    "model/vectorizer.pkl"
)

print(
    "model/encoder.pkl"
)

print("\nTraining completed.")