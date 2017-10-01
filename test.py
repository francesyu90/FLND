import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

	excelDataT358 = pd.read_excel(
		open('FilteredRealValueT358.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 3),
		parse_dates=['time'])
	excelDataT361 = pd.read_excel(
		open('FilteredRealValueT361.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 3),
		parse_dates=['time'])

	rvT358Data = pd.to_numeric(excelDataT358["value"], errors='coerce')
	rvT361Data = pd.to_numeric(excelDataT361["value"], errors='coerce')

	plt.plot(rvT358Data, rvT361Data, 'r^')

	plt.xlabel('T358 RowA.Cell03.VisioFroth.Cell03.LAB_Luminance')
	plt.ylabel('T361 RowA.Cell03.VisioFroth.Cell03.RGBColor')
	plt.title('T358 Vs T361')
	plt.grid(True)
	plt.savefig("T358VsT361.png")
	plt.show()

if __name__ == '__main__': 
    main()

