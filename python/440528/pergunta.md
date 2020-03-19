Estou fazendo um programa em Python 3.8 usando o Selenium e o Chromedrive,
para acessar um site pelo Google Chrome. Na hora de executar, o programa abre duas janelas, uma do
Google Chrome e outra do prompt. Porém, quero que esse acesso seja feito de forma invisível, sem
abrir nenhuma janela além da do Python.

Meu código está mais ou menos assim:

    from selenium import webdriver
    
    driver = webdriver.Chrome()
    
    driver.get("https://google.com")

Como faço pra deixar o processo invisível pro usuário? 
Se eu tiver que instalar alguma biblioteca, em qual pasta do Python eu coloco ela? Qual o comando?

O programa vai ser executado no windows 32.

Obrigado desde já, preciso muito dessa ajuda.
