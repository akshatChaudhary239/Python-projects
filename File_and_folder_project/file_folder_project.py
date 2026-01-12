import pyttsx3
engine = pyttsx3.init()
engine.say("hello my name is akku and iam doing a great job curently")
engine.runAndWait()


def parse_command(command):
    command = command.lower()
    if "create" in command:
        words = command