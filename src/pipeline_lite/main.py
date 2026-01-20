# src/pipeline-lite/main.py

import pipeline_eds as ple
from pipeline_eds.api.rjn import ClientRjn
from pipeline_eds.api.eds.soap.client import ClientEdsSoap 

import dworshak_access as da

ceds = ClientEdsSoap() # u_eds, p_eds
crjn = ClientRjn() # u_rjn, p_rjn

# --- plant_name = "Maxson"
tabular_data = ceds.soap_api_iess_request_tabular(plant_name = "Maxson", idcs = ["m100fi"])
data = ceds.get_tabular_as_dict(tabular_data)
for entry in data:
    print(f"Time: {entry['timestamp']} | Value: {entry.get('M100FI')} | Quality: {entry.get('M100FI_quality')}")



# --- plant_name = "Stiles"
tabular_data = ceds.soap_api_iess_request_tabular(plant_name = "Stiles", idcs = ["I-0300A"])
data = ceds.get_tabular_as_dict(tabular_data)
for entry in data:
    print(f"Time: {entry['timestamp']} | Value: {entry.get('I-0300A')} | Quality: {entry.get('I-0300A_quality')}")

service = "pipeline-rjn-clarity"
rjn_base_url = da.get_secret(service = service, item = "url")
rjn_client_id = da.get_secret(service = service, item = "username")
rjn_password = da.get_secret(service = service, item = "password")

session = ClientRjn.login_to_session(api_url = rjn_base_url,
    client_id = rjn_client_id,
    password = rjn_password)