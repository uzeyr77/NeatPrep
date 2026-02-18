"""
Prompt templates for AI interview question and feedback generation.
Feel free to customize for your needs.
"""



QUESTION_GENERATION_PROMPT = """Act as if you are a Senior Technical Hiring Manager in the {industry} industry. Your goal is to evaluate a candidate applying for the {role} role with at the {level} level.
Core Evaluation Critera:
- focus on these core skills that are required for the role: {role}
- ensure the questions are appropriate for someone with {yoe} years of experience
- Match the complexity of the scenario to a {level} level of responsibility.

Question Guidelines:
1. Start each question with a description of a real world scenario/obstacle. This scenario must be a specific, high-stakes situation common in the industry specified (e.g., a service outage during peak hours, a security audit, or a complex feature migration). This situation should also have a clear solution that the candidate should know based on the skills, yoe, and industry facts.
2. The scenario must provide enough technical context to feel like a genuine whiteboard discussion.
3. Follow the scenario with a "Strategic Inquiry." This should ask the candidate to explain their "how" and "why." 
4. DO NOT ask for code. Focus on architectural decisions, debugging logic, or project management methodology.
GOAL: 
Write 3 distinct questions. Each must be a mini-case study that tests if the candidate has actually performed this role in {industry} or if they have only memorized definitions. The questions should be clear with the answer being one that can be explained in some sentences or bullet points.
"""

FEEDBACK_GENERATION_PROMPT = """
        Assess the users interview answers for a {level} {role} in the {industry} sector. Explanation and tonality should be professional
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
        2. Weaknesses: Identify where the user lacked depth, missed an edge case, or gave a shallow answer. For a {level} level, expect them to consider different tradeoffs.
        3. Improvement Plan: Provide 2-3 actionable steps (e.g., "Research the CAP theorem," or "Practice using the STAR method for architectural tradeoffs").
        4. Model Answer: Write the "Ideal Answer." This should be a sophisticated, 1-2 paragraph response that a top-tier candidate would give. It must include the specific {skills} mentioned and address the {industry} scenario
        
        Input Data:
        Questions: {llm_question}
        Answer from user: {user_answer}
        
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
        
        """