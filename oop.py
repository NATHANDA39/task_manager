# class Chat:
#     def __init__(self, chatee, last_message, last_message_time):
#         self.chatee = chatee
#         self.last_message = last_message
#         self.last_message_time = last_message_time

#     def open(self):
#         return f"You just opened the chat with {self.chatee} with last_message {self.last_message} that was sent at {self.last_message_time}"
    
class Chat:
    def __init__(self, chatee, last_message, last_message_time):
        self.chatee = input ("Who are you chatting with? \n")
        self.last_message = input ("What was your last message? \n")
        self.last_message_time = input ("What time was the last message sent? \n")
    def  __str__(self):
        return f"You are chatting with {self.chatee}"

    def open(self):
        return f"You just opened the chat with {self.chatee} with last_message {self.last_message} that was sent at {self.last_message_time}"
    
    