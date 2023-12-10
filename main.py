import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("Collin's Live Transportation Database")
st.subheader("Live Flight Tracking")
components.iframe("https://globe.adsbexchange.com/?airport=kdfw", width=1400, height=700)
st.subheader("Current Jet Stream Conditions")
components.iframe("https://www.ventusky.com/?p=32.4;-97.4;5&l=wind-10hpa",width=1400, height=700)
st.subheader("Current Takeoff/Landing Wind Conditions")
components.iframe("https://www.ventusky.com/?p=32.4;-97.4;5&l=wind-10m",width=1400, height=700)
st.subheader("Live METAR-TAF Information")
components.iframe("https://metar-taf.com/KDFW", width=1400, height=700)
st.subheader("Flight Connections Lookup")
components.iframe("https://www.flightconnections.com/",width=1400, height=700)
st.subheader("Life ATC Radio (KDFW Arrivals)")
components.iframe("http://s1-fmt2.liveatc.net/kdfw1_atis_arr?nocache=2023121021262584678")
st.subheader("Live Marine Traffic Tracking")
components.iframe("https://www.marinetraffic.com/en/ais/embed/zoom:8/centery:29/centerx:-95/maptype:4/shownames:false/mmsi:0/shipid:0/fleet:/fleet_id:/vtypes:/showmenu:/remember:false", width=1400, height=700)
st.subheader("Live News Map - U.S.")
components.iframe("https://usa.liveuamap.com/", width=1400,height=700)

