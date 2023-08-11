import requests
import json
from sdk import DOMO_sdk, LOOKER_sdk


class DomoToLooker:
    domo_sdk = DOMO_sdk
    looker_sdk = lOOKER_sdk
   
    def retrieve_metadata_from_domo(cls, domo_report_id):
        # retrieve report metadata from DOMO using API
        # Dummy code,
        response = requests.get(domo_report_id)
        metadata = response.json()
        return metadata
    
    @staticmethod
    def process_metadata_from_domo(metadata):
        # identify and parse the useful metadata from the response
        return metadata

    @staticmethod
    def generate_sql_from_metadata(metadata):
        # parse the received JSON metadata and construct the equivalent SQL query.
        # you may need to handle for ITEM, VALUE, SERIES mappings, and LEGACY filter and NOT_IN operand.
        # implement logic to construct GROUP BY and ORDER BY clauses.
        sql_query = ''  # create your sql query here based on the metadata
        return sql_query

    @staticmethod
    def convert_sql_for_looker(sql_query):
        # convert the constructed SQL query into Looker-friendly syntax, replacing table and field names if necessary.
        looker_sql = ''  # replace with the logic to convert DOMO SQL to Looker SQL
        return looker_sql

    @staticmethod
    def execute_sql_in_looker(looker_api_endpoint, looker_sql):
        # execute the SQL query within Looker and verify the data is appearing as expected.
        # Dummy code, replace with actual API call
        response = requests.post(looker_api_endpoint, data={'sql': looker_sql})
        result = response.json()
        return result

    @staticmethod
    def create_look_in_looker(looker_api_endpoint, looker_sql_result):
        # create a new Look (saved report) in Looker using API.
        # Dummy code, replace with actual API call
        look_creation_response = requests.post(looker_api_endpoint, data={'data': looker_sql_result})
        if look_creation_response.status_code == 200:
            print('Look created in Looker')

# using the above class
domo_to_looker = DomoToLooker()
domo_metadata = domo_to_looker.retrieve_metadata_from_domo('domo_api_endpoint_here')
sql_query = domo_to_looker.generate_sql_from_metadata(domo_metadata)
looker_sql = domo_to_looker.convert_sql_for_looker(sql_query)
result = domo_to_looker.execute_sql_in_looker('looker_api_endpoint_here', looker_sql)

domo_to_looker.create_look_in_looker('looker_api_endpoint_here', result)