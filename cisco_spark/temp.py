import requests
import json
# import pyspark 


# pyspark.batch([])
# Tim: ODkwNDk1NGQtY2Y0ZS00NTFkLWFhOWItOGFiNDRlNGI1MmU3OTIxYWE3YTYtNjJh
# Jae: MzNkMDAzYjQtNDM0ZS00MDNiLWExYTctMjUyNjhiZjRkOTliZDU3MGY5ZWQtY2Fl
# Ali:
#

headers = {'Authorization': 'Bearer MzNkMDAzYjQtNDM0ZS00MDNiLWExYTctMjUyNjhiZjRkOTliZDU3MGY5ZWQtY2Fl', 'content-type': 'application/json'}


# # HOW TO INVITE PEOPLE TO THAT ROOM!
payload = {'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vODhmNjEyYzAtYWYzZS0xMWU2LTkyNGQtOGQ2MDEyZGU0MDFj',
'personEmail': 'frenchsatchel@gmail.com', 'isModerator': False}
# payload = {'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vOTA3ZWU0ZjAtYWUyZi0xMWU2LTlmZjQtYTUwYzRmNTI3ODk3','personEmail': 'jng.bus.in.ass@gmail.com', 'isModerator': False}
temp = requests.post('https://api.ciscospark.com/v1/memberships',headers=headers,json= payload)
raw_input()

# HOW TO CREATE A NEW ROOM !
body = {
    "title": "f67"
}
temp = requests.post('https://api.ciscospark.com/v1/rooms',headers=headers,json= body)
people_dict = json.loads(temp.text)
print json.dumps(people_dict, indent=4, sort_keys=True)
raw_input()







# HOW TO GET ALL OF MY ROOM
temp = requests.get('https://api.ciscospark.com/v1/rooms/',headers=headers)
people_dict = json.loads(temp.text)
print json.dumps(people_dict, indent=4, sort_keys=True)
raw_input()




# HOW TO GET ALL OF MY ROOM
temp = requests.get('https://api.ciscospark.com/v1/messages/Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYjk5NzY2YTAtYWYxNS0xMWU2LTkwZjEtMzcyYjVhYmI2Yzk5',headers=headers)
people_dict = json.loads(temp.text)
print json.dumps(people_dict, indent=4, sort_keys=True)
raw_input()
# Create webhooks for the notification
# Y2lzY29zcGFyazovL3VzL1JPT00vZDg5ODA1YTAtYWU3Zi0xMWU2LWIzZDEtYmYxNzU5ZjUzYzdk
payload = {'name': 'Notification', 'targetUrl': 'http://satch.me/webhook/', 'resource': 'messages',
'event': 'created', 'filter': 'roomId=Y2lzY29zcGFyazovL3VzL1BFT1BMRS84OGVjM2M1YS1kZTRlLTQwYjMtYjg1Ny01NTQ2MmNiMTY2ZDI'}


resp = requests.post(url='https://api.ciscospark.com/v1/webhooks', json=payload, headers=headers)

raw_input()
raw_input()
# payload = {'roomId': roomid,'personEmail': 'saj.saj44200@gmail.com', 'isModerator': False}


# HOW TO CREATE A NEW ROOM !
body = {
    "title": "fdsfds567 Outfitter want to chatfdsgafdsajh with you 2"
}
temp = requests.post('https://api.ciscospark.com/v1/rooms',headers=headers,json= body)
people_dict = json.loads(temp.text)
print json.dumps(people_dict, indent=4, sort_keys=True)
raw_input()



# HOW TO GET ALL OF MY ROOM
temp = requests.get('https://api.ciscospark.com/v1/rooms',headers=headers)
people_dict = json.loads(temp.text)
print json.dumps(people_dict, indent=4, sort_keys=True)
raw_input()





# Getting the webhooks
temp = requests.get('https://api.ciscospark.com/v1/webhooks',headers=headers)
people_dict = json.loads(temp.text)
print json.dumps(people_dict, indent=4, sort_keys=True)
raw_input()


# Create webhooks for the notification
# Y2lzY29zcGFyazovL3VzL1JPT00vZDg5ODA1YTAtYWU3Zi0xMWU2LWIzZDEtYmYxNzU5ZjUzYzdk
payload = {'name': 'Notification', 'targetUrl': 'http://ec2-54-145-160-113.compute-1.amazonaws.com/Webhooks/', 'resource': 'messages',
'event': 'created', 'filter': 'roomId=Y2lzY29zcGFyazovL3VzL1JPT00vZDg5ODA1YTAtYWU3Zi0xMWU2LWIzZDEtYmYxNzU5ZjUzYzdk'}


