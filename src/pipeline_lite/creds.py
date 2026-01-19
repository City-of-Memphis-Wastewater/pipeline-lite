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