import json
import pickle

import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout


# ============================================================
# 1. LOAD TRAINING DATA
# ============================================================

with open("data/intents.json", "r", encoding="utf-8") as file:
    data = json.load(file)


sentences = []
labels = []


for intent in data["intents"]:
    for pattern in intent["patterns"]:
        sentences.append(pattern)
        labels.append(intent["tag"])


print("=" * 50)
print("RESUME AI - MODEL TRAINING")
print("=" * 50)

print(f"Training examples: {len(sentences)}")
print(f"Number of intents: {len(set(labels))}")


# ============================================================
# 2. TEXT → NUMBERS USING TF-IDF
# ============================================================

vectorizer = TfidfVectorizer(
    lowercase=True,
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(sentences).toarray()


print(f"Vocabulary size: {X.shape[1]}")


# ============================================================
# 3. ENCODE INTENTS
# ============================================================

encoder = LabelEncoder()

y = encoder.fit_transform(labels)


print("\nIntent classes:")

for index, intent in enumerate(encoder.classes_):
    print(f"{index}: {intent}")


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
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")


# ============================================================
# 5. BUILD NEURAL NETWORK
# ============================================================

model = Sequential([
    Dense(
        128,
        activation="relu",
        input_shape=(X.shape[1],)
    ),

    Dropout(0.3),

    Dense(
        64,
        activation="relu"
    ),

    Dropout(0.2),

    Dense(
        len(encoder.classes_),
        activation="softmax"
    )
])


# ============================================================
# 6. COMPILE MODEL
# ============================================================

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


# ============================================================
# 7. TRAIN MODEL
# ============================================================

print("\nStarting training...\n")

history = model.fit(
    X_train,
    y_train,

    validation_data=(
        X_test,
        y_test
    ),

    epochs=100,

    batch_size=8,

    verbose=1
)


# ============================================================
# 8. EVALUATE MODEL
# ============================================================

loss, accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)


print("\n" + "=" * 50)
print("MODEL EVALUATION")
print("=" * 50)

print(f"Test loss: {loss:.4f}")
print(f"Test accuracy: {accuracy:.4f}")


# ============================================================
# 9. SAVE MODEL
# ============================================================

model.save(
    "model/resume_model.keras"
)


# ============================================================
# 10. SAVE TF-IDF VECTORIZER
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
# 11. SAVE LABEL ENCODER
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

print("model/resume_model.keras")
print("model/vectorizer.pkl")
print("model/encoder.pkl")

print("\nTraining completed.")