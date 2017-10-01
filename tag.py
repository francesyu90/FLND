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

	plt.figure()
	plt.subplot(311)
	lineT60, = plt.plot(timeData, rvT60Data, color='b', label="T60")

	plt.subplot(312)
	lineT61, = plt.plot(timeData, rvT61Data, color='k', label="T61")

	plt.subplot(313)
	lineT117, = plt.plot(timeData, rvT117Data, color='r', label="T117")

	plt.xlabel('Timestamp')
	# plt.ylabel('T61 RowA.Cell01.VisioFroth.Cell01.YVelocity')
	# plt.title('')
	# plt.grid(True)
	plt.subplot(311)
	plt.legend(loc='upper right', handles=[lineT60, lineT61, lineT117])
	plt.savefig("timeVsT60AT61T117.png")
	plt.show()

if __name__ == '__main__': 
    main()

