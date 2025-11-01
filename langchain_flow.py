from langchain_core.messages import SystemMessage, HumanMessage
from google_ai import llm_google

llm = llm_google

system_message = SystemMessage(content=
  "Você é um guia de viagem útil e inteligente. Pode se comunicar em português. Fornece recomendações de viagem detalhadas e personalizadas."
)

human_message = HumanMessage(content="Olá, como você está?")

messages = [system_message, human_message]

response = llm.invoke(messages)

print(f"{'AI':-^80}")
print(response.content)

messages.append(response)

while True:
    print(f"{'Você':-^80}")
    user_input = input("Você: ")
    
    if user_input.lower() in ["sair", "exit", "quit"]:
        print("Encerrando a conversa. Até mais!")
        break
    
    human_message = HumanMessage(content=user_input)
    messages.append(human_message)
    
    response = llm.invoke(messages)
    print(f"{'AI':-^80}")
    print(response.content)
    
    messages.append(response)