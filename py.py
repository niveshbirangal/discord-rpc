import rpc
import time

print("Demo for python-discord-rpc")
client_id = '467257551227191306' #Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) #Send the client ID to the rpc module
print("RPC connection successful.")

time.sleep(5)
start_time = time.time()
while True:
    activity = {
            "state": "10 Pages open",
            "details": "Editing scripts",
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "small",
                "small_image": "small",
                "large_text": "large",
                "large_image": "large"
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(30)