import os
from flask import Flask, render_template, request, jsonify
from tools.ollama_tool import OllamaTool

app = Flask(__name__)

# Configuration
TEMPLATE_PATH = os.path.join("architecture", "templates", "testcase_template.md")
tool = OllamaTool(model="llama3.2")

def get_template():
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r") as f:
            return f.read()
    return "Please generate test cases for: {{user_input}}"

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.json
    user_input = data.get("user_input", "")
    
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    # Layer 2: Reasoning/Navigation
    # 1. Prepare Data
    template = get_template()
    full_prompt = template.replace("{{user_input}}", user_input)

    # 2. Call Layer 3 Tool
    generated_text, error = tool.generate(full_prompt)

    if error:
        # Simple error handling logic
        status_code = 503 if "connect" in error.lower() else 500
        return jsonify({"error": error}), status_code

    return jsonify({
        "generated_testcases": generated_text,
        "status": "success"
    })

if __name__ == "__main__":
    print(f"Starting Local Test Case Generator on http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
