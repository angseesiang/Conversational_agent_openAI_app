from flask import Flask, request, render_template_string, send_file
from .agent import ConversationalAgent

app = Flask(__name__)
agent = ConversationalAgent()  # create on the fly; no joblib required

INDEX_HTML = """
<!doctype html>
<html>
  <head><meta charset="utf-8"><title>Conversational Agent</title></head>
  <body style="font-family: Arial; max-width: 720px; margin: 40px auto;">
    <h1>Conversational Agent</h1>
    <form method="post" action="/generate">
      <input type="text" name="user_input" placeholder="Say something…" style="width: 100%; padding: 8px;" />
      <button type="submit" style="margin-top: 10px;">Send</button>
    </form>
    {% if user_input is defined %}
      <h3>You:</h3>
      <pre>{{ user_input }}</pre>
      <h3>Agent:</h3>
      <pre>{{ response }}</pre>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(INDEX_HTML)

@app.route("/generate", methods=["POST"])
def generate():
    user_input = request.form.get("user_input", "")
    response = agent.generate_response(user_input)
    return render_template_string(INDEX_HTML, user_input=user_input, response=response)

@app.route("/download")
def download():
    # Placeholder demo file
    path = "placeholder.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write("Hello from your agent.")
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    # You will run it as a module (see next step)
    app.run(debug=True)

