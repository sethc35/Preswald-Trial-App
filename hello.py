from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px

connect()
df = get_df("healthcare_dataset")

sql = "SELECT * FROM healthcare_dataset WHERE Age > 50"
filtered_df = query(sql, "healthcare_dataset")

text("# Seth's Analysis App")
table(filtered_df, title="Filtered Data")

condition_counts = filtered_df['Medical Condition'].value_counts().reset_index()
condition_counts.columns = ['Medical Condition', 'Count']

fig = px.bar(condition_counts, x="Medical Condition", y="Count",
             title="Medical Conditions for Patients Over 50")

fig.update_xaxes(type='category')

plotly(fig)
