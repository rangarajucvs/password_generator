import streamlit as st

from password_generator import PASSWORD_LENGTH, generate_password


st.set_page_config(page_title="Password Generator", page_icon="🔐")

st.title("Password Generator")
st.write("Generate a secure, random password")

if st.button("Generate password", type="primary"):
    st.session_state["password"] = generate_password()

password = st.session_state.get("password")
if password:
    st.success(f"Generated password: {password}")
    st.code(password, language=None)
    st.caption(f"{PASSWORD_LENGTH} characters")
else:
    st.info("Select **Generate password** to create a password.")
