import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

	excelDataZn = pd.read_excel(
		open('Flows.xlsx','rb'), 
		sheetname='Flows', 
		parse_dates=['Timestamp'])
	excelDataT361 = pd.read_excel(
		open('RealValueT361.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 3),
		parse_dates=['time'])

	maskZn = (excelDataZn['Timestamp'] > pd.Timestamp('2017-2-10')) & (excelDataZn['Timestamp'] <= pd.Timestamp('2017-2-17'))
	timeT361Data = pd.to_datetime(excelDataT361["time"], errors='coerce')
	maskT361 = (timeT361Data > pd.Timestamp('2017-2-10')) & (timeT361Data <= pd.Timestamp('2017-2-17'))

	filteredExcelDataZn = excelDataZn.loc[maskZn]
	filteredExcelDataT361 = excelDataT361.loc[maskT361]

	timeZnData = pd.to_datetime(filteredExcelDataZn["Timestamp"], errors='coerce')
	znData = pd.to_numeric(filteredExcelDataZn["Zn Rougher 2 Con Flow"], errors='coerce')
	timeT361Data = pd.to_datetime(filteredExcelDataT361["time"], errors='coerce')
	t361Data = pd.to_numeric(filteredExcelDataT361["value"], errors='coerce')

	plt.figure()
	plt.subplot(211)
	lineZn, = plt.plot(timeZnData, znData, color='k', label="Zn Rougher 2 Con Flow")

	plt.subplot(212)
	lineT361, = plt.plot(timeT361Data, t361Data, color='b', label="Cell 03 RGB color")
	
	plt.subplot(211)
	# plt.legend(handles=[lineT120, lineT361, lineT595], loc = 0)

	# Put a legend below current axis
	plt.legend(loc='upper right', handles=[lineZn, lineT361])

	plt.savefig("testZnA361.png")
	plt.show()

if __name__ == '__main__': 
    main()

