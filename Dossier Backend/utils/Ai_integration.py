import os
import requests

OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY')
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "mistralai/mistral-medium" # Exemple de modèle

def generate_letter_part(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "your-website-or-app-name" # Requis par OpenRouter
    }
    data = {
        "model": MODEL,
        "prompt": prompt,
        "max_tokens": 200
    }
    try:
        response = requests.post(f"{OPENROUTER_BASE_URL}/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel à OpenRouter: {e}")
        return None

def get_company_info(company_name):
    prompt = f"Donne des informations clés sur l'entreprise {company_name} : secteur d'activité, points importants."
    return generate_letter_part(prompt)

def choose_salutation(recipient_gender):
    if recipient_gender.lower() == "female":
        return generate_letter_part("Choisis une salutation formelle pour une femme.")
    elif recipient_gender.lower() == "male":
        return generate_letter_part("Choisis une salutation formelle pour un homme.")
    else:
        return "Madame, Monsieur"
      
