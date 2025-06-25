import os
import openai
import streamlit as st

# Set your API key securely (use .env or environment variable in production)
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="🛍️ Product Describer AI")
st.title("🛍️ E-commerce Product Describer")
st.markdown("Generate compelling product titles and descriptions for your store.")

# Inputs
product_name = st.text_input("Product Name")
category = st.text_input("Category")
features = st.text_area("Product Features (comma-separated)")
tone = st.selectbox("Writing Tone", ["Professional", "Casual", "Luxurious", "Minimalist", "Playful"])

if st.button("Generate Description"):
    if not all([product_name, category, features, tone]):
        st.warning("Please fill in all fields.")
    else:
        prompt = f"""
You are a product copywriter for an e-commerce brand.

Generate a product title and a professional product description based on the details below.

Product Details:
- Product Name: {product_name}
- Category: {category}
- Features: {features}
- Tone: {tone}

Output Format:
Title: [Generated Product Title]

Description:
[Engaging product description in 3–5 sentences]
        """

        with st.spinner("Generating..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=250,
                )
                result = response.choices[0].message["content"]
                st.success("Generated Content:")
                st.markdown(result)
            except Exception as e:
                st.error(f"❌ Error: {e}")
