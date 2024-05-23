# app/routers/team_performance.py

from fastapi import APIRouter
from services.data_ingestion import load_sales_data
from services.llm_analysis import get_llm_feedback

router = APIRouter()

@router.get("/api/team_performance")
def team_performance():
    df = load_sales_data('data/sales_data.csv')
    total_revenue = df['revenue_confirmed'].sum()
    total_applications = df['applications'].sum()
    avg_deal_value = df['avg_deal_value_30_days'].mean()
    conversion_rate = df['avg_close_rate_30_days'].mean()

    prompt = f"Analyze the overall sales team performance. Total revenue: {total_revenue}, Total applications: {total_applications}, Average deal value: {avg_deal_value}, Conversion rate: {conversion_rate}"


    feedback = get_llm_feedback(prompt)

    return {"team_performance_summary": feedback}
