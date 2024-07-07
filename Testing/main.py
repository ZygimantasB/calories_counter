from flask import Flask, request, redirect, jsonify  # Import jsonify here
import requests

app = Flask(__name__)

CLIENT_ID = "1689bc17-54e7-4be6-8a1b-f5f3c01f57fb"
CLIENT_SECRET = "secret_mnFu4ObyXoAEVIxHccPXjfR9C74VuJNPf5CRHyAzPbR"
REDIRECT_URI = "https://b9b9-78-61-65-178.ngrok-free.app/callback"
TOKEN_URL = "https://api.notion.com/v1/oauth/token"

@app.route("/")
def home():
    return '<a href="/authorize">Authorize with Notion</a>'

@app.route("/authorize")
def authorize():
    auth_url = f"https://api.notion.com/v1/oauth/authorize?client_id={CLIENT_ID}&response_type=code&owner=user&redirect_uri={REDIRECT_URI}"
    return redirect(auth_url)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if code:
        response = requests.post(
            TOKEN_URL,
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": REDIRECT_URI,
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
            },
        )
        if response.status_code == 200:
            access_token = response.json().get("access_token")
            return jsonify({"access_token": access_token})
        else:
            return "Failed to get access token.", 400
    else:
        return "Authorization code not found in query parameters.", 400


if __name__ == "__main__":
    app.run(port=5000, debug=True, use_reloader=False)


