import streamlit as st
from agent import create_agent
from executor import try_execute

st.set_page_config(page_title="Coding Copilot", page_icon="💻")
st.title("🧠 Coding Copilot")

if "agent" not in st.session_state:
    st.session_state.agent = create_agent()

user_input = st.text_area("Ask me to code something or type 'execute:' to run code:")

if st.button("Submit"):
    if user_input:
        if user_input.startswith("execute:"):
            code = user_input[len("execute:"):].strip()
            with st.spinner("Executing code..."):
                output = try_execute(code)
            st.code(output)
        else:
            with st.spinner("Thinking..."):
                response = st.session_state.agent.run(user_input)
            st.write(f"**Copilot:** {response}")
