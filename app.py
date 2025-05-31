import streamlit as st
from transformers import MarianTokenizer, MarianMTModel

# Carregar modelo e tokenizer
@st.cache_resource
def load_model():
    model_name = "Helsinki-NLP/opus-mt-en-ROMANCE"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

# Função de tradução
def translate(text):
    inputs = tokenizer([text], return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

# Layout Streamlit
st.title("Tradutor de Inglês para Português 🇬🇧➡️🇧🇷")
st.write("Digite uma frase em inglês para traduzir:")

input_text = st.text_area("Texto em inglês:", height=100)

if st.button("Traduzir"):
    if input_text.strip() == "":
        st.warning("Por favor, insira algum texto.")
    else:
        with st.spinner("Traduzindo..."):
            translated_text = translate(input_text)
        st.success("Tradução:")
        st.text_area("Texto em português:", translated_text, height=100)
