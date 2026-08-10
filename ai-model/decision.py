import json

from predict import predict_intent
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
# PROJECT NAMES
# ============================================================

PROJECT_NAMES = [
    "healthstream",
    "vehicle_servicing",
    "skin_saviour",
    "chat_on",
    "lost_found",
    "agri_mart",
    "fastmech"
]


# ============================================================
# GENERIC UNKNOWN RESPONSE
# ============================================================

UNKNOWN_ANSWER = (
    "I'm designed to answer questions about "
    "Shubhank's skills, experience, education, "
    "projects and professional background."
)


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
    #
    # Example:
    #
    # Tell me about HealthStream
    # Tell me about Vehicle Servicing
    # Tell me about Chat On
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

                "semantic_intent": None,
                "semantic_score": None,
                "semantic_best": None,

                "semantic_second": None,
                "semantic_second_score": None,

                "semantic_margin": None,

                "reason":
                    "Specific project identified from conversation"
            }


    # ========================================================
    # 2. CHECK FOR FOLLOW-UP
    # ========================================================

    followup_type = detect_followup(question)


    # ========================================================
    # 2A. SPECIFIC PROJECT FOLLOW-UP
    #
    # Example:
    #
    # Tell me about HealthStream
    #
    # What features does it have?
    #
    # What technologies did you use for it?
    # ========================================================

    if (
        followup_type
        and previous_intent == "projects"
        and previous_topic
        and previous_topic in PROJECT_NAMES
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

                    "semantic_intent": None,
                    "semantic_score": None,
                    "semantic_best": None,

                    "semantic_second": None,
                    "semantic_second_score": None,

                    "semantic_margin": None,

                    "reason":
                        "Project follow-up resolved using project context"
                }


    # ========================================================
    # 2B. GENERIC PROJECT FOLLOW-UP
    #
    # Example:
    #
    # What projects have you built?
    #
    # Which one was a mobile app?
    #
    # What technologies did you use?
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

                "semantic_intent": None,
                "semantic_score": None,
                "semantic_best": None,

                "semantic_second": None,
                "semantic_second_score": None,

                "semantic_margin": None,

                "reason":
                    "Follow-up question resolved using conversation context"
            }


    # ========================================================
    # 2C. GENERIC EXPERIENCE / INTERNSHIP FOLLOW-UP
    #
    # Example:
    #
    # Where have you worked before?
    #
    # What did you do there?
    #
    # What technologies did you use there?
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

                    "semantic_intent": None,
                    "semantic_score": None,
                    "semantic_best": None,

                    "semantic_second": None,
                    "semantic_second_score": None,

                    "semantic_margin": None,

                    "reason":
                        "Follow-up question resolved using conversation context"
                }


    # ========================================================
    # 3. NORMAL LIGHTWEIGHT ML PIPELINE
    #
    # No Sentence Transformers.
    # No TensorFlow.
    # No PyTorch.
    #
    # Uses the lightweight classifier from predict.py.
    # ========================================================

    neural_intent, neural_confidence = predict_intent(
        question
    )


    # ========================================================
    # 4. CLASSIFIER DECISION
    # ========================================================

    if neural_intent == "unknown":

        final_intent = "unknown"

        reason = "Classifier detected unknown domain"


    elif neural_confidence >= 0.15:

        final_intent = neural_intent

        reason = "Lightweight classifier prediction"


    else:

        final_intent = "unknown"

        reason = "Classifier confidence is too low"


    # ========================================================
    # 5. GENERATE RESPONSE
    # ========================================================

    if final_intent == "unknown":

        answer = UNKNOWN_ANSWER


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
    # 6. UPDATE CONVERSATION CONTEXT
    #
    # Normal ML questions do not have a specific topic.
    # Therefore topic is cleared.
    # ========================================================

    conversation.update(
        question,
        final_intent,
        answer,
        None
    )


    # ========================================================
    # 7. RETURN RESULT
    # ========================================================

    return {

        "answer": answer,

        "intent": final_intent,

        "neural_intent": neural_intent,

        "neural_confidence": neural_confidence,

        "semantic_intent": None,

        "semantic_score": None,

        "semantic_best": None,

        "semantic_second": None,

        "semantic_second_score": None,

        "semantic_margin": None,

        "reason": reason
    }


# ============================================================
# LOCAL TEST CHAT
# ============================================================

if __name__ == "__main__":

    # --------------------------------------------------------
    # Create one conversation context for this terminal session
    # --------------------------------------------------------

    conversation = ConversationContext()


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


    # ========================================================
    # CHAT LOOP
    # ========================================================

    while True:

        question = input(
            "You: "
        ).strip()


        # ----------------------------------------------------
        # EXIT
        # ----------------------------------------------------

        if question.lower() == "exit":

            print(
                "\nAI: Goodbye!"
            )

            break


        # ----------------------------------------------------
        # EMPTY INPUT
        # ----------------------------------------------------

        if not question:

            continue


        # ----------------------------------------------------
        # DECISION ENGINE
        # ----------------------------------------------------

        result = decide(
            question,
            conversation
        )


        # ----------------------------------------------------
        # ANSWER
        # ----------------------------------------------------

        print(
            f"\nAI: {result['answer']}\n"
        )


        # ----------------------------------------------------
        # MODEL ANALYSIS
        # ----------------------------------------------------

        print(
            "---------------- MODEL ANALYSIS ----------------"
        )


        print(
            f"Classifier intent: "
            f"{result['neural_intent']}"
        )


        if result["neural_confidence"] is not None:

            print(
                f"Classifier confidence: "
                f"{result['neural_confidence']:.2%}"
            )

        else:

            print(
                "Classifier confidence: "
                "Not used"
            )


        print(
            f"Final intent: "
            f"{result['intent']}"
        )


        print(
            f"Decision: "
            f"{result['reason']}"
        )


        # ----------------------------------------------------
        # CONVERSATION CONTEXT
        # ----------------------------------------------------

        context = conversation.get_context()


        print(
            "\n---------------- CONVERSATION CONTEXT ----------------"
        )


        print(
            f"Last question: "
            f"{context['last_question']}"
        )


        print(
            f"Last intent: "
            f"{context['last_intent']}"
        )


        print(
            f"Last topic: "
            f"{context.get('last_topic')}"
        )


        print(
            f"Last answer: "
            f"{context['last_answer']}"
        )


        print(
            "--------------------------------------------------------"
        )