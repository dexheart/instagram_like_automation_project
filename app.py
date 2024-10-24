import pyautogui
import pyperclip
import webbrowser
from time import sleep

def writePhrase(phrase):
    pyperclip.copy(phrase)
    pyautogui.hotkey('ctrl', 'v')

def logout():
    pyautogui.click(1870,141, duration=2)
    pyautogui.click(977,980,duration=2)
    pyautogui.click(1116,972,duration=2)


while True:

### Parte de Login

    webbrowser.open_new('https://www.instagram.com/')
    sleep(2)
    loginPoint = pyautogui.locateCenterOnScreen('login.png')
    #passwordPoint = pyautogui.locateCenterOnScreen('password.png')

    pyautogui.click(loginPoint[0],loginPoint[1], duration=2)
    writePhrase('eng.seg.araujo@gmail.com')
    sleep(1)
    pyautogui.click(loginPoint[0],loginPoint[1]+50, duration=2)
    writePhrase('rato1502')
    sleep(1)
    pyautogui.click(loginPoint[0],loginPoint[1]+80,duration=2)
    sleep(5)
    # pyautogui.click(1539,89,duration=2)



    ### Bucas da Página da Nike

    #print(pyautogui.locateCenterOnScreen('search.png'))
    # Point(x=978, y=299)
    #searchPoint = pyautogui.locateCenterOnScreen('search.png')

    sleep(1)
    pyautogui.click(978, 299, duration=2)
    sleep(1)
    pyautogui.click(1078, 229, duration=2)
    sleep(1)
    writePhrase('nike')
    sleep(1)
    pyautogui.click(1078, 289, duration=2)
    sleep(5)


    ### Clicar na primeira postagem

    pyautogui.click(1153,800, duration=2)
    sleep(2)


    try:
        liked_point = pyautogui.locateCenterOnScreen('liked.png')
        sleep(2)
        logout()
        sleep(60*60*60*24)
    except Exception as e:
        pyautogui.click(1457,814,duration=2)
        sleep(1)
        pyautogui.click(1538,922,duration=2)
        sleep(1)
        writePhrase('Show!')
        sleep(1)
        pyautogui.press('enter')
        sleep(2)
        logout()
        sleep(60*60*60*24)
