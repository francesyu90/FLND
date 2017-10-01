import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

	excelDataSAG = pd.read_excel(
		open('Flows.xlsx','rb'), 
		sheetname='Flows', 
		parse_dates=['Timestamp'])
	excelDataT361 = pd.read_excel(
		open('RealValueT361.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 3),
		parse_dates=['time'])

	maskZn = (excelDataSAG['Timestamp'] > pd.Timestamp('2017-2-10')) & (excelDataSAG['Timestamp'] <= pd.Timestamp('2017-2-17'))
	timeT361Data = pd.to_datetime(excelDataT361["time"], errors='coerce')
	maskT361 = (timeT361Data > pd.Timestamp('2017-2-10')) & (timeT361Data <= pd.Timestamp('2017-2-17'))

	filteredExcelDataSAG = excelDataSAG.loc[maskZn]
	filteredExcelDataT361 = excelDataT361.loc[maskT361]

	timeSAGData = pd.to_datetime(filteredExcelDataSAG["Timestamp"], errors='coerce')
	sag1Data = pd.to_numeric(filteredExcelDataSAG["SAG1"], errors='coerce')
	sag2Data = pd.to_numeric(filteredExcelDataSAG["SAG2"], errors='coerce')
	sag3Data = pd.to_numeric(filteredExcelDataSAG["SAG3"], errors='coerce')
	timeT361Data = pd.to_datetime(filteredExcelDataT361["time"], errors='coerce')
	t361Data = pd.to_numeric(filteredExcelDataT361["value"], errors='coerce')

	plt.figure()
	plt.subplot(211)
	lineSAG1, = plt.plot(timeSAGData, sag1Data, color='b', label="SAG1")
	lineSAG2, = plt.plot(timeSAGData, sag2Data, color='r', label="SAG2")
	lineSAG3, = plt.plot(timeSAGData, sag3Data, color='k', label="SAG3")

	plt.subplot(212)
	lineT361, = plt.plot(timeT361Data, t361Data, color='g', label="Cell 03 RGB color")
	
	plt.subplot(211)
	# plt.legend(handles=[lineT120, lineT361, lineT595], loc = 0)

	# Put a legend below current axis
	plt.legend(loc='upper right', handles=[lineSAG1, lineSAG2, lineSAG3, lineT361])

	plt.savefig("sagA361Feb.png")
	plt.show()

if __name__ == '__main__': 
    main()

