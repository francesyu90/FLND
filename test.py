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

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx()
	ax3 = ax1.twinx()

	ax1.plot(timeT120Data, t120Data, 'k-', label='Cell01')
	ax1.set_xlabel('Timestamp')
	ax1.set_ylabel('RowA.VisioFroth.RGBColor')
	ax2.plot(timeT361Data, t361Data, 'b-', label='Cell03')
	ax3.plot(timeT595Data, t595Data, 'r-', label='Cell05')
	

	# plt.plot(timeData, t120Data)
	fig.tight_layout()
	plt.legend(loc='upper left')
	plt.savefig("testT120A361A595.png")
	plt.show()

