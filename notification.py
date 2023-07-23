import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = 'Alert',
            message = "This is a msg.",
            timeout = 2
        )
        time.sleep(10)
