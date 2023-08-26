import requests
import pretty_errors
import json
from looker_sdk import models as sdk_models
from helper.domo_helper import *
import os
from dotenv import load_dotenv
load_dotenv("/Users/manujarora/Shared/Custom Reports/.env")
from constants import *
import looker_sdk 
import os 
import json
from helper.domo_helper import get_card_metadata, get_session_token
from helper.format_helper import reformat_metadata


class DomoToLooker:
    def __init__(self):
        self.domo_token = None
        self.domo_instance = None
        self.card_metadata = None
        self.refrmt_metadata = None
        self.query = None
        self.sdk = looker_sdk.init40()
    
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
        query = self.sdk.create_query(
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
        look = self.sdk.create_look(
                    body=sdk_models.WriteLookWithQuery(
                                        title=self.refrmt_metadata['title'],
                                        query_id=self.query.id,
                                        folder_id=folder_id
                                                    )
                                )
        return look

# using the above class
# domo_to_looker = DomoToLooker()
# domo_to_looker.create_domo_token("edcast-558")
# domo_to_looker.retrieve_metadata_from_domo('766491542')
# print(domo_to_looker.card_metadata)
# looker_meta = domo_to_looker.process_metadata_from_domo()
# domo_to_looker.generate_query_from_metadata()
# #print(domo_to_looker.refrmt_metadata)
# domo_to_looker.create_look_in_looker(folder_id='3630')

