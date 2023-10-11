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
import numpy as np


sdk = looker_sdk.init40()
sdk_models_4 = looker_sdk.models40
# print('sdk_models_4 == ', dir(looker_sdk.models40))

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
                        body=sdk_models_4.CreateEmbedUserRequest(
                            external_user_id=external_user_id
                        ))
        return response

    def get_group_users(self, group_id):
        response = sdk.all_group_users(group_id=group_id)
        return response

    def add_user_to_group(self, group_id, user_id):
        response = sdk.add_group_user(
            group_id=group_id,
            body=sdk_models.GroupIdForGroupUserInclusion(user_id= user_id))

    def get_all_user_attributes(self):
        response = sdk.all_user_attributes(fields="id,name,label,type,default_value")
        return response

    def create_domo_token(self, domo_instance):
        email = os.environ["EMAIL"]
        password = os.environ["PASSWORD"]
        self.domo_instance=domo_instance
        self.domo_token = get_session_token(domo_instance=self.domo_instance, email=email, password=password)
   
    def get_user_attribute_group_values(self, u_a_id):
        response = sdk.all_user_attribute_group_values(user_attribute_id=u_a_id)
        return response

    def retrieve_metadata_from_domo(self, domo_report_id):
        self.card_metadata=get_card_metadata(self.domo_instance, domo_report_id, self.domo_token)
    
    def apply_user_attribute_group_values(self, u_a_id, g_id, val):
        response = sdk.set_user_attribute_group_values(
                    user_attribute_id=u_a_id,
                    body=[
                        mdls.UserAttributeGroupValue(
                            group_id=g_id,
                            value=val
                        )
                    ])

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


# =============init=====================
pdp_user_details = [
    {'csv_name': 'pdp_filter_Novartis_edcast-574_Evaluations_Test.csv','inst': 'edcast-574','dataset_id':'ca38f90e-66c4-413e-8752-355d93837144'},
    {'csv_name': 'pdp_filter_Novartis_edcast-574_EvaluationPrograms_Master.csv','inst': 'edcast-574','dataset_id':'5242c432-3861-4818-a61f-3531070b442e'},
    {'csv_name': 'pdp_filter_Novartis_edcast-574_Evaluation_Programs_ConsolidatedMaster.csv','inst': 'edcast-574','dataset_id':'8de71efb-af96-434c-958d-e194efb4628e'}
]



apply_pdp_cl = ApplyPDPValues()
apply_pdp_cl.hostname = 'novartis' #suffix for group name
apply_pdp_cl.instance_group_id = '46' #this is important as it will filter out users other than the instance group users
pdp_cur = pdp_user_details[1]

attribute_mapping = {
    'allowed_trainer_name_updated_100098':{'id':'22', 'field_name':'Trainer Name Updated', 'dataset_id':pdp_user_details[1]['dataset_id']},
    'allowed_training_director_100098':{'id':'19', 'field_name':'Training Director', 'dataset_id':pdp_user_details[1]['dataset_id']},
    'allowed_training_lead_100098':{'id':'20', 'field_name':'Training Lead', 'dataset_id':pdp_user_details[1]['dataset_id']},
    'allowed_training_name_100098':{'id':'18', 'field_name':'Training Name', 'dataset_id':pdp_user_details[1]['dataset_id']},
    'novartis_100098_evaluations_test_trainer_name_updated':{'id':'27', 'field_name':'Trainer Name Updated', 'dataset_id':pdp_user_details[0]['dataset_id']},
    'novartis_100098_evaluations_test_training_director':{'id':'28', 'field_name':'Training Director', 'dataset_id':pdp_user_details[0]['dataset_id']},
    'novartis_100098_evaluations_test_training_lead':{'id':'29', 'field_name':'Training Lead', 'dataset_id':pdp_user_details[0]['dataset_id']},
    'novartis_100098_evaluation_programs_consolidatedmaster_training_director':{'id':'23', 'field_name':'Training Director', 'dataset_id':pdp_user_details[2]['dataset_id']},
    'novartis_100098_evaluation_programs_consolidatedmaster_training_lead':{'id':'24', 'field_name':'Training Lead', 'dataset_id':pdp_user_details[2]['dataset_id']},
    'novartis_100098_evaluation_programs_consolidatedmaster_training_name':{'id':'25', 'field_name':'Training Name', 'dataset_id':pdp_user_details[2]['dataset_id']},
}
# apply_pdp_cl.create_domo_token(pdp_cur['inst'])

