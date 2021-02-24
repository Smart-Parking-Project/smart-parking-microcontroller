from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("smart_parking_api_key")
SERVER_URL = os.getenv("server_url")


TRANSPORT = RequestsHTTPTransport(
    url=SERVER_URL,
    use_json=True,
    headers={"api-key": SECRET_KEY},
    verify=False,
    retries=3,
)

CLIENT = Client(transport=TRANSPORT, fetch_schema_from_transport=True)
