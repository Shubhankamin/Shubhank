class ConversationContext:

    def __init__(self):
        self.last_intent = None
        self.last_question = None
        self.last_answer = None
        self.last_topic = None


    # --------------------------------------------------------
    # UPDATE CONTEXT
    # --------------------------------------------------------

    def update(
        self,
        question,
        intent,
        answer,
        topic=None
    ):

        self.last_question = question
        self.last_intent = intent
        self.last_answer = answer

        # Always update the topic.
        # This also clears an old topic when topic=None.
        self.last_topic = topic


    # --------------------------------------------------------
    # GET CONTEXT
    # --------------------------------------------------------

    def get_context(self):

        return {
            "last_intent": self.last_intent,
            "last_question": self.last_question,
            "last_answer": self.last_answer,
            "last_topic": self.last_topic
        }


    # --------------------------------------------------------
    # CLEAR CONTEXT
    # --------------------------------------------------------

    def clear(self):

        self.last_intent = None
        self.last_question = None
        self.last_answer = None
        self.last_topic = None