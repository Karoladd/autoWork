#AUTOR(A): KAROLINE YAMAMOTO
#ATUALIZAÇÃO: 25 DE MAIO DE 2022
#DESAFIO: AUTOMAÇÃO TAREFAS DA FATEC

# IMPORTAR BIBLIOTECA
import pyautogui
import pyperclip
import time

# ABRIR O TEAMS
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "shift", "n")
pyperclip.copy("https://teams.microsoft.com/_?culture=pt-br&country=BR&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn#/school/teams-grid/General?ctx=teamsGrid")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

#ABRIR E-MAIL FATEC
pyautogui.hotkey("ctrl","t")
pyperclip.copy("https://outlook.office.com/mail/")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

#WORD EM NUVEM
pyautogui.hotkey("ctrl","t")
pyperclip.copy("https://www.office.com/launch/word?auth=2")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

#ABRIR APP INVENTOR (PTI)
pyautogui.hotkey("ctrl","t")
pyperclip.copy("http://ai2.appinventor.mit.edu/?locale=pt_BR")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.hotkey("ctrl","t")
pyperclip.copy("https://community.appinventor.mit.edu/")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# TESTE
""" time.sleep(5)
pyautogui.position()
print(pyautogui.position()) """