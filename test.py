import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

	excelDataT535 = pd.read_excel(
		open('FilteredRealValueT535.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 3),
		parse_dates=['time'])
	excelDataT536 = pd.read_excel(
		open('FilteredRealValueT536.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 3),
		parse_dates=['time'])

	rvT535Data = pd.to_numeric(excelDataT535["value"], errors='coerce')
	rvT536Data = pd.to_numeric(excelDataT536["value"], errors='coerce')

	plt.plot(rvT535Data, rvT536Data, 'r^')

	plt.xlabel('T535 RowA.Cell05.VisioFroth.Cell05.XVelocity')
	plt.ylabel('T536 RowA.Cell05.VisioFroth.Cell05.YVelocity')
	plt.title('T535 Vs T536')
	plt.grid(True)
	plt.savefig("T535VsT536.png")
	plt.show()

if __name__ == '__main__': 
    main()

