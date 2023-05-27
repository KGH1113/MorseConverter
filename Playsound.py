from playsound import playsound
import time
import Morse

def Playsound():
    def Dot():
        playsound("/Users/gang-guhyeon1/Desktop/Python/Morse/Dot.mp3")
        time.sleep(0.1)

    def Dash():
        playsound("/Users/gang-guhyeon1/Desktop/Python/Morse/Dash.mp3")
        time.sleep(0.3)

    for i in Morse.Eng2Morse():
        length = len(i)
        list = []
        for j in range(length):
            list.append(i[j])

        for k in list:
            if k == ".":
                Dot()
            elif k == "-":
                Dash()

Playsound()