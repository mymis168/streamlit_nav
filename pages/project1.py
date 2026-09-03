import streamlit as st
import time


st.page_link("pages/myproject.py", label="返回專案首頁", icon="⬆")

if st.button("返回專案首頁2"):
    st.switch_page("pages/myproject.py")




    st.experimental_set_query_params(page="pages/myproject.py")
st.title("股票財經分析專題")
st.divider()

st.subheader("三秒後返回 專案主要畫面")

st.write("三秒後呼叫 st.switch_page() 方法 , 會依照使用者選擇的頁面 , 執行對應的程式碼")
st.code("""
time.sleep(3)
st.switch_page("pages/myproject.py")
""")
#

time.sleep(8)
st.switch_page("pages/myproject.py")




