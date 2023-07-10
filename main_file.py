from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import string
import random

app = FastAPI()
url_mapping = {}


class URLItem(BaseModel):
    long_url: str


def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url


@app.post("/shorten")
def shorten_url(item: URLItem):
    long_url = item.long_url
    if long_url is None:
        raise HTTPException(status_code=404, detail="shorten url not found")
    else:
        short_url = generate_short_url()
        url_mapping[short_url] = long_url
        return {"status": status.HTTP_200_OK, "message": "success", "short_url": short_url}


@app.get("/{short_url}")
def redirect_to_url(short_url: str):

    if short_url in url_mapping:
        long_url = url_mapping[short_url]
        return {"status": status.HTTP_200_OK, "message": "success", "redirect_url": long_url}
    else:
        raise HTTPException(status_code=404, detail="URL not found.")
