import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excelData = pd.read_excel(open('RealValue.xlsx','rb'), sheetname='Sheet2', skiprows = range(1, 2))

timeData = pd.to_datetime(excelData["time"], errors='coerce')
t120Data = pd.to_numeric(excelData["value"], errors='coerce')

plt.plot(timeData, t120Data)
plt.savefig("testT120.png")
plt.show()