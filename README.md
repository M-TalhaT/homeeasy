Note: Couldnt get access to paid version of chat gpt as whenever i used the API key it kept saying quota limit succedded. I tried other LLMs like Claude Ai, Awan LLm but none of these were free and required paid tokens to use their API
Other than this the code according to me should run fine if we a have a paid Chat gpt APi key
Implemented Error and exception handling techniques in most places 
Framewrok we haved used here is FastApi 
WE can install required packges using this command
pip install fastapi uvicorn pandas openai 
Remember to place APi key as git didnt allow to push the code with my own APi key for security
Start the project using this command uvicorn app.main:app --reload
To test first API use GET http://127.0.0.1:8000/api/rep_performance?rep_id=183
for 2nd API use GET http://127.0.0.1:8000/api/team_performance
3rd api use GET http://127.0.0.1:8000/api/performance_trends?time_period=monthly or quarterly


CODE EXplanantion:
First we created routers for each API which is a great feature of FastAPI network
Then for our First APi the parameter rep_id takes the ID of the employee we wnat to check, rep_data.to_dict() this is used to convert our panda dataframe into dictionary whihc can be easily passed toa LLM

For the Team performance code @router.get("/api/team_performance") is called a decorator whihc defines a new GET endpoint. {df.to_dict()} is used again as this dictionary contains all the sales data. The function return {"team_performance": feedback} returns a JSON response containing a generated feedback under the key team_performance.

For Performance Trends code load_sales_data is is responsible for loading the sales data, get_llm_feedback is imported from the services.llm_analysis module and is used to generate feedback using a LLM. Rest of code is smilar to previous one except for the if else statements who depending on the value of time_period the sales data is filtered to include only the relevant data for the specified time period. like monthly or quaterly.

Now for LLm_analysis.py this code here contains the actual LLm integration part where prompts are passed and LLms models are defined. def get_llm_feedback(prompt: str) -> str: take a string parameter prompt. The messages Constructs a list of messages to send to the OpenAI API. The first message sets the context by stating the role of the AI as Sales Data Analyzer and what it should do . The second message contains the actual sales data prompt provided by the user. Then below this part of code we we make a Api call to Open AI and specify the GPT model 3.5 turbo. Feedback in the code extracts the feedback text from the API response and as the response contains a list of choices and the text of the first choice is accessed and eliminates any leading or trailing whitespace
