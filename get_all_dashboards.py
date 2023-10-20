import requests
import pretty_errors
import json
from looker_sdk import models as sdk_models
import os
from dotenv import load_dotenv
load_dotenv("/Users/pkarekar/Library/CloudStorage/OneDrive-CornerstoneOnDemand/edgraph-projects/DomotoLooker/.env")
from constants import *
import looker_sdk 
import os 
import json
import pandas as pd
import numpy as np
import csv

sdk = looker_sdk.init40()
sdk_models_4 = looker_sdk.models40

class DiffDashboard:
    def __init__(self):
        self.domo_token = None
        self.domo_instance = None
        self.card_metadata = None
        self.refrmt_metadata = None
        self.hostname = None
        self.query = None
    
    def get_looker_group_reference(self, folder_id,fields,limit,offset,sorts):
        response = sdk.folder_children(
            folder_id=folder_id,
            fields=fields,
            limit=limit,
            offset=offset,
            sorts=sorts)
        
        return response

    def get_dashbboard_names(self, not_present, df_list):
        l = not_present
        for i in df_list:
            
            if (len(i['dashboards'])>0):
                titles = [j['title'] for j in i['dashboards']]
                if(i['name'] not in titles):
                    print("folder name present but not matching with dashboards title =======", i['name'])
                else:
                    l = l+[i['name']]
                    
                    print('===')
                    for d in i['dashboards']:

                        data = [{
                                    'folderName': i['name'],
                                    'dashboardName': d['title'],
                                    'dashboard_id': d['id'],
                                    'dashboard_content_metadata_id':d['content_metadata_id']
                                }]
                        
                        
                        print(d)
                        print(data)
                        print('===')
                        export_data = pd.DataFrame(data)
                        export_data.to_csv(export_csv_ref, mode='a', index=False, header=False)
            
                
        return l

    def get_dashboard_list(self,folder_id="",fields="",sorts=""):
        dataset_offset=0
        dataset_limit = 50
        loop_bool = True
        all_records = []
        filtered_dashboard = []
        while loop_bool:

            df_list = self.get_looker_group_reference(folder_id,fields,dataset_limit,dataset_offset,sorts)
            
            filtered_dashboard = self.get_dashbboard_names(df_list, df_list)

            dataset_offset +=dataset_limit
            loop_bool = not(len(df_list) < dataset_limit)

        return filtered_dashboard



# 
# 
# 
export_data = pd.DataFrame()
export_csv_ref = 'dashboard_list_inside_folder.csv'
cols = ['folderName',
'dashboardName',
'dashboard_id',
'dashboard_content_metadata_id']
df = pd.DataFrame(columns=cols)

df.to_csv(export_csv_ref, index=False, quoting=csv.QUOTE_NONE)


diff_dashboard_cl = DiffDashboard()
diff_dashboard_cl.get_dashboard_list(
    folder_id="1945",
    fields="name,id,parent_id,dashboards",
    sorts="created_at")
