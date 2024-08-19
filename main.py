
# import g4f
# import streamlit as st

# st.title('ChatBot (Helping-Center)')

# input = st.text_area('سوالی دارید مطرح کنید')

# submit = st.button('Lets Go')

# if input != "" and submit:

#     response = g4f.ChatCompletion.create(
#         model = "gpt-3.5-turbo",
#         messages=[{"role": "user", "content": input}],
#         stream = True
#     )

# for message in response:
  
#     st.write(message)





import g4f
# from g4f import ChatCompletion
import streamlit as st


# وارد کردن فایل CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
# وارد کردن فایل جاوااسکریپت
with open("script.js") as f:
    js_code = f.read()

# افزودن جاوااسکریپت به صفحه
st.markdown(f"<script>{js_code}</script>", unsafe_allow_html=True)


st.title('ChatBot | ربات سرسیل (Helping-Center)')

input = st.text_area('سوالی دارید مطرح کنید')

ok = st.button('Submit Query...')

if input != "" and ok:


    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": input}],
        # provider=g4f.Provider.HuggingChat,
        cookies={"hf-chat": "c660d747-a914-4b65-9e33-83640e364f4b"},
        stream= True
    )

    for message in response:
        st.write(message)
        
