
import time,pyautogui
import sc
center = 482,383
up = 360,288
down = 579,457
left = 354,479
right = 611,288
s = 513,407
e = 512,362
w = 449,408
n = 449,360
nw = 418,382
esc = 784,736
doctor = 449,408
sell = 498,379
sellAll = 393,395
sellConfirm = 348,395
sellConfirm2 = 136,412
nurseHeath = 478,355
petHeath = 478,390
nurseHeathConfirm = 405,435
Confirm2 = 481,433
treatment = 309,287
bag = 200,736
logout = 332,94
logoutToTown = 179,74
#
def PathDoctorToSell():
    time.sleep(2)
    pyautogui.click(e,clicks=2,interval=0.5)
    pyautogui.click(s,clicks=23,interval=0.5)
    pyautogui.click(w,clicks=2,interval=0.5)
    pyautogui.click(s,clicks=1,interval=0.5)
    time.sleep(2)
    pyautogui.click(s,clicks=1,interval=0.5)
    pyautogui.click(e,clicks=13,interval=0.5)
    pyautogui.click(n,clicks=6,interval=0.5)
    pyautogui.click(e,clicks=1,interval=0.5)
    pyautogui.click(n,clicks=14,interval=0.5)
    pyautogui.click(e,clicks=3,interval=0.5)
    time.sleep(2)
    pyautogui.click(e,clicks=26,interval=0.5)
    pyautogui.click(n,clicks=2,interval=0.5)
    time.sleep(2)
    pyautogui.click(e,clicks=8,interval=0.5)
    pyautogui.click(n,clicks=16,interval=0.5)
    pyautogui.click(e,clicks=5,interval=0.5)
    pyautogui.click(n,clicks=4,interval=0.5)
    time.sleep(2)
    pyautogui.click(n,button='right')
    time.sleep(2)
    pyautogui.click(sell)
    time.sleep(2)
    pyautogui.click(sellAll)
    time.sleep(2)
    pyautogui.click(sellConfirm)
    time.sleep(2)
    pyautogui.click(sellConfirm2)
    time.sleep(2)



def PathE1ToHospital():
    pyautogui.PAUSE = 1.5
    pyautogui.click(n,clicks=12,interval=0.5)
    pyautogui.click(w,clicks=21,interval=0.5)
    pyautogui.click(n,clicks=5,interval=0.5)

def PathE2ToHospital():
    time.sleep(2)
    pyautogui.PAUSE = 2
    pyautogui.click(s,clicks=7,interval=0.5)
    pyautogui.click(w,clicks=12,interval=0.5)
    pyautogui.click(n,clicks=2,interval=0.5)

def PathUpperE2ToHospital():
    time.sleep(2)
    pyautogui.PAUSE = 2
    pyautogui.click(s,clicks=6,interval=0.5)
    pyautogui.click(e,clicks=1,interval=0.5)
    pyautogui.click(s,clicks=14,interval=0.5)
    pyautogui.click(w,clicks=9,interval=0.5)
    pyautogui.click(n,clicks=1,interval=0.5)


def PathToNurse():
    time.sleep(3)
    pyautogui.PAUSE = 1
    pyautogui.click(n,clicks=7,interval=0.5)
    pyautogui.click(w,clicks=4,interval=0.5)
    pyautogui.click(n,clicks=1,interval=0.5)
    isNurse = pyautogui.locateCenterOnScreen('nurse.png', confidence=.85)
    if(isNurse != None):
        pyautogui.click(isNurse,button='right')
        pyautogui.PAUSE = 1.5
        pyautogui.click(nurseHeath)
        pyautogui.click(nurseHeathConfirm)
        pyautogui.click(Confirm2)
        pyautogui.click(petHeath)
        pyautogui.click(nurseHeathConfirm)
        pyautogui.click(Confirm2)
        pyautogui.click(Confirm2)
    else:
        logout()

def PathToDoctor():
    #from e2nurse to doctor
    #injuredState = pyautogui.locateCenterOnScreen('injured.png',grayscale=True,confidence=.9)
    #if(injuredState != None):
    pyautogui.PAUSE = 2.5
    pyautogui.click(n,clicks=4,interval=0.4)
    pyautogui.click(e,clicks=6,interval=0.4)
    pyautogui.click(n,clicks=12,interval=0.4)
    pyautogui.click(w,clicks=2,interval=0.4)
    time.sleep(2)
    pyautogui.click(doctor,button='right')
    time.sleep(3)
    pyautogui.moveTo(treatment)
    pyautogui.click()
    time.sleep(3)
    pyautogui.click(Confirm2)
    time.sleep(2)

def PathUpperE2ToOut():
    time.sleep(2.5)
    pyautogui.PAUSE = 1.5
    pyautogui.click(s,clicks=5,interval=0.4)
    pyautogui.click(e,clicks=6,interval=0.4)
    pyautogui.click(s,clicks=18,interval=0.4)
    pyautogui.click(e,clicks=1,interval=0.4)
    pyautogui.dragTo(512,363, 20, button='left')

def PathE1ToOut():
    time.sleep(2.5)
    pyautogui.PAUSE = 1.5
    pyautogui.click(n,clicks=12,interval=0.4)
    pyautogui.dragTo(512,363, 20, button='left')
