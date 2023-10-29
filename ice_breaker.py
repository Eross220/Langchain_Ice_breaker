from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile


if __name__ == '__main__':
    print("Hello Langchain!!")

    linkedin_profile_url = linkedin_lookup_agent(name="Alexius xie")
    summmary_template= """
        given the Linkedin information {information} about a person from I want you to create:
        1.a short summary
        2.two interesting facts about them
    """


    summmary_prompt= PromptTemplate(input_variables=["information"], template=summmary_template )

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summmary_prompt)

    

    linkedin_data= scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
    
    respons_llm=chain.run(information=linkedin_data)

    print(respons_llm)