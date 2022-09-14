#AUTOR(A): KAROLINE YAMAMOTO
#ATUALIZAÇÃO: 25 DE MAIO DE 2022
#DESAFIO: AUTOMAÇÃO ENVIO DE E-MAIL 

# IMPORTAR BIBLIOTECAS
import pyautogui
import pyperclip
import time
from datetime import date

# Passo 1: Abrir E-mail
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("outlook")
pyautogui.press("enter")
time.sleep(5)

# Passo 2: Criar Novo E-mail
pyautogui.click(x=-1894, y=87)
time.sleep(2)
pyautogui.write("dferreira@uniondigitalit.com")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.write("lhenrique@uniondigitalit.com")
pyautogui.press("enter")
pyautogui.write("pcarvalho@uniondigitalit.com")
pyautogui.press("enter")
pyautogui.press("tab")
data = date.today()
pyautogui.write("Status Report %s"%data)
pyautogui.press("enter")
texto = """ 
Boa tarde pessoal!

Abaixo se encontra as atividades realizadas no dia de hoje:

{tabela}

Qualquer dúvida estou à disposição! """
pyperclip.copy(texto)
pyautogui.hotkey("ctrl","v")

# Passo 3: Abrir Excel com o Histórico de Trabalho

# Passo 4: Realizar alterações na planilha do Excel (data e tarefas)

# Passo 5: Copiar e colar na parte {tabela} do e-mail

# Passo 6: Inserir os arquivos alterados

# Passo 7: Conferir se está correto e enviar e-mail

# TESTE
""" time.sleep(5)
pyautogui.position()
print(pyautogui.position()) """





