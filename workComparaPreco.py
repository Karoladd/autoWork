#AUTOR(A): KAROLINE YAMAMOTO
#ATUALIZAÇÃO: 30 DE JUNHO DE 2022
#DESAFIO: AUTOMAÇÃO COMPARAR PREÇO

""" 
Desafio: automatizar o processo do programa web-scraping.
Transferência de dados do programa python para MySQL.
Transferência dados MySQL para Excel.
"""

import pyautogui
import time

# ABRIR VSCODE PARA RODAR O PROGRAMA
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("vscode")
pyautogui.press("enter")
time.sleep(2) 
#open folder
pyautogui.press("tab", presses=3)
pyautogui.press("enter")
time.sleep(2) 
#area de trabalho   
pyautogui.press("tab", presses=3)
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")
#pasta scriptPython
pyautogui.write("C:\scriptPython\web-scraping")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(5)
#run ws.py
pyautogui.press("f5")
pyautogui.press("enter")
time.sleep(200) 
pyautogui.hotkey("alt","f4")

# ABRIR MYSQL 
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("MySQL Workbench")
time.sleep(2) 
pyautogui.press("enter")
time.sleep(2)  
pyautogui.write("Local Instance MySQL")
pyautogui.press("enter")
time.sleep(2)
#senha Mysql
""" pyautogui.write("password") """
pyautogui.press("enter")
time.sleep(2)
#escrever código mySQL
pyautogui.hotkey("ctrl","a")
#pyautogui.press("del")
#codMySQL ="""  use comparapreco;
# select*from precogeral;  
#alter table precogeral modify 
#	`Preço` decimal(5,2)
#;
# alter table precogeral modify 
#    `Preço em Dólar` decimal(5,2)
#;
# select*from precoatual;  
# 
# alter table precoatual modify 
#	`Preço` decimal(5,2)
#;
# alter table precoatual modify 
#    `Preço em Dólar` decimal(5,2)
#;  """
#pyautogui.write(codMySQL)
pyautogui.click(x=293, y=141)
time.sleep(2)
pyautogui.click(x=293, y=141)
time.sleep(2)
#run mysqlHistoricoComparaPreco         
time.sleep(2)
pyautogui.rightClick(x=115, y=233)
pyautogui.click(x=194, y=315)
time.sleep(2)
#next
pyautogui.press("tab",presses=8)
pyautogui.press("enter")
#browse
pyautogui.press("tab",presses=2)
pyautogui.press("enter")
pyautogui.write("HistoricoComparaPreco")
pyautogui.press("tab",presses=3)
pyautogui.press("enter")
#substituir 
pyautogui.press("tab",presses=1)
pyautogui.press("enter") 
pyautogui.press("tab",presses=8)    
pyautogui.press("enter") 
pyautogui.press("tab",presses=3)
pyautogui.press("enter") 
pyautogui.press("tab",presses=2)
pyautogui.press("enter")
pyautogui.press("tab",presses=1)
pyautogui.press("enter")
pyautogui.hotkey("alt","f4")

# ABRIR POWERBI

pyautogui.press("win")
pyautogui.write("POWER BI Desktop")
time.sleep(2) 
pyautogui.press("enter")
time.sleep(5)  
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.click(x=570, y=501)
time.sleep(5)
pyautogui.click(x=593, y=97)
