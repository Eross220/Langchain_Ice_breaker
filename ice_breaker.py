from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile
from outputpaser import person_inetel_parser

def ice_breaker(name:str)-> str:
    print("Hello Langchain!!")

    linkedin_profile_url = linkedin_lookup_agent(name=name)

    linkedin_data= scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    summmary_template= """
        given the Linkedin information {information} about a person from I want you to create:
        1.a short summary
        2.two interesting facts about them
        \n\ {format_instruction}
    """


    summmary_prompt= PromptTemplate(input_variables=["information"], template=summmary_template, partial_variables={"format_instruction":person_inetel_parser.get_format_instructions()} )

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summmary_prompt)


    
    respons_llm=chain.run(information=linkedin_data)

    return respons_llm

if __name__ == '__main__':
    result=ice_breaker("Alexius xie")

    print(result)