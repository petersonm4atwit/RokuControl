import socket
import requests
import time

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname("192.168.0.192")
port=8060
address=(ip,port)
client.connect(address)
data = client.recv(1024)
print(data)
print("Connected")

right = "keydown/Right"
right2 = "keyup/Right"
left = "keydown/Left"
left2 = "keyup/Left"
up = "keydown/Up"
up2 = "keyup/Up"
down = "keydown/Down"
down2 = "keyup/Down"
home = "keydown/Home"
home2 = "keyup/Home"
back = "keydown/Back"
back2 = "keyup/Back"
enter = "keydown/Enter"
enter2 = "keyup/Enter"
info = "keydown/Info"
info2 = "keyup/Info"
select = "keydown/Select"
select2 = "keyup/Select"

appsQ = "/query/apps"
deviceQ = "/query/device-info"


url = ("http://%s:%s/%s" % (ip, port, home))
r = requests.post(url)
url = ("http://%s:%s/%s" % (ip, port, home2))
r = requests.post(url)
time.sleep(0.5)
url = ("http://%s:%s/%s" % (ip, port, right))
r = requests.post(url)
url = ("http://%s:%s/%s" % (ip, port, right2))
r = requests.post(url)
time.sleep(0.5)
url = ("http://%s:%s/%s" % (ip, port, select))
r = requests.post(url)
url = ("http://%s:%s/%s" % (ip, port, select2))
r = requests.post(url)
#apps = ("http://%s:%s/%s" % (ip, port, appsQ))
#step2 = requests.get(apps)
#print(step2.content)
