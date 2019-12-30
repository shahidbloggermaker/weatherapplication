#-------------------------------------------------------------------------------
# Name:        Weather Application by BoredProgrammers
# Purpose:     Open Source
#
# Author:      BoredProgrammers
#
# Created:     26/12/2019
# Copyright:   (c) BoredProgrammers 2019
# Website:     www.boredprogrammers.com
#-------------------------------------------------------------------------------
import requests as rt
import tkinter as tk
from tkinter import messagebox
import colour

#https://api.openweathermap.org/data/2.5/weather?q=Delhi,In&appid=2ba176b6779095cdadce08734e517654

class connection:
    def __init__(self):
        return None

    def responsecheck(self,link):
        self.response = rt.get(link)
        if self.response.status_code == 401:
            return "Error 401"
        else:
            self.jsondata = self.response.json()
        return self.jsondata

class graphical:
    def __init__(self,twindow):
        self.twindow = twindow
        self.link = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=2ba176b6779095cdadce08734e517654"
        self.country = tk.Label(twindow,text="Country:- ",bg='#0066cc',fg='white',font=("Times", "16", "bold"),padx=30)
        self.countrytext = tk.Label(twindow,text="NIL",bg='#0099ff',fg='white',font=("Times", "16", "bold"),padx=20)
        self.country.grid(row=1,column=0,sticky=tk.W)
        self.countrytext.grid(row=1,column=1,sticky=tk.E)

        self.location = tk.Label(twindow,text="Location:- ",bg='#0066cc',fg='white',font=("Times", "16", "bold"),padx=26.5)
        self.locationtext = tk.Label(twindow,text="NIL",bg='#0099ff',fg='white',font=("Times", "16", "bold"),padx=24)
        self.location.grid(row=2,column=0,sticky=tk.W)
        self.locationtext.grid(row=2,column=1,sticky=tk.E)

        self.degree = tk.Label(twindow,text="Degree:- ",bg='#0066cc',fg='white',font=("Times", "16", "bold"),padx=35)
        self.degreetext = tk.Label(twindow,text="NIL",bg='#0099ff',fg='white',font=("Times", "16", "bold"),padx=20)
        self.degree.grid(row=3,column=0,sticky=tk.W)
        self.degreetext.grid(row=3,column=1,sticky=tk.E)

        self.enterlocation = tk.Label(twindow,text="Enter location:- ",bg='#0066cc',fg='white',font=("Times", "16", "bold"),padx=3)
        self.textbox = tk.Text(twindow,height=1,width=15)
        self.enterlocation.grid(row=4,column=0,sticky=tk.W)
        self.textbox.grid(row=4,column=1,sticky=tk.E)

        self.searchbutton = tk.Button(twindow,height=2,width=15,text="Search Location",padx=20,command=self.locini)
        self.searchbutton.grid(row=5,column=1)

        self.tempcolorbar = tk.Button(twindow,height=2,width=15,text="Temp Bar",command=self.temcolobar,padx=20)
        self.tempcolorbar.grid(row=5,column=0)

    def temcolobar(self):
        messagebox.showinfo("Temperature info", "Mainwindow Background shows the temperature color")

    def locini(self):
        self.colorcode = ""
        self.tempvar = self.textbox.get('1.0',tk.END)
        self.templink = self.link.format(self.tempvar)
        self.obj = connection()
        self.data = self.obj.responsecheck(self.templink)

        print(self.data)
        if self.data == {'cod': '404', 'message': 'city not found'}:
            return None
        else:
            if int(self.data["main"]["temp"])-273 < 0:
                self.twindow.configure(background="#3366cc")
            elif int(self.data["main"]["temp"])-273 > 0 and int(self.data["main"]["temp"])-273 < 10:
                self.twindow.configure(background="#0099ff")
            elif int(self.data["main"]["temp"])-273 > 10 and int(self.data["main"]["temp"])-273 < 20:
                self.twindow.configure(background="#99ccff")
            elif int(self.data["main"]["temp"])-273 > 20 and int(self.data["main"]["temp"])-273 < 30:
                self.twindow.configure(background="#ffff66")
            elif int(self.data["main"]["temp"])-273 > 30 and int(self.data["main"]["temp"])-273 < 40:
                self.twindow.configure(background="#ffff00")
            elif int(self.data["main"]["temp"])-273 > 40:
                self.twindow.configure(background="#cc9900")
            self.degreetext = tk.Label(self.twindow,text=int(self.data["main"]["temp"])-273,bg='#0099ff',fg='white',font=("Times", "16", "bold"),padx=20)
            self.degreetext.grid(row=3,column=1,sticky=tk.E)

            self.countrytext = tk.Label(self.twindow,text=self.data["sys"]["country"],bg='#0099ff',fg='white',font=("Times", "16", "bold"),padx=20)
            self.countrytext.grid(row=1,column=1,sticky=tk.E)

            self.locationtext = tk.Label(self.twindow,text=self.data["name"],bg='#0099ff',fg='white',font=("Times", "16", "bold"),padx=24)
            self.locationtext.grid(row=2,column=1,sticky=tk.E)

main = tk.Tk()
main.geometry("310x250")
main.resizable(0, 0)
main.title("Weather Application ")
colorcode = ""
main.configure(background='#0099ff')
g = graphical(main)
g.locini()

main.mainloop()