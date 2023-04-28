'''

Authors: Farhan Ahmad, Keyi Chai, Luyi Sun, Harish Balaji, Yikun Yang

'''

import requests
from bs4 import BeautifulSoup
import re
import os
import csv
import numpy as np
import pandas as pd
from pandasgui import show
import tkinter.ttk as ttk
from cmu_112_graphics import *
from WalnutCapitalScraping1 import walnutscraping
from RentCollegePadsScraping1 import collegepadsscraping
from TKTableR import displayTableR
from TKTableW import displayTableW
from TKTableC import displayTableC

#################################################
# Helper functions
#################################################
def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

def rgbString(red, green, blue):
     return f'#{red:02x}{green:02x}{blue:02x}'

############## MODEL #############

def appStarted(app):
    # background
    app.width = 1000
    app.height = 800
    app.margin = 50
    # main menu
    app.page = 0
    app.main = True
    app.pittsburgh = app.loadImage('Pittsburgh_Panorama.jpg') #change to your specific path if doesn't work
    #source: https://commons.wikimedia.org/wiki/File:Pittsburgh_Panorama_from_
    # the_Duquesne_Incline.jpg#/media/File:Pittsburgh_Panorama_from_the_Duquesne_Incline.jpg
    app.live = False
    app.database = False
    app.liveY = app.height*0.5+50
    app.buttonX0 = app.width*0.5
    app.buttonX1 = app.width*0.5 + 200
    # database questions
    app.uni = False
    app.uniY = app.height*0.5+20
    app.rent = False
    app.neighborhood = False
    # Based on University
    app.cmu = False
    app.upitt = False
    app.carlow = False
    app.chatham = False
    # CMU
    app.CMUMap = app.loadImage('CMUMap.jpg') #change to your specific path if doesn't work
    app.UPittMap = app.loadImage('UPittMap.jpg') #change to your specific path if doesn't work
    app.carlowMap = app.loadImage('carlowMap.jpg') #change to your specific path if doesn't work
    app.chathamMap = app.loadImage('chathamMap.jpg') #change to your specific path if doesn't work
    app.CrimeMap = app.loadImage('CrimeMap.jpg') #change to your specific path if doesn't work
    app.reset = False
    # live scraping
    app.f1 = pd.read_csv('walnutcapital_live.csv') #change to your specific path if doesn't work
    app.f2 = pd.read_csv('RentCollegePad_live.csv') #change to your specific path if doesn't work
############## CONTROLLER #############

def keyPressed(app, event):
    if (event.key == 'r') :
        print('return to the main menu')
        app.reset = True
        app.page = 0
        app.main = True
        app.live = False
        app.database = False
        app.uni = False
        app.rent = False
        app.neighborhood = False
        app.cmu = False
        app.upitt = False
        app.carlow = False
        app.chatham = False
    if (event.key == 's') :
        print('walnutcapitalscraping')
        walnutscraping()
        show(app.f1)
    if (event.key == 'v') :
        print('collegepadsscraping')
        collegepadsscraping()
        show(app.f2)
    if (event.key == 'd'):
        displayTableR()
    if (event.key == 'w'):
        displayTableW()
    if (event.key == 'c'):
        displayTableC()

def mousePressed(app, event):
    if (app.page == 0) :
        if (app.buttonX0 <= event.x <= app.buttonX1
            and app.liveY + 10 <= event.y <= app.liveY + 30):
            app.database = True
            app.page += 1
            print('choose B: database',app.page)

        if (app.buttonX0 <= event.x <= app.buttonX1
            and app.liveY - 10 <= event.y <= app.liveY + 10):
            app.live = True
            app.page += 1
            print('choose A: live scraping',app.page)
 
    elif (app.page == 1) and (app.database == True) : 
            if app.neighborhood == app.rent == False and (app.buttonX0 <= event.x <= app.buttonX1
                and app.uniY-10 <= event.y <= app.uniY+10):
                    app.uni = True
                    app.page += 1
                    print('choose based on university',app.page)

            if app.uni == app.rent == False and (app.buttonX0 <= event.x <= app.buttonX1
                and app.uniY+30 <= event.y <= app.uniY+50):
                    app.neighborhood = True
                    app.page += 1
                    print('choose based on neighborhood',app.page)
    
    elif (app.page == 2) and (app.uni == True) : 
        if (app.buttonX0 <= event.x <= app.buttonX1
            and app.height*0.5-50 <= event.y <= app.height*0.5-30):
                app.cmu = True
                app.page += 1
                print('Carnegie Mellon University',app.page)
        elif (app.buttonX0 <= event.x <= app.buttonX1
            and app.height*0.5-20 <= event.y <= app.height*0.5-10):
                app.carlow = True
                app.page += 1
                print('Carlow University',app.page)
        elif (app.buttonX0 <= event.x <= app.buttonX1
            and app.height*0.5+10 <= event.y <= app.height*0.5+30):
                app.upitt = True
                app.page += 1
                print('University of Pittsburgh',app.page)
        elif (app.buttonX0 <= event.x <= app.buttonX1
            and app.height*0.5+40 <= event.y <= app.height*0.5+60):
                app.chatham = True
                app.page += 1
                print('Chatham University',app.page)

