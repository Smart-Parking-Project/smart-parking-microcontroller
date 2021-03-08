from nanpy import ArduinoApi, SerialManager, Ultrasonic
from time import sleep
import threading
from graphql_config.mutaions import updateParkingSpaceStatus

ledPin1 = 8
echoPin1 = 9
trigPin1 = 10
ledPin1State = False

try:
    connection = SerialManager()
    a = ArduinoApi(connection=connection)
    ultrasonic1 = Ultrasonic(echoPin1, trigPin1, False, connection=connection)
except Exception as err:
    print("Failed to connect to Arduino")
    print(err)

a.pinMode(trigPin1, a.OUTPUT)
a.pinMode(echoPin1, a.INPUT)
a.pinMode(ledPin1, a.OUTPUT)

print("-----> The sensor started <-----")
try:
    a.digitalWrite(ledPin1, a.LOW)
    current_state = False
    while True:
        sleep(0.5)
        distance = ultrasonic1.get_distance()
        if distance >= 0 and distance < 30:
            on = threading.Thread(
                target=updateParkingSpaceStatus, args=(
                    "6035c931a1ffe80204b8de3a", True)
            )
            on.start()
            if current_state == False:
                print(f"{distance}cm \n")
                current_state = True
            a.digitalWrite(ledPin1, a.HIGH)
        else:
            current_state = False
            a.digitalWrite(ledPin1, a.LOW)
            off = threading.Thread(
                target=updateParkingSpaceStatus,
                args=("6035c931a1ffe80204b8de3a", False),
            )
            off.start()

except Exception as err:
    a.digitalWrite(ledPin1, a.LOW)
    print("Failed to read the distance OR System closed")
    print(err)
