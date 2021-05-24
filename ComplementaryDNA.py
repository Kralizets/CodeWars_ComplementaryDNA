def DNA_strand(dna):
    result = ""
    dic = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    
    for elem in dna:
        result += dic[elem]
    
    return result