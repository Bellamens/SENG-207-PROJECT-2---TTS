# SENG 207 - PROGRAMMING FOR ENGINEERS
# NAME : ISSABELLA MENSAH
# ID : 10981228
# PROJECT 2 - PART 1
# BMEN DEPARTMENT


import PySimpleGUI as sg
import pyttsx3


sg.theme('DarkBlue15')
font=('Comic Sans MS',11)

myEngine = pyttsx3.init()
myVoice = myEngine.getProperty('voices')


layoutMain = [    [sg.Text('Select the type of voice:', font=font),sg.Radio('Male', 'RADIO1', default=True, key='male',font=font),sg.Radio('Female', 'RADIO1', key='female',font=font)],
     [sg.Text('Enter text to speak:',font=font)],
     [sg.InputText(key='type'),sg.Button('Speak',font=font)],
      [sg.Text("Volume:",text_color= 'white',background_color='orange',font=font)],
    [sg.Slider(range=(0, 1), resolution=0.1, default_value=0.5, orientation="h", key="-VOLUME-")],
    [sg.Text("Rate:",text_color= 'white',background_color='orange',font=font)],
    [sg.Slider(range=(100, 300), resolution=10, default_value=200, orientation="h", key="-SPEED-")]
]

win = sg.Window('Bella Text-To-Speech', layoutMain,font=font)

while True:
    event, values = win.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        if values['male']:
            myEngine.setProperty('voice', myVoice[0].id)
        elif values['female']:
           myEngine.setProperty('voice', myVoice[1].id)

        
        text = values['type']
        userVolume = values["-VOLUME-"]
        userRate = values["-SPEED-"]
        myEngine.setProperty('volume', userVolume)
        myEngine.setProperty("rate", userRate)
        myEngine.say(text)
        myEngine.runAndWait() 
    
        myEngine.say(text)
        myEngine.runAndWait()

win.close()