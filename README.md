Note: Couldnt get access to paid version of chat gpt as whenever i used the API it kept saying quota limit succedded. I tried other LLMs like Claude Ai, Awan LLm but none of these were free and required paid tokens to use their API
Other than this the code according to me should run fine if we a have a paid Chat gpt APi key
Framewrok we haved used here is FastApi 
WE can install required packges using this command
pip install fastapi uvicorn pandas openai 
Remember to place APi key as git didnt allow to push the code with my own APi key for security
Start the project using this command uvicorn app.main:app --reload
to test first API use GET http://127.0.0.1:8000/api/rep_performance?rep_id=183
for 2nd API use GET http://127.0.0.1:8000/api/team_performance
3rd api use GET http://127.0.0.1:8000/api/performance_trends?time_period=monthly or quarterly

