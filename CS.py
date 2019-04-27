import rpc
import time

print("Demo for python-discord-rpc")
client_id = '467426060422873121' #Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) #Send the client ID to the rpc module
print("RPC connection successful.")

time.sleep(5)
start_time = time.time()
while True:
    activity = {
            "state": "In MatchMaking",
            "details": "Rank:Supreme Master First Class",
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "rank",
                "small_image": "rank",
                "large_text": "counterstrike",
                "large_image": "counterstrike"
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(30)