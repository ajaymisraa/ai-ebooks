from flask import Flask, request, send_file
from outline import *
from pdf import *
import io

app = Flask(__name__)

@app.route('/create_ebook', methods=['POST'])
def create_ebook_api():
    # Extract topic and audience from POST request
    data = request.json
    topic = data['topic']
    audience = data['audience']

    # Your existing logic to create an ebook
    coverimg = cover(topic, audience)
    outlines = outline(topic, audience, 5, 3)
    ebook_json = content(topic, audience, outlines)
    
    # Assuming create_ebook returns a path to the created PDF
    pdf_path = create_ebook(coverimg, ebook_json, "Misra Publishing")

    # Return the PDF file
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
