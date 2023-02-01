from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import re


PATH = "/Users/rodolfomoura/Documents/chromedriver_mac64.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.pingodoce.pt")




driver.implicitly_wait(15)


# Aceitar cookies ----- Funciona
aceitarCookies = driver.find_element(By.ID,'onetrust-accept-btn-handler').click()
time.sleep(3)

# Negar novidades --- Nao funciona
#negarNovidades = driver.find_element(By.CLASS_NAME, 'deny').click()


# Procurar na barra de pesquisa
'''

# Encotrar barra de pesquisa 
procurarBarra = driver.find_element(By.NAME,value='s')

# o que vai escrever na barra de pesquisa
procurarBarra.send_keys("Receitas de panquecas")
procurarBarra.send_keys(Keys.RETURN)
'''

# Contar panquecas --- não funciona diferença de upper e lower
'''
# Elemento a procurar
elementoContar = str("Panquecas")

# Localizar elemento
contar = driver.find_elements(By.PARTIAL_LINK_TEXT,elementoContar)

# Imprimmir a contagem
print("Numero de vezes panquecas ", len(contar))
'''


