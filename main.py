from machine import Pin
import socket
import network
import time

#Connect Relay Line 1 in Pico GP16 to control Light
LiGhT = Pin(16,Pin.OUT)
#Connect Relay Line 1 in Pico GP14 to control Fan
FaN = Pin(14,Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("SSID","PASSWORD")

#Configure Pico W with your Home wifi network
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    time.sleep(1)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('wifi connection failed')
else:
    #Display the success message with IP address
    print('connected')
    ip=wlan.ifconfig()[0]
    print('IP: ', ip)

def webpage():
    #Open the HTML file as read mode
    page = open("pico_2.html", "r")
    html = page.read()	
    page.close()
    return html

def serve(connection):
    while True:
        #Get the request from user to control Light and Fan
        client = connection.accept()[0]
        req = client.recv(1024)
        req = str(req)
        
        try:
            req = req.split()[1]
        except IndexError:
            pass
        #Check the Request and perform action according to the request
        #print(req)
        if req =='/light-on?':
            LiGhT.value(0)
        elif req =='/light-off?':
            LiGhT.value(1)
        elif req =='/fan-on?':
            FaN.value(0)
        elif req =='/fan-off?':
            FaN.value(1)
                  
        #Call the function webpage()  
        html=webpage()    
        client.send(html)
        client.close()

def open_socket(ip):
    #Create a Socket to make a communication between Pico and User to control the ON/OFF
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    print(connection)
    return(connection)

try:
    if ip is not None:
        connection=open_socket(ip)
        serve(connection)
except KeyboardInterrupt:
    machine.reset()
