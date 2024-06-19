import pyautogui
import time
import keyboard

# Defina o número de iterações do loop
num_intera = 26

scroll_valuepl = -24
scroll_valueinf = -57

for i in range(num_intera):
    if keyboard.is_pressed('q'):
        print("Loop interrompido pelo usuário.")
        break
    pyautogui.doubleClick(481,129) #adap coord Estado
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    
    
    pyautogui.click(316, 16) #adap coord pl
    pyautogui.click(103,292) #coord pl A1-
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)
    
    
    pyautogui.click(501, 22) #adap coord Site de info
    pyautogui.doubleClick(1072,130) #adap coord Abrev
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    
    
    pyautogui.click(316, 16) #adap coord pl
    pyautogui.click(216,296) #coord pl B1-
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)
    
    
    pyautogui.click(501, 22) #adap coord Site de info
    pyautogui.tripleClick(776,133) #adap coord capital
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    
   
    pyautogui.click(316, 16) #adap coord pl
    pyautogui.click(319,297) #coord pl C1-
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)
    
    
    pyautogui.click(501, 22) #adap coord Site de info
    pyautogui.click(1273,265) #adap area livre para click
    pyautogui.scroll(int(scroll_valueinf)) #adap scrool para melhor seleção em site de info
    time.sleep(0.5)  

    pyautogui.click(316, 16)
    pyautogui.click(409, 313) #adap scrool para melhor seleção em pl
    pyautogui.scroll(int(scroll_valuepl)) #rolagem na pl A2
    pyautogui.click(501, 22) #adap coord Site de info

    scroll_valueinf -=1
    scroll_valuepl -=0.5
print("Loop concluído.")
