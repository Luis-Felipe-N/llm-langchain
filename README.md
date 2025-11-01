# LLMs 

Repositorio de estudo sobre llms e ferreamentas de integração.

## LLms gratuitas

### Ollama (local)

Para testes e usar modelos locais o **Ollama** funciona bem. Ele permite fazer testes mais complexos sem estourar o limite de tokens gratuitos ou gastar demais com APIs pagas como OpenAI, Anthropic, etc.

- [Como Usar Ollama para LLMs no Seu Computador?](https://youtu.be/9Yz42WSISr4?si=aBVdWmfR8aQmtKD4)

---

### Google AI Studio (API gratuita)

Se estiver em usando um sistema que não tem hardware suficiente para rodar um modelo local. Geralmente isso exige uma boa CPU/GPU e bastante espaço em disco e memória. Mesmo quando o
hardware dá conta, pode ser que o modelo não esteja otimizado para a sua máquina
e acabe rodando de forma tão lenta que inviabiliza os testes.

Nesses casos, a alternativa são **APIs externas** (gratuitas ou pagas).

A **Google** oferece uma API Key gratuita
para desenvolvedores. Isso permite usar os modelos **Gemini**,
suficientes para testes. Você pode gerar a chave no link:

- [Google AI Studio](https://aistudio.google.com/apikey)

## Frameworks de integração

### LangChain

O **LangChain** é uma caixa de ferramentas gigante para trabalhar com LLMs. Ele
tenta resolver quase tudo: integração com diferentes modelos e providers, banco
de dados, RAG, ferramentas externas (tools), encadeamento de chamadas com o
**LCEL (LangChain Expression Language)**, e muito mais.

O próprio nome já entrega a ideia: a parte _"chain"_ vem de **chains**
(correntes, cadeias, encadeamento). Ou seja, você monta uma **sequência de
passos** onde a saída de um vira a entrada do próximo. Um fluxo típico fica
assim:

```
Prompt -> LLM -> Solução -> FIM
```
