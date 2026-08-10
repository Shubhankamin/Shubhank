# ============================================================
# CONVERSATION / FOLLOW-UP DETECTOR
# ============================================================


def detect_followup(question):

    question = question.lower().strip()


    # ========================================================
    # SPECIFIC PROJECT TECHNOLOGIES
    # ========================================================

    specific_project_technologies = [
        "what technologies did you use for it",
        "what technologies did you use in it",
        "which technologies did you use for it",
        "which technologies did you use in it",
        "what tech stack did you use for it",
        "what tech stack did you use",
        "what tools did you use for it",
        "which tools did you use for it",
        "what technologies were used for it",
        "what technologies were used in it",
    ]

    for pattern in specific_project_technologies:

        if pattern in question:
            return "specific_project_technologies"


    # ========================================================
    # SPECIFIC PROJECT FEATURES
    # ========================================================

    specific_project_features = [
        "what features does it have",
        "what features does the project have",
        "what are its features",
        "what features are included",
        "what features does the app have",
        "what features does the application have",
        "what can it do",
        "what does it do",
    ]

    for pattern in specific_project_features:

        if pattern in question:
            return "specific_project_features"


    # ========================================================
    # SPECIFIC PROJECT WORKFLOW
    # ========================================================

    specific_project_workflow = [
        "how does it work",
        "how does the project work",
        "how did it work",
        "how does the application work",
        "how does the app work",
        "how did the application work",
        "how did the app work",
    ]

    for pattern in specific_project_workflow:

        if pattern in question:
            return "specific_project_workflow"


    # ========================================================
    # PROJECT MOBILE
    # ========================================================

    project_mobile = [
        "which one was a mobile app",
        "which one was mobile",
        "which project was a mobile app",
        "which project was mobile",
        "which projects were mobile",
        "what mobile applications have you built",
        "what mobile apps have you built",
    ]

    for pattern in project_mobile:

        if pattern in question:
            return "project_mobile"


    # ========================================================
    # PROJECT TECHNOLOGIES
    # ========================================================

    project_technology = [
        "what technologies did you use for that project",
        "what technologies did you use for the project",
        "which technologies did you use for that project",
        "which technologies did you use for the project",
        "what technologies were used in that project",
        "what technologies were used for that project",
        "what tech stack did you use for that project",
        "which tech stack did you use for that project",
        "what tools did you use for that project",
    ]

    for pattern in project_technology:

        if pattern in question:
            return "project_technologies"


    # ========================================================
    # PROJECT DETAILS
    # ========================================================

    project_details = [
        "tell me more about that project",
        "tell me more about the project",
        "tell me about that project",
        "what was that project about",
        "what was the project about",
        "can you explain that project",
        "can you explain the project",
        "how did that project work",
    ]

    for pattern in project_details:

        if pattern in question:
            return "project_details"


    # ========================================================
    # EXPERIENCE / INTERNSHIP FOLLOW-UP
    # ========================================================

    what_did_you_do = [
        "what did you do there",
        "what did you do",
        "what was your role",
        "what was your role there",
        "what were your responsibilities",
        "what responsibilities did you have",
        "what did you work on there",
        "what work did you do there",
    ]

    for pattern in what_did_you_do:

        if pattern in question:
            return "what_did_you_do"


    # ========================================================
    # TECHNOLOGIES USED THERE
    # ========================================================

    technologies = [
        "what technologies did you use there",
        "what technologies did you use",
        "which technologies did you use there",
        "which technologies did you use",
        "what tools did you use there",
        "what tools did you use",
    ]

    for pattern in technologies:

        if pattern in question:
            return "technologies"


    # ========================================================
    # ROLE
    # ========================================================

    role = [
        "what was your position there",
        "what position did you have there",
        "what was your job there",
        "what role did you have",
    ]

    for pattern in role:

        if pattern in question:
            return "role"


    return None


# ============================================================
# SPECIFIC PROJECT DETECTOR
# ============================================================

def detect_project(question):

    question = question.lower().strip()


    # --------------------------------------------------------
    # HEALTHSTREAM
    # --------------------------------------------------------

    if "healthstream" in question:

        return "healthstream"


    # --------------------------------------------------------
    # VEHICLE SERVICING
    # --------------------------------------------------------

    if (
        "vehicle servicing" in question
        or "vehicle service" in question
    ):

        return "vehicle_servicing"


    # --------------------------------------------------------
    # SKIN SAVIOUR
    # --------------------------------------------------------

    if (
        "skin saviour" in question
        or "skin savior" in question
    ):

        return "skin_saviour"


    # --------------------------------------------------------
    # CHAT ON
    # --------------------------------------------------------

    if "chat on" in question:

        return "chat_on"


    # --------------------------------------------------------
    # LOST AND FOUND
    # --------------------------------------------------------

    if (
        "lost and found" in question
        or "lost & found" in question
    ):

        return "lost_found"


    # --------------------------------------------------------
    # AGRI MART
    # --------------------------------------------------------

    if (
        "agri mart" in question
        or "agri-mart" in question
    ):

        return "agri_mart"


    # --------------------------------------------------------
    # FASTMECH
    # --------------------------------------------------------

    if "fastmech" in question:

        return "fastmech"


    return None