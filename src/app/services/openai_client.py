from openai import OpenAI
import json
from pydantic import BaseModel
import os

client = OpenAI(api_key="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")

llm_questions: str = ""
llm_feedback: str = ""
interview_question_prompt: str = """Act as if you are a Senior Technical Hiring Manager in the industry specified. Your goal is to evaluate a candidate applying for the role with the specific level. This information is provided in a dictionary.
Core Evaluation Critera:
- focus on the skills that are included for the role
- ensure the questions are appropriate for someone with the given number of years of experience
- Prioritize "Systems Thinking": How the candidate handles trade-offs, scalability, and edge cases within their industry on interest

Question Guidelines:
1. Start each question with a "Real-World Scenario." This scenario must be a specific, high-stakes situation common in the industry (e.g., a service outage during peak hours, a security audit, or a complex feature migration).
2. The scenario must provide enough technical context to feel like a genuine whiteboard discussion.
3. Follow the scenario with a "Strategic Inquiry." This should ask the candidate to explain their "how" and "why." 
4. DO NOT ask for code. Focus on architectural decisions, debugging logic, or project management methodology.

GOAL: 
Write 3 distinct questions. Each must be a mini-case study that tests if the candidate has actually performed this role in [industry] or if they have only memorized definitions. The questions should be clear with the answer being one that can be explained in some sentences or bullet points.
"""

class InterviewQuestions(BaseModel):
    question_1: str
    question_2: str
    question_3: str

class UserFeedBack(BaseModel):
    feedback_1: str
    feedback_2: str
    feedback_3: str

def get_llm_questions(role_info:dict) -> dict:
        
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages = [
            {
                "role": "system",
                "content": f"""Act as if you are a Senior Technical Hiring Manager in the {role_info["industry"]} industry. Your goal is to evaluate a candidate applying for the {role_info["role"]} role with at the {role_info["level"]} level.
Core Evaluation Critera:
- focus on these core skills that are required for the role: {role_info["skills"]}
- ensure the questions are appropriate for someone with {role_info["yoe"]} years of experience
- Match the complexity of the scenario to a {role_info["level"]} level of responsibility.

Question Guidelines:
1. Start each question with a description of a real world scenario/obstacle. This scenario must be a specific, high-stakes situation common in the industry specified (e.g., a service outage during peak hours, a security audit, or a complex feature migration). This situation should also have a clear solution that the candidate should know based on the skills, yoe, and industry facts.
2. The scenario must provide enough technical context to feel like a genuine whiteboard discussion.
3. Follow the scenario with a "Strategic Inquiry." This should ask the candidate to explain their "how" and "why." 
4. DO NOT ask for code. Focus on architectural decisions, debugging logic, or project management methodology.

GOAL: 
Write 3 distinct questions. Each must be a mini-case study that tests if the candidate has actually performed this role in {role_info["industry"]} or if they have only memorized definitions. The questions should be clear with the answer being one that can be explained in some sentences or bullet points.
"""
            }
        ],
        response_format = {
            "type": "json_format",
            "json_schema": {
                "name": "user_feedback",
                "strict": True,
                "schema": InterviewQuestions.model_json_schema()
            }
        },
        temperature= 0.7
    )
    
    llm_feedback = json.loads(response.choices[0].message.content)
    return llm_feedback

def main():
    info_dict = {
        "role": "software developer",
        "level": "intern",
        "skills": "javascript, python, html, css",
        "industry": "fintech",
        "yoe": 0
    }
    print(get_llm_questions(info_dict))
    # print(get_llm_questions())

if __name__ == "__main__":
    main()