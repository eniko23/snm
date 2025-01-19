import csv
import json

def convert_dataset(input_file_path, output_file_path):
    try:
        with open(input_file_path, mode='r', encoding="utf-8") as input_file:
            data = json.load(input_file)  

            with open(output_file_path, mode='w', encoding="utf-8", newline='') as output_file:
                csv_writer = csv.writer(output_file)

                for key, value in data.items():
                    csv_writer.writerow([key, value])

        print(f"Dönüştürme işlemi başarıyla tamamlandı. Çıktı dosyası: {output_file_path}")
    
    except FileNotFoundError:
        print(f"Dosya bulunamadı: {input_file_path}")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

input_file_path = r"C:\Users\frten\Desktop\testalani\ocr_Ceviri\data\datasq.csv" 
output_file_path = r"C:\Users\frten\Desktop\testalani\ocr_Ceviri\data\databir.csv"  

convert_dataset(input_file_path, output_file_path)
