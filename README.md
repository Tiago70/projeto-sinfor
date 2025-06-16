# Passos para a instalação e configuração do sistema

O sistema está dividido em duas partes: Front end e Back end.
O front end não tem nenhum segredo, usando os clássicos html, css e javascrit.
Já o back end, é preciso realizar algumas instalações e configurações para o funcionamento correto da API.

## Bibliotecas

O back end foi construído no modelo API rest utilizando o Django + Django rest framework. Ao todo são 3 bibliotecas, abaixo está o comando para instalar todas usando o gerenciador de pacotes do python "pip':

    pip install django
    pip install djangorestframework
    pip install django-cors-headers

## Configurações

Com todas as bibliotecas instaladas agora é preciso configurar o CORS para que a API aceite as requisições do site onde o front end está. Para adicionar o endereço do site acesse o seguinte caminho: 

    sinfor api/src/settings.py

Após abrir o arquivo `settings.py` procure pela variável chamada `CORS_ALLOWED_ORIGINS` e adicione o endereço  do seu front end
Exemplo: https://meusite.com

Com isso, o back end já deve estar funcionando corretamente
