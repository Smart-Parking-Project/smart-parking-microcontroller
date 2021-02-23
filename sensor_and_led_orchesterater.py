from nanpy import (ArduinoApi, SerialManager, Ultrasonic)
from time import sleep

ledPin1 = 8
echoPin1 = 9
trigPin1 = 10
ledPin1State = False

try:
    connection = SerialManager()
    a = ArduinoApi (connection=connection)
    ultrasonic1 = Ultrasonic(echoPin1, trigPin1, False, connection=connection)
except:
    print("Failed to connect to Arduino")

a.pinMode (trigPin1, a.OUTPUT)
a.pinMode (echoPin1, a.INPUT)
a.pinMode (ledPin1, a.OUTPUT)

print("-----> The sensor started <-----")
try:
    a.digitalWrite(ledPin1, a.LOW)
    while True:
        sleep(0.5)
        distance = ultrasonic1.get_distance()
        if distance >= 0 and distance < 30:
          print(f'{distance}cm \n')
          a.digitalWrite(ledPin1, a.HIGH)
        else:
          #print(f'{distance}cm \n')
          a.digitalWrite(ledPin1, a.LOW)
except:
    a.digitalWrite(ledPin1, a.LOW)
    print("Failed to read the distance OR System closed")
 

  