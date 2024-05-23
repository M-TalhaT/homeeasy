import openai
import logging

openai.api_key = 'sk-proj-2iPdPbGsTKBzJU2qtuZTT3BlbkFJIqBLHeLuRdEmiC4eMpDr'  # Set your OpenAI API key here

def get_llm_feedback(prompt: str) -> str:
    try:
        messages = [
            {"role": "user", "content": "As a Sales Data Analyzer, provide feedback and actionable insights based on the provided sales data."},
            {"role": "user", "content": prompt}
        ]
        
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        
        feedback = completion.choices[0].message['content'].strip()
        logging.info(f"LLM response: {feedback}")
        return feedback

    except openai.error.OpenAIError as e:
        logging.exception(f"Error generating feedback: {str(e)}")
        if "quota" in str(e).lower():
            return "Error generating feedback: You have exceeded your current OpenAI API quota. Please check your plan and billing details."
        else:
            return f"Error generating feedback: {str(e)}"
