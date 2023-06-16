import time
from behave import *
from selenium.webdriver.common.by import By


@given("que estou na página inicial")
def step_pagina_inicial(context):
    # Lógica para simular o usuário estar na página inicial
    # Substitua pelo URL do site real
    context.web.get("https://www.voeazul.com.br/br/pt/home#comprar")


@when('eu seleciono a origem como "{origem}"')
def step_selecionar_origem(context, origem):
    # Lógica para selecionar a origem
    # Substitua pelo ID correto do campo de origem
    context.element = context.web.find_element(By.NAME, "Origem1")
    # context.element.click()
    context.element.send_keys(origem)
    time.sleep(2)


@when('eu seleciono o destino como "{destino}"')
def step_selecionar_destino(context, destino):
    # Lógica para selecionar o destino
    context.element = context.web.find_element(By.NAME, "Destino1")
    # context.element.click()
    context.element.send_keys(destino)
    time.sleep(2)


@when('eu escolho a data ida como "{ida}"')
def step_selecionar_ida(context, ida):
    # Lógica para selecionar o destino
    context.element = context.web.find_element(By.ID, "datepicker_temp1")
    context.element.send_keys(ida)
    time.sleep(2)


@when('eu escolho a data retorno como "{retorno}"')
def step_selecionar_retorno(context, retorno):
    # Lógica para selecionar o destino
    context.element = context.web.find_element(By.ID, "return-1")
    context.element.send_keys(retorno)


@when("eu clico no botão de pesquisa")
def step_clicar_pesquisa(context):
    # Lógica para simular o clique no botão de pesquisa
    path = "#spa-root > main > div:nth-child(1) > div.aem-page.AzulPage.page.basicpage > div:nth-child(1) > div.aem-container.aem-Grid.aem-Grid--12.aem-Grid--default--12 > div:nth-child(3) > div.aem-container.aem-Grid.aem-Grid--12.aem-Grid--tablet--12.aem-Grid--default--12.aem-Grid--phone--12 > div:nth-child(1) > div.css-1sel6ui > div.css-16ub5e0 > div > nav > div > div > div:nth-child(1) > div.css-1eztqvd > div:nth-child(1) > ul > li:nth-child(2) > div > div.form-stations-wrapper.css-187knvu > div > div.css-nzp9bm > div > div > div.css-1p9ikbq > button"
    button = context.web.find_element(By.CSS_SELECTOR, path)
    button.click()
    time.sleep(100)
    # WebDriverWait(context.driver, 10).until(
    #    EC.presence_of_element_located((By.ID, "flight-list"))
    # )


@then("eu vejo uma lista de voos disponíveis")
def step_ver_lista_voos(context):
    # Lógica para verificar se a lista de voos está sendo exibida corretamente
    pass
