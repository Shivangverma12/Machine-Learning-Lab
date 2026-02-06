import pandas as pd


#TO performe import,export operations(xl,csv etc.) using pandas in python
#define Dataframe

data={
    "ID" :[1,2,3,4,5],
    "Name" :["SHIVANG VERMA","TANYA VERMA","MANAS GUPTA","RISHU PAL","RAHUL SINGH"],
    "Marks" :[99,87,89,76,87]
}

data_frame=pd.DataFrame(data)

#---------export---------

data_frame.to_excel(r"C:\Users\Asus\Documents\student11.xlsx",index=False)
data_frame.to_csv(r"C:\Users\Asus\Documents\student12.csv",index=False)
data_frame.to_csv(r"C:\Users\Asus\Documents\student13.txt",index=False,sep='\t')
print("Data exported to CSV,XLSX AND TXT files.") 

#-------import-------
csv_df=pd.read_csv(r"C:\Users\Asus\Documents\student12.csv")
print("\nCSV DATA: \n",csv_df)

xlsx_df=pd.read_excel(r"C:\Users\Asus\Documents\student11.xlsx")
print("\nEXCEL DATA: \n",xlsx_df)

txt_df=pd.read_csv(r"C:\Users\Asus\Documents\student13.txt",sep='\t')
print("\nTXT DATA :\n",txt_df)