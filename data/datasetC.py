import re
import csv
import pdfplumber

pdf_path = "C:\\Users\\frten\\Desktop\\osmanlica_ceviri\\kamus-i-turki-orj_compress.pdf"  
csv_path = "kelime_listesii.csv"  

kelime_listesi = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        #regex
        matches = re.findall(r"([\u0600-\u06FF\s]+)\s(.+):", text)  #([a-zA-Z’]+)\s\((.*?)\)\s\[([\u0600-\u06FF\s]+)\]

        kelime_listesi.extend(matches)

with open(csv_path, mode="w", encoding="utf-8-sig", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Kelime (Arapça)", "Anlamı"]) 
    writer.writerows(kelime_listesi)

print(f"{len(kelime_listesi)} kelime başarıyla '{csv_path}' dosyasına yazıldı.")
