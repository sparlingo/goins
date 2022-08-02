import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_csv("data/baseballDB/core/Teams.csv")

option = st.selectbox(
	'Which team?',
	('TOR', 'BOS', "NYA", "TBA", "BAL")
)
st.write('You selected:', option)

team = df[df["teamID"] == option]
#data = team[["W","yearID"]]
#st.dataframe(data=data)

wby = alt.Chart(team).mark_line().encode(
	alt.X('yearID',
		scale=alt.Scale(zero=False)
	),
	y='W',
)

st.altair_chart(wby)