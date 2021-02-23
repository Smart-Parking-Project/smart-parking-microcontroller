from nanpy import ArduinoApi

a = ArduinoApi()
a.pinMode(13, a.OUTPUT)
a.digitalWrite(13, a.HIGH)