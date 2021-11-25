# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from sense_hat import SenseHat
import random
import time

from socket import *

sense = SenseHat()

BROADCAST_TO_PORT = 9031

class promilleClass:
    Name = "null"
    Id = 1
    Time = 1
    alkoholNiveau = 0

def pust(s, promille):

    print("test")
    promille += random.uniform(0.1, 1)

    data = promille
    s.sendto(bytes(str(data), "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
    print(data)
    return promille

def UDP():


    promille = 0

    s = socket(AF_INET, SOCK_DGRAM)
    # s.bind(('', 14593))     # (ip, port)
    # no explicit bind: will bind to default IP + random port
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    while True:
        event = sense.stick.wait_for_event(emptybuffer=True)
        if event.direction == "middle":
            time.sleep(4)
            promille = pust(s, promille)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    UDP()


