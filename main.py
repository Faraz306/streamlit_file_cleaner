import streamlit as st
import time


def make_page(title, text):
    st.title(title)
    st.markdown(text, unsafe_allow_html=True)
    st.write("Enter the file.")
def read_file():
    if 'clicked' not in st.session_state:
        st.session_state['clicked'] = False
    uploaded = st.file_uploader("Choose a file")
    if uploaded:
        with st.spinner('Loading file...'):
            time.sleep(5)
        content = uploaded.getvalue().decode("utf-8")

        # 2. Display content (as a string or list)

        # 3. If you want it in a table format without pandas:
        rows = [line.split(',') for line in content.split('\n') if line]
        st.table(rows)
        if st.button("Click here to remove thing from all columns."):
            st.session_state['clicked'] = True

            # REPAIR: Check the session state, NOT the button variable b1
        if st.session_state['clicked']:
            i1 = st.text_input("Which thing to remove?")
            if i1:
                if st.button(f"Remove {i1}"):
                    new_rows = []
                    for row in rows:
                        # This keeps the column count the same, but blanks out the match
                        new_row = [cell.replace(i1, "") for cell in row]
                        new_rows.append(new_row)
                    st.table(new_rows)
make_page("My pandas!", text="My pandas!")
read_file()