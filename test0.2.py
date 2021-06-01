import speech_recognition as sr
import pyttsx3
import os
import webbrowser
from datetime import datetime

engine = pyttsx3.init()
recognizer  = sr.Recognizer()
micro = sr.Microphone()
login = os.getlogin()
today = datetime.now().time()

engine.say("Bonjour " + str(login) + ". Il est " + today.strftime("%H heures : %M minutes") +" que puis-je pour toi")
engine.runAndWait()
while True:
    with micro as source:
        print("Listening ...")
        audio = recognizer.listen(source,5,5)
        try:
            text = recognizer.recognize_google(audio, language="fr-FR")
            print(text)
        except sr.UnknownValueError:
            engine.say("Désolé, je n'ai pas compris")
            engine.runAndWait()


# engine.say("Bonjour " + str(login) + ". Il est " + today.strftime("%H heures : %M minutes") +" que puis-je pour toi")
# engine.runAndWait()
# with sr.Microphone() as source:
#     print("Dites quelque chose")
#     audio = r.listen(source)
#     try:
#         text = r.recognize_google(audio, language="fr-FR")
#         if 'ferme la session' ==  text:
#             engine.say('fermeture de la session')
#             engine.runAndWait()
#             os.system('shutdown -l')
#         else:
#             webbrowser.open_new(text)
#             engine.say("Voilà tous ce que j'ai trouvé à ce sujet")
#             engine.runAndWait()
#     except sr.UnknownValueError:
#         engine.say("L'audio n'as pas été compris")
#         engine.runAndWait()
#     except sr.RequestError as e:
#         print("Le service Google Speech API ne fonctionne plus" + format(e))
# #login = os.getlogin()
#engine.say("Bonjour " + str(login) + " que puis-je pour toi")
#engine.runAndWait()
#engine.say("Il est " + str(datetime.now().time()))
#print(datetime.now().time())
#engine.runAndWait()
