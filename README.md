# Ubidots MQTTClient Exemplos

### 🚀 Descrição

Essa aplicação foi um trabalho dado pelo professor Alan Lima Lemes, da disciplina de Tecnologias de Telecomunicações, e tinha o objetivo nos familiarizar com o uso de Python para criar conexões MQTT e também a integração da linguagem com a plataforma [Ubidots](https://ubidots.com/).

<h1></h1>

### 👩‍🚀 Como funciona

Executando o arquivo main.py, o programa se conectara com a sua conta na plataforma Ubidots e apresentará, no terminal, um menu com as seguintes opções:

- Enviar uma informação àos dispositivos 1, 2 ou 3 (ou criá-los, se não existirem);
- Ler o valor de um dispositivo já criado;

<h1></h1>

### 🏃‍♂️ Como usar

Primeiro, é nescessário criar um arquivo env.py na pasta src e preenche-lo seguindo o modelo do arquivo env-example.py. Substitua as variáveis vazias pelas suas informações, tais como o seu Token de acesso à plataforma, o dispositivo à ser modificado e as variáveis à serem lidas ou alteradas.

Após ter essas informações configuradas, instale a biblioteca paho, que é utilizada para gerar a comunicação entre o programa e o Ubidots, com o comando:

```bash
pip install paho-mqtt
```

Agora, apenas execute o arquivo main.py com o comando:

```bash
python main.py
```

Você deverá receber um retorno igual à este:

```bash
---------ESCOLHA UMA OPÇÃO----------
(1) Enviar informação dispositivo 01
(2) Enviar informação dispositivo 02
(3) Enviar informação dispositivo 03
(4) Ler dispositivo 04
(5) Sair
```

<br>
<h1></h1>

👋 Esse repositório foi criado por Diego Eiras. [Get in touch!](https://www.linkedin.com/in/diegoeiras)