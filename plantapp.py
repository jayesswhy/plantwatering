import os
from datetime import datetime
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

class Plant(object):
    def __init__(self, name, freq):
        self.name = name
        self.freq = freq

    def __str__(self):
        return "Plant: " + self.name + ", water " + str(self.freq) + " times a week"


basil = Plant("basil", 2)
catnip = Plant("catnip", 3)
chives = Plant("basil", 2)
kale = Plant("kale", 5)
dill = Plant("dill", 3)
coriander = Plant("coriander", 3)
plants = [basil, catnip, chives, kale, dill, coriander]
dayN = datetime.now().timetuple().tm_yday

def plantsToWater(plants, dayN):
    wateringList = []
    for p in plants:
        if dayN % p.freq == 0:
            wateringList.append(p.name)

    return wateringList

# PlantList -> String
def formatMessage(waterList):
    return "Please water the following plants today:\n" + '\n'.join(waterList)

waterList = plantsToWater(plants,dayN)
message = formatMessage(waterList)



# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=message,
                     from_=os.getenv('from_number'),
                     to=os.getenv('to_number')
                 )

print(message.sid)
