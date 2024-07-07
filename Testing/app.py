from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("<h1>Welcome to Our Integration</h1><p>This is a placeholder for our integration's main webpage.</p>")

@app.route("/privacy-policy")
def privacy_policy():
    return render_template_string("<h1>Privacy Policy</h1><p>This is a placeholder for our privacy policy.</p>")

@app.route("/terms-of-use")
def terms_of_use():
    return render_template_string("<h1>Terms of Use</h1><p>This is a placeholder for our terms of use.</p>")

@app.route("/support")
def support():
    return render_template_string("<h1>Support</h1><p>For support, please email us at <a href='mailto:support@yourcompany.com'>support@yourcompany.com</a>.</p>")

if __name__ == "__main__":
    app.run(debug=True)
