# NeatPrep
## 1. Project Overview
NeatPrep AI powered interview preperation tool that generates personalized technical interview questions. These questions are based on the specifications from the user and once answered the AI provides feedback on how they performed. Useful for job seekers to prepare for interviews with role specific questions that focus on real-world scenarios.

## 2. Key Features
- Personalized questions generated based on user specifics (e.i role, level, yoe etc.)
- Detailed AI feedback with strengths, Weaknesses, and Model Answers
- Clean and intuitive UI built with streamlit

## 3. Stages
1. Information Collection: The user is promted for details about the position they would like to prepare for. 
- What is the position?
- What role exactly?
- How many years of experience are required?
- What skills are needed?
- The company and/or industry can be provided for individuals that would like more specific questions
2. Question Generation: Based on the information provide by the user, **Google Gemini AI** generates 3 questions that model real-world problems that are faced in the position the individual specified.
3. Answering: The user then answers the questions to the best of their ability with the clean and interactive UI built with **Streamlit**
4. Feedback Generation: Finally, when the user is done answering the questions they get feedback from **Gemini AI** that explains the strengths and weaknesses of the answer, as well as what the ideal answer would look like

