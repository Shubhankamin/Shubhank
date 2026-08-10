import json

from predict import predict_intent
from semantic import semantic_predict
from conversation import ConversationContext
from context import detect_followup, detect_project


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
# DECISION ENGINE
# ============================================================

def decide(question, conversation):

    # ========================================================
    # GET CURRENT CONTEXT
    # ========================================================

    context = conversation.get_context()

    previous_intent = context["last_intent"]
    previous_topic = context.get("last_topic")


    # ========================================================
    # 1. CHECK FOR SPECIFIC PROJECT
    # ========================================================

    project_name = detect_project(question)


    if project_name:

        project_data = resume_data.get(
            "projects",
            {}
        )

        project_details = project_data.get(
            "project_details",
            {}
        )

        project_answer = project_details.get(
            project_name
        )


        if project_answer:

            conversation.update(
                question,
                "projects",
                project_answer,
                project_name
            )


            return {
                "answer": project_answer,
                "intent": "projects",

                "neural_intent": None,
                "neural_confidence": None,

                "semantic_intent": "projects",
                "semantic_score": 1.0,
                "semantic_best": "projects",

                "semantic_second": None,
                "semantic_second_score": 0.0,

                "semantic_margin": 1.0,

                "reason":
                    "Specific project identified from conversation"
            }


    # ========================================================
    # 2. CHECK FOR FOLLOW-UP
    # ========================================================

    followup_type = detect_followup(question)


    # ========================================================
    # 2A. SPECIFIC PROJECT FOLLOW-UP
    # ========================================================

    if (
        followup_type
        and previous_intent == "projects"
        and previous_topic
        and previous_topic in [
            "healthstream",
            "vehicle_servicing",
            "skin_saviour",
            "chat_on",
            "lost_found",
            "agri_mart",
            "fastmech"
        ]
    ):

        project_data = resume_data.get(
            "projects",
            {}
        )

        project_followups = project_data.get(
            "project_followups",
            {}
        )

        current_project = project_followups.get(
            previous_topic
        )


        if current_project:

            followup_answer = current_project.get(
                followup_type
            )


            if followup_answer:

                conversation.update(
                    question,
                    "projects",
                    followup_answer,
                    previous_topic
                )


                return {
                    "answer": followup_answer,
                    "intent": "projects",

                    "neural_intent": None,
                    "neural_confidence": None,

                    "semantic_intent": "projects",
                    "semantic_score": 1.0,
                    "semantic_best": "projects",

                    "semantic_second": None,
                    "semantic_second_score": 0.0,

                    "semantic_margin": 1.0,

                    "reason":
                        "Project follow-up resolved using project context"
                }


    # ========================================================
    # 2B. GENERIC PROJECT FOLLOW-UP
    # ========================================================

    if (
        followup_type
        and previous_intent == "projects"
    ):

        project_data = resume_data.get(
            "projects",
            {}
        )

        followup_answers = project_data.get(
            "followups",
            {}
        )

        followup_answer = followup_answers.get(
            followup_type
        )


        if followup_answer:

            topic = None


            if followup_type == "project_mobile":

                topic = "mobile_projects"


            elif followup_type == "project_technologies":

                topic = "project_technologies"


            elif followup_type == "project_details":

                topic = "project_details"


            conversation.update(
                question,
                "projects",
                followup_answer,
                topic
            )


            return {
                "answer": followup_answer,
                "intent": "projects",

                "neural_intent": None,
                "neural_confidence": None,

                "semantic_intent": "projects",
                "semantic_score": 1.0,
                "semantic_best": "projects",

                "semantic_second": None,
                "semantic_second_score": 0.0,

                "semantic_margin": 1.0,

                "reason":
                    "Follow-up question resolved using conversation context"
            }


    # ========================================================
    # 2C. GENERIC EXPERIENCE / INTERNSHIP FOLLOW-UP
    # ========================================================

    if (
        followup_type
        and previous_intent
        and previous_intent != "projects"
    ):

        previous_data = resume_data.get(
            previous_intent
        )


        if previous_data:

            followup_answers = previous_data.get(
                "followups",
                {}
            )

            followup_answer = followup_answers.get(
                followup_type
            )


            if followup_answer:

                conversation.update(
                    question,
                    previous_intent,
                    followup_answer,
                    previous_topic
                )


                return {
                    "answer": followup_answer,
                    "intent": previous_intent,

                    "neural_intent": None,
                    "neural_confidence": None,

                    "semantic_intent": previous_intent,
                    "semantic_score": 1.0,
                    "semantic_best": previous_intent,

                    "semantic_second": None,
                    "semantic_second_score": 0.0,

                    "semantic_margin": 1.0,

                    "reason":
                        "Follow-up question resolved using conversation context"
                }


    # ========================================================
    # 3. NORMAL ML PIPELINE
    # ========================================================

    neural_intent, neural_confidence = predict_intent(
        question
    )


    # ========================================================
    # SEMANTIC MODEL
    # ========================================================

    (
        semantic_intent,
        semantic_average,
        semantic_best,
        second_intent,
        second_average
    ) = semantic_predict(question)


    # ========================================================
    # SEMANTIC MARGIN
    # ========================================================

    semantic_margin = (
        semantic_average - second_average
    )


    # ========================================================
    # RULE 1 — VERY STRONG NEURAL PREDICTION
    # ========================================================

    if neural_confidence >= 0.85:

        final_intent = neural_intent

        reason = "Strong neural prediction"


    # ========================================================
    # RULE 2 — SEMANTIC MODEL SAYS UNKNOWN
    # ========================================================

    elif semantic_intent == "unknown":

        final_intent = "unknown"

        reason = "Semantic model detected unknown domain"


    # ========================================================
    # RULE 3 — STRONG SEMANTIC MATCH
    # ========================================================

    elif (
        semantic_average >= 0.65
        and semantic_margin >= 0.08
    ):

        final_intent = semantic_intent

        reason = "Strong semantic match"


    # ========================================================
    # RULE 4 — BOTH MODELS AGREE
    # ========================================================

    elif neural_intent == semantic_intent:

        final_intent = neural_intent

        reason = "Both models agree"


    # ========================================================
    # RULE 5 — LOW CONFIDENCE / DISAGREEMENT
    # ========================================================

    else:

        final_intent = "unknown"

        reason = (
            "Models disagree or confidence is too low"
        )


    # ========================================================
    # GENERATE RESPONSE
    # ========================================================

    if final_intent == "unknown":

        answer = (
            "I'm designed to answer questions about "
            "Shubhank's skills, experience, education, "
            "projects and professional background."
        )

    else:

        answer_data = resume_data.get(
            final_intent
        )


        if answer_data:

            answer = answer_data["answer"]

        else:

            answer = (
                "I don't have information about that yet."
            )


    # ========================================================
    # UPDATE CONVERSATION CONTEXT
    #
    # Normal ML responses do not have a specific topic.
    # This clears any previous project topic.
    # ========================================================

    conversation.update(
        question,
        final_intent,
        answer,
        None
    )


    # ========================================================
    # RETURN RESULT
    # ========================================================

    return {
        "answer": answer,
        "intent": final_intent,

        "neural_intent": neural_intent,
        "neural_confidence": neural_confidence,

        "semantic_intent": semantic_intent,
        "semantic_score": semantic_average,
        "semantic_best": semantic_best,

        "semantic_second": second_intent,
        "semantic_second_score": second_average,

        "semantic_margin": semantic_margin,

        "reason": reason
    }


# ============================================================
# LOCAL TEST CHAT
# ============================================================

if __name__ == "__main__":

    # Create ONE context for this terminal session
    conversation = ConversationContext()


    print("=" * 60)
    print("              SHUBHANK AI")
    print("          RESUME ASSISTANT")
    print("=" * 60)

    print("\nAsk me something about Shubhank.")
    print("Type 'exit' to stop.\n")


    while True:

        question = input("You: ").strip()


        if question.lower() == "exit":

            print("\nAI: Goodbye!")
            break


        if not question:

            continue


        result = decide(
            question,
            conversation
        )


        print(
            f"\nAI: {result['answer']}\n"
        )