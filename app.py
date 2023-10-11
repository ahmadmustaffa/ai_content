import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Create a Streamlit app title
st.title('AI Blog Generator')

openai_api_key = st.sidebar.text_input('Enter you OpenAI API key', type= 'password')
# openai_api_key = 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

# Create a textarea widget for user input
prompt = st.text_area('Enter the title of your blog')

# Create a button widget to trigger content generation
if st.button('Generate'):
    if prompt:
        # Initialize AI models and templates
        prompt_template = PromptTemplate.from_template(f"Generate a blog on title {prompt}?")
        llm = OpenAI(temperature=0.3, openai_api_key= openai_api_key)
        chain = LLMChain(llm=llm, prompt=prompt_template)

        # Generate content
        output = chain.run({"prompt": prompt})

        # Display the generated content
        st.markdown(output)
    else:
        st.warning('Please enter a title for your blog.')




# Add navigation links if needed (similar to your HTML navigation)
# You can use st.write or st.markdown to display navigation links

# Example:
# st.markdown('### Navigation Links')
# st.write('[Home](#)')
# st.write('[About](#)')
# st.write('[Services](#)')
# st.write('[Contact](#)')
