from pyautogui import press
import time
import pyautogui
import os
import subprocess
import pydirectinput
import sc
import sys
from PIL import Image
import cv2
import loc
import numpy as np
#os.chdir('/Users/nyto9/OneDrive/桌面')
os.chdir('/Users/nyto9/python_venv/quickMacro/resource')
PATH = '/Users/nyto9/python_venv/quickMacro/resource/'
#subprocess.Popen('C:\\Users\\nyto9\\OneDrive\\桌面\\ClientVer20210314\\BlueCrossgate\\BlueLogin.exe')
pyautogui.FAILSAFE = True

def countdown(y):
    for x in range(3):
        print(y-x)
        time.sleep(0.5)
    return print('go!')

def outside():
    checkState()
    roaming()
    attack()




def roaming():

    while True:

        inFight = pyautogui.locateCenterOnScreen('notFight.png',grayscale=True,confidence=.9)
        if(inFight == None):
            print('Fight!!')
            break
        pyautogui.PAUSE = 1.5
        pyautogui.click(loc.down)
        pyautogui.click(loc.up)
        pyautogui.click(loc.left)
        pyautogui.click(loc.right)




def attack():
    time.sleep(3)
    img = pyautogui.screenshot()
    r,g,b = img.getpixel((808,34))
    print('戰鬥內確認')


    while(r == 250, g == 247):#戰鬥框
        m1 = monster('tree')
        m2 = monster('bee')
        m3 = monster('theif')
        m4 = monster('theifBack')

        if(m1[0] != None):
            pyautogui.click(m1[0])
            print('attack'+m1[1])
        elif(m2[0] != None):
            pyautogui.click(m2[0])
            print('attack'+m2[1])
        elif(m3[0] != None):
            pyautogui.click(m3[0])
            print('attack'+m3[1])
        elif(m4[0] != None):
            pyautogui.click(m4[0])
            print('attack'+m4[1])
        else:
            inFight = pyautogui.locateCenterOnScreen('notFight.png',grayscale=True,confidence=.9)
            img = pyautogui.screenshot()
            r,g,b = img.getpixel((808,34))
            if(inFight != None):
                outside()
            if(r != 250 and g != 247): #已攻擊
                print('戰鬥中'+str(r)+' '+str(g))
                time.sleep(2)
            print('searching')




def checkState():
    lowHp()

#登出435,337 城內登出278,318
def lowHp():
    time.sleep(1)
    img = pyautogui.screenshot()
    r,g,b = img.getpixel((475,388)) #血條的一半
    print(r)
    print(g)
    if(r != 255):
        logout()
        goHeal()


def goHeal():
    #isCrystal = pyautogui.locateCenterOnScreen('crystal.png', confidence=.9)
    e2 = pyautogui.locateCenterOnScreen('e2.png',grayscale=True,confidence=.9)
    while(e2 == None):
        print("Searching e2")
        isCrystal = pyautogui.locateCenterOnScreen('crystal.png', confidence=.85)
        time.sleep(1)
        pyautogui.click(isCrystal,button='right')

        e2 = pyautogui.locateCenterOnScreen('e2.png',grayscale=True,confidence=.9)
        e1 = pyautogui.locateCenterOnScreen('bank.png', confidence=.85)
        if(e1 != None):
            #back to hospital n12 w21 n5
            loc.PathE1ToHospital()
            healAndSell()

        upperE2 = pyautogui.locateCenterOnScreen('upperE2.png', confidence=.85)
        if(upperE2 != None):
            loc.PathUpperE2ToHospital()
            healAndSell()


    #Path from e2 to hospital
    loc.PathE2ToHospital()
    healAndSell()


def healAndSell():
    loc.PathToNurse()
    loc.PathToDoctor()
    loc.PathDoctorToSell()
    drop()



def goOutside():

        #isCrystal = pyautogui.locateCenterOnScreen('crystal.png', confidence=.9)
    e2 = pyautogui.locateCenterOnScreen('e2.png',grayscale=True,confidence=.9)
    while(e2 == None):
        print("Searching e2")
        isCrystal = pyautogui.locateCenterOnScreen('crystal.png', confidence=.85)
        time.sleep(1)
        pyautogui.click(isCrystal,button='right')

        e2 = pyautogui.locateCenterOnScreen('e2.png',grayscale=True,confidence=.9)
        e1 = pyautogui.locateCenterOnScreen('bank.png', confidence=.85)
        if(e1 != None):
            #back to hospital n12 w21 n5
            loc.PathE1ToOut()


        upperE2 = pyautogui.locateCenterOnScreen('upperE2.png', confidence=.85)
        if(upperE2 != None):
            loc.PathUpperE2ToOut()
            outside()




    #Path from e2 to hospital
    print('e2')





def imageToString(x,y,w,h, name):
    image = pyautogui.screenshot(region=(x, y, w, h))
    im = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
    cv2.imwrite(name+".png", im)
    imageOpen = Image.open(name+".png")
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    currentHp = pytesseract.image_to_string(imageOpen, lang='eng', config='--psm 8 --oem 3 -c tessedit_char_whitelist=0123456789/')
    return currentHp

def openUI(xy):
    time.sleep(1)
    isUI = pyautogui.locateCenterOnScreen('UI.png',confidence=.7)
    if(isUI == None):
        pyautogui.click(xy)
        time.sleep(1.5)
        isUI = pyautogui.locateCenterOnScreen('UI.png',confidence=.7)

    time.sleep(1.5)
    pyautogui.moveTo(isUI)
    time.sleep(1.5)
    pyautogui.dragTo(440,100,3,button="left")
    time.sleep(1.5)

def drop():
    openUI(loc.bag)
    start=[180,80]
    cell = 46
    for j in range(0,3):
        for i in range(0,5):
            cx = float(start[0]+(cell*i)+(cell/2))
            cy = float(start[1]+(cell*j)+(cell/2+0.1))
            pyautogui.click(cx,cy,button='left')
            pyautogui.click(623,399)
    isUI = pyautogui.locateCenterOnScreen('UI.png',confidence=.7)
    time.sleep(2)
    if(isUI != None): #結束drop之後 確認被包已關閉
        pyautogui.click(loc.bag)
    logout()
    goOutside()

def logout():
    openUI(loc.esc)
    pyautogui.PAUSE = 1.5
    pyautogui.click(loc.logout)
    time.sleep(1)
    pyautogui.click(loc.logoutToTown)
    time.sleep(1)




#

def test():
    pyautogui.click(200,736)
    time.sleep(2)
    isbag = pyautogui.locateCenterOnScreen('bag.png',confidence=.7)
    if(isbag != None):
        pyautogui.moveTo(isbag)
        time.sleep(1)
        pyautogui.dragTo(440,160,3,button="left")

def monster(monster):
    isMonster = pyautogui.locateCenterOnScreen(monster+'.png', confidence=.65)
    return isMonster,monster


def roaming2():

    while True:

        inFight = pyautogui.locateCenterOnScreen('outside2.png',grayscale=True,confidence=.9)
        pyautogui.PAUSE = 1.5
        pyautogui.click(1043,819)
        pyautogui.click(1063,774)
        pyautogui.click(842,730)
        pyautogui.click(1099,937)



countdown(3)
roaming2()







