# URL - https://app.prefect.cloud/account/8ff8f613-92c4-44ce-b811-f9956023e78d/workspace/04d8fca9-df2e-40c8-ae4f-a3733114c475/dashboard

# URL - https://app.prefect.cloud/api/docs

import requests

# Replace these variables with your actual Prefect Cloud credentials
PREFECT_API_KEY = "pnu_Dmt476lvZUvXPmVjAdQrD4gzxbsvXn48lXEk"  # Your Prefect Cloud API key
ACCOUNT_ID = "1ad1f5eb-3fa3-437c-aae3-a2d0de99dabd"  # Your Prefect Cloud Account ID
WORKSPACE_ID = "b5993e26-48d5-4824-858e-29a3a4cf67d1"  # Your Prefect Cloud Workspace ID
DEPLOYMENT_ID = "a28bdd27-2778-492c-b685-5b80faba853b"  # Your Deployment ID

# Correct API URL to get deployment details
PREFECT_API_URL = f"https://api.prefect.cloud/api/accounts/{ACCOUNT_ID}/workspaces/{WORKSPACE_ID}/deployments/{DEPLOYMENT_ID}"

# Set up headers with Authorization
headers = {"Authorization": f"Bearer {PREFECT_API_KEY}"}

# Make the request using GET
response = requests.get(PREFECT_API_URL, headers=headers)

# Check the response status
if response.status_code == 200:
    deployment_info = response.json()
    print(deployment_info)
else:
    print(f"Error: Received status code {response.status_code}")
    print(f"Response content: {response.text}")
