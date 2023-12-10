import streamlit as st
import pandas as pd

import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("Collin's Live Transportation Database")
st.subheader("Live Flight Tracking")
components.iframe("https://globe.adsbexchange.com/?airport=kdfw", width=1120, height=700)
st.subheader("Current Jet Stream Conditions")
components.iframe("https://www.ventusky.com/?p=32.4;-97.4;5&l=wind-10hpa",width=1120, height=560)
st.subheader("Current Takeoff/Landing Wind Conditions")
components.iframe("https://www.ventusky.com/?p=32.4;-97.4;5&l=wind-10m",width=1120, height=560)
st.subheader("Live METAR-TAF Information")
components.iframe("https://metar-taf.com/KDFW", width=1120, height=700)
st.subheader("Flight Connections Lookup")
components.iframe("https://www.flightconnections.com/",width=1120, height=700)
st.subheader("Life ATC Radio (KDFW Arrivals)")
components.html(
    """
    <html><head><meta name="viewport" content="width=device-width"></head><body cz-shortcut-listen="true"><video controls="" autoplay="" name="media"><source src="http://s1-bos.liveatc.net/kdfw1_atis_arr?nocache=2023121022420437625" type="audio/mpeg"></video></body></html>
    
    """


)
st.subheader("Live Marine Traffic Tracking")
components.iframe("https://www.marinetraffic.com/en/ais/embed/zoom:8/centery:29/centerx:-95/maptype:4/shownames:false/mmsi:0/shipid:0/fleet:/fleet_id:/vtypes:/showmenu:/remember:false", width=1120, height=700)
st.subheader("Live News Map - U.S.")
components.iframe("https://usa.liveuamap.com/", width=1120,height=560)

st.subheader("Live Taiwan Election Polls")
components.iframe("https://flo.uri.sh/story/2010781/embed#slide-0", width=1120, height=700)
