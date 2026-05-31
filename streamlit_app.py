import streamlit as st
from generate_recipe import generate_recipe

st.set_page_config(page_title="Cook With Caitie", page_icon="🍳")

st.title("🍳 Cook With Caitie")
st.write("Enter your available ingredients and allergens to generate a safe recipe.")

ingredients = st.text_area(
    "Available ingredients (comma-separated)",
    placeholder="chicken, garlic, lemon"
)

allergens = st.text_input(
    "Allergens to avoid (comma-separated)",
    placeholder="dairy, nuts"
)

if st.button("Generate Recipe"):
    if not ingredients.strip():
        st.error("Please enter at least one ingredient.")
    else:
        with st.spinner("Cooking up something delicious…"):
            ingredients_list = [i.strip() for i in ingredients.split(",") if i.strip()]
            allergens_list = [a.strip() for a in allergens.split(",") if a.strip()]

            recipe_json = generate_recipe(ingredients_list, allergens_list)

        st.subheader("Generated Recipe")
        st.code(recipe_json, language="json")
