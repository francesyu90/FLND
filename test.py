import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

	excelDataT117 = pd.read_excel(
		open('FilteredRealValueT117.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 3),
		parse_dates=['time'])
	excelDataT61 = pd.read_excel(
		open('FilteredRealValueT61.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 3),
		parse_dates=['time'])
	excelDataT60 = pd.read_excel(
		open('FilteredRealValueT60.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 3),
		parse_dates=['time'])

	timeData = pd.to_datetime(excelDataT117["time"], errors='coerce')
	rvT117Data = pd.to_numeric(excelDataT117["value"], errors='coerce')
	rvT61Data = pd.to_numeric(excelDataT61["value"], errors='coerce')
	rvT60Data = pd.to_numeric(excelDataT60["value"], errors='coerce')
	
	plt.plot(timeData, rvT61Data)

	plt.xlabel('Timestamp')
	plt.ylabel('T61 RowA.Cell01.VisioFroth.Cell01.YVelocity')
	# plt.title('')
	plt.grid(True)
	plt.savefig("timeVsT61I.png")
	plt.show()

if __name__ == '__main__': 
    main()

