# src/pipeline-lite/main.py

import pipeline_eds as ple
from pipeline_eds.api.rjn import ClientRjn
from pipeline_eds.api.eds.soap.client import ClientEdsSoap 

ceds = ClientEdsSoap() # u_eds, p_eds
#crjn = ClientRjn() # u_rjn, p_rjn

plant_name = "Stiles"
#plant_name = "Maxson"
#tabular_data = ceds.soap_api_iess_request_tabular(plant_name = "Maxson", idcs = ["m100fi"])
tabular_data = ceds.soap_api_iess_request_tabular(plant_name = "Stiles", idcs = ["I-0300A"])
#print(f"tabular_data = {tabular_data}")
data = ceds.get_tabular_as_dict(tabular_data)

#print(f"data = {data}")
for entry in data:
    print(f"Time: {entry['timestamp']} | Value: {entry.get('I-0300A')} | Quality: {entry.get('I-0300A_quality')}")
