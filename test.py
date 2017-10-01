import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

	excelDataT592 = pd.read_excel(
		open('FilteredRealValueT592.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 3),
		parse_dates=['time'])
	excelDataT535 = pd.read_excel(
		open('FilteredRealValueT535.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 3),
		parse_dates=['time'])

	rvT592Data = pd.to_numeric(excelDataT592["value"], errors='coerce')
	rvT535Data = pd.to_numeric(excelDataT535["value"], errors='coerce')

	plt.plot(rvT592Data, rvT535Data, 'r^')

	plt.xlabel('T592 RowA.Cell05.VisioFroth.Cell05.LAB_Luminance')
	plt.ylabel('T535 RowA.Cell05.VisioFroth.Cell05.XVelocity')
	plt.title('T592 Vs T535')
	plt.grid(True)
	plt.savefig("T592VsT535.png")
	plt.show()

if __name__ == '__main__': 
    main()

