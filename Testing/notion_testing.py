import requests
from datetime import datetime
import json

NOTION_TOKEN = 'secret_kz94sk3BMwRgKQb8jmK70vxCx2QCXPbxwaj98VYHRWk'
DATABASE_ID = '869762209a8c44b4a2e69e1766384cdf'

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}



def get_pages():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    payload = {"page_size": 100}
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    # Print the structure of the response to understand how to access the properties
    print(json.dumps(data, indent=4))

    results = data.get('results', [])
    return results

pages = get_pages()

for page in pages:
    page_id = page.get('id')
    props = page.get('properties', {})

    url = None
    if 'URL' in props and props['URL']['title']:
        url = props['URL']['title'][0]['text']['content']

    title = None
    if 'Title' in props and props['Title']['multi_select']:
        title = props['Title']['multi_select'][0]['name']

    published = None
    if 'Published' in props and props['Published']['rich_text']:
        published = props['Published']['rich_text'][0]['text']['content']

    print(url, title, published)


