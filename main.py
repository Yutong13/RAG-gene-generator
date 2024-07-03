from code_generator import predict_icd_code
import pandas as pd

def main():
    query = input("Query for PubMed: ") # ask for search query
    icd_code = predict_icd_code(query) # list of ICD code
    for i in range(len(icd_code)):
        icd_code[i] = "".join(icd_code[i].split("."))
    print("ICD codes: ",icd_code)

    df = pd.read_csv("Section111ValidICD10-Jan2024.csv")
    names = []
    for code in icd_code:
        icd_row = df[df['CODE'] == code] # search for ICD code
        names.append(icd_row.iloc[:, 1].to_list()[0]) # Names in Short is second column in scv
    print("Names:\n", names)

main()