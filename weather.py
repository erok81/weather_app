import tkinter as tk
import requests
from tkinter import font

height = 500
width = 600
# API Key: 947a8d0e8e98c51e035fba276dd9d67
# API Call: api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

def get_weather(entry):
    weather_key = '947a8d0e8e98c510e035fba276dd9d67'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key,
              'q': entry,
              'units': 'imperial',
             }
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)

def format_response(weather):
    try:
        city = weather['name']
        conditions = weather['weather'][0]['description'].title()
        temperature = weather['main']['temp']
        return f'City: {city} \nCurrent Conditions: {conditions} \nCurrent Temp: {temperature} \u00b0F'
    except:
        return 'Sorry that city was not valid. Please re-enter'

root = tk.Tk()

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

background_image = tk.PhotoImage(file='bg.png')
backgound_label = tk.Label(root, image=background_image)
backgound_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Monospace', 15))
entry.place(relwidth=0.64, relheight=1)

button = tk.Button(frame, text='Get Weather', font=('Monospace', 10), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg='white', font=('Monospace', 15), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()