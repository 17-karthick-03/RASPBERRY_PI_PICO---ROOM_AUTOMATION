# RASPBERRY_PI_PICO---ROOM_AUTOMATION

THE PURPOSE OF THIS PROJECT IS TO CONTROL THE ROOM APPLIANCE LIKE FAN AND LIGHT

# REQUIREMENTS
⭐ RASPBERRY PI PICO W

⭐ 2 CHANNEL RELAY MODULE ( IT'S DEPENDS UPON YOUR USAGE)

⭐ JUMPER WIRES

⭐ 5V EXTRNAL ADAPTER FOR POWERING PICO

COPY THE FILES main.py AND pico_2.html TO PICO W

# IT'S MY CODE EXPLANATION...

1.Connect Relay Line 1 in Pico GP16 to control Light

LiGhT = Pin(16,Pin.OUT)

2.Connect Relay Line 1 in Pico GP14 to control Fan

FaN = Pin(14,Pin.OUT)


RELAY PIN OUTS
CONNECT GROUND WIRE DIRECTLY TO YOUR APPLIANCE
CONNECT LINE WIRE TO RELAY'S COMMON PIN
CONNECT NORMALLY OPEN WITH OTHER END OF APPLIANCE

CONNECT YOUR HOME WIFI NETWORK
wlan.connect("SSID","PASSWORD")

LET CONNECT WITH ABOVE MENTIONED WIFI NETWORK
"""wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    time.sleep(1)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('wifi connection failed')"""

THIS LINE WILL DISPLAY THE IP ADDRESS, WHICH YOU SIMPLE COPY AND PASTE IT ON YOUR FAVOURITE BROWSER AND CONTROL YOUR ROOM LINE AND FAN
print('IP: ', ip)
OR SIMPLY GO TO SETTING AND SELECT WIFI AND SELECT DETAIL SEE WIFI IP'S ADDR

CONTROL YOUR ROOM LIGHT AND FAN LIKE SMART WAY 😌
