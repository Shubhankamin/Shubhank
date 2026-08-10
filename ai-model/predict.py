import json
import pickle
import numpy as np

from tensorflow.keras.models import load_model


# ============================================================
# LOAD MODEL
# ============================================================

model = load_model("model/resume_model.keras")


# ============================================================
# LOAD VECTORIZER
# ============================================================

with open("model/vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)


# ============================================================
# LOAD LABEL ENCODER
# ============================================================

with open("model/encoder.pkl", "rb") as file:
    encoder = pickle.load(file)


# ============================================================
# LOAD RESUME DATA
# ============================================================

with open(
    "data/resume_data.json",
    "r",
    encoding="utf-8"
) as file:

    resume_data = json.load(file)


# ============================================================
# PREDICT INTENT
# ============================================================

def predict_intent(question):

    # Convert text to TF-IDF vector
    X = vectorizer.transform(
        [question]
    ).toarray()

    # Neural network prediction
    probabilities = model.predict(
        X,
        verbose=0
    )[0]

    # Highest probability
    index = np.argmax(probabilities)

    intent = encoder.inverse_transform(
        [index]
    )[0]

    confidence = float(
        probabilities[index]
    )

    return intent, confidence


# ============================================================
# GENERATE RESPONSE
# ============================================================

def generate_response(question):

    intent, confidence = predict_intent(question)

    # --------------------------------------------------------
    # UNKNOWN INTENT
    # --------------------------------------------------------

    if intent == "unknown":

        return (
            "I'm designed to answer questions about "
            "Shubhank's skills, experience, education, "
            "projects and professional background."
        ), intent, confidence


    # --------------------------------------------------------
    # LOW CONFIDENCE
    # --------------------------------------------------------

    if confidence < 0.60:

        return (
            "I'm not confident enough to answer that. "
            "Try asking about Shubhank's skills, experience, "
            "education, projects or technologies."
        ), intent, confidence


    # --------------------------------------------------------
    # FIND RESUME ANSWER
    # --------------------------------------------------------

    answer_data = resume_data.get(intent)

    if answer_data is None:

        return (
            "I don't have information about that yet."
        ), intent, confidence


    return (
        answer_data["answer"],
        intent,
        confidence
    )
# ============================================================
# CHAT
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("              SHUBHANK AI")
    print("          RESUME ASSISTANT")
    print("=" * 60)

    print("\nAsk me something about Shubhank.")
    print("Type 'exit' to stop.\n")

    while True:

        question = input("You: ")

        if question.lower().strip() == "exit":

            print("\nAI: Goodbye!")
            break

        answer, intent, confidence = generate_response(
            question
        )

        print(
            f"\nAI: {answer}"
        )

        print(
            f"\n[Intent: {intent} | "
            f"Confidence: {confidence:.2%}]\n"
        )