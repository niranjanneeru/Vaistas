import requests
import pickle

response = dict()
with open('pickles/name.pickle','rb') as file:
    response['name'] = pickle.load(file)
with open('pickles/age.pickle','rb') as file:
    response['age'] = pickle.load(file)
with open('pickles/gender.pickle','rb') as file:
    response['gender'] = pickle.load(file)
with open('pickles/weight.pickle','rb') as file:
    response['weight'] = pickle.load(file)
with open('pickles/height.pickle','rb') as file:
    response['height'] = pickle.load(file)
with open('pickles/heart_rate.pickle','rb') as file:
    response['heart_beat_rate'] = pickle.load(file)
with open('pickles/eye_blink_count.pickle','rb') as file:
    response['eye_blink_rate'] = pickle.load(file)
with open('pickles/emotion.pickle','rb') as file:
    response['emotion'] = pickle.load(file)
with open('pickles/speech_rate.pickle','rb') as file:
    response['speech_rate'] = pickle.load(file)

print(response)

r = requests.post("https://makeatonapi.herokuapp.com/",data=response)
if(r.status_code!=200):
    print(r.json())