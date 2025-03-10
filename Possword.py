import streamlit as st
import re

def check_password_strength(password: str):
    # Define password strength rules
    length = len(password)
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    # Calculate score (out of 5)
    score = sum([length >= 8, has_upper, has_lower, has_digit, has_special])
    
    return score

def get_strength_label(score):
    labels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    colors = ["#FF4B4B", "#FF8040", "#FFD700", "#90EE90", "#008000"]
    return labels[score - 1], colors[score - 1]

def main():
    st.title(" Password Strength Meter")
    st.write("Enter a password to check its strength.")
    
    password = st.text_input("Enter Password", type="password")
    
    if password:
        score = check_password_strength(password)
        strength_label, color = get_strength_label(score)
        
        st.markdown(f"<h3 style='color: {color};'>{strength_label}</h3>", unsafe_allow_html=True)
        st.progress(score / 5)  # Progress bar (0 to 1 scale)
        
        st.subheader("Suggestions to Improve Password:")
        if score < 5:
            if len(password) < 8:
                st.write("- Use at least 8 characters.")
            if not re.search(r"[A-Z]", password):
                st.write("- Include at least one uppercase letter.")
            if not re.search(r"[a-z]", password):
                st.write("- Include at least one lowercase letter.")
            if not re.search(r"\d", password):
                st.write("- Include at least one number.")
            if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
                st.write("- Include at least one special character (!@#$%^&* etc.).")

if __name__ == "__main__":
    main()
