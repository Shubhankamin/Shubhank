import json
import pickle
import numpy as np


# ============================================================
# LOAD CLASSIFIER
# ============================================================

with open(
    "model/resume_model.pkl",
    "rb"
) as file:

    model = pickle.load(file)


# ============================================================
# LOAD VECTORIZER
# ============================================================

with open(
    "model/vectorizer.pkl",
    "rb"
) as file:

    vectorizer = pickle.load(file)


# ============================================================
# LOAD LABEL ENCODER
# ============================================================

with open(
    "model/encoder.pkl",
    "rb"
) as file:

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

    # Convert question to TF-IDF

    X = vectorizer.transform(
        [question]
    )


    # Get probabilities

    probabilities = model.predict_proba(
        X
    )[0]


    # Highest probability

    index = np.argmax(
        probabilities
    )


    # Convert index → intent

    intent = encoder.inverse_transform(
        [index]
    )[0]


    confidence = float(
        probabilities[index]
    )


    return (
        intent,
        confidence
    )


# ============================================================
# GENERATE RESPONSE
# ============================================================

def generate_response(question):

    intent, confidence = predict_intent(
        question
    )


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
    # FIND RESUME ANSWER
    # --------------------------------------------------------

    answer_data = resume_data.get(
        intent
    )


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
# TEST CHAT
# ============================================================

if __name__ == "__main__":

    print("=" * 60)

    print(
        "              SHUBHANK AI"
    )

    print(
        "          RESUME ASSISTANT"
    )

    print("=" * 60)

    print(
        "\nAsk me something about Shubhank."
    )

    print(
        "Type 'exit' to stop.\n"
    )


    while True:

        question = input(
            "You: "
        )


        if question.lower().strip() == "exit":

            print(
                "\nAI: Goodbye!"
            )

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