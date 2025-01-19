import csv
from grammar_rules import find_root, apply_grammar_rules

def load_dataset():
    dataset = {}
    with open(r"C:\Users\frten\Desktop\testalani\ocr_Ceviri\data\turkce_osmanlicakelimeler.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                osmanlica, turkce = row[0].strip(), row[1].strip()  
                dataset[osmanlica] = turkce  
    return dataset

dataset = load_dataset()

TURKISH_TO_OTTOMAN = {
    'a': 'ا', 'b': 'ب', 'c': 'ج', 'ç': 'چ', 'd': 'د', 'e': 'ه',
    'f': 'ف', 'g': 'گ', 'ğ': 'غ', 'h': 'ح', 'ı': 'ی', 'i': 'ی',
    'j': 'ژ', 'k': 'ک', 'l': 'ل', 'm': 'م', 'n': 'ن', 'o': 'و',
    'ö': 'و', 'p': 'پ', 'r': 'ر', 's': 'س', 'ş': 'ش', 't': 'ط',
    'u': 'و', 'ü': 'و', 'v': 'و', 'y': 'ﻯ', 'z': 'ز', 'k': 'ك',
    '\'': 'ع', 's': 'ص', 'ı': 'ي', 'k': 'ق', 'ê': 'ؤ', 'z': 'ظ',
    't': 'ت',
}

OTTOMAN_TO_TURKISH = {v: k for k, v in TURKISH_TO_OTTOMAN.items()}  

def convert_to_ottoman(word):
    return ''.join([TURKISH_TO_OTTOMAN.get(char, char) for char in word])

def convert_to_turkish(word):

    if word in dataset:
        return dataset[word]
    
    root = find_root(word) 
    if root in dataset:
        return apply_grammar_rules(dataset[root], word)
    

    print(f"Kelime veri setinde bulunamadı. Harf dönüşümü uygulanıyor: {word}")
    return ''.join([OTTOMAN_TO_TURKISH.get(char, char) for char in word])
