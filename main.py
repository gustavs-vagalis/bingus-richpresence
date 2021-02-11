from pypresence import Presence
import time
import sys

client_id = str(sys.argv[1])  # Reads client ID from argument #1
print(sys.argv)
RPC = Presence(client_id)  # Initialize the Presence client
RPC.connect()
buttons = [{"label": "Join the House of Bingus", "url": "https://discord.gg/bingus"}]

while True:
    RPC.update(
        large_image=str(sys.argv[2]),
        details="My beloved",  # Reads image key from argument #2
        large_text="Bingus",
        buttons=buttons
    )
    time.sleep(15)
