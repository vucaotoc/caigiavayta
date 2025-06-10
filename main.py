import streamlit as st

st.set_page_config(page_title="Trang HTML + CSS", layout="centered")
st.title("🌐 Demo HTML + CSS trong Streamlit")

# HTML + CSS nội tuyến
html_code = """
<div style="background-color:#f0f0f0;padding:20px;border-radius:10px;text-align:center;">
    <h2 style="color:#2c3e50;">Xin chào!</h2>
    <p style="font-size:18px;">Đây là nội dung <b>HTML</b> có CSS tùy chỉnh.</p>
    <button style="background-color:red;color:white;border:none;padding:10px 20px;border-radius:5px;">Nhấn vào đây</button>
</div>
"""

st.markdown(html_code, unsafe_allow_html=True)
