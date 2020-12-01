#https://www.youtube.com/watch?v=rXH4nVoecBE
#https://pypi.org/project/pyotp/

import pyotp
import streamlit as st
import time
import random
from random import randint
from datetime import datetime

#READ THIS
#https://github.com/andfanilo/streamlit-lyondatascience-20200422


#random.seed(datetime.now())

st.title("Streamlit OTP generation APP - by Anirban Banerjee")
st.write("My first attempt to publish my APP on https://share.streamlit.io/")

#UserID = str(randint(500,999))
UserName = st.empty()
UserNameInput = st.text_input("Please Enter the Username")

if st.button('Submit'):
    UserName.text(f'UserName : {UserNameInput}')



#st.write('UserID: %s' % UserID )
#UserID = "Anir"
Timer = 30

totp = pyotp.TOTP(UserNameInput)
StartTimer = False

if st.button('Generate OTP'):
    st.write('OTP: %s' % totp.now())
    StartTimer = True

Timeleft = st.empty()
my_bar = st.progress(0)

userinput = st.text_input("Please Enter the OTP")
if st.button('Submit OTP'):
    StartTimer = False
    if totp.verify(userinput):
        st.balloons()
        st.success('Successfully Verified OTP')
    else:
        st.error('Failed to Verify OTP')

i_timeleft = Timer
if StartTimer:
    for percent_complete in range(Timer):
        my_bar.progress(percent_complete)
        i_timeleft = i_timeleft-1
        Timeleft.text(f'TimeLeft : {i_timeleft}')
        time.sleep(1)
    if i_timeleft == 0:
        st.button('Re run Generate OTP')
else:
    Timeleft.text(f'TimeLeft : {i_timeleft}')
