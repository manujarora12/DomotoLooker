import json
import logging
import requests
from constants import *


def get_card_metadata(domo_instance, card_id, session_token):
  url = f"https://{domo_instance}.domo.com/api/content/v1/cards?urns={card_id}&parts=datasources,metadata,slicers,subscriptions&includeFiltered=true"
  payload = {}
  headers = {'Content-Type': 'application/json',
                     'x-domo-authentication': session_token}
  response = requests.request("GET", url, headers=headers, data=payload)
  return response.json()
  
def get_session_token(domo_instance, email, password, full_response=False):
    auth_api = 'https://{}.domo.com/api/content/v2/authentication'.format(domo_instance)
    auth_body = json.dumps({
        "method": "password",
        "emailAddress": email,
        "password": password
    })
    auth_headers = {'Content-Type': 'application/json'}
    auth_response = requests.post(auth_api, data=auth_body, headers=auth_headers)
    auth_status = auth_response.status_code
    resp = auth_response.json()
    if auth_status == 200:
        if (resp['success'] is False):
            token_error_string = "Failed to login to the instance : {} ,  reason: {}".format(domo_instance,
                                                                                             resp['reason'])
            return (None, token_error_string)
        else:
            logging.info('Session token acquired.')
            if full_response:
                return resp
            else:
                return resp['sessionToken']
    else:
        token_error_string = 'Token request ended up with status code {}'.format(auth_status)
        logging.error(token_error_string)
        logging.error(auth_response.text)
        raise Exception(token_error_string)
        return None


    