class Chat:
    def __init__(self, image, chatee, last_message, last_message_time):
        self.image = image
        self.chatee = chatee
        self.last_message = last_message
        self.last_message_time = last_message_time
        
    def open(self):
        return f"You just opened the chat with {self.chatee} with last_message {self.last_message} that was sent at {self.last_message_time}"
    