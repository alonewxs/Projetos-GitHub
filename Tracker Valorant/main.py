import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

region = input("Escolha a Região EU, NA, BR, AP, KR: ").lower()
name = input("Nome do jogador: ")
tag = input("Tag do jogador: ")



response_rank = requests.get(
    f"https://api.henrikdev.xyz/valorant/v2/mmr/{region}/{name}/{tag}",
    headers={"Authorization":API_KEY,"Accept":"*/*"},
)


data = response_rank.json()

## --- BASE --- ##
player_data = data["data"]
current_data = player_data["current_data"]

## --- USER --- ##
nome = player_data["name"]
tag = player_data["tag"]

## --- MMR --- ##
mmr_atual = current_data["ranking_in_tier"]
mmr_lastgame = current_data["mmr_change_to_last_game"]

## --- RANK --- ##
rank_atual = current_data["currenttierpatched"]
peak_rank = player_data["highest_rank"]["patched_tier"]


os.system("cls")

print(f"\nUsuario: {nome}#{tag}") ## nome e a tag do user
print(f"Rank Atual: {rank_atual}")
print(f"Peak Rank: {peak_rank}")
print(f"MMR Ultimo Jogo: {mmr_lastgame}")
print(f"MMR Atual: {mmr_atual}")

