from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import zipfile
import wget

# Definir navegador
options = webdriver.ChromeOptions()
navegador = webdriver.Chrome(options)


# Definir site
navegador.get("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos")


# Rejeitar cookies
botao_rejeitar = navegador.find_element(By.XPATH, "//button[contains(text(), 'Rejeitar')]").click()

time.sleep(5)


# Downloads anexos 1 e 2
link_1 = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
wget.download(link_1, 'anexo1.pdf')
try:
    print('Baixado com sucesso')
except:
    print('Não foi possivel realizar o download')

link_2 = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf'
wget.download(link_2, 'anexo2.pdf')
try:
    print('Baixado com sucesso')
except:
    print('Não foi possivel realizar o download')


# Criar uma pasta zip
lista_arquivos = os.listdir()
pasta = "compactacao.zip"

# Criar ou abrir o arquivo ZIP
with zipfile.ZipFile(pasta, 'w') as zipf:
    for arquivo in lista_arquivos:
        if arquivo.endswith('.pdf'):
            zipf.write(arquivo, arquivo) 
            os.remove(arquivo)  

print(f"Arquivos PDF foram compactados em {pasta}.")
