from code_generator import predict_icd_code

def main():
    query = input("Query for PubMed: ") # ask for search query
    icd_code = predict_icd_code(query) # list of ICD code
    print(icd_code)

main()