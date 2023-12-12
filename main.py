import streamlit as st
import pandas as pd

import streamlit.components.v1 as components


st.title("Collin's Live Transportation Database")

col_0, col_01 = st.columns([0.25, 0.75])
with col_0:
    st.subheader("Welcome to your personalized dashboard for all things moving.")
    with st.container(border=0):
        st.write("            ")
        st.write("To the right, you'll find a flight tracking software similar to FlightRadar24. ")
        st.write("            ")
        st.write("  Below, you'll find the current jet stream conditions and wind speeds on the ground to have an idea of what pilots are working with.")
        st.write("            ")
        st.write("  You'll also find the latest published METARS that pilots are reading prior to takeoff. To know where they are going, you can quickly look up every flight route that is available to any given airport.")
        st.write("            ")
        st.write("Your plane tracking experience wouldn't be complete without live ATC radio transmission of each DFW arrival, so that's included upon startup.")
        st.write("            ")

with col_01:
    st.subheader("Live Flight Tracking")
    components.iframe("https://globe.adsbexchange.com/?airport=kdfw", width=1120, height=700)


col1, col2 = st.columns(2)

with col1:
    st.subheader("Current Jet Stream Conditions")
    components.iframe("https://www.ventusky.com/?p=32.4;-97.4;5&l=wind-10hpa",height=560)
    st.subheader("Live METAR-TAF Information")
    components.iframe("https://metar-taf.com/KDFW", height=700)

with col2:
    st.subheader("Current Takeoff/Landing Wind Conditions")
    components.iframe("https://www.ventusky.com/?p=32.4;-97.4;5&l=wind-10m", height=560)

    st.subheader("Flight Connections Lookup")
    components.iframe("https://www.flightconnections.com/", height=700)

st.subheader("Life ATC Radio (KDFW Arrivals)")
components.html(
    """
    <html><head><meta name="viewport" content="width=device-width"></head><body cz-shortcut-listen="true"><video controls="" autoplay="" name="media"><source src="http://s1-bos.liveatc.net/kdfw1_atis_arr?nocache=2023121022420437625" type="audio/mpeg"></video></body></html>
    
    """


)
st.header("Why stop at aircraft?")

st.markdown("""
<style>
.big-font {
    font-size:25px
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Below you\'ll find a marine tracking software similar to the above programs, logging every registered vessel on the open ocean. Due to maritime restrictions, only those near the U.S. border can be classified, however.</p>', unsafe_allow_html=True)
st.markdown('<p class="big-font">In addition to that, you\'ll find the latest location-based news in the U.S. and updated polls of the 2024 Taiwan Election, which takes place on your next birthday.</p>', unsafe_allow_html=True)
col_03,col_04 = st.columns([0.90, 0.10])
with col_03:

    st.subheader("Live Marine Traffic Tracking")
    components.iframe("https://www.marinetraffic.com/en/ais/embed/zoom:8/centery:29/centerx:-95/maptype:4/shownames:false/mmsi:0/shipid:0/fleet:/fleet_id:/vtypes:/showmenu:/remember:false", height=700)

    st.subheader("Live News Map - U.S.")
    components.iframe("https://usa.liveuamap.com/",height=560)

    st.subheader("Live Taiwan Election Polls")
    components.iframe("https://flo.uri.sh/story/2010781/embed#slide-0", height=700)
