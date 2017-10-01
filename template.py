import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

	excelDataT117 = pd.read_excel(
		open('FilteredRealValueT117.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 3),
		parse_dates=['time'])
	excelDataT120 = pd.read_excel(
		open('FilteredRealValueT120.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 3),
		parse_dates=['time'])

	rvT117Data = pd.to_numeric(excelDataT117["value"], errors='coerce')
	rvT120Data = pd.to_numeric(excelDataT120["value"], errors='coerce')
	
	plt.plot(rvT117Data, rvT120Data, 'r^')

	plt.xlabel('T117 RowA.Cell01.VisioFroth.Cell01.LAB_Luminance')
	plt.ylabel('T120 RowA.Cell01.VisioFroth.Cell01.RGBColor')
	# plt.title('')
	plt.grid(True)
	plt.savefig("T117VsT120I.png")
	plt.show()

if __name__ == '__main__': 
    main()

