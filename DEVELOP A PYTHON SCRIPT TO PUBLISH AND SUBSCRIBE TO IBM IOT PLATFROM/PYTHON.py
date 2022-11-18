import random
import time
#IBM Watson IOT Platform
#pip install wiotp-sdk
import wiotp.sdk.device
myConfig = {
 "identity": {
 "orgId": "o8mv0s",
 "typeId": "RIVERQUALITYMONITOR",
 "deviceId":"53558"
 },
 "auth": {
 "token": "12345678"
 }
}
def myCommandCallback(cmd):
 print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
 m=cmd.data['command']
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
while True:
 temp=random.randint(-20,125)
 hum=random.randint(0,100)
 pH=random.randint(0,14)
 O2=random.randint(0,100)
 turbidity=random.randint(0,500)
 myData={'temperature':temp, 'humidity':hum, 'phvalue':pH, 'dissolved_oxygen':O2, 'Turbidity':turbidity}
 client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
 print("Published data Successfully: %s", myData)
 client.commandCallback = myCommandCallback
 time.sleep(5)
client.disconnect(5)
