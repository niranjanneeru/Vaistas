# Vaistas
## Hackathon Project @ MAKE A TON

#### Stress and Health Diagonoser, Voice Assistants , Django Rest Framework API 

##### Stress and Health Diagonoser

___
Tracks
   > HeartBeat<br>
>Speech rate<br>
>Eye Blink Rate<br>
>Emotions


The __[Pitchdeck](https://prezi.com/view/6RAhoPsEw4MRdFsZ2ETn/)__ of this project.

---

## Code

Details about the __[Project](https://github.com/niranjanneeru/Vaistas)__ ,__[Backend](https://github.com/niranjanneeru/Vaistas-API)__ , ChatBot in Voiceflow which is in maintenance until 5.30 pm

---

## Set-Up

```bash
$ pip install -r requirements.txt
```


Run the main.py file

> click any of the diagnosis method avaialble 
Once you are finished click sync/History

> Now go to the chat application and talk to it
It gives you suggestions based on what you just updated

---
# Vaistas 

#### PyQT,OpenCV,Tensorflow


## Working


| Purpose | File 
|--------|------
|PyQt App Running File |      main.py|
|User Interface Design |      DSD.ui|
|Data | [train and test data for emotion](https://drive.google.com/file/d/1X60B-uR3NtqPd4oosdotpbDgy8KOfUdr/view)|
| Speech Rate |audio-speech.py|
|For Calculating Speech Rate|speech.wav|
|User Credentials Storing|cred.py|
|Haar Cascade Files|      [Eye](https://github.com/anaustinbeing/haar-cascade-files/blob/master/haarcascade_eye.xml)  [Face](https://github.com/anaustinbeing/haar-cascade-files/blob/master/haarcascade_frontalface_default.xml)|
|Heartbeat using Color Magnification Algorithm|      heartbeat.py|
|      Read the data from the server and display History|read.py |
|Upload data to server | store.py|
|Eye Blinking and Emotion Running in Threads|thread.py|

## Graph Plotting

### Line plot

Line graphs are plotted using matplotlib module
According to heartbeat range are produced

---
## Future Implementation

<ul>
  <li>NLP For Chat Bot</li> 
  <li>ML Model which predicts the state of user for details age,BMI,Heart rate, Eye Blink rate,Speech rate and Emotion</li>
</ul>

---

## Contributors


<table>
  <tr>
    1. Emil<br>
    2. Mili<br>
    3. Laveena<br>
    4. Niranjan<br>
    5. Shibin<br>
    </tr>

</table>

---

## References

> https://people.csail.mit.edu/mrub/evm/ <br>
> Haar Cascade Classifier<br>
> 5282a81a6b13b952acc5bd2d8971716096c2f2f5<br>
> Google Speech Recognition Python Library
