import requests

response = requests.get("https://hp-api.onrender.com/api/spells")
spell_list = []

if response.status_code == 200:
    items = response.json()
    for spell in items:
        spell_list.append(spell['name'])
