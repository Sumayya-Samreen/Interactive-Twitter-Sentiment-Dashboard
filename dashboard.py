import os
from jinja2 import Template

def generate_dashboard(all_results, summaries):
    os.makedirs("outputs", exist_ok=True)
    html_path = os.path.join("outputs", "dashboard.html")

    template_str = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Twitter Sentiment Dashboard</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { color: #333; }
            h2 { color: #555; }
            .keyword-section { margin-bottom: 50px; }
            img { max-width: 100%; height: auto; }
            pre { background: #f4f4f4; padding: 10px; }
        </style>
    </head>
    <body>
        <h1>Interactive Twitter Sentiment Dashboard</h1>
        {% for keyword, sentiments in all_results.items() %}
        <div class="keyword-section">
            <h2>{{ keyword }}</h2>
            <h3>Sentiment Plot</h3>
            <img src="{{ keyword }}_sentiment_plot.png" alt="Sentiment plot for {{ keyword }}">
            <h3>Summary</h3>
            <pre>{{ summaries[keyword] }}</pre>
        </div>
        {% endfor %}
    </body>
    </html>
    """

    template = Template(template_str)
    rendered = template.render(all_results=all_results, summaries=summaries)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(rendered)

    print(f"[INFO] Dashboard generated: {html_path}")
