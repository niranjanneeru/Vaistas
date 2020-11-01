import pickle

import speech_recognition as sr

r = sr.Recognizer()

file_audio = sr.AudioFile('speech.wav')

with file_audio as source:
    audio_text = r.record(source)

print(type(audio_text))
print(r.recognize_google(audio_text))


def word_count(str):
    counts = 0
    words = str.split()

    for word in words:
        counts = counts + 1

    return counts


with open('pickles/speech_rate.pickle','wb') as file:
    print()
    pickle.dump(word_count(r.recognize_google(audio_text)), file)
