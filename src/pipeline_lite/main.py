# src/pipeline-lite/main.py

import pipeline_eds as ple
from pipeline_eds.api.rjn import ClientRjn
from pipeline_eds.api.eds.soap.client import ClientEdsSoap 

import dworshak_access as da

import logging
logger = logging.getLogger(__name__)


# ------ Calling data from our two plant APIs (EDS) -----------
"""
## --- plant_name = "Maxson"
ceds = ClientEdsSoap() # u_eds, p_eds
tabular_data = ceds.soap_api_iess_request_tabular(plant_name = "Maxson", idcs = ["m100fi"])
data = ceds.get_tabular_as_dict(tabular_data)
for entry in data:
    print(f"Time: {entry['timestamp']} | Value: {entry.get('M100FI')} | Quality: {entry.get('M100FI_quality')}")


## --- plant_name = "Stiles"
tabular_data = ceds.soap_api_iess_request_tabular(plant_name = "Stiles", idcs = ["I-0300A"])
data = ceds.get_tabular_as_dict(tabular_data)
for entry in data:
    print(f"Time: {entry['timestamp']} | Value: {entry.get('I-0300A')} | Quality: {entry.get('I-0300A_quality')}")
"""
# ------ Sending to a third party, RJN -----------

service = "pipeline-rjn-clarity"
TEST = da.get_secret(service = service, item = "test", fail = True)
print(f"TEST = {TEST}")


rjn_base_url = da.get_secret(service = service, item = "url", fail = True)
print(f"rjn_base_url = {rjn_base_url}")
rjn_client_id = da.get_secret(service = service, item = "username", fail = True)
rjn_password = da.get_secret(service = service, item = "password", fail = True)
print(f"rjn_client_id = {rjn_client_id}")
print(f"rjn_password = {rjn_password}")

crjn = ClientRjn(api_url = rjn_base_url) # u_rjn, p_rjn
bool_session = crjn.login_to_session(
    client_id = rjn_client_id,
    password = rjn_password)

print(f"bool_session = {bool_session}")

"""
bool_transmit = crjn.send_data_to_rjn(session = session, 
                      base_url =  rjn_base_url, 
                      project_id=None, 
                      entity_id=None, 
                      timestamps=None, 
                      values=None  )
print(f"bool_transmit = {bool_transmit}")
                      
                      """
