import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Record audio from a microphone
with sr.Microphone() as source:
    print("Say something...")
    audio = recognizer.listen(source)

# audio_path = 'Downloads\\audio1.mp3' 
# audio = recognizer.listen(audio_path)

# Use a speech recognition engine to convert audio to text
try:
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
