from google import genai
from pydantic import BaseModel
import streamlit as st
# from google.genai import types
import json
client = genai.Client(api_key="***REMOVED***")
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
class FeedBackItem(BaseModel):
    strengths: str
    weaknesses: str
    improvement_plan: str
    model_answer: str
class UserFeedBack(BaseModel):
    feedback_1: FeedBackItem
    feedback_2: FeedBackItem
    feedback_3: FeedBackItem

def get_llm_questions(role_info:dict) -> dict: 
    
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents = f"""Act as if you are a Senior Technical Hiring Manager in the {role_info["industry"]} industry. Your goal is to evaluate a candidate applying for the {role_info["role"]} role with at the {role_info["level"]} level.
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
""",
        config = {
            "response_mime_type": "application/json",
            "response_schema": InterviewQuestions.model_json_schema(),
            
            }
    )
    llm_questions = json.loads(response.text)
    return llm_questions

def get_llm_feedback(user_answers:dict, role_info:dict) -> dict:
    
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents = f"""
        Assess the users interview answers for a {role_info["level"]} {role_info["role"]} in the {role_info["industry"]} sector. Explanation and tonality should be professional
        Output Guideline:
        - start immediately with the feedback
        - no introduction required
        - No conclusions or hiring decsisions
        - The feedback should be clear concise and not too wordy
        - Use first person pronouns
        - Should not be too convaluted, use proper spacing for explaining each guideline.
        TASK:
        Analyze the candidate's answers and provide constructive, high-fidelity feedback. Use your expertise to identify technical gaps, communication strengths, and industry-specific nuances.
        
        EVALUATION GUIDELINES (in this order for each of the users answers):
        1. Strengths: Highlight specific technical concepts or soft skills the user demonstrated correctly. Avoid generic praise; mention exactly which part of their logic was "Senior" or "Associate" level.
        2. Weaknesses: Identify where the user lacked depth, missed an edge case, or gave a shallow answer. For a {role_info["level"]} level, expect them to consider different tradeoffs.
        3. Improvement Plan: Provide 2-3 actionable steps (e.g., "Research the CAP theorem," or "Practice using the STAR method for architectural tradeoffs").
        4. Model Answer: Write the "Ideal Answer." This should be a sophisticated, 1-2 paragraph response that a top-tier candidate would give. It must include the specific {role_info["skills"]} mentioned and address the {role_info["industry"]} scenario
        
        Input Data:
        Questions: {llm_questions}
        Answer from user: {user_answers}
        
        Goal: Write 3 feedback sections, one for each of the users answer and make sure to highlight each of the evaluation guidelines so the individual gets a thorough understanding of where improvements should be made.
        
        Output ONLY valid JSON in this EXACT structure (no other text):
        {{
            "feedback_1": {{
                "strengths": "your detailed strengths analysis here",
                "weaknesses": "your detailed weaknesses analysis here", 
                "improvement_plan": "your 2-3 actionable steps here",
                "model_answer": "your 2-3 paragraph ideal answer here"
            }},
            "feedback_2": {{
                "strengths": "...",
                "weaknesses": "...",
                "improvement_plan": "...",
                "model_answer": "..."
            }},
            "feedback_3": {{
                "strengths": "...",
                "weaknesses": "...",
                "improvement_plan": "...",
                "model_answer": "..."
            }}
        }}
        
        """,  config = {
            "response_mime_type": "application/json",
            "response_schema": UserFeedBack.model_json_schema(),
            
            }
    )
    llm_feedback = json.loads(response.text)
    return llm_feedback



if __name__ == "__main__":    
    info_dict = {
        "role": "software developer",
        "level": "intern",
        "skills": "javascript, python, html, css",
        "industry": "fintech",
        "yoe": 0
    }
    user_answers = {
        "answer_1": "The first step before anything would be to go ahead and role back the last code that was pushed just incase it introduced new problems. The second step I would take is look at the classes that deal with the checkout system. What data structures and/or databases are beiing used to store and retrieve the data. Often times it could be optimized by using a different data structure or reviewing the algorithms to understand what is slowing things down.",
        "answer_2": "",
        "answer_3": ""
    }
    print(get_llm_feedback(user_answers,info_dict))
