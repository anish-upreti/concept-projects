from abc import ABC, abstractmethod
    
class NotificationPlugin(ABC):
    
    @abstractmethod
    def send(self, message, recipient):
        """This method must be implemented by all subclasses."""
        pass

    @staticmethod
    def validate_message(message):
        if not message:
            raise ValueError("Message cannot be empty")


class EmailPlugin(NotificationPlugin):
    def __init__(self, smtp_server):
        self.smtp_server = smtp_server

    def send(self, message, recipient):
        EmailPlugin.validate_message(message)
        print(f"Greetings {recipient}\n {message}\n Sent via {self.smtp_server}")
        with open("notification.log", "a") as f:
            f.write(f"Greetings {recipient}\n {message}\n Sent via {self.smtp_server}\n")


class SMSPlugin(NotificationPlugin):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def send(self, message, recipient):
        SMSPlugin.validate_message(message)
        print(f"Namaste {recipient} \n {message} \n Sent via {self.phone_number}")
        with open("notification.log", "a") as f:
            f.write(f"Namaste {recipient} \n {message} \n Sent via {self.phone_number}\n")


class SlackPlugin(NotificationPlugin):
    def __init__(self, channel):
        self.channel = channel

    def send(self, message, recipient):
        SlackPlugin.validate_message(message)
        print(f"Ciao {recipient} \n {message} \n Sent via channel: {self.channel}")
        with open("notification.log", "a") as f:
            f.write(f"Ciao {recipient} \n {message} \n Sent via channel: {self.channel}\n")

class PluginManager:
    def __init__(self):
        self.plugins = []

    def register(self, plugin):
        self.plugins.append(plugin)

    def notify_all(self, message, recipient):
        for plugin in self.plugins:
            plugin.send(message, recipient)

    def notify_one(self, plugin_name, message, recipient):
        for plugin in self.plugins:
            if plugin.__class__.__name__ == plugin_name:
                plugin.send(message, recipient)
                break         # found the plugin, so stop looping
        else:
            print("Plugin not found")     # only runs if break doesn't happen

## Test

manager = PluginManager()
manager.register(EmailPlugin("smtp.gmail.com"))
manager.register(SMSPlugin("+977-9812258478"))
manager.register(SlackPlugin("#general"))

manager.notify_all("System is down!", recipient="anish@example.com")

manager.notify_one("SlackPlugin", "Test message", "anish@example.com")
manager.notify_one("WhatsAppPlugin", "Test message", "anish@example.com")