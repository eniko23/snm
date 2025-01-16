import pytesseract
from PIL import Image
from flask import Flask, request, render_template
from translation import convert_to_turkish

app = Flask(__name__)

# Tesseract OCR yolu
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\frten\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def perform_ocr(file):
    # Dosyanın doğru bir resim formatı olup olmadığını kontrol edin
    try:
        image = Image.open(file)
        custom_oem_psm_config = r'--oem 3 --psm 6 -l ara'
        text = pytesseract.image_to_string(image, config=custom_oem_psm_config)
        print(f"OCR Çıktısı: {text}")  # OCR çıktısını konsola yazdır
        return text
    except Exception as e:
        print(f"Hata: {e}")  # Hata mesajını konsola yazdır
        return ""

@app.route("/", methods=["GET", "POST"])
def translate_ocr():
    result = ""
    if request.method == "POST":
        if 'file' in request.files:
            file = request.files['file']

            # Dosya yüklenmiş mi kontrol et
            if file.filename == "":
                return render_template("index.html", result="Lütfen bir dosya seçin.")

            # Desteklenen resim formatlarını kontrol et
            if file.content_type not in ["image/png", "image/jpeg", "image/jpg"]:
                return render_template("index.html", result="Lütfen PNG veya JPEG formatında bir dosya yükleyin.")

            try:
                # OCR işlemini başlat
                ocr_text = perform_ocr(file)
                if ocr_text.strip():
                    result = " ".join([convert_to_turkish(word) for word in ocr_text.split()])
                else:
                    result = "OCR işlemi başarısız. Resim okunamadı."
            except Exception as e:
                print(f"Hata: {e}")
                result = "OCR işlemi sırasında bir hata oluştu."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
