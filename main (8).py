from gtts import gTTS
from playsound import playsound
from englisttohindi.englisttohindi import EngtoHindi

a=input("write what you want converted from English to Hindi")

message = a
var = EngtoHindi(message=message)

text=var.convert
var = gTTS(text=text, lang="hi")
var.save("hin.mp3")
playsound(".\hin.mp3")