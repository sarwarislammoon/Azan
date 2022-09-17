from os import path
from pydub import AudioSegment

src = "Fajar.mp3"
dst = "Fajar.wav"

sound=AudioSegment.from_mp3(src)
sound.export(dst, format="wav") 


