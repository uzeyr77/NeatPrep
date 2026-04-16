# NeatPrep
NeatPrep AI powered interview preperation tool that generates personalized technical interview questions. These questions are based on the specifications from the user and once answered the AI provides feedback on how they performed. Useful for job seekers to prepare for interviews with role specific questions that focus on real-world scenarios.

## 1. Key Features
- Personalized questions generated based on user specifics (e.i role, level, yoe etc.)
- Detailed AI feedback with strengths, Weaknesses, and Model Answers
- Clean and intuitive UI built with streamlit

## 2. Stages
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
<img width="1917" height="997" alt="image" src="https://github.com/user-attachments/assets/5449db85-e4ff-4335-a4ed-f07548cbc56c" />
**
**2. Profile Setup: Enter the role you want to prepare for**
<img width="1919" height="989" alt="Screenshot 2026-02-26 221724" src="https://github.com/user-attachments/assets/7e100138-f548-47d4-a610-d0ccde8a4047" />
**3. Prep: Answer 3 AI-Generated questions**
<img width="1916" height="995" alt="image" src="https://github.com/user-attachments/assets/c27d05c4-449f-4c8f-a105-b723b42e6347" />
**4. Feedback: Recieve Tailored feedback for eaach question**
<img width="1914" height="987" alt="image" src="https://github.com/user-attachments/assets/9874643a-8ee3-480e-b16c-94604f618531" />

## Setup 

### Prerequisites
- Python 3.8+
- Google Gemini API key

### Installation
1. Clone the repository
```bash
git clone https://github.com/uzeyr77/interview-prep-app.git
cd interview-prep-app
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Set up your API key
Create a `.env` file in the root directory:
```
GEMINI_API_KEY=your_api_key_here
```
Or set it as an environment variable:
```bash
export GEMINI_API_KEY=your_api_key_here
```
4. Run the app
Running the command below should open the app in your default browser
```bash
streamlit run app.py
```




