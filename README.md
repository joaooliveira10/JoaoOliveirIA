# 📚 Documentação: João IA 🧠
O "João IA 🧠" é uma aplicação web interativa que permite conversar com um **modelo de linguagem aberta** usando a interface intuitiva do Streamlit. O backend utiliza LangChain com o servidor local Ollama.
## 📌 Pré-requisitos
Antes de instalar "João IA 🧠", certifique-se de possuir as seguintes ferramentas e requisitos básicos instalados no seu sistema operacional:
- Python 3.8 ou superior ([Instalar Python](https://www.python.org/downloads/))
- Git ([Download Git](https://git-scm.com/downloads))

## 🚀 Como Instalar
### 1. Clone o repositório (caso esteja utilizando Git):
``` bash
    git clone https://github.com/joaooliveira10/JoaoOliveirIA.git
    cd JoaoOliveirIA
```
**Alternativa:** Copie manualmente o arquivo `JoaoIA.py` e o arquivo `requirements.txt` para um diretório desejado.
### 2. Crie um ambiente virtual dedicado:
Recomendado para manter o ambiente limpo e organizado:
``` bash
    python -m venv venv
```
- **Windows:**
``` 
    venv\Scripts\activate
```
- **Linux/MacOS:**
``` sh
    source venv/bin/activate
```
### 3. Instale as dependências necessárias:
``` bash
    pip install -r requirements.txt
```
## 🖥 Instalar e Configurar o Ollama
**Ollama** é usado como servidor local rodando o modelo Gemma3. Siga estes passos para configurá-lo:
### 1. Instalação do Ollama:
Visite o site oficial Ollama e instale-o seguindo as documentações:
- [Site Oficial do Ollama](https://ollama.com/)

Após instalado, inicie o servidor Ollama garantindo que ele fique disponível localmente:
``` sh
    ollama serve
```
### 2. Baixar o modelo Gemma3 via Ollama:
``` bash
    ollama pull gemma3
```
Certifique-se de que o modelo esteja disponível localmente (`gemma3:latest`).
## 🚦 Executando a aplicação "João IA 🧠"
Após configurar todas as dependências e ter o Ollama ativo, execute estes comandos no terminal da pasta onde está **JoaoIA.py**:
``` bash 
    streamlit run JoaoIA.py
```
**Acessar a Aplicação:** Normalmente abre uma janela do navegador automaticamente. Caso isso não ocorra, abra seu navegador e navegue até:
``` 
    http://localhost:8501
```
## 📌 Como Usar o João IA 🧠?
A interface é simples e autoexplicativa:
- Digite uma mensagem no campo interativo localizado na parte inferior.
- Pressione **Enter** para enviar sua mensagem ao João IA.
- A resposta do João IA será mostrada na interface logo em seguida.

As mensagens anteriores permanecem na interface enquanto a sessão estiver aberta.
## 🛠 Informações técnicas detalhadas (opcional):
- **Dependências principais utilizadas:**
    - `streamlit==1.43.2`: Utilizado para criar a aplicação web interativa e amigável.
    - `langchain-ollama==0.3.0`: Facilita a conexão direta com modelos hospedados localmente via Ollama.

- **Estrutura do Projeto:**

Estrutura recomendada dos arquivos do seu projeto:
``` plaintext
JoaoIA-projeto/
├── requirements.txt    # Dependências python
├── JoaoIA.py           # Código Streamlit da aplicação
└── venv/               # Ambiente virtual python
```
## ⚠️ Problemas e Soluções Comuns
**Ollama não inicia:**
- Certifique-se de que nenhum Firewall ou sistema de segurança esteja impedindo a comunicação local.

**Modelo não encontrado ou não disponível:**
- Confirme que baixou o modelo corretamente com `ollama pull gemma3`.

**Problemas com instalação de dependências:**
- Verifique a versão correta do seu Python e assegure-se de atualizar o pip (`pip install --upgrade pip`).

🎉 Agora você está pronto para usar o João IA e aproveitar toda a facilidade e potencial desta aplicação interativa!

## Extra

## 🌐 Colocando o João IA Online com Ngrok
O **Ngrok** é uma ferramenta útil que permite expor serviços locais para acesso público seguro via internet através de túneis seguros. É ideal para testar rapidamente e compartilhar a aplicação com outras pessoas.
### ⚙️ Instalação do Ngrok:
1. Acesse o site oficial do Ngrok para baixar e instalar: [Baixar Ngrok](https://ngrok.com/download)
2. Após baixar, descompacte ou instale o executável em um local de fácil acesso.

### 🔑 Obtenha um Token (Autenticação):
1. Você precisará de uma conta gratuita no Ngrok. Crie através do site oficial: [Criar conta no Ngrok](https://dashboard.ngrok.com/signup)
2. Após criar e validar sua conta, acesse seu painel Ngrok [aqui](https://dashboard.ngrok.com/get-started/your-authtoken). Copie seu token de autenticação.

_Exemplo de Token:_
``` 
    ngrok config add-authtoken <SEU_TOKEN>
```
### 🌍 Inicialização do túnel Ngrok:
Com o Streamlit rodando já normalmente localmente (`streamlit run JoaoIA.py`):
Abra um novo terminal e utilize Ngrok para criar o túnel:
``` bash
    ngrok http 8501
```
(_Porta padrão utilizada pelo Streamlit: 8501_)
### ✅ Utilização e acesso online:
Após iniciar o comando, o Ngrok fornecerá uma URL pública temporária em seu terminal. Exemplo típico da saída do Ngrok:
``` 
Forwarding                    https://seutunel.ngrok-free.app -> http://localhost:8501
```
**Copie a URL fornecida pelo Ngrok e compartilhe com outras pessoas** para acessarem remotamente esse endereço e utilizarem o João IA 🧠 imediatamente através da internet!
### 🔒 Recomendações Importantes (Segurança):
- Cada sessão gratuita do Ngrok gera uma URL aleatória e expira automaticamente ao encerrar o serviço.
- Não esqueça de **encerrar o túnel com Ctrl+C** no terminal após o uso.
- Para usos mais duradouros ou fixos, considere a possibilidade de assinatura paga, que permite URLs permanentes e adicionais configurações.

✨ Agora seu João IA está acessível de qualquer lugar usando o Ngrok, aproveitando ainda mais as possibilidades dessa ferramenta poderosa e prática!

