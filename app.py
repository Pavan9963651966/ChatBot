import os
from flask import Flask, render_template, request
from vectordb_agent import VectorDBAgent
from web_agent import WebAgent
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# ✅ Provide the required 'url' argument when creating WebAgent
web_agent = WebAgent("https://www.aciesglobal.com/")

# ✅ Initialize VectorDBAgent
vector_agent = VectorDBAgent()

@app.route("/", methods=["GET", "POST"])
def home():
    response = None
    query = ""

    if request.method == "POST":
        query = request.form["query"]
        source = request.form["source"]  # Dropdown: 'vectordb' or 'web'

        if source == "vectordb":
            response = vector_agent.retrieve(query)
        elif source == "web":
            response = web_agent.retrieve_from_web(query)

    return render_template("index.html", query=query, response=response)

if __name__ == "__main__":
    app.run(debug=True)
