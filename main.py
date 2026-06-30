import pandas as pd
df = pd.read_excel(r"C:\Users\ELCOT\Desktop\Amazon Recommendation Engine\Amazon jan-may.xlsx")
df.rename(columns={
    "Particulars": "Month",
    "Unnamed: 17": "Growth Rate"
}, inplace=True)
max_cpc = df["CPC"].max()
avg_cvr = round(df["CVR"].tail(3).mean(), 3)
avg_asp = round(df["ASP"].tail(3).mean(), 2)
avg_tasp = round(df["TASP"].tail(3).mean(), 2)
avg_organic_pct = df["Organic %"].iloc[-1] + 0.01
print("========== KPIs Used ==========")
print(f"Maximum CPC          : {max_cpc:.2f}")
print(f"Average CVR          : {avg_cvr:.2%}")
print(f"Average ASP          : {avg_asp:.2f}")
print(f"Forecast Organic %   : {avg_organic_pct:.2%}")
print(f"Average TASP         : {avg_tasp:.2f}")
def recommend_plan(daily_spend, days):
    spend = daily_spend * days
    clicks = spend / max_cpc
    ad_units = clicks * avg_cvr
    ad_sales = ad_units * avg_asp
    ad_roas = ad_sales / spend
    acos = spend / ad_sales
    total_sales = ad_sales / (1 - avg_organic_pct)
    organic_sales = total_sales - ad_sales
    total_units = total_sales / avg_tasp
    total_roas = total_sales / spend
    tacos = spend / total_sales
    print("\n========== RECOMMENDED PLAN ==========\n")
    print(f"Days            : {days}")
    print(f"Spend           : {spend:,.0f}")
    print(f"Clicks          : {clicks:,.0f}")
    print(f"CPC             : {max_cpc:.2f}")
    print(f"CVR             : {avg_cvr:.2%}")
    print(f"Ad Units        : {ad_units:,.0f}")
    print(f"ASP             : {avg_asp:.2f}")
    print(f"Ad Sales        : {ad_sales:,.0f}")
    print(f"Ad ROAS         : {ad_roas:.2f}")
    print(f"ACOS            : {acos:.2%}")
    print(f"Organic Sales   : {organic_sales:,.0f}")
    print(f"Organic %       : {avg_organic_pct:.2%}")
    print(f"Total Sales     : {total_sales:,.0f}")
    print(f"TASP            : {avg_tasp:.2f}")
    print(f"Total Units     : {total_units:,.0f}")
    print(f"Total ROAS      : {total_roas:.2f}")
    print(f"TACOS           : {tacos:.2%}")
daily_spend = float(input("Enter Daily Spend: "))
days = int(input("Enter Number of Days: "))
recommend_plan(daily_spend, days)