import requests
import os
from dotenv import load_dotenv
load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape linkedin information from the linkedin Profile"""

    api_endpoint ="https://nubela.co/proxycurl/api/v2/linkedin"
    PROXYURL_API_KEY= os.getenv('PROXYCURL_APIPKEY')
   
    header_dic={"Authorization": f'Bearer {PROXYURL_API_KEY}'}
    
    print(linkedin_profile_url)
    response = requests.get(api_endpoint, params={"linkedin_profile_url": linkedin_profile_url}, headers=header_dic)
    data=response.json()
    
    #Filter redundant fileds which are empty...

    data ={
        k:v
        for k, v in data.items()
        if v not in ([],"","", None)
            and k not in ("people_also_viewed","certifications")
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    
    return data