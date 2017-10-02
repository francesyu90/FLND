import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def main():

	excelDataAssays = pd.read_excel(
		open('Assays.xlsx','rb'), 
		sheetname='Assays', 
		parse_dates=['Timestamp'])

	train, test = train_test_split(excelDataAssays, test_size=0.2)
	print(train)

	# timeAData = pd.to_datetime(excelDataAssays["Timestamp"], errors='coerce')
	# z2RCData = pd.to_numeric(excelDataAssays["Z2RC Zn"], errors='coerce')

	


if __name__ == '__main__': 
    main()

