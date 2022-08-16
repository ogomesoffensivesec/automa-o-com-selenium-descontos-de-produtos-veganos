
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# faz com que o browser não abra durante o processo
options.add_argument("--headless")
# caminho para o seu webdriver

driver = webdriver.Chrome(
    executable_path=r'./chromedriver.exe', options=options)
wait = WebDriverWait(driver, 10)


def extractInfos():
    index = 1
    lista_prod = []
    lista_old = []
    lista_new = []
    while index != 5:
        print(f'Escaneando a {index}º página')
        print(60*'=')
        driver.get(
            f'https://www.vegin.com.br/desconto-verde.html?p={index}')

        time.sleep(1)
        infoprodutos = driver.find_elements(
            By.CLASS_NAME, 'infobox')
        olds = driver.find_elements(By.CLASS_NAME, 'old-price')
        news = driver.find_elements(By.CLASS_NAME, 'special-price')

        for produtos, p_antigo, p_novo in zip(infoprodutos, olds, news):
            ext_produto = produtos.find_element(By.TAG_NAME, 'h2').text
            ext_valor_antigo = p_antigo.find_element(
                By.CLASS_NAME, 'price').text
            ext_valor_novo = p_novo.find_element(By.CLASS_NAME, 'price').text
            lista_prod.append(ext_produto)
            lista_old.append(ext_valor_antigo)
            lista_new.append(ext_valor_novo)
        index = index + 1

    return lista_prod, lista_old, lista_new


def criarFrame():
    lista = []
    lista = extractInfos()
    dicio_lista = {
        'Produto': lista[0], 'Antigo Valor': lista[1], 'Novo Valor': lista[2]}
    dados = pd.DataFrame(data=dicio_lista)
    print(len(lista[0]))
    return dados


# criarFrame()


def saveInfosinExcelFile():
    dados = criarFrame()
    dados.to_excel('dados.xlsx', index=False)
    print(f'Páginas escaneadas e informações extraídas para uma planilha Excel!')
