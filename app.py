# create a streamlit app with input box and left navigation having input boxes
from dotenv import load_dotenv
load_dotenv("/Users/manujarora/Shared/Custom Reports/.env")
import pretty_errors
import json

import streamlit as st
from DomoToLooker import DomoToLooker
import os


#app icon on streamlit
st.image("domo2looker.png", width=70)


st.title("Domo to Looker")
st.write("This app will help you to create a look in Looker from a Domo card")


#take input from user
st.sidebar.subheader("Domo Instance")
st.session_state['domo_instance'] = st.sidebar.text_input("Domo Instance e.g. edcast-558")
# selection dropdown for region
st.sidebar.subheader("Region")
st.session_state['region'] = st.sidebar.selectbox("Select Looker Region", ["WEST", "EAST", "EU", "AUS"])
region = st.session_state['region']
if region:
    try:
        os.environ["LOOKERSDK_BASE_URL"] = os.environ[region + "_LOOKERSDK_BASE_URL"]
        os.environ["LOOKERSDK_CLIENT_ID"] = os.environ[region + "_LOOKERSDK_CLIENT_ID"]
        os.environ["LOOKERSDK_CLIENT_SECRET"] = os.environ[region + "_LOOKERSDK_CLIENT_SECRET"]
    except:
        st.write("Please set the environment variables for the selected region")
        
# folder id in looker to save the look
st.sidebar.subheader("Folder ID to save look")
st.session_state['folder_id'] = st.sidebar.text_input("Please enter the folder id where you want to save the look")

# Domo report id input in main interface
st.subheader("Domo Report ID")
report_id = st.text_input("Please enter the Domo Report ID")

#execute the code on button click
if st.button("Create Look in Looker"):
    domo_to_looker = DomoToLooker()
    domo_to_looker.create_domo_token(domo_instance=st.session_state['domo_instance'])
    domo_to_looker.retrieve_metadata_from_domo(report_id)
    looker_meta = domo_to_looker.process_metadata_from_domo()
    domo_to_looker.generate_query_from_metadata()
    domo_to_looker.create_look_in_looker(folder_id=st.session_state['folder_id'])
    st.markdown("### Look Created Successfully")  
    st.json(json.dumps(domo_to_looker.refrmt_metadata))

# domo_to_looker = DomoToLooker()
# domo_to_looker.create_domo_token("edcast-558")
# domo_to_looker.retrieve_metadata_from_domo('766491542')
# print(domo_to_looker.card_metadata)
# looker_meta = domo_to_looker.process_metadata_from_domo()
# domo_to_looker.generate_query_from_metadata()
# #print(domo_to_looker.refrmt_metadata)
# domo_to_looker.create_look_in_looker(folder_id='3630')

