import streamlit as st

quine_code = '''\
code = %r
'''

def main():
    st.title("Python Code Display")
    # Text input for the user to enter Python code
    user_code = st.text_area("Enter your Python code here:")
    # Button to submit the code
    if st.button("Display Code"):
        # Display the user's code
        st.code(user_code, language="python")
        # Hide the inline version
        # quine_output = quine_code % user_code
        # st.code(quine_output, language="python")

if __name__ == "__main__":
    main()