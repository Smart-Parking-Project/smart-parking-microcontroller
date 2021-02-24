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


update_parking_space_status = gql(
    """
    mutation updateParkingSpace($id: ID! $parkingSpaceDetails:ParkingSpaceDetailsInput! ) {
      updateParkingSpace(id: $id parkingSpaceDetails:$parkingSpaceDetails ) {
          id
        parkingLotIdentifier
        isOccupied
        spaceNumber
      }
    }
"""
)


def updateParkingSpaceStatus(id, is_occupied):
    params = {"id": id, "parkingSpaceDetails": {"isOccupied": is_occupied}}
    updated_space = CLIENT.execute(update_parking_space_status, variable_values=params)
    return updated_space
