import streamlit as st

st.set_page_config(page_title="Akshu Calculator", page_icon="🧮")

st.markdown("# 🧮 Akshu Calculator")
st.markdown("---")

num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

operator = st.selectbox(
    "Choose an operator",
    ["1. Addition ➕", "2. Subtraction ➖", "3. Multiplication ✖️", "4. Division ➗"]
)

if st.button("Calculate 🚀"):
    if operator.startswith("1"):
        result = num1 + num2
        symbol = "+"
    elif operator.startswith("2"):
        result = num1 - num2
        symbol = "-"
    elif operator.startswith("3"):
        result = num1 * num2
        symbol = "*"
    elif operator.startswith("4"):
        if num2 == 0:
            st.error("❌ Error: Division by zero is not allowed!")
            st.stop()
        else:
            result = num1 / num2
            symbol = "/"

    st.success(f"✅ {num1} {symbol} {num2} = {result:.2f}")
    st.balloons()
    

