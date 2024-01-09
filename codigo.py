# Passo a passo do projeto

# Passo 1 - Entrar no sistema da empresa
## https://dlp.hashtagtreinamentos.com/p...
# Passo 2 - Fazer login
# Passo 3 - Importar a base de dados
# Passo 4 - Cadastrar um produto
# Passo 5 - Repetir isso até acabar a base de dados
import pyautogui
import time
import pandas
# clicar -> pyautoguir.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar duas teclas -> pyautogui.hotkey("ctrl", "c")
pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
# esperar 4 segundos    
time.sleep(4)

pyautogui.click(x=418, y=374)
pyautogui.write("perau@hotmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.click(x=670, y=540)
time.sleep(3)
tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    # criando o primeiro produto
    pyautogui.click(x=452, y=260)
    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write("MOLO000251")
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria 
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    # enviar o produto
    pyautogui.press("enter")
    
    pyautogui.scroll(5000)