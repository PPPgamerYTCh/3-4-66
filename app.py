import streamlit as st
import time
# Set page title in the middle
st.markdown('<h1 style="text-align: center; font-size: 72px;"> 3 April 2023 </h1>', unsafe_allow_html=True)
# Add a button to start the celebration
if st.button("Start Celebration", use_container_width=True):
    # Define HTML code for image positioning
    st.markdown('<h2 style="text-align: center; font-size: 48px;">Happy Birthday! 🎉🎂🎈</h2>', unsafe_allow_html=True)
    st.markdown(
        """
        <div style="display:flex; justify-content:center; align-items:center;">
            <div style="flex: 1;">
                <img src="https://drive.google.com/uc?id=1w5KzlpYQdeQxWG2SrWYe1CT9kazdKJEx" style="width:100%; height:auto;">
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    time.sleep(2)
    # Define HTML code for text positioning
    st.markdown('<h2 style="text-align: center; font-size: 36px; margin-top: 50px;">สุขสันต์วันเกิดนะเว้ยไอ่เขตเพื่อน</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 24px;">ตอนที่ได้ทำโครงงานกับมึงกูสนุกมากเลย หวังว่าเราจะได้ร่วมงานกันอีกเรื่อย ๆ เลยนะ ยังไงมึงก็เทพอยู่แล้ว ต้องมีมึงแบกพวกเราถึงจะเทพสุด ๆ ไปด้วยกัน ยังไงก็....<br>วันเกิดมึงปีนี้ ก็ขอให้มีความสุขนะ การเรียนก็ขอให้ดีขึ้นเรื่อย ๆ เป็นที่รักของทุก ๆ คน สุขภาพแข็งแรงนะเว้ยย</p>', unsafe_allow_html=True)


