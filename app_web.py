from flask import Flask, render_template_string, request
from predict_url import predict_url

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Phishing URL Detector</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-dark text-light d-flex flex-column align-items-center" style="min-height:100vh; padding-top: 50px;">
    <div class="container text-center">
        <h1 class="mb-4">🔒 Phishing URL Detector</h1>
        <form method="POST" class="w-75 mx-auto">
            <div class="input-group mb-3">
                <input type="text" name="url" class="form-control" placeholder="Enter URL" required>
                <button class="btn btn-success" type="submit">Check</button>
            </div>
        </form>
        {% if result is defined %}
            <div class="alert {% if result == 'Phishing' %}alert-danger{% else %}alert-success{% endif %} mt-4" role="alert">
                <h4>Result: {{ result }}</h4>
            </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form['url'].strip()
        result = predict_url(url)
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
