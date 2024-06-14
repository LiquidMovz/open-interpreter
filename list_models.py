
from google.oauth2 import service_account
from google.cloud import aiplatform_v1

# Set up the path to the service account key file
SERVICE_ACCOUNT_FILE = r'C:\Users\ChaseRemmen\oi\open-interpreter\runner\work\vertexai-credentials.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=['https://www.googleapis.com/auth/cloud-platform']
)

project = "api-project-1029913225919"
location = "us-central1"

# Initialize the Vertex AI client without ClientInfo
client = aiplatform_v1.ModelServiceClient(credentials=credentials)

parent = f"projects/{project}/locations/{location}"

# List models in the specified project and location
try:
    response = client.list_models(parent=parent)
    for model in response:
        print(f"Model: {model.display_name}, ID: {model.name}")
except Exception as e:
    print("An error occurred:", e)
