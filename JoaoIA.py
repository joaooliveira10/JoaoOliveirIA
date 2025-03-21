import streamlit as st
from langchain_ollama import ChatOllama

# Configurar LLM
llm = ChatOllama(model="gemma3:latest", base_url='http://localhost:11434')

# Configurar Streamlit
st.set_page_config(page_title="João IA 🧠", layout="centered")
st.title("Converse com o João IA 🧠!")

# Criar histórico de mensagens
if "mensagens" not in st.session_state:
    st.session_state['mensagens'] = []
mensagens = st.session_state['mensagens']

# Exibir mensagens anteriores
for tipo, conteudo in mensagens:
    chat = st.chat_message(tipo)
    chat.markdown(conteudo)

# Pegar entrada do usuário
prompt = st.chat_input('Mande sua mensagem para o João IA 🧠...')

if prompt:
    mensagens.append(('human', prompt))

    # Exibir pergunta do usuário
    chat = st.chat_message('human')
    chat.markdown(prompt)

    # Gerar resposta da IA
    resposta = llm.invoke(mensagens).content
    mensagens.append(('ai', resposta))

    # Exibir resposta da IA
    chat = st.chat_message('ai')
    chat.markdown(resposta)
