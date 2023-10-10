import requests
import pretty_errors
import json
from looker_sdk import models as sdk_models
from helper.domo_helper import *
import os
from dotenv import load_dotenv
load_dotenv("/Users/pkarekar/Library/CloudStorage/OneDrive-CornerstoneOnDemand/edgraph-projects/DomotoLooker/.env")
from constants import *
import looker_sdk 
import os 
import json
from helper.domo_helper import get_card_metadata, get_session_token
from helper.format_helper import reformat_metadata
import pandas as pd

sdk = looker_sdk.init40()

class ApplyPDPValues:
    def __init__(self):
        self.domo_token = None
        self.domo_instance = None
        self.card_metadata = None
        self.refrmt_metadata = None
        self.hostname = None
        self.query = None
    
    def get_looker_group_reference(self, group_name):
        response = sdk.search_groups(name=group_name)
        
        if len(response)>0:
            return response[0]
        else:
            return []
    
    def create_group(self, group_name):
        response = sdk.create_group(
                        body=sdk_models.WriteGroup(
                            can_add_to_content_metadata=True,
                            name=group_name
                        ))
        return response
    
    def set_group_attribute_value(self, group_id,user_attribute_id, val):
        look = sdk.update_user_attribute_group_value(
            group_id=group_id,
            user_attribute_id=user_attribute_id,
            value=val,
            body=sdk_models.UserAttributeGroupValue())

    def get_user_by_email(self, email, instance_group_id):
        response = sdk.search_users(email=email, group_id=instance_group_id)
        if len(response)>0:
            return response[0]
        else:
            return []

    def create_embed_user(self, external_user_id):
        response = sdk.create_embed_user(
                        body=sdk_models.CreateEmbedUserRequest(
                            external_user_id=external_user_id
                        ))
    def get_group_users(self, group_id):
        response = sdk.all_group_users(group_id=group_id)
        return response

    def add_user_to_group(self, group_id, user_id):
        response = sdk.add_group_user(
            group_id=group_id,
            body=sdk_models.GroupIdForGroupUserInclusion(user_id= user_id))

    def create_domo_token(self, domo_instance):
        email = os.environ["EMAIL"]
        password = os.environ["PASSWORD"]
        self.domo_instance=domo_instance
        self.domo_token = get_session_token(domo_instance=self.domo_instance, email=email, password=password)
   
    def retrieve_metadata_from_domo(self, domo_report_id):
        self.card_metadata=get_card_metadata(self.domo_instance, domo_report_id, self.domo_token)
    
    def process_metadata_from_domo(self):
        self.refrmt_metadata = reformat_metadata(self.card_metadata[0])
        return self.refrmt_metadata

    def generate_query_from_metadata(self):
        print(f"""                                   model="concord",
                                        view={str(self.refrmt_metadata['view'])},
                                        fields={self.refrmt_metadata['fields']},
                                        filters={self.refrmt_metadata['filters']},
                                        pivots={self.refrmt_metadata['pivots']},
                                        dynamic_fields={self.refrmt_metadata.get('dynamic_fields')}
        
        """)
        query = sdk.create_query(
            body=sdk_models.WriteQuery(
                                        model="concord",
                                        view=str(self.refrmt_metadata['view']),
                                        fields=self.refrmt_metadata['fields'],
                                        filters=self.refrmt_metadata['filters'],
                                        pivots=self.refrmt_metadata['pivots'],
                                        dynamic_fields=self.refrmt_metadata.get('dynamic_fields')
                                        )
                        )
        self.query = query 
    
    def create_look_in_looker(self, folder_id=None):
        look = sdk.create_look(
                    body=sdk_models.WriteLookWithQuery(
                                        title=self.refrmt_metadata['title'],
                                        query_id=self.query.id,
                                        folder_id=folder_id
                                                    )
                                )
        return look



apply_pdp_cl = ApplyPDPValues()
apply_pdp_cl.hostname = 'novartis' #suffix for group name
apply_pdp_cl.instance_group_id = '46' #this is important as it will filter out users other than the instance group users

df = pd.read_csv('pdp_filter_Novartis_edcast-574_Evaluations_Test.csv')
for i, pdp_read in df.iterrows():
    email = pdp_read.user_email
    group_name = "{}_{}".format(apply_pdp_cl.hostname,email)
    # print("="+group_name+'=')
    # check for the group name using looker API starting from {hostname}_{emailtest_before_@}
    group_ref = apply_pdp_cl.get_looker_group_reference(group_name)
    
    if(len(group_ref) == 0):
        # if not : create group with the name {hostname}_{emailtest_before_@} for each given email id list
        group_ref = apply_pdp_cl.create_group(group_name)
        
    # print('group_ref ===')
    # print(group_ref)
    # print('group_ref ===')
    
#   if exists : execute next line
    user_ref = apply_pdp_cl.get_user_by_email(email, apply_pdp_cl.instance_group_id)
    # print('user_ref ===')
    # print(user_ref)
    # print('user_ref ===')
    if(len(user_ref) > 0):
        print('==== add_user_to_group =====')
        # print(user_ref.id,' , email = ', user_ref.email, ' , group_name = ', group_ref.name)
        # print(apply_pdp_cl.get_group_users(group_ref.id))
        apply_pdp_cl.add_user_to_group(group_ref.id, user_ref.id)
        print('==== add_user_to_group =====')
    else:
        print('====not in looker=====')
        print('email = ', email, ' , group_name = ', group_ref.name)
        print('====not in looker=====')
        
# check if the embed user exist in looker with the email
#   if yes: add the looker embed looker user to the looker group created for this embed looker user
#   if no: create user from the LXP user id(refer domo U1 latest metadata dataset to get the userid and hit looker API passing the LXP user ID to create looker embed user)
# add this embed looker user to the looker group we created

# fetch the list of user attributes we created for looker embed users from a csv using pandas dataframes
# loop on the these users
#   find the looker group we created with the name {hostname}_{emailtest_before_@} 
#   set the value of this group from the users csv to the looker user attribute 



