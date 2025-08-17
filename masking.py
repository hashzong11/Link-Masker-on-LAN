from flask import Flask, redirect, request, render_template_string

app = Flask(__name__)

# Dictionary for masked links
masked_links = {
    "offer": "https://example.com/real-offer",
    "yt": "https://youtube.com",
    "gh": "https://github.com",
}

# Homepage
@app.route("/")
def home():
    return """
    <h2>Custom Link Masking Service</h2>
    <p>Try visiting: /go/yt , /go/gh , /go/offer</p>
    """

# Redirect route
@app.route("/go/<alias>")
def mask(alias):
    if alias in masked_links:
        return redirect(masked_links[alias])
    else:
        return f"<h3>No masked link found for alias: {alias}</h3>", 404

if __name__ == "__main__":
    app.run(debug=True)
