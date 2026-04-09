def build_prompt(resume, job_description):
    return f"""
    You are an AI HR assistant.

    Analyze the resume against the job description.

    Resume:
    {resume}

    Job Description:
    {job_description}

    Give:
    1. Match Percentage
    2. Missing Skills
    3. Improvement Suggestions
    """