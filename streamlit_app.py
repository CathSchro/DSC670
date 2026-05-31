import streamlit as st
from generate_recipe import generate_recipe
import json

st.set_page_config(page_title="Cook With Caitie", page_icon="🍳", layout="centered")

# --- HEADER ---
st.title("🍳 Cook With Caitie")
st.markdown(
    "Welcome! Enter your available ingredients and any allergens to avoid, "
    "and I’ll generate a safe, delicious recipe just for you."
)

# --- INPUTS ---
st.subheader("📝 Ingredients & Allergens")

ingredients = st.text_area(
    "Available ingredients (comma-separated)",
    placeholder="chicken, garlic, lemon, olive oil"
)

allergens = st.text_input(
    "Allergens to avoid (comma-separated)",
    placeholder="dairy, nuts, gluten"
)

generate = st.button("Generate Recipe")

# --- OUTPUT ---
if generate:
    if not ingredients.strip():
        st.error("Please enter at least one ingredient.")
    else:
        with st.spinner("Cooking up something delicious…"):
            ingredients_list = [i.strip() for i in ingredients.split(",") if i.strip()]
            allergens_list = [a.strip() for a in allergens.split(",") if a.strip()]

            raw_output = generate_recipe(ingredients_list, allergens_list)

        st.subheader("📦 Raw Model Output (JSON)")
        st.code(raw_output, language="json")

        # Try to pretty‑format the JSON
        try:
            recipe = json.loads(raw_output)

            st.subheader("🍽️ Recipe Title")
            st.markdown(f"### {recipe.get('title', 'Untitled Recipe')}")

            st.subheader("🧾 Description")
            st.write(recipe.get("description", ""))

            st.subheader("🥕 Ingredients")
            for item in recipe.get("ingredients", []):
                st.write(f"- {item}")

            st.subheader("👩‍🍳 Steps")
            for i, step in enumerate(recipe.get("steps", []), start=1):
                st.write(f"**Step {i}:** {step}")

            st.subheader("🛡️ Allergy Safe For")
            safe_list = recipe.get("allergy_safe_for", [])
            if safe_list:
                st.success(", ".join(safe_list))
            else:
                st.info("No allergens detected or none were avoided.")

        except Exception:
            st.error("The model returned invalid JSON. Check the raw output above.")
