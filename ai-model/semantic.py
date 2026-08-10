import json

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# LOAD EMBEDDING MODEL
# ============================================================

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


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

        patterns.append(pattern)

        pattern_intents.append(
            intent["tag"]
        )


# ============================================================
# CREATE EMBEDDINGS FOR EACH PATTERN
# ============================================================

pattern_embeddings = embedding_model.encode(
    patterns,
    normalize_embeddings=True
)


# ============================================================
# SEMANTIC PREDICTION
# ============================================================

def semantic_predict(question):

    query_embedding = embedding_model.encode(
        [question],
        normalize_embeddings=True
    )

    similarities = cosine_similarity(
        query_embedding,
        pattern_embeddings
    )[0]


    # --------------------------------------------------------
    # Group similarities by intent
    # --------------------------------------------------------

    intent_scores = {}


    for index, intent in enumerate(pattern_intents):

        score = float(
            similarities[index]
        )

        if intent not in intent_scores:

            intent_scores[intent] = []

        intent_scores[intent].append(score)


    # --------------------------------------------------------
    # Take best 3 matches for every intent
    # --------------------------------------------------------

    ranked_intents = []


    for intent, scores in intent_scores.items():

        scores.sort(reverse=True)

        top_scores = scores[:3]

        average_score = sum(top_scores) / len(top_scores)

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


    best = ranked_intents[0]

    second = ranked_intents[1]


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

        question = input("\nYou: ")


        if question.lower().strip() == "exit":

            break


        (
            intent,
            average_score,
            best_score,
            second_intent,
            second_score
        ) = semantic_predict(question)


        print(
            f"\nBest intent: {intent}"
        )

        print(
            f"Top-3 average: {average_score:.2%}"
        )

        print(
            f"Best pattern: {best_score:.2%}"
        )

        print(
            f"Second best: {second_intent}"
        )

        print(
            f"Second average: {second_score:.2%}"
        )