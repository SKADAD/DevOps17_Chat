
class Commands:
    def __init__(self,message_from_client_):
        self.command = message_from_client_

    def command_to_execute(self):
        print("Hej")