
from flask import Flask, request, render_template_string
import markdown

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Markdown File Viewer</title>
    <meta charset="UTF-8">
    <style>
        body {
            margin: 0;
            background: #f4f6f8;
            font-family: Inter, Arial, sans-serif;
            color: #1f2937;
        }

        .upload-box, .container {
            max-width: 900px;
            margin: 40px auto;
            background: white;
            padding: 35px;
            border-radius: 18px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.08);
        }

        h1, h2, h3 {
            color: #111827;
            margin-top: 30px;
        }

        h1 {
            font-size: 2.3rem;
            border-bottom: 2px solid #e5e7eb;
            padding-bottom: 12px;
        }

        p, li {
            line-height: 1.8;
            font-size: 17px;
        }

        code {
            background: #f3f4f6;
            padding: 3px 6px;
            border-radius: 6px;
            color: #dc2626;
        }

        pre {
            background: #111827;
            color: #f9fafb;
            padding: 20px;
            border-radius: 14px;
            overflow-x: auto;
            font-size: 15px;
        }

        pre code {
            background: transparent;
            color: inherit;
            padding: 0;
        }

        blockquote {
            border-left: 5px solid #6366f1;
            background: #eef2ff;
            padding: 15px 20px;
            margin: 25px 0;
            border-radius: 10px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
        }

        th, td {
            border: 1px solid #e5e7eb;
            padding: 12px;
        }

        th {
            background: #f9fafb;
        }

        a {
            color: #2563eb;
            text-decoration: none;
            font-weight: 600;
        }

        input[type="file"] {
            width: 100%;
            padding: 14px;
            border: 2px dashed #c7d2fe;
            border-radius: 12px;
            background: #eef2ff;
        }

        button {
            margin-top: 18px;
            background: #4f46e5;
            color: white;
            border: none;
            padding: 12px 22px;
            border-radius: 10px;
            font-size: 16px;
            cursor: pointer;
        }

        button:hover {
            background: #4338ca;
        }

        .filename {
            color: #6b7280;
            margin-top: 10px;
        }
    </style>
</head>
<body>

<div class="upload-box">
    <h1>Markdown File Viewer</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="markdown_file" accept=".md,.markdown,.txt" required>
        <button type="submit">Upload & Render</button>
    </form>

    {% if filename %}
        <p class="filename">Rendered file: {{ filename }}</p>
    {% endif %}
</div>

{% if rendered_html %}
<div class="container">
    {{ rendered_html|safe }}
</div>
{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    rendered_html = ""
    filename = ""

    if request.method == "POST":
        file = request.files.get("markdown_file")

        if file and file.filename:
            filename = file.filename
            markdown_text = file.read().decode("utf-8", errors="ignore")

            rendered_html = markdown.markdown(
                markdown_text,
                extensions=[
                    "fenced_code",
                    "tables",
                    "toc",
                    "sane_lists",
                    "nl2br"
                ]
            )

    return render_template_string(
        HTML_TEMPLATE,
        rendered_html=rendered_html,
        filename=filename
    )

if __name__ == "__main__":
    app.run(debug=True)