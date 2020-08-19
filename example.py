import rpc
import time
from time import mktime

print("Demo for python-discord-rpc")
client_id = '467570845993271307'  # Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module
print("RPC connection successful.")

time.sleep(5)
start_time = mktime(time.localtime())
while True:
    activity = {
            "state": "Adobe",
            "details": "Editing",
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "Adobe",
                "small_image": "adobe",
                "large_text": "Illustrator",
                "large_image": "illustrator"
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(30)