# fetch the list of user attributes we created for looker embed users
# for i in apply_pdp_cl.get_all_user_attributes():
#     print('=====')
#     # get attribute id from here
#     print(i)
#     print('=====')

domo_ds = pd.read_csv('100098_Glue_Users [U][1] [Latest Metadata].csv', low_memory=False) # had to set to low_memory=False as DtypeWarning: Columns (8,19) have mixed types.


df = pd.read_csv(pdp_cur['csv_name'])


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
    # check if the embed user exist in looker with the email
    if(len(user_ref) > 0):
        # if yes: add the looker embed looker user to the looker group created for this embed looker user
        # print('==== add_user_to_group =====')
        # print(apply_pdp_cl.get_group_users(group_ref.id))
        apply_pdp_cl.add_user_to_group(group_ref.id, user_ref.id)
        # print('==== add_user_to_group =====')
    else:
        print('====not in looker=====')
        u = domo_ds[domo_ds.Email == email]
        print(u['User ID'].iloc[0])
        print('email = ', email, ' , group_name = ', group_ref.name)
        
        #if no: create user from the LXP user id(refer domo U1 latest metadata dataset to get the userid and hit looker API passing the LXP user ID to create looker embed user)
        user_ref = apply_pdp_cl.create_embed_user(str(u['User ID'].iloc[0]))
        
        # add this embed looker user to the looker group we created
        apply_pdp_cl.add_user_to_group(group_ref.id, user_ref.id)
        print('====not in looker=====')
    
    # print('domo pdp column name - ',  pdp_read.pdp_filter_name)
    # print('pdp_read',pdp_read)
    #   check if the domo pdp value is null/nan, if its null which means this user has all rows enabled for pdp
    if pdp_read.pdp_filter_name is np.nan:
        #   set group attribute val="%" to all the user attributes of the dataset_id for the group_ref
        print('pdp_name ===!!is nan!!==== ', pdp_read.pdp_name)
        wildcard_att = {k:v for k,v in attribute_mapping.items() if v['dataset_id'] == pdp_read.dataset_id}
        for k,v in wildcard_att.items():
            print('wildcard_att == ',wildcard_att)
            print("===========applying % value to group in attributes===========")
            print("looker attribute id : ", v['id'])
            print("looker attribute name : ", k)
            print("looker group id : ", group_ref.id)
            print("looker group name : ", group_name)
            print("looker user id : ", user_ref.id)
            print("email : ", email)
            print("pdp field name : ", pdp_read.pdp_filter_name)
            print("pdp value : ", '%')
            print("===========applying % value to group in attributes===========")
            # apply_pdp_cl.apply_user_attribute_group_values( v['id'], group_ref.id, "%")

    else: # this is the case where pdp has filter on column
        
        #   create a comprehension of a list which should return 1 user attribute id
        #   iterates over all the attribute_mapping 
        #   has condition where attribute_mapping's dataset_id matches with the domo pdp record dataset_id and
        #   has condition where the  attribute_mapping's field name matches with the domo pdp record field name
        u_a_id = [{v['id']:k} for k,v in attribute_mapping.items() if (v['dataset_id'] == pdp_read.dataset_id and v['field_name'] == pdp_read.pdp_filter_name) ]
        u_a_id = list(u_a_id[0].items())[0]
        
        ua_group_val_l = apply_pdp_cl.get_user_attribute_group_values(u_a_id[0])
        print("ua_group_val_l ============ ",ua_group_val_l)
        
        ua_group_val_l = [i for i in ua_group_val_l if str(i['group_id']) == str(group_ref.id)]
        print("after == ua_group_val_l ============ ",ua_group_val_l)

        # if there are no group and its values added for the attribute, hence len(ua_group_val_l) will be 0
        if len(ua_group_val_l) == 0:
            print('pdp_name ===!!!!!! ua_group_val_l == 0 !!!!!==== ', pdp_read.pdp_name)
            
            print("===========adding new group and its  values===========")
            print("looker attribute id : ", u_a_id[0])
            print("looker attribute name : ", u_a_id[1])
            print("looker group id : ", group_ref.id)
            print("looker group name : ", group_name)
            print("looker user id : ", user_ref.id)
            print("email : ", email)
            print("pdp field name : ", pdp_read.pdp_filter_name)
            print("pdp value : ", pdp_read.pdp_value)
            print("===========adding new group and its values===========")
            # apply_pdp_cl.apply_user_attribute_group_values( v['id'], group_ref.id, "%")
        else:
        # this is the case where there are 1 to many values added for the group of a user
            ua_group_value = ua_group_val_l[0]['value']
            if "'" in ua_group_value:
                val_to_apply = ua_group_value.split("','")
                val_to_apply = [i.replace("'", '') for i in val_to_apply ]
                if pdp_read.pdp_value not in val_to_apply:
                    val_to_apply.append(pdp_read.pdp_value)
                    val_to_apply = ",".join(["'{}'".format(i) for i in val_to_apply])

                    print("===========concating values to existing===========")
                    print("looker attribute id : ", u_a_id[0])
                    print("looker attribute name : ", u_a_id[1])
                    print("looker group id : ", group_ref.id)
                    print("looker group name : ", group_name)
                    print("looker user id : ", user_ref.id)
                    print("email : ", email)
                    print("pdp field name : ", pdp_read.pdp_filter_name)
                    print("pdp value : ", val_to_apply)
                    print("===========concating values to existing===========")
                    # apply_pdp_cl.apply_user_attribute_group_values( u_a_id[0], group_ref.id, val_to_apply)
                else:
                    print("===========!!!!already presen!!!!===========")
                    print("looker attribute id : ", u_a_id[0])
                    print("looker attribute name : ", u_a_id[1])
                    print("looker group id : ", group_ref.id)
                    print("looker group name : ", group_name)
                    print("looker user id : ", user_ref.id)
                    print("email : ", email)
                    print("pdp field name : ", pdp_read.pdp_filter_name)
                    print("existing value : ", ua_group_value)
                    print("===========!!!!already present!!!!===========")
            else:
                #   add condition when the domo pdp val is not in the group user attribute value
                if pdp_read.pdp_value not in ua_group_value:
                    #   combine value
                    val_to_apply = "'{}','{}'".format(ua_group_value,pdp_read.pdp_value)
                    print("===========adding more than 1 values to existing===========")
                    print("looker attribute id : ", u_a_id[0])
                    print("looker attribute name : ", u_a_id[1])
                    print("looker group id : ", group_ref.id)
                    print("looker group name : ", group_name)
                    print("looker user id : ", user_ref.id)
                    print("email : ", email)
                    print("pdp field name : ", pdp_read.pdp_filter_name)
                    print("pdp value : ", val_to_apply)
                    print("===========adding more than 1 values to existing===========")
                    # apply_pdp_cl.apply_user_attribute_group_values( u_a_id[0], group_ref.id, val_to_apply)
                else:
                    print("===========!!!!already presen!!!!===========")
                    print("looker attribute id : ", u_a_id[0])
                    print("looker attribute name : ", u_a_id[1])
                    print("looker group id : ", group_ref.id)
                    print("looker group name : ", group_name)
                    print("looker user id : ", user_ref.id)
                    print("email : ", email)
                    print("pdp field name : ", pdp_read.pdp_filter_name)
                    print("existing value : ", ua_group_value)
                    print("===========!!!!already present!!!!===========")
            #   get group referen ce{hostname}_{emailtest_before_@} 
            #   set the value of this group from the users csv to the looker user attribute

    