resp = requests.post(url='https://api.ciscospark.com/v1/webhooks', json=payload, headers=headers)

raw_input()



# HOW TO CREATE A NEW ROOM !
body = {
    "title": "Urban Outfitter want to chat with you 2"
}
temp = requests.post('https://api.ciscospark.com/v1/rooms',headers=headers,json= body)
people_dict = json.loads(temp.text)
print json.dumps(people_dict, indent=4, sort_keys=True)


roomid = people_dict["id"]
# raw_input()

payload = {'roomId': roomid, 'text': 'Hey you just walk past by Urban outfitters!'}

resp = requests.post('https://api.ciscospark.com/v1/messages', json=payload, headers=headers)

# raw_input()
# payload = {'roomId': roomid,'personEmail': 'saj.saj44200@gmail.com', 'isModerator': False}
payload = {'roomId': roomid,'personEmail': 'jng.bus.in.ass@gmail.com', 'isModerator': False}

# payload = {'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vOTA3ZWU0ZjAtYWUyZi0xMWU2LTlmZjQtYTUwYzRmNTI3ODk3','personEmail': 'jng.bus.in.ass@gmail.com', 'isModerator': False}
temp = requests.post('https://api.ciscospark.com/v1/memberships',headers=headers,json= payload)


raw_input()



# 1. Getting all of the room
# temp = requests.get('https://api.ciscospark.com/v1/rooms',headers=headers)
# people_dict = json.loads(temp.text)
# print json.dumps(people_dict, indent=4, sort_keys=True)
# raw_input()

        #     "created": "2016-11-19T14:59:47.350Z",
        #     "creatorId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS84OGVjM2M1YS1kZTRlLTQwYjMtYjg1Ny01NTQ2MmNiMTY2ZDI",
        #     "id": "Y2lzY29zcGFyazovL3VzL1JPT00vZDAyODFiNjAtYWU2OC0xMWU2LTk2Y2YtNDc4YWJiYzVhODQ0",
        #     "isLocked": false,
        #     "lastActivity": "2016-11-19T14:59:47.382Z",
        #     "title": "Test Room2",
        #     "type": "group"
        # },

# Nov 18 - the room that we just created
# {
#     "created": "2016-11-19T08:09:59.231Z",
#     "creatorId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS84OGVjM2M1YS1kZTRlLTQwYjMtYjg1Ny01NTQ2MmNiMTY2ZDI",
#     "id": "Y2lzY29zcGFyazovL3VzL1JPT00vOTA3ZWU0ZjAtYWUyZi0xMWU2LTlmZjQtYTUwYzRmNTI3ODk3",
#     "isLocked": false,
#     "lastActivity": "2016-11-19T08:09:59.265Z",
#     "title": "Test Room",
#     "type": "group"
# }


# # HOW TO INVITE PEOPLE TO THAT ROOM!
payload = {'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vZDAyODFiNjAtYWU2OC0xMWU2LTk2Y2YtNDc4YWJiYzVhODQ0',
'personEmail': 'frenchsatchel@gmail.com', 'isModerator': False}
# payload = {'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vOTA3ZWU0ZjAtYWUyZi0xMWU2LTlmZjQtYTUwYzRmNTI3ODk3','personEmail': 'jng.bus.in.ass@gmail.com', 'isModerator': False}
temp = requests.post('https://api.ciscospark.com/v1/memberships',headers=headers,json= payload)

# {
#     "created": "2016-11-19T08:19:30.222Z",
#     "id": "Y2lzY29zcGFyazovL3VzL01FTUJFUlNISVAvYWIzMzcxOGMtZDNhYy00YjE1LTk4MjAtNzI0ZDg0MDY4MzYxOjkwN2VlNGYwLWFlMmYtMTFlNi05ZmY0LWE1MGM0ZjUyNzg5Nw",
# #     "isModerator": false,
# #     "isMonitor": false,
# #     "personDisplayName": "Satchel French",
# #     "personEmail": "frenchsatchel@gmail.com",
# #     "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hYjMzNzE4Yy1kM2FjLTRiMTUtOTgyMC03MjRkODQwNjgzNjE",
# #     "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vOTA3ZWU0ZjAtYWUyZi0xMWU2LTlmZjQtYTUwYzRmNTI3ODk3"
# #
