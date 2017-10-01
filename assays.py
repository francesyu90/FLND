import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

	excelDataAssays = pd.read_excel(
		open('Assays.xlsx','rb'), 
		sheetname='Assays', 
		parse_dates=['Timestamp'])

	timeAData = pd.to_datetime(excelDataAssays["Timestamp"], errors='coerce')
	maskA = (timeAData > pd.Timestamp('2017-2-10')) & (timeAData <= pd.Timestamp('2017-2-17'))
	filteredExcelDataAssays = excelDataAssays.loc[maskA]

	timeData = pd.to_datetime(filteredExcelDataAssays["Timestamp"], errors='coerce')
	z2RCData = pd.to_numeric(filteredExcelDataAssays["Z2RC Zn"], errors='coerce')
	z1RCData = pd.to_numeric(filteredExcelDataAssays["Z1RC Zn"], errors='coerce')
	zrCCData = pd.to_numeric(filteredExcelDataAssays["ZRCC Zn"], errors='coerce')

	plt.figure()
	plt.subplot(311)
	lineZ2RCZn, = plt.plot(timeData, z2RCData, color='b', label="Z2RC Zn")

	plt.subplot(312)
	lineZ1RCZn, = plt.plot(timeData, z1RCData, color='k', label="Z1RC Zn")

	plt.subplot(313)
	lineZRCCZn, = plt.plot(timeData, zrCCData, color='r', label="ZRCC Zn")

	plt.xlabel('Timestamp')
	# plt.ylabel('T61 RowA.Cell01.VisioFroth.Cell01.YVelocity')
	# plt.title('')
	# plt.grid(True)
	plt.subplot(311)
	plt.legend(loc='upper right', handles=[lineZ2RCZn, lineZ1RCZn, lineZRCCZn])
	plt.savefig("z2RCAZ1RCAZRCCI.png")
	plt.show()

if __name__ == '__main__': 
    main()

