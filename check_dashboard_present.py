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

    def get_dashbboard_names(self, not_present, df_list, df):
        l = not_present
        for i in df_list:
            
            if (len(i['dashboards'])>0):
                titles = [j['title'] for j in i['dashboards']]
                if(i['name'] not in titles):
                    print("folder name present but not matching with dashboards title =======", i['name'])
                else:
                    l = l+[i['name']]
                    chk_val = df['report_title'][df['report_title'] == i['name']]
                    
                    if not(len(chk_val.tolist()) >0):
                        data = [{
                                    'reportName': i['name'],
                                    'reason': "looker dashboard name not present the csv list"
                                }]
                        export_data = pd.DataFrame(data)
                        export_data.to_csv(export_csv_ref, mode='a', index=False, header=False)
                        print("looker dashboard name not present the list =======", i['name'])
            
                
        return l

    def check_dashboard_present(self,folder_id="",fields="",sorts="",df={}):
        dataset_offset=0
        dataset_limit = 50
        loop_bool = True
        all_records = []
        filtered_dashboard = []
        while loop_bool:

            df_list = self.get_looker_group_reference(folder_id,fields,dataset_limit,dataset_offset,sorts)
            
            all_records = all_records + [i['name'] for i in df_list] #this is reference to iterate only
            print('all_records === ',len(all_records))
            filtered_dashboard = self.get_dashbboard_names(filtered_dashboard, df_list, df)
            print('filtered_dashboard === ',len(filtered_dashboard))

            dataset_offset +=dataset_limit
            loop_bool = not(len(df_list) < dataset_limit)

        return filtered_dashboard



# 
# 
# 
export_data = pd.DataFrame()
export_csv_ref = 'difference_in_reports.csv'
cols = ['reportName',
'reason']
df = pd.DataFrame(columns=cols)

df.to_csv(export_csv_ref, index=False, quoting=csv.QUOTE_NONE)


diff_dashboard_cl = DiffDashboard()
df = pd.read_csv('diageoList.csv', encoding ='latin1')
df = df[df['Status'].str.lower() == "completed"]
dashboards = diff_dashboard_cl.check_dashboard_present(
    folder_id="1945",
    fields="name,id,parent_id,dashboards",
    sorts="created_at",
    df=df)
print("======!!dashboards!!=======")
print(dashboards)
print("======!!dashboards!!=======")
csv_report_names = set(df['report_title'])
looker_report_names = set(dashboards)
diff= csv_report_names.difference(looker_report_names)
print('Report names not present in looker:', *diff, sep='\n')
for k in diff:
    data = [{
                'reportName': k,
                'reason': "Report names not present in looker"
            }]
    export_data = pd.DataFrame(data)
    export_data.to_csv(export_csv_ref, mode='a', index=False, header=False)
