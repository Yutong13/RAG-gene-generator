from code_generator import predict_icd_code

def main():
    query = input("Query for PubMed: ") # ask for search query
    icd_code = predict_icd_code(query) # list of ICD code
    for i in range(len(icd_code)):
        icd_code[i] = "".join(icd_code[i].split("."))
    print(icd_code)
    
main()