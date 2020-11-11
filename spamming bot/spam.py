#pip install pyautogui
#time.sleep is 10 in this case. So you have to 
#take your cursor to the typing space in 
#any social media chat after executing the command
#terminate the program from your ide to make it stop
import pyautogui, time
time.sleep(10)
f= open("bee.txt",'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    