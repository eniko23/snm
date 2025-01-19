import csv
import pytesseract
from PIL import Image
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\frten\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def load_dataset(file_path):
    dataset = {}
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                osmanlica, turkce = row[0].strip(), row[1].strip()
                dataset[osmanlica] = turkce
    return dataset

dataset = load_dataset("data/databir.csv")

def perform_ocr(file):
    try:
        image = Image.open(file)
        custom_oem_psm_config = r'--oem 3 --psm 6 -l ara'
        text = pytesseract.image_to_string(image, config=custom_oem_psm_config)
        print(f"OCR Çıktısı: {text}")  
        return text
    except Exception as e:
        print(f"Hata: {e}")
        return ""

from translation import convert_to_ottoman, convert_to_turkish

@app.route("/", methods=["GET", "POST"])
def translate():
    ocr_text = ""
    result = ""
    error = None
    if request.method == "POST":
        direction = request.form.get('direction')
        text = request.form.get('text', '').strip()
        file = request.files.get('file')

        if direction:
            if text and not file:
                if direction == "to_ottoman":
                    result = " ".join([convert_to_ottoman(word) for word in text.split()])
                else:
                    result = " ".join([convert_to_turkish(word) for word in text.split()])
            elif file and not text:
                ocr_text = perform_ocr(file)
                if ocr_text.strip():
                    if direction == "to_ottoman":
                        result = " ".join([convert_to_ottoman(word) for word in ocr_text.split()])
                    else:
                        result = " ".join([convert_to_turkish(word) for word in ocr_text.split()])
                else:
                    error = "OCR işlemi başarısız. Resim okunamadı."

    return render_template("index.html", error=error, ocr_text=ocr_text, result=result, text="", file=None)

@app.route('/search')
def search_page():
    return render_template('search.html')

@app.route('/api/search', methods=['GET'])
def search_word():
    query = request.args.get('query', '').strip()
    if not query:
        return jsonify([])

 
    results = [
        {'osmanlica': osmanlica, 'turkce': turkce}
        for osmanlica, turkce in dataset.items()
        if query in osmanlica or query in turkce
    ][:10]  
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
