from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


client = OpenAI(

    api_key=os.environ.get("API_KEY"),
    base_url="https://api.groq.com/openai/v1",

)


PROMPT_SUPORTE = os.getenv("PROMPT_SUPORTE")
PROMPT_DIVERTIDO = os.getenv("PROMPT_DIVERTIDO")
PROMPT_PROFESSOR = os.getenv("PROMPT_PROFESSOR")
PROMPT_OBJETIVO = os.getenv("PROMPT_OBJETIVO")


prompts = {
    "suporte": PROMPT_SUPORTE,
    "divertido": PROMPT_DIVERTIDO,
    "professor": PROMPT_PROFESSOR,
    "objetivo": PROMPT_OBJETIVO,
}


nomes = list(prompts.keys())


for i, nome in enumerate(nomes, start=1):
    print(f"{i} - {nome}")


try:
    escolha = int(input("Qual prompt você deseja? "))
    modo = nomes[escolha - 1]
except:
    modo = "suporte"


prompt_escolhido = prompts[modo]


while True:
    pergunta = input("Pergunta: ")

    response = client.responses.create(
        model="openai/gpt-oss-20b",
        input=[
            {"role": "system", "content": prompt_escolhido},
            {"role": "user", "content": pergunta}
        ]
    )

    print(response.output_text)