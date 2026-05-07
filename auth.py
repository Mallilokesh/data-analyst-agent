import streamlit_authenticator as stauth

names = ["Admin User", "Normal User"]
usernames = ["admin", "user"]

passwords = ["admin123", "user123"]

hashed_passwords = stauth.Hasher(passwords).generate()

credentials = {
    "usernames": {
        usernames[0]: {
            "name": names[0],
            "password": hashed_passwords[0]
        },
        usernames[1]: {
            "name": names[1],
            "password": hashed_passwords[1]
        }
    }
}

authenticator = stauth.Authenticate(
    credentials,
    "data_analyst_cookie",
    "abcdef",
    cookie_expiry_days=1
)