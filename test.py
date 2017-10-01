import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

	excelDataT301 = pd.read_excel(
		open('FilteredRealValueT301.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 3),
		parse_dates=['time'])
	excelDataT302 = pd.read_excel(
		open('FilteredRealValueT302.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 3),
		parse_dates=['time'])

	rvT301Data = pd.to_numeric(excelDataT301["value"], errors='coerce')
	rvT302Data = pd.to_numeric(excelDataT302["value"], errors='coerce')

	plt.plot(rvT301Data, rvT302Data, 'r^')

	plt.xlabel('T301 RowA.Cell03.VisioFroth.Cell03.XVelocity')
	plt.ylabel('T302 RowA.Cell03.VisioFroth.Cell03.YVelocity')
	plt.title('T301 Vs T302')
	plt.grid(True)
	plt.savefig("T301VsT302.png")
	plt.show()

if __name__ == '__main__': 
    main()

