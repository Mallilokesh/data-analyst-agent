import streamlit as st

USERS = {
    "admin": {"password": "admin123", "name": "Admin User", "role": "admin"},
    "user":  {"password": "user123",  "name": "Demo User",  "role": "user"},
}

class Authenticator:
    def login(self, title, location):
        if "auth_status" not in st.session_state:
            st.session_state.auth_status = None
            st.session_state.auth_name = None
            st.session_state.auth_username = None

        if st.session_state.auth_status:
            return st.session_state.auth_name, True, st.session_state.auth_username

        st.title(f"🔐 {title}")

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("### Welcome to Data Analyst AI Agent")

            with st.expander("👀 Demo credentials"):
                st.code("Admin → username: admin | password: admin123")
                st.code("User  → username: user  | password: user123")

            username = st.text_input("Username", placeholder="admin or user")
            password = st.text_input("Password", type="password", placeholder="••••••••")

            if st.button("Sign in →", use_container_width=True, type="primary"):
                if username in USERS and USERS[username]["password"] == password:
                    st.session_state.auth_status = True
                    st.session_state.auth_name = USERS[username]["name"]
                    st.session_state.auth_username = username
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password")

        return st.session_state.auth_name, st.session_state.auth_status, st.session_state.auth_username

    def logout(self, label, location):
        if st.sidebar.button(label):
            st.session_state.auth_status = None
            st.session_state.auth_name = None
            st.session_state.auth_username = None
            st.rerun()

authenticator = Authenticator()
