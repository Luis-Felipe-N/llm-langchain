from dotenv import load_dotenv
import os
from pathlib import Path

try:
    from google.oauth2 import service_account
except Exception: 
    service_account = None

from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
try:
    from langchain.schema import SystemMessage, HumanMessage
except Exception: 
    SystemMessage = HumanMessage = None

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_APPLICATION_CREDENTIALS") or os.getenv("SERVICE_ACCOUNT_FILE")

print("GOOGLE_API_KEY set:", bool(GOOGLE_API_KEY))
print("SERVICE_ACCOUNT_FILE:", SERVICE_ACCOUNT_FILE)

creds = None
if SERVICE_ACCOUNT_FILE:
    p = Path(SERVICE_ACCOUNT_FILE).expanduser()
    if p.exists() and service_account is not None:
        creds = service_account.Credentials.from_service_account_file(str(p))
        print("Loaded service account credentials from:", str(p))
    else:
        print("SERVICE_ACCOUNT_FILE was provided but could not be loaded (missing file or google-auth not installed).")

llm_google = ChatGoogleGenerativeAI(model="gemini-2.5-flash", credentials=creds) if creds else ChatGoogleGenerativeAI(model="gemini-2.5-pro")
