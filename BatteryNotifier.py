import psutil
from plyer import notification
import time

while True:
    battery = psutil.sensors_battery()
    percent = battery.percent
    timeleft = battery.secsleft
    power = battery.power_plugged

    hours, remainder = divmod(timeleft, 3600)
    minutes, seconds = divmod(remainder, 60)


    def plugpower():
        if power:
            return "charger plugged in!"
        else:
            return "charger not plugged in!"
        
    notification.notify(
        title="Battery Percentage",
        message=f"{percent}% Battery remaining\n{hours}h {minutes}m {seconds}s left\n{plugpower()}",
        timeout=10
    )

    time.sleep(60*60)