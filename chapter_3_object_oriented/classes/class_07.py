from abc import ABC, abstractmethod
import os

os.system('cls')

class Notification(ABC):
    def __init__(self, message):
        self.message = message

    @abstractmethod
    def to_send(self) -> bool: ...

class NotificationEmail(Notification):
    def to_send(self) -> bool:
        print('Sending the e-mail: ', self.message)
        return True
    
class NotificationSMS(Notification):
    def to_send(self) -> bool:
        print('Sending the SMS: ', self.message)
        return False

def notify(notification: Notification):
    notification_sent = notification.to_send()

    if notification_sent:
        print('Notification sent!')
    else:
        print('Notification did not send!')

notification_email = NotificationEmail('testing email sending')
notify(notification_email)

notification_sms = NotificationSMS('testing sms sending')
notify(notification_sms)