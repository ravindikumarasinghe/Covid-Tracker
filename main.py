import tkinter as tk
from tkinter import *
import requests
import datetime


def getCovidData():
    api = "https://disease.sh/v3/covid-19/all"
    json_data = requests.get(api).json()
    total_cases = str(json_data['cases'])
    total_deaths = str(json_data['deaths'])
    today_cases = str(json_data['todayCases'])
    today_deaths = str(json_data['todayDeaths'])
    today_recovered = str(json_data['todayRecovered'])
    updated_at = json_data['updated']
    date = datetime.datetime.fromtimestamp(updated_at / 1e3)
    label.config(text="Total cases        : " + today_cases +
                      "\nTotal Deaths   : " + today_deaths +
                      "\nToday Cases      : " + today_cases +
                      "\nToday Deaths : " + today_deaths +
                      "\nToday Recovered : " + today_recovered)
    label2.config(text=date)


canvas = tk.Tk()
canvas.geometry("800x500")
canvas.title("Ultimate Covid Tracker")
canvas = tk.Canvas(bg="black")
canvas.pack(expand=True, fill="both")
gif = PhotoImage(file="images/blue-world.png")
canvas.create_image(0, 0, image=gif, anchor="nw")
# my_label = Label(canvas, image=gif)
# my_label.place(x=0, y=0, relwidth=1, relheight=1)

fx = ("Open Sans", 20, "bold")
f1 = ("Open Sans", 16)
f2 = ("Open Sans", 12)

login_btn = PhotoImage(file='images/refresh.png')
img_label = Label(image=login_btn)
# img_label.pack(pady=20)

labelX = tk.Label(canvas, font=fx, bg="black", fg="cyan", text="Epidemic Data")
labelX.pack(pady=20)

label = tk.Label(canvas, font=f1, bg="black", fg="white")
label.pack(pady=60)

label2 = tk.Label(canvas, font=f2, bg="black", fg="white")
label2.pack(pady=20)
getCovidData()

button = tk.Button(canvas, font=f1, image=login_btn, command=getCovidData, borderwidth=0, highlightthickness=0)
button.pack(pady=0)

canvas.mainloop()
