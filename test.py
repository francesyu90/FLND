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

	timeT117Data = pd.to_datetime(excelDataT117["time"], errors='coerce')
	rvT117Data = pd.to_numeric(excelDataT117["value"], errors='coerce')
	timeT120Data = pd.to_datetime(excelDataT120["time"], errors='coerce')
	rvT120Data = pd.to_numeric(excelDataT120["value"], errors='coerce')

	plt.figure()
	plt.subplot(211)
	lineT117, = plt.plot(timeT117Data, rvT117Data, color='b', label="T117 RowA.Cell01.VisioFroth.Cell01.LAB_Luminance")

	plt.subplot(212)
	lineT120, = plt.plot(timeT120Data, rvT120Data, color='k', label="T120 RowA.Cell01.VisioFroth.Cell01.RGBColor")
	
	plt.subplot(211)
	# plt.legend(handles=[lineT120, lineT361, lineT595], loc = 0)

	# Put a legend below current axis
	plt.legend(loc='upper right', handles=[lineT117, lineT120])

	plt.savefig("T117VsT120.png")
	plt.show()

if __name__ == '__main__': 
    main()