############# VIEWER #############
def drawMainMenu(app,canvas): #1
    canvas.create_rectangle(0,0,app.width,app.height,fill = 'white')
    canvas.create_image(app.width*0.5, 100, image=ImageTk.PhotoImage(app.pittsburgh))
    canvas.create_text(app.width*0.5, 100, 
                        text ='BETTER  LIFE  IN  PGH', font = f'Arial 50 bold', 
                        fill = 'white')
    canvas.create_text(app.width*0.5, app.height*0.5-100, 
                        text ='Hello! New Pittsburghers!', font = f'Arial 20 bold', 
                        fill = 'black')
    canvas.create_line(app.width*0.5-200, app.height*0.5-25,app.width*0.5+200, app.height*0.5-25)
    canvas.create_text(app.width*0.5, app.height*0.5-50, 
                        text ='''We are here to help new domestic and international students find the best off-campus housing''', font = f'Arial 10 bold', 
                        fill = 'black')
    canvas.create_text(app.width*0.5, app.height*0.5, 
                        text ='What type of data do you want to access?', 
                        fill = 'black')
    canvas.create_rectangle(app.buttonX0,app.height*0.5+40,
                            app.buttonX1,app.height*0.5+55,fill = 'black')
    canvas.create_text(app.width*0.5, app.height*0.5+50, 
                        text ='A. Live Data Scraping', 
                        fill = 'white')
    canvas.create_rectangle(app.buttonX0,app.height*0.5+60,
                            app.buttonX1,app.height*0.5+75,fill = 'black')                    
    canvas.create_text(app.width*0.5, app.height*0.5+70, 
                        text ='B. From the Stored Database', 
                        fill = 'white')

def drawLive(app, canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill = 'white')
    canvas.create_text(app.width*0.5, app.height*0.5, 
                        text ='How would you like to begin exploring your off-campus housing?', 
                        fill = 'black')
    canvas.create_text(app.width*0.5, app.height*0.5+50, 
                        text ='''Press 's' to live scraping the Walnut Capital data''', 
                        fill = 'red')
    canvas.create_text(app.width*0.5, app.height*0.5+70, 
                        text ='''Press 'v' to live scraping the Rent College Pads data''', 
                        fill = 'red')

def drawBaseQuestion(app, canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill = 'white')
    canvas.create_text(app.width*0.5, app.height*0.5-20, 
                        text ='How would you like to begin exploring your off-campus housing?', 
                        fill = 'black')
    canvas.create_text(app.width*0.5, app.height*0.5+20, 
                        text ='1. Based on University', 
                        fill = 'black')
    canvas.create_text(app.width*0.5, app.height*0.5+60, 
                        text ='2. Based on Neighborhood', 
                        fill = 'black')

def drawUniversiy(app, canvas):
    if app.uni == True:
        canvas.create_rectangle(0,0,app.width,app.height,fill = 'white')
        canvas.create_text(100, 50, 
                            text ='''1.Based on University
                            ''', 
                            fill = 'red', anchor='n')
        canvas.create_text(app.width*0.5-50, 200, 
                            text ='Select the University you are studying at?',fill = 'black')
        #buttons
        canvas.create_rectangle(app.buttonX0,app.height*0.5-50,
                            app.buttonX1,app.height*0.5-30,fill = 'black') 
        canvas.create_text(app.width*0.5, app.height*0.5-40, 
                            text ='1. Carnegie Mellon University',
                            fill = 'white')
        canvas.create_rectangle(app.buttonX0,app.height*0.5-20,
                            app.buttonX1,app.height*0.5,fill = 'black') 
        canvas.create_text(app.width*0.5, app.height*0.5-10, 
                            text ='2. Carlow University',
                            fill = 'white')
        canvas.create_rectangle(app.buttonX0,app.height*0.5+10,
                            app.buttonX1,app.height*0.5+30,fill = 'black') 
        canvas.create_text(app.width*0.5, app.height*0.5+20, 
                            text ='3. University of Pittsburgh',
                            fill = 'white')
        canvas.create_rectangle(app.buttonX0,app.height*0.5+40,
                            app.buttonX1,app.height*0.5+60,fill = 'black') 
        canvas.create_text(app.width*0.5, app.height*0.5+50, 
                            text ='4. Chatham University',
                            fill = 'white')   
        
