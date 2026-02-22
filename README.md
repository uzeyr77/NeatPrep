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

## API key Required
This app uses the Google Gemini API. Google has a free tier which includes:
- 10 to 50 requests per minute depending on the model (e.i Gemini 2.5 flash)
- 250 - 1,500 RPD (requests per day)
- 250,000 - 1M TPM (tokens per minute)
**Note: the above API rate limits depend on the model**
**Get your free api key here: [Get Free Gemini API Key](https://aistudio.google.com/welcome?utm_source=PMAX&utm_medium=display&utm_campaign=Cloud-SS-DR-AIS-FY26-global-pmax-1713578&utm_content=pmax&gad_source=1&gad_campaignid=23417432327&gbraid=0AAAAACn9t65VhCnloy-FPiDiu_oAfNY9p&gclid=Cj0KCQiA7-rMBhCFARIsAKnLKtDyNxh0O9g1kYbvDVY8k06hHPS_jcI4C4QX-NoiIV29iZQDqIzjSDwaAihdEALw_wcB)**

## Usage
**1. Landing page: press Begin**
<img width="1797" height="981" alt="image" src="https://github.com/user-attachments/assets/303da5c5-b820-4c4c-b8e3-48ff410b5467" />
**
**2. Profile Setup: Enter the role you want to prepare for**
<img width="1914" height="986" alt="image" src="https://github.com/user-attachments/assets/84b87012-e0f9-458e-89e8-3f092b8dbac4" />
<img width="1917" height="999" alt="image" src="https://github.com/user-attachments/assets/4daafbfb-3482-45f2-ad55-44ae4cc7ae83" />
**3. Recieve 3 AI-Generated questions**



