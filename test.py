import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

	excelDataT592 = pd.read_excel(
		open('FilteredRealValueT592.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 3),
		parse_dates=['time'])
	excelDataT595 = pd.read_excel(
		open('FilteredRealValueT595.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 3),
		parse_dates=['time'])

	rvT592Data = pd.to_numeric(excelDataT592["value"], errors='coerce')
	rvT595Data = pd.to_numeric(excelDataT595["value"], errors='coerce')

	plt.plot(rvT592Data, rvT595Data, 'r^')

	plt.xlabel('T592 RowA.Cell05.VisioFroth.Cell05.LAB_Luminance')
	plt.ylabel('T595 RowA.Cell05.VisioFroth.Cell05.RGBColor')
	plt.title('T592 Vs T595')
	plt.grid(True)
	plt.savefig("T592VsT595.png")
	plt.show()

if __name__ == '__main__': 
    main()

