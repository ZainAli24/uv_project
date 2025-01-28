from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

import os
from uv_project.api_key import GEMINI_API_KEY

os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

def langchain():
    model = ChatGoogleGenerativeAI (
    model="gemini-1.5-flash",
    temperature=0.9,
    )
    response = model.invoke("Which specific Mercedes model is considered one of the best?")
    print(response.content)


def langchain2():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-exp",
        temperature=0.9,
    )

    template = PromptTemplate(
        input_variables=["history", "query"],
        template="""Previous history:\n\n{history}\n
        You are a customer support agent specializing in the web development field.
        Please respond to the following query in a polite and professional manner:
        {query}
        If the query is unrelated to web development, politely inform the user that you are here to assist only with web development-related questions.
        """
    )
    chain = LLMChain(
    llm=llm,
    prompt=template,
    )
    response = chain.invoke({"history": "", "query": "Which specific Mercedes model is considered one of the best?"})
    print(response['text'])
    
