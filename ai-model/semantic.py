import json
import pickle

from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# LOAD VECTORIZER
# ============================================================

with open(
    "model/vectorizer.pkl",
    "rb"
) as file:

    vectorizer = pickle.load(file)


# ============================================================
# LOAD INTENTS
# ============================================================

with open(
    "data/intents.json",
    "r",
    encoding="utf-8"
) as file:

    data = json.load(file)


# ============================================================
# PREPARE PATTERNS
# ============================================================

patterns = []
pattern_intents = []


for intent in data["intents"]:

    for pattern in intent["patterns"]:

        patterns.append(
            pattern
        )

        pattern_intents.append(
            intent["tag"]
        )


# ============================================================
# CREATE TF-IDF EMBEDDINGS
# ============================================================

pattern_embeddings = vectorizer.transform(
    patterns
)


# ============================================================
# SEMANTIC PREDICTION
# ============================================================

def semantic_predict(question):

    # --------------------------------------------------------
    # Convert question to TF-IDF
    # --------------------------------------------------------

    query_embedding = vectorizer.transform(
        [question]
    )


    # --------------------------------------------------------
    # Calculate cosine similarity
    # --------------------------------------------------------

    similarities = cosine_similarity(
        query_embedding,
        pattern_embeddings
    )[0]


    # --------------------------------------------------------
    # Group scores by intent
    # --------------------------------------------------------

    intent_scores = {}


    for index, intent in enumerate(
        pattern_intents
    ):

        score = float(
            similarities[index]
        )


        if intent not in intent_scores:

            intent_scores[intent] = []


        intent_scores[intent].append(
            score
        )


    # --------------------------------------------------------
    # Calculate average + best score
    # --------------------------------------------------------

    ranked_intents = []


    for intent, scores in intent_scores.items():

        scores.sort(
            reverse=True
        )


        top_scores = scores[:3]


        average_score = (
            sum(top_scores)
            / len(top_scores)
        )


        best_score = top_scores[0]


        ranked_intents.append(
            (
                intent,
                average_score,
                best_score
            )
        )


    # --------------------------------------------------------
    # Sort intents
    # --------------------------------------------------------

    ranked_intents.sort(
        key=lambda x: x[1],
        reverse=True
    )


    # --------------------------------------------------------
    # Handle empty result
    # --------------------------------------------------------

    if not ranked_intents:

        return (
            "unknown",
            0.0,
            0.0,
            "unknown",
            0.0
        )


    # --------------------------------------------------------
    # Best intent
    # --------------------------------------------------------

    best = ranked_intents[0]


    # --------------------------------------------------------
    # Second intent
    # --------------------------------------------------------

    if len(ranked_intents) > 1:

        second = ranked_intents[1]

    else:

        second = (
            "unknown",
            0.0,
            0.0
        )


    # --------------------------------------------------------
    # UNKNOWN THRESHOLD
    # --------------------------------------------------------

    if best[1] < 0.20:

        return (
            "unknown",
            best[1],
            best[2],
            second[0],
            second[1]
        )


    return (
        best[0],
        best[1],
        best[2],
        second[0],
        second[1]
    )


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    print("=" * 60)

    print(
        "SEMANTIC INTENT TEST"
    )

    print("=" * 60)


    while True:

        question = input(
            "\nYou: "
        )


        if question.lower().strip() == "exit":

            break


        (
            intent,
            average_score,
            best_score,
            second_intent,
            second_score
        ) = semantic_predict(
            question
        )


        print(
            f"\nBest intent: {intent}"
        )


        print(
            f"Top-3 average: "
            f"{average_score:.2%}"
        )


        print(
            f"Best pattern: "
            f"{best_score:.2%}"
        )


        print(
            f"Second best: "
            f"{second_intent}"
        )


        print(
            f"Second average: "
            f"{second_score:.2%}"
        )