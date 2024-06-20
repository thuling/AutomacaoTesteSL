import pyautogui
import keyboard
import time

num_intera = 8

pgclick1 = (1304, 252)
pgclick2 = (1376, 250)
pgclick3 = (1156, 290)

plA = (129, 313)
plB = (270, 314)
plC = (392, 313)

for i in range(num_intera):
    if keyboard.is_pressed('q'):
        print("Loop interrompido pelo usuário.")
        break
    
    pyautogui.click(1098, 396) # click na tela info1
    # time.sleep(0.5)  # Pequeno atraso
    pyautogui.doubleClick(pgclick1) # click para copiar
    pyautogui.hotkey('ctrl', 'c')
    # time.sleep(0.5)  # Pequeno atraso
    
    pyautogui.click(plA)
    pyautogui.hotkey('ctrl', 'v')
    # time.sleep(0.5)  # Pequeno atraso
    
    pyautogui.click(1098, 396) # click na tela info1
    pyautogui.doubleClick(pgclick2) # click para copiar
    pyautogui.hotkey('ctrl', 'c')
    # time.sleep(0.5)  # Pequeno atraso
    
    pyautogui.click(plB)
    pyautogui.hotkey('ctrl', 'v')
    # time.sleep(0.5)  # Pequeno atraso
    
    pyautogui.click(1220, 23) # click plDDD
    pyautogui.click(pgclick3) # click para copiar
    pyautogui.hotkey('ctrl', 'c')
    # time.sleep(0.5)  # Pequeno atraso
    
    pyautogui.click(plC) 
    pyautogui.hotkey('ctrl', 'v')
    # time.sleep(0.5)  # Pequeno atraso
    
    pyautogui.click(1054, 24)
    # time.sleep(0.5)  # Pequeno atraso

    pgclick1 = (pgclick1[0], pgclick1[1] + 40)
    pgclick2 = (pgclick2[0], pgclick2[1] + 40)
    pgclick3 = (pgclick3[0], pgclick3[1] + 22)
    plA = (plA[0], plA[1] + 22)
    plB = (plB[0], plB[1] + 22)
    plC = (plC[0], plC[1] + 22)

print("Loop finalizado")
