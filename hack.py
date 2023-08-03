import requests
import threading

def click():
    while 1:
        requests.post("http://127.0.0.1:5000/click")
for i in range(1,100):
    t = threading.Thread(target=click)
    t.start()
input("STOP")