# Projeto Semestral de Inteligência Artificial

Este repositório contém um projeto de tradução automática de inglês para português, utilizando o modelo **MarianMT** da Hugging Face.

## Índice
1. [Código completo e executável](#Código-completo-e-executável-em-um-notebook-Python)
2. [Aplicação Streamlit](#Aplicação-Streamlit)
3. [Texto/Artigo](#Texto-/-Artigo-do-projeto)
4. [Vídeo de apresentação](#Vídeo-de-Apresentação)

## Código completo e executável em um notebook Python

👉 [Acesse o notebook aqui](Projeto_IA.ipynb)

##  Aplicação Streamlit
Para consumir o modelo via uma aplicação Streamlit, siga os passos:

### 1. Clone o repositório

```bash
git clone https://github.com/erikhsu08/projetoIA.git
cd projetoIA
```

### 2. Baixe o modelo treinado
👉 [Download modelo_final.zip](https://drive.google.com/file/d/1NyLsw22E6XrfyftoYIfC9zzd3Y3btcXt/view?usp=sharing)

[⚠️**IMPORTANTE**] Após o download:
 - Extraia o conteúdo na mesma pasta onde está o `app.py`
 - Certifique-se de que a estrutura do diretório fique assim:  
![image](https://github.com/user-attachments/assets/c822ff1e-4bde-4271-8b32-f92e67a6e1ef)

### 3. No terminal, instale as dependências

```bash
pip install streamlit transformers torch sentencepiece protobuf numpy pillow
```

### 4. Execute a aplicação Streamlit

```bash
streamlit run app.py
```

### 5. Acesse a aplicação

Após executar o comando acima, o Streamlit abrirá automaticamente seu navegador padrão. Caso isso não aconteça, acesse manualmente:

```
http://localhost:8501
```

### 6. Resultado esperado
Segue uma printscreen da aplicação Streamlit que deverá ser exibida para consumo do modelo desenvolvido:
![image](https://github.com/user-attachments/assets/9631e39b-a201-4e3b-9263-93850773add1)



## Texto / Artigo do Projeto

## Vídeo de Apresentação
- inserir link aqui
