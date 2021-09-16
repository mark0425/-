#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.7),
    on 七月 17, 2019, at 17:11
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.' 
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import randint, normal, shuffle
import random
import os  # handy system and path functions
import sys  # to get file system encoding
import pandas as pd
import socket
from socket import AF_INET, SOCK_DGRAM
import json

# setting routines time
showIDScreenTime = 4.000000
Fixation4sTime = 4.000000
DEC1Time = 10.000000
TRA1Time = 3.000000
FB1Time = 3.000000
ISITime = 2.000000
DEC2Time = 15.000000
ITITime = 2.000000

# setting clock
ExperimentClock = core.Clock()

# record missing times
missedCountList = [0, 0, 0, 0, 0, 0]

# only 1 player
missedCount = 0

# default currentTrial num
currentTrial = 0

# Not Missing Trial List 
not_missing_list = []

# all gifts' code to their gift name, picture file name and price
giftsDict = {'A':['透明文具袋',     'images/gift_A.png', 35],  'B':['濕拭衛生紙 10 抽', 'images/gift_B.png', 49],  
			 'C':['記帳本',         'images/gift_C.png', 75],  'D':['按鍵式魔擦筆',   'images/gift_D.png', 75], 
			 'E':['U型充氣頸枕',    'images/gift_E.png', 99],  'F':['吸水杯墊',        'images/gift_F.png', 127], 
			 'G':['漱口杯',         'images/gift_G.png', 129], 'H':['茶包30入',       'images/gift_H.png', 129],
			 'I':['隨行水杯',       'images/gift_I.png', 135], 'J':['素色馬克杯',      'images/gift_J.png', 140], 
			 'K':['素色環保飲料提袋','images/gift_K.png', 180], 'L':['大衣防塵罩',      'images/gift_L.png', 185],
			 'M':['日檢N3-N5單字書','images/gift_M.png', 197], 'N':['手機指環支架',     'images/gift_N.png', 199], 
			 'O':['夾腳拖',         'images/gift_O.png', 199], 'P':['隨身碟16GB X1',   'images/gift_P.png', 229],
			 'Q':['USB桌上風扇',    'images/gift_Q.png', 249], 'R':['防滑保暖手套',     'images/gift_R.png', 250], 
			 'S':['止滑地墊',       'images/gift_S.png', 255], 'T':['透氣坐墊/椅墊',     'images/gift_T.png', 290],
			 'U':['貓咪造型小夜燈',  'images/gift_U.png', 299], 'V':['角落生物防水束口袋','images/gift_V.png', 299], 
			 'W':['保濕沐浴乳3入組', 'images/gift_W.png', 329], 'X':['不銹鋼餐具組',    'images/gift_X.png', 330],}


# read prepare run's data
df_fixed = pd.read_excel('ExchangeGift_runset.xlsx')
df_random = pd.read_excel('ExchangeGift_random_runset.xlsx')

# WinSize [1920,1080] to [1024,768]
def to_1024_768_2D(x1,y1):

    if int(win.size[0]) == 1024:
        x2 = x1*1.3*(1024/1920)
        y2 = y1*(768/1080)
        a = (x2,y2)

    else:
        a = (x1,y1)
        
    return a
