from selenium import webdriver # Permite criar um navegador
from selenium.webdriver.common.keys import Keys # Permite escrever no navegador
from selenium.webdriver.common.by import By # Permite selecionar itens no navegador


#Caso queira que o navegador não abra, pode usar os comandos
    #from selenium.webdriver.chrome.options import Options
    #chrome_options = Options()
    #chrome_options.headless = True
    #navegador = webdriver.Chrome(options=chrome_options)

# Passo 1: Pegar a cotação do Dolar
    # Passo 1: abrir o navegador e entrar no google
    # Passo 2: Procurar por cotação do dolar
    # Passo 3: Pegar o valor

navegador = webdriver.Chrome()
navegador.get('https://www.google.com.br')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Cotação Dolar')


# Passo 2: Pegar a cotação do Euro
# Passo 3: Pegar a cotação do Ouro
# Passo 4: Atualizar a base de preços (atualizando preço de compra e venda)
# Passo 5: Exportar base