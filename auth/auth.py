
import streamlit as st
from db.mongo_conn import users_collection
import bcrypt

# Create a new user
def signup(username, email, password):
    if users_collection.find_one({"username": username}):
        return False, "❌ Username already exists."

    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user = {"username": username, "email": email, "password": hashed_pw}
    users_collection.insert_one(user)
    return True, "✅ Account created! You can log in now."

# Log in an existing user
def login(username, password):
    user = users_collection.find_one({"username": username})
    if not user:
        return False, "❌ Username not found."

    if bcrypt.checkpw(password.encode(), user["password"]):
        return True, f"✅ Welcome back, {username}!"
    else:
        return False, "❌ Incorrect password."

# Streamlit login/signup form
def auth_ui():
    if "auth_mode" not in st.session_state:
        st.session_state["auth_mode"] = "Login"

    if st.session_state["auth_mode"] == "Login":
        st.title("🔐 Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            success, msg = login(username, password)
            st.info(msg)
            if success:
                st.session_state["user"] = username
                st.rerun()
        st.button("Don't have an account? Sign Up", on_click=lambda: st.session_state.update({"auth_mode": "SignUp"}))

    elif st.session_state["auth_mode"] == "SignUp":
        st.title("📝 Sign Up")
        username = st.text_input("Choose a username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Create Account"):
            success, msg = signup(username, email, password)
            st.info(msg)
            if success:
                st.session_state["auth_mode"] = "Login"
        st.button("Already have an account? Login", on_click=lambda: st.session_state.update({"auth_mode": "Login"}))

# Check if logged in
def is_logged_in():
    return "user" in st.session_state

# Logout
def logout_button():
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()
