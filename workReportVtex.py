#AUTOR(A): KAROLINE YAMAMOTO
#ATUALIZAÇÃO: 25 DE MAIO DE 2022
#TAREFA: FACILITAR O ENVIO DE E-MAIL 

import pyautogui
import pyperclip
import time

""" # EMAIL
# Passo 1: Abrir E-mail
pyautogui.press("win")
pyautogui.write("outlook")
pyautogui.press("enter")
time.sleep(3)
# Passo 2: Criar Novo E-mail
pyautogui.click(x=-1894, y=87)
time.sleep(2)
pyautogui.write("pablo@sudambeef.com")
pyautogui.press("enter")
pyautogui.write("pedro@sudambeef.com")
pyautogui.press("enter")
pyautogui.write("lpimentel@sudambeef.com")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.write("lhenrique")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.write("E-commerce - Desempenho")
pyautogui.press("tab")
texto = """ 
#Boa tarde Pessoal, tudo bem?

#Segue o Desempenho do E-commerce

"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl","v") """


#ECOMMERCE
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyperclip.copy("https://sudambeef.myvtex.com/admin/")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)
#performace de vendas
pyautogui.press("tab",presses=10)
pyautogui.press("enter")
time.sleep(5)

#PRINT GESTÃO DE VENDAS
pyautogui.hotkey("win", "shift", "s")
pyautogui.click(pyautogui.moveTo(x=-25, y=162))
pyautogui.dragTo(-1700,550,4,button='left') 


time.sleep(5)
pyautogui.position()
print(pyautogui.position())