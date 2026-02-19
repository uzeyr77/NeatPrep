from dotenv import load_dotenv
import os
from google import genai
from pydantic import BaseModel
from services.prompts import QUESTION_GENERATION_PROMPT, FEEDBACK_GENERATION_PROMPT
import streamlit as st
# from google.genai import types
import json
client = genai.Client(os.getenv("GEMINI_API_KEY"))
llm_questions: str = ""
llm_feedback: str = ""
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
    prompt = QUESTION_GENERATION_PROMPT.format(
        role = role_info["role"],
        level = role_info["level"],
        yoe = role_info["yoe"],
        skills = role_info["skills"],
        # company = role_info["company"],
        industry = role_info["industry"]
    )
    
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents = prompt,
        config = {
            "response_mime_type": "application/json",
            "response_schema": InterviewQuestions.model_json_schema(),
            
            }
    )
    llm_questions = json.loads(response.text)
    return llm_questions

def get_llm_feedback(user_answers:dict, role_info:dict) -> dict:
    prompt = FEEDBACK_GENERATION_PROMPT.format(
        role = role_info["role"],
        level = role_info["level"],
        yoe = role_info["yoe"],
        skills = role_info["skills"],
        industry = role_info["industry"],
        llm_question = llm_questions,
        user_answer = user_answers
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents = prompt,
        config = {
            "response_mime_type": "application/json",
            "response_schema": UserFeedBack.model_json_schema(),
            
            }
    )
    llm_feedback = json.loads(response.text)
    return llm_feedback

