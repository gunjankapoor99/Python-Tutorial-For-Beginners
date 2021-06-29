import speech_recognition as sr
r = sr.Recogniser()
with sr.Microphone() as source:
    print("speek something: ")
    audio = r.listen(source)
    text = r.recognise_google(audio)
