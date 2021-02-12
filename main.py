from pypresence import Presence
import time

with open('credentials.txt', 'r') as credentials:
    client_id = credentials.readline()
    large_image = credentials.readline()

RPC = Presence(client_id)  # Initialize the Presence client
RPC.connect()
buttons = [{"label": "Join the House of Bingus", "url": "https://discord.gg/bingus"},
           {"label": "Get this RP", "url": "https://github.com/gustavs-vagalis/bingus-richpresence"}]

while True:
    RPC.update(
        large_image=large_image,
        details='My beloved',  # Reads image key from argument #2
        large_text='Bingus',
        buttons=buttons
    )
    time.sleep(15)
