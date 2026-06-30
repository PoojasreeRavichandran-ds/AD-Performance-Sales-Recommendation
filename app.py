import streamlit as st
import pandas as pd
df = pd.read_excel("Amazon jan-may.xlsx")
cpc = df["CPC"].max()
cvr = round(df["CVR"].tail(3).mean(), 3)
asp = round(df["ASP"].tail(3).mean(), 2)
tasp = round(df["TASP"].tail(3).mean(), 2)
organic_pct = round(df["Organic %"].tail(3).mean(), 1)
def recommend_plan(daily_spend, days):
    spend = daily_spend * days
    clicks = spend / cpc
    ad_units = clicks * cvr
    ad_sales = ad_units * asp
    ad_roas = ad_sales / spend
    acos = spend / ad_sales
    total_sales = ad_sales / (1 - organic_pct)
    organic_sales = total_sales - ad_sales
    total_units = total_sales / tasp
    total_roas = total_sales / spend
    tacos = spend / total_sales
    return {
        "Days": days,
        "Spend": round(spend),
        "Clicks": round(clicks),
        "CPC": round(cpc, 2),
        "CVR": f"{cvr:.2%}",
        "Ad Units": round(ad_units),
        "ASP": round(asp, 2),
        "Ad Sales": round(ad_sales),
        "Ad ROAS": round(ad_roas, 2),
        "ACOS": f"{acos:.2%}",
        "Organic Sales": round(organic_sales),
        "Organic %": f"{organic_pct:.2%}",
        "Total Sales": round(total_sales),
        "TASP": round(tasp, 2),
        "Total Units": round(total_units),
        "Total ROAS": round(total_roas, 2),
        "TACOS": f"{tacos:.2%}"
    }
st.set_page_config(
    page_title="Sales Recommendation Engine",
    layout="centered"
)
st.title("AD Performance Recommendation")
daily_spend = st.number_input(
    "Enter Daily Spend (₹)",
    min_value=0.0,
    step=1000.0
)
days = st.number_input(
    "Enter Number of Days",
    min_value=1,
    max_value=31,
    value=30
)
if st.button("Generate Plan"):
    plan = recommend_plan(daily_spend, days)
    st.subheader("📈 Monthly Plan Forecasting")
    for key, value in plan.items():
        if isinstance(value, int):
            st.write(f"**{key}:** {value:,}")
        elif isinstance(value, float):
            if key == "TASP":
                st.write(f"**{key}:** {value:,.0f}")
            elif key in ["CPC", "ASP", "Ad ROAS", "Total ROAS"]:
                st.write(f"**{key}:** {value:,.2f}")
            else:
                st.write(f"**{key}:** {value:,}")
        else:
            st.write(f"**{key}:** {value}")
