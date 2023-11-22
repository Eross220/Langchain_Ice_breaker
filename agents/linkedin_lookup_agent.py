from tools.tools import get_profile_url
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.agents import initialize_agent , Tool 
from langchain.agents import AgentType

def lookup(name: str) -> str:
    llm=ChatOpenAI(temperature=0,model="gpt-3.5-turbo")
    template= """
    given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
                          Your answer should contain only a URL
    """
    
    tools_for_agents=[
        Tool(
            name="Crawl Google for linkedin profile page",
            func=get_profile_url,
            description="useful for when you need get the linkedin Page URL",
            )
    ]

    agent= initialize_agent(
        tools=tools_for_agents,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    prompt_template= PromptTemplate(
        template=template,
        input_variables=['name_of_person']
    )


    linked_profile_url= agent.run(prompt_template.format_prompt(name_of_person=name))
        
    return linked_profile_url