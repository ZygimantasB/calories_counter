import requests

# NOTION_TOKEN = 'secret_kz94sk3BMwRgKQb8jmK70vxCx2QCXPbxwaj98VYHRWk' # my secret key
NOTION_TOKEN = 'secret_r2kzOJiB2cVxxCIQiAEXUwtePFaoFTRetVJm8ACEhtY' # eric secret key
# DATABASE_ID = '2bc76fbc81c44e58b47cdd6426372483' # my database
DATABASE_ID = 'eb9f18b8412246c58c26ec875572183d' # eric database

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}


def get_pages():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    payload = {"page_size": 100}
    response = requests.post(url, json=payload, headers=headers)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        print("Response:", response.text)
        return []

    data = response.json()
    return data.get('results', [])

pages = get_pages()

for page in pages:
    props = page.get('properties', {})

    project = props.get('Project', {}).get('title', [])[0].get('text', {}).get('content') if props.get('Project', {}).get('title') else None
    task_type = props.get('Type', {}).get('select', {}).get('name') if props.get('Type', {}).get('select') else None
    assigned_members = [user['name'] for user in props.get('Assigned members', {}).get('multi_select', [])] if props.get('Assigned members', {}).get('multi_select') else None
    due_date_start = props.get('Due Date', {}).get('date', {}).get('start') if props.get('Due Date', {}).get('date', {}).get('start') else None
    due_date_end = props.get('Due Date', {}).get('date', {}).get('end') if props.get('Due Date', {}).get('date', {}).get('end') else None
    status = props.get('Status', {}).get('select', {}).get('name') if props.get('Status', {}).get('select') else None
    description = props.get('Description', {}).get('rich_text', [])[0].get('text', {}).get('content') if props.get('Description', {}).get('rich_text') else None
    # Add other fields as needed

    print(f"Project: {project}, Type: {task_type}, Assigned Members: {assigned_members}, Due Date: {due_date_start} to {due_date_end}, Status: {status}, Description: {description}")
