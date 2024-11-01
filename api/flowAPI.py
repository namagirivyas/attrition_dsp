# URL - https://app.prefect.cloud/account/8ff8f613-92c4-44ce-b811-f9956023e78d/workspace/04d8fca9-df2e-40c8-ae4f-a3733114c475/dashboard

# URL - https://app.prefect.cloud/api/docs

import requests

# Replace these variables with your actual Prefect Cloud credentials
PREFECT_API_KEY = "pnu_Dmt476lvZUvXPmVjAdQrD4gzxbsvXn48lXEk"  # Your Prefect Cloud API key
ACCOUNT_ID = "1ad1f5eb-3fa3-437c-aae3-a2d0de99dabd"  # Your Prefect Cloud Account ID
WORKSPACE_ID = "b5993e26-48d5-4824-858e-29a3a4cf67d1"  # Your Prefect Cloud Workspace ID
FLOW_ID = "470e3914-16de-418b-b799-9377ac3bf0e0"  # Your Flow ID

# Correct API URL to get flow details
PREFECT_API_URL = f"https://api.prefect.cloud/api/accounts/{ACCOUNT_ID}/workspaces/{WORKSPACE_ID}/flows/{FLOW_ID}"

# Set up headers with Authorization
headers = {"Authorization": f"Bearer pnu_Dmt476lvZUvXPmVjAdQrD4gzxbsvXn48lXEk"}

# Make the request using GET
response = requests.get(PREFECT_API_URL, headers=headers)

# Check the response status
if response.status_code == 200:
    flow_info = response.json()
    print(flow_info)
else:
    print(f"Error: Received status code {response.status_code}")
    print(f"Response content: {response.text}")
