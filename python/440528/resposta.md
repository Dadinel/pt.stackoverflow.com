Para não exibir o navegador, você precisar criar uma `ChromeOptions` e adicionar o argumento `--headless`.

Você não vai precisar instalar nenhuma biblioteca, pois a `ChromeOptions` está no `webdriver` do `selenium`, biblioteca a qual você já está utilizando.


----------

Criando o `ChromeOptions` e a opção *headless*:

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

Agora com a variável `options` pronta, você precisa enviar a mesma no momento que for instanciar o driver do Chrome:

    driver = webdriver.Chrome(chrome_options=options)


----------

Seu código ficará da seguinte forma:

    from selenium import webdriver
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://google.com")
    
    #Restante do código
    
    driver.quit()
