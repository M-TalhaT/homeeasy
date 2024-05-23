# app/routers/rep_performance.py

from fastapi import APIRouter, Query
from services.llm_analysis import get_llm_feedback
from services.data_ingestion import load_sales_data
import logging

router = APIRouter()

@router.get("/api/rep_performance")
def rep_performance(rep_id: int = Query(...)):
    try:

        df = load_sales_data('data/sales_data.csv')
        logging.info(f"Data loaded successfully. Data shape: {df.shape}")
        rep_data = df[df['employee_id'] == rep_id]
        logging.info(f"Filtered data for rep_id {rep_id}. Data shape: {rep_data.shape}")
        
        if rep_data.empty:
            logging.error(f"Representative {rep_id} not found.")
            return {"error": "Representative not found"}
        
        prompt = f"Analyze the following sales data for representative {rep_id}: {rep_data.to_dict()}"
        logging.info(f"Prompt for LLM: {prompt}")
        
        feedback = get_llm_feedback(prompt)
        logging.info(f"Feedback received: {feedback}")
        
        if "Error generating feedback" in feedback:
            return {"error": feedback}

        return {"rep_id": rep_id, "feedback": feedback}
    except Exception as e:
        logging.exception(f"Error in rep_performance endpoint: {str(e)}")
        return {"detail": f"Internal Server Error: {str(e)}"}
