def find_root(word):
    suffixes = [
    # Çoğul ekleri 
    "لر", "لری", "لار", "لارı", "lerini",

    # İyelik ekleri 
    "یم", "ین", "ی", "یمیز", "ینiz", "یون", "یونız", "مان", "مانız", "ت", "تان", "تانız",

    # Hal ekleri 
    "ده", "دن", "ا", "ه", "یله", "دیر", "چون", "ی", "یی", "لی", "دین", "دendir", "یش", "در",

    # Şart ekleri
    "سه", "سَ", "سَن", "سا", "یاب", "یacağım", "yacak", "yaşarım", "tümüyle",

    # Soru ekleri 
    "می", "مو", "مای", "دَ", "تِ", "نَ", "نا", "کی", "دور", "تان", "یعنی",

    # Zaman kipleri
    "جک", "جاق", "دی", "دو", "مش", "موش", "یور", "ایر", "میش", "tı", "dım", "din", "dık", "tıg", "ki", "mış", "di", "da", "du", "dir",

    # Emir kipleri 
    "سن", "ن", "نیز", "یز", "سَن", "شوند", "وا", "ور", "کı", "سنiz", "سر", "زی",

    # Geçmiş zaman birleşik çekimi
    "ایردی", "ایrmış", "دیrdı", "میش", "میردی", "mıştı", "dı", "dı", "dıgın", "mış", "tı", "dır", "dıı", "dırdı",

    # Geniş zaman birleşik çekimi 
    "یوردی", "ایوردی", "yordu", "iyordu", "yor", "mıştı", "iydi", "ılıyordu", "idi",

    # Dilek/İstek kipleri 
    "ای", "سی", "سون", "سین", "ک", "سان", "kı", "sı", "bileceği",

    # Fiilden fiil yapım ekleri 
    "یش", "ت", "تر", "tır", "dır", "tı", "tırdı", "yı", "yordu", "e", "sin", "me", "yormak", "maktan", "len", "in", "sin", "mak", "ılmak", "lacak", "yormak", "iş", "ilik", "a", "nın", "ni",

    # Ek fiil ekleri 
    "im", "ız", "ı", "e", "an", "dım", "dur", "ama", "tek",

    # Bağlaçlar 
    "ve", "ya", "ya da", "ya da ki", "çünkü", "halbuki", "çünkü de", "öyle", "o yüzden", "bu yüzden",

    # Zarf 
    "na", "hala", "şimdi", "geçen", "çok", "bazen", "asla", "hiç", "belki", "henüz", "mü", "yine", "hem", "sonra", "önce", "yakın", "biri", "her zaman", "hala",
    ]

    for suffix in suffixes:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word



def apply_grammar_rules(root, original_word):
    suffix_mapping = {
    # İyelik ekleri 
    "یم": "im", "ین": "in", "ی": "i", "یمیز": "imiz", "ینiz": "iniz", "یون": "in", "یونız": "iniz",

    # Hal ekleri
    "ده": "de", "دن": "den", "ا": "a", "ه": "e", "یله": "ile", "دیر": "dir", "چون": "çün", "ی": "i",

    # Şart ekleri 
    "سه": "se", "سَ": "sa", "سَن": "san", "سا": "sa",

    # Soru ekleri
    "می": "mi", "مو": "mu", "مای": "mı", "دَ": "da", "تِ": "te", "نَ": "ne", "نا": "na",

    # Zaman kipleri 
    "جک": "cek", "جاق": "cak", "دی": "di", "دو": "du", "مش": "miş", "موش": "muş", "یور": "yor", "ایر": "er",
    "میش": "miş", "تی": "ti", "دیم": "dim", "دین": "din", "دیمیز": "dimiz", "دینiz": "diniz", "میشی": "mişi",

    # Emir kipleri 
    "سن": "sen", "ن": "in", "نیز": "iniz", "یز": "iz", "سَن": "sen", "سون": "sun", "سین": "sin",

    # Geçmiş zaman birleşik çekimi 
    "ایردی": "erdi", "ایrmış": "ermiş", "دیrdı": "dirdi", "میش": "miş", "میردی": "mirdi", "mişti": "mişti",

    # Geniş zaman birleşik çekimi 
    "یوردی": "yordu", "ایوردی": "iyordu", "یور": "yor", "مشتر": "mişti", "مشته": "mişti",

    # Dilek/İstek kipleri 
    "ای": "e", "سی": "si", "سون": "sun", "سین": "sin", "ک": "k", "شان": "şan",

    # Fiilden fiil yapım ekleri 
    "یش": "iş", "ت": "t", "تر": "tir", "tır": "tır", "دَ": "dır", "dı": "dı", "dı": "dı",
    "یور": "yor", "پ": "p", "ه": "he", "گی": "gi", "سی": "si", "اک": "ak", "ی": "i", "ش": "ş", 

    # Bağlaçlar 
    "و": "ve", "یا": "ya", "ya da": "ya da", "ne...ne de": "ne...ne de", "ki": "ki", "çünkü": "çünkü", "halbuki": "halbuki",

    # Zarf 
    "نا": "na", "حالا": "şimdi", "علیه": "aleyhine", "زیاد": "çok", "دریافت": "almış", "هرگز": "asla",
    }

    if original_word.endswith("لر"):
        return root + ("lar" if root[-1] in "aıou" else "ler")
    if original_word.endswith("لری"):
        return root + ("ları" if root[-1] in "aıou" else "leri")
    for suffix, turkish_suffix in suffix_mapping.items():
        if original_word.endswith(suffix):
            return root + turkish_suffix
    return root
