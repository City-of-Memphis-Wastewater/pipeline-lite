# src/pipeline-lite/main.py

import pipeline_eds as ple
from pipeline_eds.api.rjn import ClientRjn
from pipeline_eds.api.eds.soap.client import ClientEdsSoap 

u_eds = None
p_eds = None

u_rjn = None
p_rjn = None

ceds = ClientEdsSoap() # u_eds, p_eds
#crjn = ClientRjn() # u_rjn, p_rjn

ceds.soap_api_iess_request_tabular(plant_name = "Stiles", idcs = "m100fi")
