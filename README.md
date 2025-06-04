# 📱 Carrossel_Social

Carrossel Social é um protótipo de aplicação com integração à OpenAI que gera carrosséis para redes sociais usando inteligência artificial. O sistema cria tanto o conteúdo textual (em formato Markdown) quanto imagens ilustrativas por slide, de acordo com o público-alvo e tom desejado.

![image](https://github.com/user-attachments/assets/0cfe2819-3fe2-444a-821b-948051f4ea41)

## 🚀 Funcionalidades
Geração automática de carrosséis com GPT-4o.

Produção de imagens para cada slide usando DALL·E 3.

Interface amigável via Streamlit.

Personalização por conteúdo, público-alvo e tom de voz.

## 🛠️ Tecnologias

- Python
- Streamlit
- OpenAI API (ChatGPT + DALL·E 3)

LangChain

## ▶️ Como usar
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

## 🧪 Exemplo de uso

Preencha os campos:

Conteúdo: o tema central do post.

Público-alvo: para quem o post é direcionado.

Tom de voz: escolha entre Amigável, Profissional, Urgente ou Divertido.

Clique em Gerar para receber os slides em Markdown + imagens.

## Exemplo Prático

![image](https://github.com/user-attachments/assets/2de54c3f-d809-4c30-ae4c-05b902b29638)
![image](https://github.com/user-attachments/assets/ece07ae8-5cca-48d3-a77a-2fa0bdcfc9ce)

## ⚠️ Observações

O uso das APIs da OpenAI pode gerar custos.

Verifique os limites da sua conta para evitar erros na geração de imagens.

## Aviso de Direitos Autorais
Este projeto foi desenvolvido por **Lucas Rial**. O código é de propriedade exclusiva de Lucas Rial e está licenciado sob a **Licença MIT**. A reutilização do código é permitida, desde que a autoria seja devidamente reconhecida. Se você utilizar ou modificar este código, deve incluir uma referência a **Lucas Rial** em qualquer distribuição ou derivação.

## Contribuição
Sinta-se à vontade para abrir issues e pull requests para melhorias.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
