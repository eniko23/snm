def find_root(word):
#ek kaldırma
    suffixes = [
        #çoğul eki
        "لر", "لری",

        #iyelik eki
        "یم", "ین", "ی", "یمیز", "ینیز",

        #hal eki
        "ده", "دن", "ا", "ه", "یله",

        #şart eki
        "سه",

        #soru eki
        "می", "مو",

        #zaman kipleri
        "جک", "جاق", "دی", "دو", "مش", "موش", "یور",

        #emir kipi
        "سن", "ن", "نیز"
    ]

    #ek bul çıkar kök dön 
    for suffix in suffixes:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word


def apply_grammar_rules(root, original_word):
#anlam
    suffix_mapping = {
        #iyelik eki
        "یم": "im", "ین": "in", "ی": "i", "یمیز": "imiz", "ینیز": "iniz",

        #hal eki
        "ده": "de", "دن": "den", "ا": "a", "ه": "e", "یله": "ile",

        #şart eki
        "سه": "se",

        #soru eki
        "می": "mi", "مو": "mu",

        #zaman kipi
        "جک": "cek", "جاق": "cak", "دی": "di", "دو": "du", "مش": "miş",
        "موش": "muş", "یور": "yor",

        #emir kipi
        "سن": "sen", "ن": "in", "نیز": "iniz"
    }

    #çoğul ekleri ayrıca
    if original_word.endswith("لر"):
        #ünlü uyumu
        if root[-1] in "aıou":  
            return root + "lar"
        else: 
            return root + "ler"

    #çoğul ve iyelik
    if original_word.endswith("لری"):
        if root[-1] in "aıou":
            return root + "ları"
        else: 
            return root + "leri"

    #genel eşleşme
    for suffix, turkish_suffix in suffix_mapping.items():
        if original_word.endswith(suffix):
            return root + turkish_suffix

    
    return root
