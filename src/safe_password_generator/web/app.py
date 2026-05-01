import streamlit as st
import os
from safe_password_generator.core.generator import generate_password
from safe_password_generator.core.exceptions import PasswordGeneratorError

# Page configuration for a professional look
st.set_page_config(
    page_title="Safe Password Generator",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def load_css():
    """Load custom CSS from the assets folder."""
    css_file = os.path.join(os.path.dirname(__file__), "assets", "style.css")
    try:
        with open(css_file, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except Exception as e:
        st.warning(f"Could not load custom CSS: {e}")

def main():
    load_css()

    # Header section
    st.markdown('<h1 class="title-text">Safe Password Generator</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-text">Generate secure, cryptographically strong passwords locally.</p>', unsafe_allow_html=True)

    # Initialize session state for password if not exists
    if "password" not in st.session_state:
        st.session_state.password = ""

    # UI Components in a clean layout
    with st.container():
        st.subheader("Configuration")
        
        # Length Slider
        length = st.slider("Password Length", min_value=4, max_value=128, value=16, step=1)
        
        # Checkboxes for criteria in columns
        col1, col2 = st.columns(2)
        with col1:
            use_upper = st.checkbox("Uppercase Letters (A-Z)", value=True)
            use_lower = st.checkbox("Lowercase Letters (a-z)", value=True)
        with col2:
            use_numbers = st.checkbox("Numbers (0-9)", value=True)
            use_specials = st.checkbox("Special Characters (!@#...)", value=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Generate Button
        if st.button("Generate Password", use_container_width=True):
            try:
                pwd = generate_password(
                    length=length,
                    use_upper=use_upper,
                    use_lower=use_lower,
                    use_numbers=use_numbers,
                    use_specials=use_specials
                )
                st.session_state.password = pwd
            except PasswordGeneratorError as e:
                st.markdown(f'<div class="error-msg">{str(e)}</div>', unsafe_allow_html=True)
                st.session_state.password = ""

    # Password Display Section
    if st.session_state.password:
        st.markdown(f'<div class="password-box">{st.session_state.password}</div>', unsafe_allow_html=True)
        
        # Optional: A simple button to copy to clipboard (Note: Streamlit doesn't have native clipboard API without JS hacks,
        # but displaying it in a code block also provides a copy button natively in Streamlit >= 1.0)
        st.code(st.session_state.password, language="text")

if __name__ == "__main__":
    main()
