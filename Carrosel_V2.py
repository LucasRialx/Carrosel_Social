import streamlit as st
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import re

# ====== Sua chave OpenAI aqui ======
OPENAI_KEY = "SUA CHAVE OPENAI AQUI"
# ===================================

# Inicializa APIs
chat = ChatOpenAI(
    temperature=0.7,
    model_name="gpt-4o",
    openai_api_key=OPENAI_KEY
)

client = OpenAI(api_key=OPENAI_KEY)

# UI do app
st.title("Carrossel_Social 🚀")
conteudo = st.text_input("Conteúdo")
publico = st.text_input("Público-alvo")
tom = st.selectbox("Tom de voz", ["Amigável", "Profissional", "Urgente", "Divertido"])

# Template do prompt
template = """
Você é um copywriter especialista. Gere:
1) Um carrossel de Instagram. Me devolva uma resposta em Markdown, separando os slides do carrossel com títulos claros como **Slide 1**, **Slide 2** etc.
2) Uma descrição ótima.
conteúdo: {conteudo}
Público-alvo: {publico}
Tom de voz: {tom}
"""

prompt = PromptTemplate.from_template(template)

if st.button("Gerar"):
    # Gera carrossel
    resposta = chat.invoke(prompt.format(conteudo=conteudo, publico=publico, tom=tom))
    st.subheader("Carrossel Instagram")
    markdown_text = resposta.content
    st.markdown(markdown_text)

    # Divide slides com base em títulos do markdown
    slides = re.findall(r"\*\*Slide \d+\*\*(.*?)\n(?=\*\*|$)", markdown_text, re.DOTALL)

    st.subheader("Imagens por Slide")

    for idx, slide_text in enumerate(slides, start=1):
        prompt_img = f"Crie uma imagem visualmente atraente e moderna para um post do Instagram com o conteúdo: {slide_text.strip()}, tom: {tom}, público-alvo: {publico}."

        with st.spinner(f"Gerando imagem do Slide {idx}..."):
            try:
                img_response = client.images.generate(
                    model="dall-e-3",
                    prompt=prompt_img,
                    size="1024x1024",
                    quality="standard",
                    n=1
                )

                # Debug: mostrar resposta completa
                # st.write(f"Resposta da imagem (Slide {idx}):", img_response)

                image_url = img_response.data[0].url if img_response.data else None

                if image_url:
                    st.image(image_url, caption=f"Slide {idx}")
                else:
                    st.warning(f"Nenhuma imagem gerada para Slide {idx}. Verifique sua chave ou limite de uso.")
            except Exception as e:
                st.error(f"Erro ao gerar imagem para o Slide {idx}: {e}")
