import requests
import random
import os
from PIL import Image
from io import BytesIO

BASE_URL = "https://api.enem.dev/v1/exams/"
LANGUAGE = random.choice(["ingles", "espanhol"])

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        def fetch_question(ano: str, numero: str) -> dict:
            url = f"{BASE_URL}{ano}/questions/{numero}"
            querystring = {"language": LANGUAGE}
            try:
                response = requests.get(url, params=querystring)
                response.raise_for_status()
                return response.json()
            except requests.RequestException as e:
                print(f"Error fetching question: {e}")
                return {}

        def get_random():
            ano = str(random.randrange(2010, 2023))
            numero = str(random.randint(1, 180))
            question = fetch_question(ano, numero)
            
            files = question.get('files', [])
            if files:
                for file in files:
                    response = requests.get(file)
                    img = Image.open(BytesIO(response.content))
                    img.show()

            print(question.get('context', 'No context found'))
            print(question.get('alternativesIntroduction', 'No alternatives introduction found'))
            
            alternatives = question.get('alternatives', [])
            for alternative in alternatives:
                print(f"{alternative['letter']}) {alternative['text']}")
            
            resp = input('QUAL a alternativa correta? ')
            if resp.lower() == 'a' or resp.lower() == 'b' or resp.lower() == 'c' or resp.lower() == 'd' or resp.lower() == 'e':
                if resp:
                    resposta = str(question.get("correctAlternative", "No correct alternative found"))
                    if resp.lower() == resposta.lower():
                        print('Resposta correta!')
                    else:
                        print(28*'#' + '\n' + f'Errado. Resposta correta: {question.get("correctAlternative", "No correct alternative found")}' + '\n' + 28*'#')
            else:
                print('Não entendi.')

        escolha = input('Quer uma pergunta aleatoria ou quer escolher?\nDigite "aleatoria" ou "escolher": ')
        if escolha.lower() == 'aleatoria':
            get_random()
        elif escolha.lower() == 'escolher':
            ano = input('Digite o ano: ')
            if int(ano) < 2010 or int(ano) > 2023:
                print('Ano inválido.')
                continue
            numero = input('Digite o número da questão: ')
            print(fetch_question(ano, numero).get('context', 'No context found'))
            
            print(fetch_question(ano, numero).get('alternativesIntroduction', 'No alternatives introduction found'))
            alternatives = (fetch_question(ano, numero)).get('alternatives', [])
            for alternative in alternatives:
                print(f"{alternative['letter']}) {alternative['text']}")
            resp = input('QUAL a alternativa correta? ')
            if resp.lower() == 'a' or resp.lower() == 'b' or resp.lower() == 'c' or resp.lower() == 'd' or resp.lower() == 'e':
                if resp:
                    resposta = str(fetch_question(ano, numero).get("correctAlternative", "No correct alternative found"))
                    if resp.lower() == resposta.lower():
                        print('Resposta correta!')
                    else:
                        print(28*'#' + '\n' + f'Errado. Resposta correta: {(fetch_question(ano, numero).get("correctAlternative", "No correct alternative found"))}' + '\n' + 28*'#')
        else:
            print('Opção inválida.')
        sair = input('Sair? ')
        if sair.lower() == 'sair':
            break
        elif sair.lower() == 'sim':
            break
        elif sair.lower() == 's':
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

if __name__ == "__main__":
    main()