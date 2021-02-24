import os
import threading
from graphql_config.mutaions import updateParkingSpaceStatus

on = threading.Thread(
    target=updateParkingSpaceStatus, args=("6035c931a1ffe80204b8de3a", True)
)
on.start()

# updateParkingSpaceStatus("6035c931a1ffe80204b8de3a", True)
