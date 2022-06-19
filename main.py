import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "*Break Time*",
            message = "Your screen is on for 50 minutes. Its time for break. Break time of 10 minutes is recommended.",
            app_name = "Break Reminder",
            app_icon = "C:\Users\czans\Downloads\having_break_coffee_workspace_icon_176867.ico",
            ticker = "notification coming ...",
            timeout = 600
        )
        time.sleep(3000)
            