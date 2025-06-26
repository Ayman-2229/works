import pandas as pd
from utils.visuals import forecast_line_chart
from components.forecast import forecast_expenses

def budget_coach(df: pd.DataFrame):
    total_spending = df['amount'].sum()
    categories = df.groupby('category')['amount'].sum()
    insights = []
    score = 100

    # Heuristics for individual categories
    def pct(value): return (value / total_spending) * 100 if total_spending > 0 else 0

    # General spending health
    if total_spending > 100000:
        insights.append("💸 Your total expenses this period are quite high. Consider setting a monthly budget cap.")
        score -= 10

    # Food spending
    food_spend = categories.get('Food', 0)
    if pct(food_spend) > 20:
        insights.append(f"🍕 Food accounts for {pct(food_spend):.1f}% of your expenses. Try home-cooked meals or meal planning.")
        score -= 5

    # Subscriptions
    sub_spend = categories.get('Subscription', 0)
    if sub_spend > 1500:
        insights.append(f"📺 Subscriptions cost you Rs. {sub_spend:.2f}. Consider cancelling services you rarely use.")
        score -= 3

    # Travel
    travel_spend = categories.get('Travel', 0)
    if pct(travel_spend) > 15:
        insights.append(f"🚗 Travel is {pct(travel_spend):.1f}% of your total. Carpooling or using public transport could help.")
        score -= 4

    # EMI
    emi_spend = sum(categories.get(cat, 0) for cat in categories.index if "emi" in cat.lower())
    if pct(emi_spend) > 25:
        insights.append(f"💳 EMIs are taking up {pct(emi_spend):.1f}% of your spend. Make sure this aligns with your income level.")
        score -= 8

    # Utilities
    util_spend = categories.get('Utilities', 0)
    if util_spend > 3000:
        insights.append("💡 High utility bills detected. Review electricity and internet usage for savings.")
        score -= 2

    # Investment check
    invest_spend = categories.get('Investment', 0)
    if invest_spend < 1000:
        insights.append("📉 Investments are low this period. Try to allocate at least 10% of income to savings or investments.")
        score -= 4
    else:
        insights.append("📈 Great job on your investments! Stay consistent for long-term financial health.")
        score += 2

    # Education and health
    if 'Healthcare' in categories and categories['Healthcare'] > 2000:
        insights.append("🏥 You’ve had notable healthcare expenses. Consider maintaining an emergency fund.")
        score -= 2

    if 'Education' in categories and categories['Education'] > 3000:
        insights.append("🎓 Education spending detected — consider it an investment in future returns.")

    # Overall assessment
    if score >= 90:
        insights.append("\n✅ You're doing great overall! Just keep tracking your habits.")
    elif score >= 75:
        insights.append("\n👍 You're on track. A few adjustments can boost your financial fitness.")
    else:
        insights.append("\n⚠️ Time to tighten up your budget and revisit your financial priorities.")

    forecast_df = forecast_expenses(df)
    forecast_fig = forecast_line_chart(forecast_df)

    # Return insights and forecast figure as a tuple
    return "\n".join(insights), forecast_fig
