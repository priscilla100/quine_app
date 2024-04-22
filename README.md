# quine_app
What is a quine program?
This is the core of the quine behavior, which is a program that prints its own source code.

This application is implemented in Python with Streamlit app used for deployment.

Streamlit app allows the user to enter Python code.
The "Display code" button when clicked, performs the following actions:
1. Displays the user's code in a code block using `st.code(user_code, language="python")`.
2. Creates a new string quine_output by replacing `%r` in quine_code with the user_code string, effectively creating a quine code snippet with the user's code embedded in it.
3. Displays the quine_output string in a code block using `st.code(quine_output, language="python")`.


A multi-line string variable called `quine_code`. This string represents a Python code snippet that takes a string representation of itself `(%r)` and prints it using string formatting `(print(code %% code))`. 



In summary, this program essentially prints out its own source code by embedding the code within a string and then printing that string, formatted with itself.


