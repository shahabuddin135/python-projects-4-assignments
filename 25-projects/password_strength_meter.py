import streamlit as st
import string
import math

def evaluate_strength(password):
    # Initialize criteria checks
    length = len(password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    
    # Calculate entropy (complexity)
    char_pool = 0
    if has_upper: char_pool += len(string.ascii_uppercase)
    if has_lower: char_pool += len(string.ascii_lowercase)
    if has_digit: char_pool += len(string.digits)
    if has_symbol: char_pool += len(string.punctuation)
    
    entropy = length * math.log2(char_pool) if char_pool > 0 else 0
    
    # Strength rating logic
    strength = "Weak 🔴"
    if entropy >= 60: strength = "Very Strong 🔵"
    elif entropy >= 40: strength = "Strong 🟢"
    elif entropy >= 20: strength = "Medium 🟡"
    
    return {
        "strength": strength,
        "entropy": f"{entropy:.1f} bits",
        "length": length,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_symbol": has_symbol
    }

# Streamlit UI
st.title("🔑 Password Strength Meter")
password = st.text_input("Enter a password to evaluate:", type="password")

if password:
    report = evaluate_strength(password)
    
    # Strength indicator with color bar
    strength_color = {
        "Weak 🔴": "#FF0000", 
        "Medium 🟡": "#FFD700", 
        "Strong 🟢": "#00FF00", 
        "Very Strong 🔵": "#0066CC"
    }
    st.markdown(f"""
    <div style='height: 10px; background-color: {strength_color[report["strength"]]}; 
                border-radius: 5px; margin: 10px 0;'>
    </div>
    """, unsafe_allow_html=True)
    
    # Metrics
    st.subheader("Security Report")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Strength Rating", report["strength"])
    with col2:
        st.metric("Entropy (Complexity)", report["entropy"])
    with col3:
        st.metric("Length", report["length"])
    
    # Criteria checklist
    st.subheader("Criteria Check")
    st.write(f"✅ Uppercase Letters: {report['has_upper']}")
    st.write(f"✅ Lowercase Letters: {report['has_lower']}")
    st.write(f"✅ Numbers: {report['has_digit']}")
    st.write(f"✅ Symbols: {report['has_symbol']}")
    
    # Feedback messages
    if report["length"] < 8:
        st.error("⚠️ Password is too short! Use at least 8 characters.")
    if not report["has_symbol"]:
        st.warning("🔧 Tip: Add symbols (!, @, #) to improve strength.")