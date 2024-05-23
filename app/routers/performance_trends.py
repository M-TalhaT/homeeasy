# app/routers/performance_trends.py

from fastapi import APIRouter, Query, HTTPException
from services.data_ingestion import load_sales_data
from services.llm_analysis import get_llm_feedback
import pandas as pd

router = APIRouter()

@router.get("/api/performance_trends")
def performance_trends(time_period: str = Query(..., description="The time period for analyzing performance trends, e.g., monthly, quarterly")):
    # Load data
    df = load_sales_data('data/sales_data.csv')
    
    # Validate and process the time period
    if time_period == "monthly":
        df['period'] = df['dated'].dt.to_period('M')
    elif time_period == "quarterly":
        df['period'] = df['dated'].dt.to_period('Q')
    else:
        raise HTTPException(status_code=400, detail="Invalid time period specified. Please use 'monthly' or 'quarterly'.")

    # Group by the time period and calculate performance metrics
    trend_data = df.groupby('period').agg({
        'revenue_confirmed': 'sum',
        'applications': 'sum',
        'tours_booked': 'sum'
    }).reset_index()

    # Create the prompt for LLM analysis
    prompt = f"Analyze the following sales performance data for the {time_period} period: {trend_data.to_dict(orient='records')}. Provide trends and forecast future performance."

    # Generate feedback using LLM
    feedback = get_llm_feedback(prompt)
    
    return {"performance_trends": feedback}
