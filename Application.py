#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from ttk import *

from datetime import date
import json


class Application(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        Label(self, text="Узнай кто ты по гороскопу!").grid(row=0, columnspan=5)
        Label(self, text="Когда у тебя день рождения? дд/мм/гггг").grid(row=1)

        self.day = StringVar()
        self.month = StringVar()
        self.year = StringVar()

        Spinbox(self, from_=1, to=31, width=4, textvariable=self.day).grid(row=1, column=1)
        Spinbox(self, from_=1, to=12, width=4, textvariable=self.month).grid(row=1, column=2)
        Spinbox(self, from_=1900, to=2016, width=4, textvariable=self.year).grid(row=1, column=3)

        btn = Button(self, text="Поехали :)")
        btn.grid(row=1, column=4)
        btn.bind("<Button-1>", lambda event: self.on_submit())

        for child in self.winfo_children():
            child.grid_configure(padx=3, pady=3)
            pass

        self.sign_file_name = "sign_data.json"
        self.horoscope_file_name = "horoscope_data.json"

        pass

    def getZodiacData(self, day, month, year):
        try:
            with open(self.sign_file_name) as json_data:
                data = json.load(json_data)
                pass
            pass
        except Exception as exception:
            print "Exception {}: {}".format(type(exception), exception)
            return None
            pass

        b_date = date(year, month, day)


        for key in data:
            from_year = year
            if data[key]["minus_year"] is True:
                from_year -= 1
            from_day, from_month = tuple(data[key]["from"].split("."))
            from_date = date(from_year, int(from_month), int(from_day))

            to_day, to_month = tuple(data[key]["to"].split("."))
            to_date = date(year, int(to_month), int(to_day))

            if from_date <= b_date <= to_date:
                sign = data[key]["sign"]
                interval = "{:02d}.{:02d} - {:02d}.{:02d}".format(
                    from_date.day, from_date.month, 
                    to_date.day, to_date.month)
                description = data[key]["description"]

                return key, sign, interval, description
                pass
            pass

        return None
        pass

    def getHoroscopeData(self, key):
        try:
            with open(self.horoscope_file_name) as json_data:
                data = json.load(json_data)
                pass
            pass
        except Exception as exception:
            print "Exception {}: {}".format(type(exception), exception)
            return None
            pass

        sign = data[key]["sign"]
        horoscope = data[key]["horoscope"]
        return sign, horoscope
        pass

    def horoscope(self, key):
        horoscope_data = self.getHoroscopeData(key)
        if horoscope_data is None:
            horoscope_data is None
            return
            pass

        sign, horoscope = horoscope_data

        top = Toplevel(self)
        top.title(u"Гороскоп: {}".format(sign))
        top.focus_set()
        
        Message(top, text=horoscope).grid(row=0)

        def closeWindow(*args):
            top.destroy()
            pass

        top.bind("<Escape>", closeWindow)

        btn = Button(top, text="Закрыть")
        btn.bind("<Button-1>", closeWindow)
        btn.bind("<Return>", closeWindow)
        btn.grid(row=1)
        btn.focus_set()

        for child in top.winfo_children():
            child.grid_configure(padx=3, pady=3)
            pass
        pass

    def on_submit(self):
        try:
            day = int(self.day.get())
            month = int(self.month.get())
            year = int(self.year.get())
        except Exception as exception:
            print "Exception {}: {}".format(type(exception), exception)
            pass

        b_date = "{:02d}.{:02d}.{}".format(day, month, year)

        zodiac_data = self.getZodiacData(day, month, year)
        if zodiac_data is None:
            print "zodiac_data is None"
            return
            pass

        key, sign, interval, description = zodiac_data
        
        top = Toplevel(self)
        top.title(sign)
        top.focus_set()
        
        Label(top, text="День рождения:").grid(row=0, sticky=E)
        Label(top, text=b_date).grid(row=0, column=1, sticky=W)
        
        Label(top, text="Знак Зодиака:").grid(row=1, sticky=E)
        Label(top, text=sign).grid(row=1, column=1, sticky=W)
        
        Label(top, text="Период:").grid(row=2, sticky=E)
        Label(top, text=interval).grid(row=2, column=1, sticky=W)
        
        Label(top, text="Описание:").grid(row=3, sticky=(E, N))
        Message(top, text=description).grid(row=3, column=1)

        def openHoroscope(*args):
            self.horoscope(key)
            pass

        btn = Button(top, text="Гороскоп на неделю")
        btn.bind("<Button-1>", openHoroscope)
        btn.bind("<Return>", openHoroscope)
        btn.grid(row=4, columnspan=2)

        def closeWindow(*args):
            top.destroy()
            pass

        top.bind("<Escape>", closeWindow)

        btn = Button(top, text="Закрыть")
        btn.bind("<Button-1>", closeWindow)
        btn.bind("<Return>", closeWindow)
        btn.grid(row=5, columnspan=2)
        btn.focus_set()

        for child in top.winfo_children():
            child.grid_configure(padx=3, pady=3)
            pass

        pass
    pass