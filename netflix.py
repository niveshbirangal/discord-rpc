import rpc
import time

print("Demo for python-discord-rpc")
client_id = '467419833542377472' #Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) #Send the client ID to the rpc module
print("RPC connection successful.")

time.sleep(5)
start_time = time.time()
while True:
    activity = {
            "state": "Season 3 Episode 2",
            "details": "The Black List",
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "theblacklist",
                "small_image": "theblacklist",
                "large_text": "netflix",
                "large_image": "netflix"
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(30)