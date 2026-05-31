import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_recipe(ingredients, allergens):
    """
    Generate an allergy-safe recipe using the provided ingredients.
    Returns a JSON string with title, description, ingredients, steps, and allergy info.
    """

    prompt = f"""
You are a dietician and chef. Using ONLY the provided ingredients, create a recipe that includes a full ingredient list and instructions.

Allowed ingredients: {", ".join(ingredients)}

Avoid ALL of these allergens or restricted ingredients:
{", ".join(allergens)}

Rules:
- You may add additional ingredients as long as they are NOT allergens.
- Do NOT include any ingredient that is an allergen or contains an allergen.
- If a recipe requires an allergen, suggest a safe alternative.
- Output must be valid JSON with this structure:

{{
  "title": "",
  "description": "",
  "ingredients": ["item 1", "item 2"],
  "steps": ["step 1", "step 2", "step 3"],
  "allergy_safe_for": ["list of allergens avoided"]
}}
"""

    response = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:personal:allergen-recipe-model:De9dV0Vl",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content
