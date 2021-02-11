from pypresence import Presence
import time
import sys

client_id = str(sys.argv[1])  # Reads client ID from argument #1
print(sys.argv)
RPC = Presence(client_id)  # Initialize the Presence client
RPC.connect()
buttons = [{"label": "Join the House of Bingus", "url": "https://discord.gg/bingus"},  # Clickable RP buttons
           {"label": "Get this status for yourself", "url": "https://github.com/gustavs-vagalis/bingus-richpresence"}]

while True:
    RPC.update(
        details="My beloved",
        large_image=str(sys.argv[2]),  # Reads image key from argument #2
        large_text="Bingus",
        buttons=buttons
    )
    time.sleep(15)
