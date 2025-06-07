import streamlit as st

# Danh sách tài khoản mẫu (có thể thay thế bằng database thật)
USER_CREDENTIALS = {
    "admin": "123456",
    "user": "password"
}

# Hàm kiểm tra đăng nhập
def check_login(username, password):
    return USER_CREDENTIALS.get(username) == password

# Tiêu đề
st.set_page_config(page_title="Login Page", page_icon="🔐")
st.title("🔐 Đăng Nhập Hệ Thống")

# Nhập thông tin đăng nhập
username = st.text_input("Tên đăng nhập")
password = st.text_input("Mật khẩu", type="password")

# Nút đăng nhập
if st.button("Đăng nhập"):
    if check_login(username, password):
        st.success(f"Chào mừng, **{username}**! Bạn đã đăng nhập thành công ✅.")
        # Có thể chuyển sang giao diện chính bằng session_state hoặc st.experimental_rerun()
    else:
        st.error("Sai tên đăng nhập hoặc mật khẩu ❌")

# Gợi ý
st.markdown("👉 Tài khoản mẫu: `admin / 123456`")
