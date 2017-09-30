import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excelData = pd.read_excel(open('Flows.xlsx','rb'), sheetname='Flows')

timeData = pd.to_datetime(excelData["Timestamp"])
znData = pd.to_numeric(excelData["Zn Rougher 2 Con Flow"], errors='coerce')
# print(znData)

plt.plot(timeData, znData)
plt.savefig("test.png")
plt.show()