def to_1024_768_1D(y):

    if int(win.size[0]) == 1024:
        y2 = y*(768/1080)

    else:
        y2 = y
        
    return y2

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.7'
expName = 'ExchangeGift'  # from the Builder filename that created this script
expInfo = {'ID': 'A', 'Practice' : 1, 'Participants(2/4/6)': 4, 'Random': 1}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion
practice_flag = int(expInfo['Practice'])

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['ID'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Mark\\Documents\\PsychoPy\\ExchangeGift\\ExchangeGift_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1024, 768], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "PressEnterScreen"
PressEnterScreenClock = core.Clock()
textPressEnter = visual.TextStim(win=win, name='textPressEnter',
    text='Welcome to the experiment\nPress SPACE to continue.',
    font='Microsoft JhengHei UI',
    pos=(0, 0), height=to_1024_768_1D(0.07), wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
textWelcomeScreen = visual.TextStim(win=win, name='textWelcomeScreen',
    text='Wait for trigger...',
    font='Microsoft JhengHei UI',
    pos=(0, 0), height=to_1024_768_1D(0.07), wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "IDscreen"
IDscreenClock = core.Clock()
textIDscreen = visual.TextStim(win=win, name='textIDscreen',
    text='default text',
    font='Microsoft JhengHei UI',
    pos=(0, 0), height=to_1024_768_1D(0.07), wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Fixation4s"
Fixation4sClock = core.Clock()
textPlus = visual.TextStim(win=win, name='textPlus',
    text='+',
    font='Microsoft JhengHei UI',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "DEC1"
DEC1Clock = core.Clock()
textDEC1 = visual.TextStim(win=win, name='textDEC1',
    text='default text',
    font='Microsoft JhengHei UI',
    pos=to_1024_768_2D(-0.3, 0.35), height=to_1024_768_1D(0.07), wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
imageGift1 = visual.ImageStim(
    win=win,
    name='imageGift1', 
    image='sin', mask=None,
    ori=0, pos=to_1024_768_2D(-0.35, -0.01), size=to_1024_768_2D(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
imageGift2 = visual.ImageStim(
    win=win,
    name='imageGift2', 
    image='sin', mask=None,
    ori=0, pos=to_1024_768_2D(0.35, -0.01), size=to_1024_768_2D(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
textGift1 = visual.TextStim(win=win, name='textGift1',
    text='default text',
    font='Microsoft JhengHei UI',
    pos=to_1024_768_2D(-0.35, -0.3), height=to_1024_768_1D(0.065), wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
textGift2 = visual.TextStim(win=win, name='textGift2',
    text='default text',
    font='Microsoft JhengHei UI',
    pos=to_1024_768_2D(0.35, -0.3), height=to_1024_768_1D(0.065), wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
textGift1Price = visual.TextStim(win=win, name='textGift1Price',
    text='default text',
    font='Microsoft JhengHei UI',
    pos=to_1024_768_2D(-0.35, -0.4), height=to_1024_768_1D(0.07), wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
textGift2Price = visual.TextStim(win=win, name='textGift2Price',
    text='default text',
    font='Microsoft JhengHei UI',
    pos=to_1024_768_2D(0.35, -0.4), height=to_1024_768_1D(0.07), wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "AllianceCheckWait"
AllianceCheckWaitClock = core.Clock()
textWait = visual.TextStim(win=win, name='textWait',
    text='+',
    font='Microsoft JhengHei UI',
    pos=(0, 0), height=(0.07), wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "TRA1"
TRA1Clock = core.Clock()
textTRA1 = visual.TextStim(win=win, name='textTRA1',
    text='+',
    font='Microsoft JhengHei UI',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "FB1"
FB1Clock = core.Clock()
textFB1 = visual.TextStim(win=win, name='textFB1',
    text='default text',
    font='Microsoft JhengHei UI',
    pos=to_1024_768_2D(-0.35, 0.35), height=to_1024_768_1D(0.07), wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
imageFB = visual.ImageStim(
    win=win,
    name='imageFB', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=to_1024_768_2D(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
textGift3 = visual.TextStim(win=win, name='textGift3',
    text='default text',
    font='Microsoft JhengHei UI',
    pos=to_1024_768_2D(0, -0.35), height=to_1024_768_1D(0.07), wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
textPlus_3 = visual.TextStim(win=win, name='textPlus_3',
    text='+',
    font='Microsoft JhengHei UI',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "DEC2"
DEC2Clock = core.Clock()
textDEC2 = visual.TextStim(win=win, name='textDEC2',
    text='Enter selling price',
    font='Microsoft JhengHei UI',
    pos=to_1024_768_2D(-0.35, 0.35), height=to_1024_768_1D(0.07), wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
imageDEC2 = visual.ImageStim(
    win=win,
    name='imageDEC2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.07), size=to_1024_768_2D(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
textGiftDEC2 = visual.TextStim(win=win, name='textGiftDEC2',
    text='default text',
    font='Microsoft JhengHei UI',
    pos=to_1024_768_2D(0, -0.18), height=to_1024_768_1D(0.07), wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
textDECzero = visual.TextStim(win=win, name='textDECzero',
    text='NT 0 <',
    font='Microsoft JhengHei UI',
    pos=to_1024_768_2D(-0.4, -0.3), height=to_1024_768_1D(0.075), wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
textDECthreeHund = visual.TextStim(win=win, name='textDECthreeHund',
    text='< NT 330',
    font='Microsoft JhengHei UI',
    pos=to_1024_768_2D(0.42, -0.3), height=to_1024_768_1D(0.075), wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
textInput = visual.TextStim(win=win, name='textInput',
    text='default text',
    font='Microsoft JhengHei UI',
    pos=to_1024_768_2D(-0.17, -0.3), height=to_1024_768_1D(0.075), wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
textPlus_4 = visual.TextStim(win=win, name='textPlus_4',
    text='+',
    font='Microsoft JhengHei UI',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "BDM"
BDMClock = core.Clock()
textTrial = visual.TextStim(win=win, name='textTrial',
    text='default text',
    font='Microsoft JhengHei UI',
    pos=(0, 0.4), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textWTA = visual.TextStim(win=win, name='textWTA',
    text='default text',
    font='Microsoft JhengHei UI',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textRemainBudget = visual.TextStim(win=win, name='textRemainBudget',
    text='default text',
    font='Microsoft JhengHei UI',
    pos=(0, 0.3), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textGift_BDM = visual.TextStim(win=win, name='textGift_BDM',
    text='default text',
    font='Microsoft JhengHei UI',
    pos=(0, 0.1), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
imageBDM = visual.ImageStim(
    win=win,
    name='imageBDM', 
    image='sin', mask=None,
    ori=0, pos=(0, -0.2), size=to_1024_768_2D(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "PressEnterScreen"-------
t = 0
PressEnterScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_space = event.BuilderKeyResponse()
# keep track of which components have finished
PressEnterScreenComponents = [textPressEnter, key_resp_space]
for thisComponent in PressEnterScreenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "PressEnterScreen"-------
while continueRoutine:
    # get current time
    t = PressEnterScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textPressEnter* updates
    if t >= 0.0 and textPressEnter.status == NOT_STARTED:
        # keep track of start time/frame for later
        textPressEnter.tStart = t
        textPressEnter.frameNStart = frameN  # exact frame index
        textPressEnter.setAutoDraw(True)
    
    # *key_resp_space* updates
    if t >= 0.0 and key_resp_space.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_space.tStart = t
        key_resp_space.frameNStart = frameN  # exact frame index
        key_resp_space.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_space.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_space.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_space.keys = theseKeys[-1]  # just the last key pressed
            key_resp_space.rt = key_resp_space.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PressEnterScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PressEnterScreen"-------
for thisComponent in PressEnterScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_space.keys in ['', [], None]:  # No response was made
    key_resp_space.keys=None
thisExp.addData('key_resp_space.keys',key_resp_space.keys)
if key_resp_space.keys != None:  # we had a response
    thisExp.addData('key_resp_space.rt', key_resp_space.rt)
thisExp.nextEntry()
# the Routine "PressEnterScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

if practice_flag != 1:

    ### Tcpip socket (client part) ###
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # server IP
    host = '140.116.182.232'
    port = 8088
    s.connect((host,port))
    s.settimeout(None)
    print('Sucessfully Connect to Server')

# ------Prepare to start Routine "WelcomeScreen"-------
t = 0
WelcomeScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_welcome = event.BuilderKeyResponse()

# participant is subject's ID (A or B or C)
clientID = str(expInfo['ID'])
clientID = clientID.capitalize()

# group members' ID [playerA playerB playerC]
# stand-alone version default members'id [1,2,3]
group_num_list = [1, 1, 2, 2, 3, 3]
groupMember_dict = {0 : 'A', 1 : 'B', 2 : 'C', 3 : 'D', 4 :'E', 5 : 'F'}

group_num_list = group_num_list[0 : int(expInfo['Participants(2/4/6)'])]
partiRange = range(0, int(expInfo['Participants(2/4/6)']))
groupMember_dict = {key:groupMember_dict[key] for key in set(partiRange) & set(groupMember_dict)}

if practice_flag == 1:
	continueRoutine = False

# keep track of which components have finished
WelcomeScreenComponents = [textWelcomeScreen, key_welcome]
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "WelcomeScreen"-------
while continueRoutine:
    # get current time
    t = WelcomeScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWelcomeScreen* updates
    if t >= 0.0 and textWelcomeScreen.status == NOT_STARTED:
        # keep track of start time/frame for later
        textWelcomeScreen.tStart = t
        textWelcomeScreen.frameNStart = frameN  # exact frame index
        textWelcomeScreen.setAutoDraw(True)

    # *key_welcome* updates
    if t >= 0.0 and key_welcome.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_welcome.tStart = t
        key_welcome.frameNStart = frameN  # exact frame index
        key_welcome.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_welcome.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

    ### Tcpip socket (client part) ###
    message_5 = s.recv(1024)
    if str(message_5.decode()) == '5': 
        continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen"-------
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

routineTimer.reset()

# ------Prepare to start Routine "IDscreen"-------
t = 0
IDscreenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(showIDScreenTime)
# update component parameters for each repeat
textIDscreen.setText('ID : ' + str(clientID))
# keep track of which components have finished
IDscreenComponents = [textIDscreen]
for thisComponent in IDscreenComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "IDscreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = IDscreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textIDscreen* updates
    if t >= 0.0 and textIDscreen.status == NOT_STARTED:
        # keep track of start time/frame for later
        textIDscreen.tStart = t
        textIDscreen.frameNStart = frameN  # exact framesame index
        textIDscreen.setAutoDraw(True)
    frameRemains = 0.0 + int(showIDScreenTime)- win.monitorFramePeriod * 0.75  # most of one frame period left
    if textIDscreen.status == STARTED and t >= frameRemains:
        textIDscreen.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IDscreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    #win.getMovieFrame()   # Defaults to front buffer, I.e. what's on screen now.
    #win.saveMovieFrames('IDscreen.jpg')  # save with a descriptive and unique filename. 
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "IDscreen"-------
for thisComponent in IDscreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "showIDScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Fixation4s"-------
t = 0
Fixation4sClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(Fixation4sTime)
# update component parameters for each repeat
# keep track of which components have finished
Fixation4sComponents = [textPlus]
for thisComponent in Fixation4sComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Fixation4s"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Fixation4sClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textPlus* updates
    if t >= 0.0 and textPlus.status == NOT_STARTED:
        # keep track of start time/frame for later
        textPlus.tStart = t
        textPlus.frameNStart = frameN  # exact frame index
        textPlus.setAutoDraw(True)
    frameRemains = 0.0 + int(Fixation4sTime)- win.monitorFramePeriod * 0.75  # most of one frame period left
    if textPlus.status == STARTED and t >= frameRemains:
        textPlus.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Fixation4sComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fixation4s"-------
for thisComponent in Fixation4sComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Fixation4s" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

if practice_flag != 1:
	trialsNum = 36
else:
	trialsNum = 6

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=trialsNum, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "DEC1"-------
    t = 0
    DEC1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.reset()
    routineTimer.add(DEC1Time)
    # update component parameters for each repeat
    key_resp_DEC1 = event.BuilderKeyResponse()

    # update current trial
    currentTrial += 1

    # default client not missing
    oops = False
    oops2 = False

    if int(expInfo['Random']) == 0:
        df = df_fixed
    else:
        df = df_random
        group_num = df.at[currentTrial - 1,'group_num']
        group_num_list = []

        for k in range(1, len(group_num)-1, 2):
            group_num_list.append(int(group_num[k]))

    
    # assign subject's role in group
    for k in range(0, len(groupMember_dict)):
    	d = groupMember_dict[k]
    	if clientID == d :
    		role = 'p' + str(d.lower())
    		role_alphabet = str(d)
    		group_num = group_num_list[k]
    		partner_idx = [j for j, e in enumerate(group_num_list) if e == group_num and j != k][0]
    		partnerID = groupMember_dict[partner_idx]

    # read gift code
    DEC1_gift1_code = str(df.at[currentTrial - 1,'Gift_1_' + str(role)])
    DEC1_gift2_code = str(df.at[currentTrial - 1,'Gift_2_' + str(role)])

    imageGift1.setImage(giftsDict[DEC1_gift1_code][1])
    imageGift2.setImage(giftsDict[DEC1_gift2_code][1])

    # setting text
    if int(expInfo['Random']) == 0:
    	textDEC1.setText('Choose a gift send to ID '+str(partnerID))
    else:
    	# Don't tell who to send when is random exchange
        textDEC1.setText('Choose a gift to send')

    textGift1.setText(str(giftsDict[DEC1_gift1_code][0]))
    textGift2.setText(str(giftsDict[DEC1_gift2_code][0]))
    textGift1Price.setText('NT ' + str(giftsDict[DEC1_gift1_code][2]))
    textGift2Price.setText('NT ' + str(giftsDict[DEC1_gift2_code][2]))

    # keep track of which components have finished
    DEC1Components = [textDEC1, imageGift1, imageGift2, textGift1, textGift2, textGift1Price, textGift2Price, key_resp_DEC1]
    for thisComponent in DEC1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # record start trial time(DecOns1)  
    startTrialT = ExperimentClock.getTime()
    
    # -------Start Routine "DEC1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = DEC1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textDEC1* updates
        if t >= 0.0 and textDEC1.status == NOT_STARTED:
            # keep track of start time/frame for later
            textDEC1.tStart = t
            textDEC1.frameNStart = frameN  # exact frame index
            textDEC1.setAutoDraw(True)
        frameRemains = 0.0 + int(DEC1Time)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textDEC1.status == STARTED and t >= frameRemains:
            textDEC1.setAutoDraw(False)
        
        # *imageGift1* updates
        if t >= 0.0 and imageGift1.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageGift1.tStart = t
            imageGift1.frameNStart = frameN  # exact frame index
            imageGift1.setAutoDraw(True)
        frameRemains = 0.0 + int(DEC1Time)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if imageGift1.status == STARTED and t >= frameRemains:
            imageGift1.setAutoDraw(False)
        
        # *imageGift2* updates
        if t >= 0.0 and imageGift2.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageGift2.tStart = t
            imageGift2.frameNStart = frameN  # exact frame index
            imageGift2.setAutoDraw(True)
        frameRemains = 0.0 + int(DEC1Time)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if imageGift2.status == STARTED and t >= frameRemains:
            imageGift2.setAutoDraw(False)
        
        # *textGift1* updates
        if t >= 0.0 and textGift1.status == NOT_STARTED:
            # keep track of start time/frame for later
            textGift1.tStart = t
            textGift1.frameNStart = frameN  # exact frame index
            textGift1.setAutoDraw(True)
        frameRemains = 0.0 + int(DEC1Time)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textGift1.status == STARTED and t >= frameRemains:
            textGift1.setAutoDraw(False)
        
        # *textGift2* updates
        if t >= 0.0 and textGift2.status == NOT_STARTED:
            # keep track of start time/frame for later
            textGift2.tStart = t
            textGift2.frameNStart = frameN  # exact frame index
            textGift2.setAutoDraw(True)
        frameRemains = 0.0 + int(DEC1Time)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textGift2.status == STARTED and t >= frameRemains:
            textGift2.setAutoDraw(False)

        # *textGift1Price* updates
        if t >= 0.0 and textGift1Price.status == NOT_STARTED:
            # keep track of start time/frame for later
            textGift1Price.tStart = t
            textGift1Price.frameNStart = frameN  # exact frame index
            textGift1Price.setAutoDraw(True)
        frameRemains = 0.0 + int(DEC1Time)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textGift1Price.status == STARTED and t >= frameRemains:
            textGift1Price.setAutoDraw(False)

        # *textGift2Price* updates
        if t >= 0.0 and textGift2Price.status == NOT_STARTED:
            # keep track of start time/frame for later
            textGift2Price.tStart = t
            textGift2Price.frameNStart = frameN  # exact frame index
            textGift2Price.setAutoDraw(True)
        frameRemains = 0.0 + int(DEC1Time)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textGift2Price.status == STARTED and t >= frameRemains:
            textGift2Price.setAutoDraw(False)

        # *key_resp_DEC1* updates
        if t >= 0.0 and key_resp_DEC1.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_DEC1.tStart = t
            key_resp_DEC1.frameNStart = frameN  # exact frame index
            key_resp_DEC1.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_DEC1.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + int(DEC1Time)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_DEC1.status == STARTED and t >= frameRemains:
            key_resp_DEC1.status = FINISHED
        if key_resp_DEC1.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_DEC1.keys = theseKeys[-1]  # just the last key pressed
                key_resp_DEC1.rt = key_resp_DEC1.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DEC1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        #win.getMovieFrame()   # Defaults to front buffer, I.e. what's on screen now.
        #win.saveMovieFrames('DEC1.jpg')  # save with a descriptive and unique filename. 
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "DEC1"-------
    # record end alliance decesion time(Dec1End)
    Dec1End = ExperimentClock.getTime()

    # calculate how much time to compensate in DEC1
    patch_Dec1 = float(int(DEC1Time) - (Dec1End-startTrialT))

    for thisComponent in DEC1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # the Routine "DEC1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # check responses
    if key_resp_DEC1.keys in ['', [], None]:  # No response was made
        key_resp_DEC1.keys=None

    # record subjuct's key response
    subject_DEC1_choice = key_resp_DEC1.keys

    # create subject_DEC1_choice to gift code dictionary
    choices_dict = { '1' : DEC1_gift1_code, '2' : DEC1_gift2_code, 'None' : 'Missed'}
    stage1_choice = choices_dict[str(subject_DEC1_choice)]

    ### Tcpip socket (client part) ###
    # send tra1 to server
    if practice_flag != 1:
        tra1 = {}
        tra1['trial' + role] = currentTrial
        tra1[role] = str(stage1_choice)
        tra1['stage' + role] = 1
        tra1['group' + role] = 1
        tra1['partner' + role] = str(partnerID)

    # ------Prepare to start Routine "AllianceCheckWait"-------
    t = 0
    AllianceCheckWaitClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    AllianceCheckWaitComponents = [textWait]
    for thisComponent in AllianceCheckWaitComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    ### Tcpip socket (client part) ###
    # sending alliance choice to server
    if practice_flag != 1:
        message_tra1 = json.dumps(tra1).encode('utf-8')
        s.sendall(message_tra1)
    else:
    	continueRoutine = False
    
    # -------Start Routine "AllianceCheckWait"-------
    while continueRoutine:
        # get current time
        t = AllianceCheckWaitClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textWait* updates
        if t >= 0.0 and textWait.status == NOT_STARTED:
            # keep track of start time/frame for later
            textWait.tStart = t
            textWait.frameNStart = frameN  # exact frame index
            textWait.setAutoDraw(True)
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        
        ### Tcpip socket (client part) ###
        # receive ret_data
        message_ret_data = s.recv(1024)
        message_ret_data = message_ret_data.decode()
        break
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AllianceCheckWaitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AllianceCheckWait"-------
    for thisComponent in AllianceCheckWaitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # the Routine "AllianceCheckWait" was not non-slip safe, so reset the non-slip timer
    
    # ------Prepare to start Routine "TRA1"-------
    t = 0
    TRA1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat

    # default text : '+'
    textTRA1.setText('Exchanging gift ...')

    whoMissed = ''

    if practice_flag != 1:
        ### Tcpip socket (client part) ###
        # turn ret_data to each client's data
        data_clients = json.loads(message_ret_data)
        
        # check whether someone missed
        for k in range(len(data_clients)):
            if data_clients[k][str(list(data_clients[k].keys())[1])] == 'Missed':
    
            	for q in range(0, len(groupMember_dict)):
    
            		if 'trialp' + str(groupMember_dict[q].lower()) in data_clients[k]:
            			missedCountList[q] += 1
    
            			# check whether that missing guy is me or my partner
            			if str(groupMember_dict[q]) == str(partnerID) or str(groupMember_dict[q]) == str(clientID):
            				oops = True
            				whoMissed += 'ID' + str(groupMember_dict[q]) + 'Missing #' + str(missedCountList[q]) + '\n'
    else:
    	# check whether client missed
    	if str(stage1_choice) == 'Missed':
    		missedCount += 1
    		whoMissed += 'ID' + str(clientID) + 'Missing #' + str(missedCount) + '\n'
    		oops = True

    if oops == True:
    	whoMissed += 'Please Wait for Next Trial'
    	textTRA1.setText(str(whoMissed))

    # keep track of which components have finished
    TRA1Components = [textTRA1]
    for thisComponent in TRA1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # record ISI on time
    TRA1On = ExperimentClock.getTime()

    # calculate how much time to cut, due to tral transimission delay
    delay_tra1 = float(TRA1On-Dec1End)

    # TRA1 time
    TRA1_duration = TRA1Time + patch_Dec1 - delay_tra1
    routineTimer.reset()
    routineTimer.add(float(TRA1_duration))
    
    # -------Start Routine "TRA1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TRA1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textTRA1* updates
        if t >= 0.0 and textTRA1.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTRA1.tStart = t
            textTRA1.frameNStart = frameN  # exact frame index
            textTRA1.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TRA1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TRA1"-------
    # record ISI end time
    TRA1End = ExperimentClock.getTime()

    for thisComponent in TRA1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    textTRA1.setText('+')
    
    # ------Prepare to start Routine "FB1"-------
    t = 0
    FB1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    textFB1.setText('Receive from ID ' + str(partnerID) + ' :')

    if oops == True:
    	continueRoutine = False
    else:
    	# create data clients list contains all six partcipants (for standalone version)
    	data_clients_list = []

    	for k in range(0, len(groupMember_dict)):
    		r = groupMember_dict[k].lower()
    		choiceList = ['A', 'B', 'C', 'D', 'E', 'F']
    		#random.shuffle(choiceList)
    		group_num = group_num_list[k]

    		data_client_player = {"trialp" + str(r) : currentTrial, 
    							     "p"   + str(r) : choiceList[int(currentTrial - ((currentTrial - 1 )//6)*6 - 1)],
    							  "stagep" + str(r) : 1,
    							  "groupp" + str(r) : 1,   # groupp != group_num, it's for server reading
    							  "partnerp" + str(r) : groupMember_dict[[j for j, e in enumerate(group_num_list) if e == group_num and j != k][0]]}

    		data_clients_list.append(data_client_player)

    	# replace data_clients_list with data_clients (if it's online version)
    	if practice_flag != 1:
            for y in range(len(data_clients)):
                data_client = data_clients[y]  

            	# who's in the data_clients list
                for z in range(len(data_clients)):
                    r = groupMember_dict[z].lower()    

                    if 'trialp'+str(r) in data_client:
                        data_clients_list[z] = data_client

    	# find partner(through partner's index) and his/her giving gift 
    	giftReceived = data_clients_list[partner_idx]['p'+str(partnerID.lower())]

    	# setting gift text
    	textGift3.setText(giftsDict[str(giftReceived)][0])
    	textGiftDEC2.setText(giftsDict[str(giftReceived)][0])

    	# setting image
    	imageFB.setImage(giftsDict[str(giftReceived)][1])

    # keep track of which components have finished
    FB1Components = [textFB1, imageFB, textGift3]
    for thisComponent in FB1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # record FB1 on time
    Fb1On = ExperimentClock.getTime()
    
    # -------Start Routine "FB1"-------
    while continueRoutine:
        # get current time
        t = FB1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textFB1* updates
        if t >= 0.0 and textFB1.status == NOT_STARTED:
            # keep track of start time/frame for later
            textFB1.tStart = t
            textFB1.frameNStart = frameN  # exact frame index
            textFB1.setAutoDraw(True)
        frameRemains = int(FB1Time) - win.monitorFramePeriod * 0.75
        if textFB1.status == STARTED and t >= frameRemains:
            textFB1.setAutoDraw(False)
        
        # *imageFB* updates
        if t >= 0.0 and imageFB.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageFB.tStart = t
            imageFB.frameNStart = frameN  # exact frame index
            imageFB.setAutoDraw(True)
        frameRemains = int(FB1Time) - win.monitorFramePeriod * 0.75
        if imageFB.status == STARTED and t >= frameRemains:
            imageFB.setAutoDraw(False)
        
        # *textGift3* updates
        if t >= 0.0 and textGift3.status == NOT_STARTED:
            # keep track of start time/frame for later
            textGift3.tStart = t
            textGift3.frameNStart = frameN  # exact frame index
            textGift3.setAutoDraw(True)
        frameRemains = int(FB1Time) - win.monitorFramePeriod * 0.75
        if textGift3.status == STARTED and t >= frameRemains:
            textGift3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FB1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        #win.getMovieFrame()   # Defaults to front buffer, I.e. what's on screen now.
        #win.saveMovieFrames('FB1.jpg')  # save with a descriptive and unique filename. 

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FB1"-------
    # record feedback S1 end time
    Fb1End = ExperimentClock.getTime()

    for thisComponent in FB1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished

    ISIComponents = [textPlus_3]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # record IStageI on time
    ISIon = ExperimentClock.getTime()
    
    # -------Start Routine "ISI"-------
    while continueRoutine:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textPlus_3* updates
        if t >= 0.0 and textPlus_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            textPlus_3.tStart = t
            textPlus_3.frameNStart = frameN  # exact frame index
            textPlus_3.setAutoDraw(True)
        frameRemains = 0.0 + int(ISITime)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textPlus_3.status == STARTED and t >= frameRemains:
            textPlus_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    # record IStageI on time
    ISIoff = ExperimentClock.getTime()

    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "DEC2"-------
    t = 0
    DEC2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat

    # prepare for key in numbers
    theseKeys=""
    shift_flag = False
    textInput.alignHoriz ='left'
    shift_flag_count = 0
    inputText=""

    if oops == False:
        # setting image
        imageDEC2.setImage(giftsDict[str(giftReceived)][1])
        textDEC2.setText('Enter selling price (From ID '+str(partnerID)+')')
    else:
    	# Don't show the picture
    	imageDEC2.setImage('images/gift_A.png')
    	continueRoutine = False

    key_resp_DEC2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    DEC2Components = [textDEC2, textGiftDEC2, imageDEC2, textDECzero, textDECthreeHund, textInput, key_resp_DEC2]
    for thisComponent in DEC2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # record on distribution decesion time
    Dec2on = ExperimentClock.getTime()
    routineTimer.reset()
    routineTimer.add(DEC2Time)
    
    # -------Start Routine "DEC2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = DEC2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        n= len(theseKeys)
        i = 0
        while i < n:
            if theseKeys[i] == 'backspace':
                inputText = inputText[:-1]  # lose the final character
                i = i + 1

            # key_resp_DEC2 don't allow 'space'
            elif theseKeys[i] == 'space':
                inputText += ' '
                i = i + 1       

            # key_resp_DEC2 don't allow 'caplock'
            elif theseKeys[i] == 'capslock':
                shift_flag_count += 1
                if int(shift_flag_count % 2) == 1:
                    shift_flag = True
                else:
                    shift_flag = False
                i = i + 1
            elif theseKeys[i][0:4] == 'num_':
                if len(inputText) < 3:
                    inputText += theseKeys[i][-1]
                i = i + 1
            else:
                if len(theseKeys[i]) == 1:
                    # we only have 1 char so should be a normal key, 
                    # otherwise it might be 'ctrl' or similar so ignore it
                    if shift_flag and len(inputText) < 3:
                        inputText += chr( ord(theseKeys[i]) - ord(' '))
                    else:
                    	if len(inputText) < 3:
                            inputText += theseKeys[i]
                i = i + 1
        # *textDEC2* updates
        if t >= 0.0 and textDEC2.status == NOT_STARTED:
            # keep track of start time/frame for later
            textDEC2.tStart = t
            textDEC2.frameNStart = frameN  # exact frame index
            textDEC2.setAutoDraw(True)
        #frameRemains = 0.0 + int(DEC2Time)- win.monitorFramePeriod * 0.75  # most of one frame period left
        #if textDEC2.status == STARTED and t >= frameRemains:
        #    textDEC2.setAutoDraw(False)
        
        # *textGiftDEC2* updates
        if t >= 0.0 and textGiftDEC2.status == NOT_STARTED:
            # keep track of start time/frame for later
            textGiftDEC2.tStart = t
            textGiftDEC2.frameNStart = frameN  # exact frame index
            textGiftDEC2.setAutoDraw(True)
        #frameRemains = 0.0 + int(DEC2Time)- win.monitorFramePeriod * 0.75  # most of one frame period left
        #if textGiftDEC2.status == STARTED and t >= frameRemains:
        #    textGiftDEC2.setAutoDraw(False)

        # *imageDEC2* updates
        if t >= 0.0 and imageDEC2.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageDEC2.tStart = t
            imageDEC2.frameNStart = frameN  # exact frame index
            imageDEC2.setAutoDraw(True)
        #frameRemains = 0.0 + int(DEC2Time)- win.monitorFramePeriod * 0.75  # most of one frame period left
        #if imageDEC2.status == STARTED and t >= frameRemains:
        #    imageDEC2.setAutoDraw(False)
        
        # *textDECzero* updates
        if t >= 0.0 and textDECzero.status == NOT_STARTED:
            # keep track of start time/frame for later
            textDECzero.tStart = t
            textDECzero.frameNStart = frameN  # exact frame index
            textDECzero.setAutoDraw(True)
        #frameRemains = 0.0 + int(DEC2Time)- win.monitorFramePeriod * 0.75  # most of one frame period left
        #if textDECzero.status == STARTED and t >= frameRemains:
        #    textDECzero.setAutoDraw(False)
        
        # *textDECthreeHund* updates
        if t >= 0.0 and textDECthreeHund.status == NOT_STARTED:
            # keep track of start time/frame for later
            textDECthreeHund.tStart = t
            textDECthreeHund.frameNStart = frameN  # exact frame index
            textDECthreeHund.setAutoDraw(True)
        #frameRemains = 0.0 + int(DEC2Time)- win.monitorFramePeriod * 0.75  # most of one frame period left
        #if textDECthreeHund.status == STARTED and t >= frameRemains:
        #    textDECthreeHund.setAutoDraw(False)
        
        # *textInput* updates
        if t >= 0.0 and textInput.status == NOT_STARTED:
            # keep track of start time/frame for later
            textInput.tStart = t
            textInput.frameNStart = frameN  # exact frame index
            textInput.setAutoDraw(True)
        #frameRemains = 0.0 + int(DEC2Time)- win.monitorFramePeriod * 0.75  # most of one frame period left
        #if textInput.status == STARTED and t >= frameRemains:
        #    textInput.setAutoDraw(False)
        if textInput.status == STARTED:  # only update if drawing
            textInput.setText(('NT ' + inputText), log=False)
        
        # *key_resp_DEC2* updates
        if t >= 0.0 and key_resp_DEC2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_DEC2.tStart = t
            key_resp_DEC2.frameNStart = frameN  # exact frame index
            key_resp_DEC2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_DEC2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        #frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        #if key_resp_DEC2.status == STARTED and t >= frameRemains:
        #    key_resp_DEC2.status = FINISHED
        if key_resp_DEC2.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'backspace', 'num_0', 'num_1', 'num_2', 'num_3', 'num_4', 'num_5', 'num_6', 'num_7', 'num_8', 'num_9'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_DEC2.keys.extend(theseKeys)  # storing all keys
                key_resp_DEC2.rt.append(key_resp_DEC2.clock.getTime())
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DEC2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        #win.getMovieFrame()   # Defaults to front buffer, I.e. what's on screen now.
        #win.saveMovieFrames('DEC2.jpg')  # save with a descriptive and unique filename. 

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "DEC2"-------
    # record end distribution decesion time
    Dec2End = ExperimentClock.getTime()

    for thisComponent in DEC2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # check responses
    if key_resp_DEC2.keys in ['', [], None]:  # No response was made
        key_resp_DEC2.keys=None
    
    # ------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [textPlus_4]
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # player Missed DEC2 (WTA)
    if len(inputText) == 0 and oops == False:
        textPlus_4.setText('Missed Price Input !')

    if len(inputText) != 0 and oops == False:
    	not_missing_list.append(currentTrial)

    # record ITI on time  # adjust according position in lastrun
    ITIOn = ExperimentClock.getTime()

    # calculate delay
    delay = float((ITIOn - startTrialT) - int(FB1Time) - int(ISITime) -int(DEC2Time) - int(DEC1Time) - int(TRA1Time))    

    # fixation2s time
    ITI_duration = float(ITITime - delay)
    
    # -------Start Routine "ITI"-------
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textPlus_4* updates
        if t >= 0.0 and textPlus_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            textPlus_4.tStart = t
            textPlus_4.frameNStart = frameN  # exact frame index
            textPlus_4.setAutoDraw(True)
        frameRemains = float(ITI_duration) - win.monitorFramePeriod * 0.75
        if textPlus_4.status == STARTED and t >= frameRemains:
            textPlus_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    # record ITI on time   
    ITIEnd = ExperimentClock.getTime()

    textPlus_4.setText('+')

    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()

    trials.addData('player',clientID)
    trials.addData('currentTrial',currentTrial)
    trials.addData('partner',partnerID)
    trials.addData('startTrialT',startTrialT)
    trials.addData('Dec1End',Dec1End)
    trials.addData('patch_Dec1',patch_Dec1)
    trials.addData('delay_tra1',delay_tra1)
    trials.addData('TRA1On',TRA1On)
    trials.addData('TRA1End',TRA1End)
    trials.addData('Fb1On',Fb1On)
    trials.addData('Fb1End',Fb1End)
    trials.addData('ISIon',ISIon)
    trials.addData('ISIoff',ISIoff)
    trials.addData('Dec2on',Dec2on)
    trials.addData('Dec2End',Dec2End)
    trials.addData('delay',delay)
    trials.addData('ITIOn',ITIOn)
    trials.addData('ITIEnd',ITIEnd)
    trials.addData('gift1_code',DEC1_gift1_code)
    trials.addData('gift2_code',DEC1_gift2_code)
    trials.addData('gift1_price',str(giftsDict[DEC1_gift1_code][2]))
    trials.addData('gift2_price',str(giftsDict[DEC1_gift2_code][2]))
    trials.addData('stage1_choice',str(stage1_choice))
    if oops == False:
    	trials.addData('giftReceived (opponent stage1_choice)',str(giftReceived))
    	trials.addData('giftReceived_price',str(giftsDict[str(giftReceived)][2]))
    trials.addData('WTA',str(inputText))
    trials.addData('key_resp_DEC1.keys',key_resp_DEC1.keys)
    if key_resp_DEC1.keys != None:  # we had a response
        trials.addData('key_resp_DEC1.rt', key_resp_DEC1.rt)
    trials.addData('key_resp_DEC2.keys',key_resp_DEC2.keys)
    if key_resp_DEC2.keys != None:  # we had a response
        trials.addData('key_resp_DEC2.rt', key_resp_DEC2.rt)

# completed 36 repeats of 'trials'
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()

# ------Prepare to start Routine "BDM"-------
t = 0
BDMClock.reset()  # clock
frameN = -1
continueRoutine = True

# random draw a number
randomTrial = int(random.choice(not_missing_list))

# read the data file and find the info of random trial
df_data = pd.read_csv(filename+'.csv')
randomWTA = df_data.at[randomTrial + 1, 'WTA'].astype(np.int64)
randomGift = df_data.at[randomTrial + 1, 'giftReceived (opponent stage1_choice)']
remainBudget = 330 - int(giftsDict[str(df_data.at[randomTrial + 1, 'stage1_choice'])][2])

# change showing text
textTrial.setText('#' + str(randomTrial))
textRemainBudget.setText('Remain budget : '+str(remainBudget))
textWTA.setText('Price want to sell : '+str(randomWTA))
textGift_BDM.setText('Gift : '+str(giftsDict[str(randomGift)][0]))
imageBDM.setImage(giftsDict[str(randomGift)][1])

# update component parameters for each repeat
# keep track of which components have finished
BDMComponents = [textTrial, textRemainBudget, textWTA, imageBDM, textGift_BDM]
for thisComponent in BDMComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "BDM"-------
while continueRoutine:
    # get current time
    t = BDMClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
        
    # *textTrial* updates
    if t >= 0.0 and textTrial.status == NOT_STARTED:
        # keep track of start time/frame for later
        textTrial.tStart = t
        textTrial.frameNStart = frameN  # exact frame index
        textTrial.setAutoDraw(True)

    # *textRemainBudget* updates
    if t >= 0.0 and textRemainBudget.status == NOT_STARTED:
        # keep track of start time/frame for later
        textRemainBudget.tStart = t
        textRemainBudget.frameNStart = frameN  # exact frame index
        textRemainBudget.setAutoDraw(True)

    # *textWTA* updates
    if t >= 0.0 and textWTA.status == NOT_STARTED:
        # keep track of start time/frame for later
        textWTA.tStart = t
        textWTA.frameNStart = frameN  # exact frame index
        textWTA.setAutoDraw(True)

    # *textGift_BDM* updates
    if t >= 0.0 and textGift_BDM.status == NOT_STARTED:
        # keep track of start time/frame for later
        textGift_BDM.tStart = t
        textGift_BDM.frameNStart = frameN  # exact frame index
        textGift_BDM.setAutoDraw(True)

    # *imageBDM* updates
    if t >= 0.0 and imageBDM.status == NOT_STARTED:
        # keep track of start time/frame for later
        imageBDM.tStart = t
        imageBDM.frameNStart = frameN  # exact frame index
        imageBDM.setAutoDraw(True)
        
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
        
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BDMComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    #win.getMovieFrame()   # Defaults to front buffer, I.e. what's on screen now.
    #win.saveMovieFrames('BDM.jpg')  # save with a descriptive and unique filename. 

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    
# -------Ending Routine "BDM"-------
for thisComponent in BDMComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
