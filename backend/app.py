from fastapi import FastAPI
from pydantic import BaseModel
from URLChecker import  find_text_from_URL, extract_text_from_URL
import json

app = FastAPI()


# query parameter
# https://fastapi.tiangolo.com/tutorial/query-params/
@app.get("/extract_text/")
# /extract_text/?URL=http://google.com
def extract_text(URL: str):
    print(URL)
    text = extract_text_from_URL(URL)
    return {"extracted_text": text}

#  request body
# https://fastapi.tiangolo.com/tutorial/body/
class SiteInfo(BaseModel):
    URL: str = "http://google.com"
    text_to_find: str = '404'
    phone_number: str


@app.post("/add_site")
def add_site(site_info:SiteInfo):
    # return site_info.URL
    return {"added site": site_info.URL}


@app.post("/remove_site")
def remote_site(site_info:SiteInfo):
    # return site_info.URL
    return {"remove site": site_info.URL}