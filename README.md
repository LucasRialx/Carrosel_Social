## 📱 Carrossel_Social##

Carrossel Social é um protótipo de aplicação com integração à OpenAI que gera carrosséis para redes sociais usando inteligência artificial. O sistema cria tanto o conteúdo textual (em formato Markdown) quanto imagens ilustrativas por slide, de acordo com o público-alvo e tom desejado.

# 🚀 Funcionalidades
Geração automática de carrosséis com GPT-4o.

Produção de imagens para cada slide usando DALL·E 3.

Interface amigável via Streamlit.

Personalização por conteúdo, público-alvo e tom de voz.

# 🛠️ Tecnologias

- Python
- Streamlit
- OpenAI API (ChatGPT + DALL·E 3)

LangChain

# ▶️ Como usar
Clone este repositório:

```
git clone https://github.com/seu-usuario/post-pronto.git
cd post-pronto
```

Instale as dependências:

```
pip install -r requirements.txt
Adicione sua chave OpenAI:
No código, substitua "SUA CHAVE OPENAI AQUI" pela sua chave pessoal.
```

Rode o app:

```
streamlit run app.py
```

# 🧪 Exemplo de uso

Preencha os campos:

Conteúdo: o tema central do post.

Público-alvo: para quem o post é direcionado.

Tom de voz: escolha entre Amigável, Profissional, Urgente ou Divertido.

Clique em Gerar para receber os slides em Markdown + imagens.

## ⚠️ Observações

O uso das APIs da OpenAI pode gerar custos.

Verifique os limites da sua conta para evitar erros na geração de imagens.
