## Introdução

O Pycord é um wrapper de API moderno, fácil de usar, rico em recursos e pronto para assíncrono para o Discord, escrito em Python.

---

### Voce deve ter noção de:

- Variáveis
- Tipos de Dados
- Funções
- Pacotes
- Condicionais
- Loops
- Classes
- Programação Orientada a Objetos
- Herança
- Manuseio de Exceções
- Iteradores
- Coroutinas
- Async/Await

---

### Instalação

Antes de começar a usar o Pycord, você precisa instalar a biblioteca:

```python
pip install py-cord
```

Se você precisa de suporte por voz para o seu bot, você deve executar:

```python
pip install "py-cord[voice]"
```

⚡Python 3.8 O acima é necessário utilizar Pycord.

---

### Atualizando Pycord
Se você estiver atualizando a partir de uma versão anterior do Pycord, você pode usar o seguinte comando em seu terminal para atualizar para a versão mais recente:

```python
pip install -U py-cord
```
#### Migrando de outras bibliotecas
Se você estiver migrando de outra biblioteca, digamos, `discord.py`, em primeiro lugar, você precisa desinstalá-lo.

```python
pip uninstall discord.py
```

Então, você pode instalar o Pycord, é tão simples quanto isso!:

```python
pip install py-cord
```

---

### Instalando Outras Construções
#### Desenvolvimento Build

Para instalar a compilação de desenvolvimento, você pode usar o seguinte comando no seu terminal:

```python
pip install -U git+https://github.com/Pycord-Development/pycord
```

---

### Criando Seu Primeiro Bot
#### Protegendo Tokens
##### Usando dotenv

- Você pode armazenar seus tokens em .env arquivos. Esta é uma maneira simples de armazenar informações confidenciais.

- Crie um arquivo com o nome `.env` (apenas a extensão, com um ponto/período no início e sem um nome antes).
Defina o token no `.env` arquivo (substitua o valor de exemplo pelo seu token).

```python
TOKEN =
```

#### Instalar python-dotenv
```python
python -m pip install python-dotenv
```

#### Carregue o token do .env arquivo
```python
import dotenv
dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))
```

#### Passe seu token como parâmetro ao executar o bot
```python
client.run(token)
```

### Codificando o Básico
Aqui está um exemplo de código que você escreverá com Pycord:

```python
import discord
import os
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user}: Eu estou online!")

@bot.slash_command(name = "ola", description = "Imprima uma mensagem do bot")
async def ola(ctx):
    await ctx.respond(f"Olá {ctx.author.mention}!")

bot.run(os.getenv('TOKEN'))
```
---

### Vamos ver o código
#### Primeiro, as importações

Na primeira linha, `import discord`, importamos Pycord

Nós importamos então `os` e `dotenv`. `os` é um módulo padrão que usaremos para obter o token do arquivo env. `dotenv` é um módulo que usaremos para carregar o arquivo env. Você instalou isso com `pip install python-dotenv`.

Em seguida, carregamos o arquivo env com `load_dotenv()`
```python
import discord
import os
from dotenv import load_dotenv
```
```python
bot = discord.Bot()
```
Nesta linha, criamos uma nova instância de `discord.Bot`. Neste objeto, podemos passar vários parâmetros para fins de configuração, tais como `owner_ids` e `intents`.

```python
@bot.event
async def on_ready():
    print(f"{bot.user}: Eu estou online!")
```
Nós usamos o `event` decorador para substituir o `on_ready` função para definir um evento que é chamado automaticamente quando o bot está pronto para uso.
```python
@bot.slash_command(name = "ola", description = "Imprima uma mensagem de "Olá" do bot")
async def ola(ctx):
    await ctx.respond(f"Olá {ctx.author.mention}!")
```

Aqui, usamos o `slash_command` decorador para definir um comando de barra. Nós especificamos o `name` e `description` argumentos. Se não especificado, o nome do comando slash seria o nome da função e a descrição do comando seria esteja vazio.

Finalmente, você deseja executar o bot usando o token especificado no `.env` arquivo.

### Execute seu bot:
Abra o terminal e digite:
```python
python main.py
```
⚡Caso você tenha colocado outro nome ao invés de  `main.py`, substitua ele.

### Mapa:
```python
seu_projeto/
├── .env
├── main.py
```