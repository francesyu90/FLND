import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

	excelDataT592 = pd.read_excel(
		open('FilteredRealValueT592.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 3),
		parse_dates=['time'])
	excelDataT536 = pd.read_excel(
		open('FilteredRealValueT536.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 3),
		parse_dates=['time'])

	rvT592Data = pd.to_numeric(excelDataT592["value"], errors='coerce')
	rvT536Data = pd.to_numeric(excelDataT536["value"], errors='coerce')

	plt.plot(rvT592Data, rvT536Data, 'r^')

	plt.xlabel('T592 RowA.Cell05.VisioFroth.Cell05.LAB_Luminance')
	plt.ylabel('T536 RowA.Cell05.VisioFroth.Cell05.YVelocity')
	plt.title('T592 Vs T536')
	plt.grid(True)
	plt.savefig("T592VsT536.png")
	plt.show()

if __name__ == '__main__': 
    main()

