from nanpy import ArduinoApi, SerialManager, Ultrasonic
from time import sleep
import threading
from graphql_config.mutaions import updateParkingSpaceStatus
#----- sensor #1 -----#
ledPin1 = 8
echoPin1 = 9
trigPin1 = 10
ledPin1State = False
#----- sensor #2 -----#
ledPin2 = 13
echoPin2 = 12
trigPin2 = 11
ledPin2State = False

#----- sensor #3 -----#
ledPin3 = 5
echoPin3 = 7
trigPin3 = 6
ledPin3State = False

try:
    connection = SerialManager()
    a = ArduinoApi(connection=connection)
    ultrasonic1 = Ultrasonic(echoPin1, trigPin1, False, connection=connection)
    ultrasonic2 = Ultrasonic(echoPin2, trigPin2, False, connection=connection)
    ultrasonic3 = Ultrasonic(echoPin3, trigPin3, False, connection=connection)

except Exception as err:
    print("Failed to connect to Arduino")
    print(err)

#----- sensor #1 -----#
a.pinMode(trigPin1, a.OUTPUT)
a.pinMode(echoPin1, a.INPUT)
a.pinMode(ledPin1, a.OUTPUT)

#----- sensor #2 -----#
a.pinMode(trigPin2, a.OUTPUT)
a.pinMode(echoPin2, a.INPUT)
a.pinMode(ledPin2, a.OUTPUT)

#----- sensor #3 -----#
a.pinMode(trigPin3, a.OUTPUT)
a.pinMode(echoPin3, a.INPUT)
a.pinMode(ledPin3, a.OUTPUT)

print("-----> The sensor started <-----")
try:
    a.digitalWrite(ledPin1, a.LOW)
    a.digitalWrite(ledPin2, a.LOW)

    current_state1 = False
    current_state2 = False

    while True:
        sleep(0.2)
        read_distance = 20

        #----- sensor #1 -----#
        distance1 = ultrasonic1.get_distance()
        if distance1 >= 0 and distance1 < read_distance:
            on = threading.Thread(
                target=updateParkingSpaceStatus, args=(
                    "6035c931a1ffe80204b8de3a", True)
            )
            on.start()
            if current_state1 == False:
                print(f"{distance1}cm \n")
                current_state1 = True
            a.digitalWrite(ledPin1, a.HIGH)
        else:
            current_state1 = False
            a.digitalWrite(ledPin1, a.LOW)
            off = threading.Thread(
                target=updateParkingSpaceStatus,
                args=("6035c931a1ffe80204b8de3a", False),
            )
            off.start()

        #----- sensor #2 -----#
        distance2 = ultrasonic2.get_distance()
        if distance2 >= 0 and distance2 < read_distance:
            on = threading.Thread(
                target=updateParkingSpaceStatus, args=(
                    "6035c9585cf54a578030f8b5", True)
            )
            on.start()
            if current_state2 == False:
                print(f"{distance2}cm \n")
                current_state2 = True
            a.digitalWrite(ledPin2, a.HIGH)
        else:
            current_state2 = False
            a.digitalWrite(ledPin2, a.LOW)
            off = threading.Thread(
                target=updateParkingSpaceStatus,
                args=("6035c9585cf54a578030f8b5", False),
            )
            off.start()

        #----- sensor #3 -----#
        distance3 = ultrasonic3.get_distance()
        if distance3 >= 0 and distance3 < read_distance:
            on = threading.Thread(
                target=updateParkingSpaceStatus, args=(
                    "60499be628e43006a0175fb0", True)
            )
            on.start()
            if current_state3 == False:
                print(f"{distance3}cm \n")
                current_state3 = True
            a.digitalWrite(ledPin3, a.HIGH)
        else:
            current_state3 = False
            a.digitalWrite(ledPin3, a.LOW)
            off = threading.Thread(
                target=updateParkingSpaceStatus,
                args=("60499be628e43006a0175fb0", False),
            )
            off.start()

except Exception as err:
    a.digitalWrite(ledPin1, a.LOW)
    print("Failed to read the distance OR System closed")
    print(err)
