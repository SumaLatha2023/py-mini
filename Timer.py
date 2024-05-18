import time

def count(t):

    while t:
        min, sec = divmod(t,60)
        hr, min = divmod(min,60)

        timer = (f"{hr:02d}:{min:02d}:{sec:02d}")
        print(timer, end="\r")

        time.sleep(1)
        t -= 1

    print("TIME UP !!")

input_time = input("Enter the time to set the timer (hh:mm:ss) ")
h, m, s = map(int,input_time.split(":"))

total_seconds = h*3600 + m*60 + s
count(total_seconds)