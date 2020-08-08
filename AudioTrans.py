import speech_recognition as sr 
from googletrans import Translator
print("AudioFilesTranslator")

audio_sample = "audio.wav"
r = sr.Recognizer() 
##print(type(r))
with sr.AudioFile(audio_sample) as source: 
    audio = r.record(source)
##print(type(audio)) 
print("Dang doc file audio...")
ScratchTXT = r.recognize_google(audio,language = "en-EN") ##Language from the source can be edited here
print()
print("Tu ngu goc trong file audio:")
print(ScratchTXT)
traducteur = Translator()
TranslatedTXT = traducteur.translate(ScratchTXT, src='en', dest='vi') ##"src" is the source language, and "dest" the destination one; here we want to translate from French to English.
print()
print("Tu ngu da duoc dich tu audio:")
print(TranslatedTXT)

