#AUTOR(A): KAROLINE YAMAMOTO
#ATUALIZAÇÃO: 25 DE MAIO DE 2022
#TAREFA: FACILITAR O ENVIO DE E-MAIL 

import pyautogui
import pyperclip
import time

# Processo E-commerce: fazer todos os dias análise de 3 pedidos
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("excel")
pyautogui.press("enter")
time.sleep(2) 
pyautogui.click(x=-1862, y=417)
pyautogui.click(x=-1192, y=249)
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(2) 
pyperclip.copy("https://sudambeef.myvtex.com/admin/")
pyautogui.hotkey("ctrl", "v")

# Automação Python: verificar funcionamento
pyautogui.press("win")
pyautogui.write("vscode")
pyautogui.press("enter")
time.sleep(2) 

# Site sudambeef: melhorias nas funcionalidades
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(2) 
pyperclip.copy("https://www.sudambeef.com.br/")
pyautogui.hotkey("ctrl", "v")

# Curso Udemy
#AUTOMAÇÃO DE PROCESSOS
#Transformar o arquivo em executável: https://www.youtube.com/watch?v=cGSerUmK0CE

# UDEMY
""" pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyperclip.copy("https://www.udemy.com/")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=1635, y=192, clicks=1)
time.sleep(2)
pyautogui.click(x=570, y=708)
time.sleep(2) """

# workReportVtex automação 

""" time.sleep(5)
pyautogui.position()
print(pyautogui.position()) """