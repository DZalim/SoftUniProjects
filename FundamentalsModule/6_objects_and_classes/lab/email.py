class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


messages = []

information = input()
while information != "Stop":
    sender, receiver, content = information.split()
    email = Email(sender, receiver, content)
    messages.append(email)
    information = input()

send_emails = [int(index) for index in input().split(", ")]

for index in send_emails:
    messages[index].send()

for current_email in messages:
    print(current_email.get_info())
