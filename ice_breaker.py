from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os

information = """
Bruce Frederick Joseph Springsteen (born September 23, 1949) is an American rock singer, songwriter, and guitarist. Nicknamed "the Boss", Springsteen has released 21 studio albums spanning six decades; most of his albums feature the E Street Band, his backing band since 1972. Springsteen is a pioneer of heartland rock, combining commercially successful rock with poetic, socially conscious lyrics that reflect working class American life. He is known for his energetic concerts, some of which last more than four hours.
"""

if __name__ == "__main__":
    load_dotenv()
    print("Hello Langchain!!")

    try:
        print(os.environ["OPENAI_API_KEY"])
    except KeyError as e:
        print(f"Error: Missing environment variable {e}")

    summary_template = """
        Given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    chain = summary_prompt_template | llm

    result = chain.invoke({"information": information})
    print(result)
