import csv
from grammar_rules import find_root, apply_grammar_rules

def load_dataset():
    dataset = {}
    with open("data/turkce_osmanlicakelimeler.csv", "r", encoding="utf-8") as file:
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
    'u': 'و', 'ü': 'و', 'v': 'و', 'y': 'ی', 'z': 'ز'
}

OTTOMAN_TO_TURKISH = {v: k for k, v in TURKISH_TO_OTTOMAN.items()}  

def convert_to_ottoman(word):
    return ''.join([TURKISH_TO_OTTOMAN.get(char, char) for char in word])

def convert_to_turkish(word):
    #dataset eşleşme kontrol
    if word in dataset:
        return dataset[word]
    
    #kök analizi
    root = find_root(word)
    if root in dataset:
        return apply_grammar_rules(dataset[root], word)
    
    #eğer sonuç çıkmazsa sonuç olarak harf dönüşümü
    print(f"Tahmini çeviri uygulanıyor: {word}")
    return ''.join([OTTOMAN_TO_TURKISH.get(char, char) for char in word])
