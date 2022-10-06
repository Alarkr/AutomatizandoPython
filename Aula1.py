import pyautogui
import pyperclip
import pandas as pd
import numpy
import openpyxl
from time import sleep

pyautogui.PAUSE = 2

# Passo 1: Entrar no sistema da empresa (no nosso caso é o link do drive kkk)
    # Abrir navegador -> Pegaria o link necessario -> Ctrl c + v -> colar na barra de pesquisa -> e dar enter para abrir o link
    # Abrir nova aba- 1°- Mouse e click no + do navegador ou 2° Ctrl + T
def abrirNavegador():
    pyautogui.press('win')
    pyautogui.write('chrome')
    pyautogui.press('enter')
    sleep(1)
    # pyautogui.click(-55, 90)
def abrirSite():
    pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    sleep(8)
abrirNavegador()
abrirSite()


# Passo 2: Navegar dentro do sistema e encontrar a base de vendas (entrar na pasta exportar)
    # No nosso caso é necessario usar o mouse para dar um click
    # Necessario dizer 2 posições obrigatorias para o mouse encontrar onde deve clicar
    # Para pegar o X e Y do mouse na tela... -> x , y = pyautogui.position() // print(f'x = {x} e y = {y}')
def abrirPasta():
    pyautogui.click(385, 296, clicks=2)  # abrir a pasta
    sleep(3)
abrirPasta()


#Passo 3: Fazer o Download da base de vendas
    # continuar usando os clicks para baixar a base
def downArquivo():
    pyautogui.click(385, 296)  # clicar uma vez no arquivo
    pyautogui.click(1716, 188)  # clicar nos 3 pontinhos
    sleep(1)
    pyautogui.click(1462, 625)  # clicar para baixar o arquivo
    sleep(3)
    pyautogui.click(793, 513)  # clicar para especificar a pasta do downloar
    sleep(3)  # esperar o download finalizar
downArquivo()
# Passo 4: Importar a base de vendas pro Python
tabela = pd.read_excel(r'C:\Users\Paulo\Downloads\Vendas - Dez.xlsx')

# Passo 5: Calcular os indicadores da Empresa
faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()
print(f'O total de peças vendidas foi {quantidade:.2f}\n'
      f'O Faturamento foi de  R${faturamento:.2f}')


# Passo 6: Enviar um e-mail (gmail) para a diretoria com os indicadores de venda
    #Passo 1: Abrir aba nova
    #Passo 2: Entrar no link do email mail.google.com/mail/u/0/#inbox
    #Passo 3: Clicar no botão escrever
    #Passo 4: Enviar o email

def abrirEmail():
    pyautogui.hotkey('ctrl', 't')
    pyperclip.copy('mail.google.com/mail/u/0/#inbox')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    sleep(8)
abrirEmail()

def escreverEmail():
    pyautogui.click(145, 202)
    sleep(2)
    pyperclip.copy('izasnog@gmail.com')
    pyautogui.hotkey('ctrl', 'v') #Email
    sleep(2)

    pyautogui.press('tab') #Selecionar email
    sleep(1)
    pyautogui.write('Aula 1- Automatizando') #Assunto
    sleep(1)
    pyautogui.press('tab') #Pular para corpo do email

    txtEemail = f'''
    Prezada, 
    Segue relatório de vendas e em anexo o arquivo do excel usado para realiza-lo.
    Faturamento: R${faturamento:,.2f}
    Quantidade de produtos vendidos: {quantidade:,.2f}
    
    
    Qualquer dúvida pega no meu pauzão
    Att.
    O paulin 
    '''
    pyperclip.copy(txtEemail)
    pyautogui.hotkey('ctrl', 'v')

def anexarPlanilha():
    pyautogui.click(1435, 957) #clicando no botao anexar
    sleep(2)
    pyautogui.click(214, 485) #clicando no campo nome do arquivo
    pyautogui.write('Vendas - Dez.xlsx')
    pyautogui.press('enter')
    sleep(3)

def enviarEmail():
    pyautogui.hotkey('ctrl', 'enter')

escreverEmail()
anexarPlanilha()
#enviarEmail()
