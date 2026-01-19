import pyhabitat as ph
import keyring
# Replace these with the actual service and user names your library uses
service = "pipeline-eds-api-Stiles" 
user = "operator" 
print(f"WSL Keyring value: {keyring.get_password(service, "username")}")
print(f"WSL Keyring value: {keyring.get_password(service, "password")}")

service = "pipeline-eds-api-Maxson" 
user = "admin" 
print(f"WSL Keyring value: {keyring.get_password(service, "username")}")
print(f"WSL Keyring value: {keyring.get_password(service, "password")}")


print(f"ph.interactive_terminal_is_available() = {ph.interactive_terminal_is_available()}")
print(f"ph.tkinter_is_available() = {ph.tkinter_is_available()}")
print(f"ph.web_browser_is_available() = {ph.web_browser_is_available()}")

from pipeline_eds.security_and_config import SecurityAndConfig as SC
SC.prompt_for_value(prompt_message = "prompt_message", force_tkinter=True)