def drawCMU(app, canvas):
    if app.uni == True and app.cmu == True:
        canvas.create_rectangle(0,0,app.width,app.height,fill = 'white')
        canvas.create_image(app.width*0.5, app.height*0.5, image=ImageTk.PhotoImage(app.CMUMap))
        canvas.create_rectangle(40,10,380,40,fill = 'white',outline="white", width=0)
        canvas.create_text(50, 50, 
                            text ='''Off-campus Housing near Carnegie Mellon University
                            ''', 
                            fill = 'purple', anchor='sw')

def drawCarlow(app, canvas):
    if app.uni == True and app.carlow == True:
        canvas.create_rectangle(0,0,app.width,app.height,fill = 'white')
        canvas.create_image(app.width*0.5, app.height*0.5, image=ImageTk.PhotoImage(app.carlowMap))
        canvas.create_rectangle(40,10,380,40,fill = 'white',outline="white", width=0)
        canvas.create_text(50, 50, 
                            text ='''Off-campus Housing near Carlow University
                            ''', 
                            fill = 'purple', anchor='sw')

def drawUpitt(app, canvas):
    if app.uni == True and app.upitt == True:
        canvas.create_rectangle(0,0,app.width,app.height,fill = 'white')
        canvas.create_image(app.width*0.5, app.height*0.5, image=ImageTk.PhotoImage(app.UPittMap))
        canvas.create_rectangle(40,10,380,40,fill = 'white',outline="white", width=0)
        canvas.create_text(50, 50, 
                            text ='''Off-campus Housing near University of Pittsburgh
                            ''', 
                            fill = 'purple', anchor='sw')

def drawChatham(app, canvas):
    if app.uni == True and app.chatham == True:
        canvas.create_rectangle(0,0,app.width,app.height,fill = 'white')
        canvas.create_image(app.width*0.5, app.height*0.5, image=ImageTk.PhotoImage(app.chathamMap))
        canvas.create_rectangle(40,10,380,40,fill = 'white',outline="white", width=0)
        canvas.create_text(50, 50, 
                            text ='''Off-campus Housing near Chatham University
                            ''', 
                            fill = 'purple', anchor='sw')

def drawneighborhood(app, canvas):
    if app.neighborhood == True:
        canvas.create_rectangle(0,0,app.width,app.height,fill = 'white')
        canvas.create_image(app.width*0.5, app.height*0.5, image=ImageTk.PhotoImage(app.CrimeMap))
        canvas.create_text(100, 50, 
                            text ='''3.Based on Neighborhood
                            ''', 
                            fill = 'red', anchor='n')

def redrawAll(app, canvas):
    #background
    if app.main == True:
        drawMainMenu(app,canvas)
    if app.database == True:
        drawBaseQuestion(app, canvas)
        canvas.create_text(app.width-50, app.height - 70, 
                        text ='''Press 'd' to open the Rockwell table''', 
                        fill = 'maroon', anchor='e')
        canvas.create_text(app.width-50, app.height - 90, 
                        text ='''Press 'w' to open the Walnut Capital table''', 
                        fill = 'maroon', anchor='e')
        canvas.create_text(app.width-50, app.height - 110, 
                        text ='''Press 'c' to open the College Pad table''', 
                        fill = 'maroon', anchor='e')
        if app.uni == True:
            drawUniversiy(app, canvas)
            if app.cmu == True:
                drawCMU(app, canvas)
            elif app.carlow == True:
                drawCarlow(app, canvas)
            elif app.upitt == True:
                drawUpitt(app, canvas)
            elif app.chatham == True:
                drawChatham(app, canvas)
        elif app.neighborhood == True:
            drawneighborhood(app, canvas)

    elif app.live == True :
        drawLive(app, canvas)
                
    canvas.create_text(app.width*0.5, app.height - 10, 
                        text ='''copyright@Better Life in Pittsburgh''',
                        fill = 'maroon', anchor='s')
    canvas.create_text(app.width*0.5, app.height - 40, 
                        text ='''Press 'r' to return to the main menu''',
                        fill = 'maroon')

runApp(width = 1200, height =800)