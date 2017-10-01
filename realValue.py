import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

	excelDataT120 = pd.read_excel(
		open('RealValue.xlsx','rb'), 
		sheetname='Sheet2', 
		skiprows = range(1, 2))
	excelDataT361 = pd.read_excel(
		open('RealValueT361.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 2))
	excelDataT595 = pd.read_excel(
		open('RealValueT595.xlsx','rb'), 
		sheetname='Sheet1', 
		skiprows = range(1, 2))

	timeT120Data = pd.to_datetime(excelDataT120["time"], errors='coerce')
	t120Data = pd.to_numeric(excelDataT120["value"], errors='coerce')
	timeT361Data = pd.to_datetime(excelDataT361["time"], errors='coerce')
	t361Data = pd.to_numeric(excelDataT361["value"], errors='coerce')
	timeT595Data = pd.to_datetime(excelDataT595["time"], errors='coerce')
	t595Data = pd.to_numeric(excelDataT595["value"], errors='coerce')

	plt.figure()
	ax = plt.subplot(311)
	lineT120, = plt.plot(timeT120Data, t120Data, color='k', label="Cell 01")

	plt.subplot(312)
	lineT361, = plt.plot(timeT361Data, t361Data, color='b', label="Cell 03")

	plt.subplot(313)
	lineT595, = plt.plot(timeT595Data, t595Data, color='r', label="Cell 05")
	
	# plt.subplot(311)
	# plt.legend(handles=[lineT120, lineT361, lineT595], loc = 0)

	# Put a legend below current axis
	ax.legend(loc='upper right', handles=[lineT120, lineT361, lineT595])

	plt.savefig("testT120A361A595II.png")
	plt.show()

