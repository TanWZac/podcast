import pyttsx3

def launch(text):
    engine = pyttsx3.init(driverName='sapi5')
    engine.setProperty("rate", 180)
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    f = open("dummy text", "r")
    launch(f.read())