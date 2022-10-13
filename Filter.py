from PyQt6.QtWidgets import QApplication, QWidget
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


app = QApplication(sys.argv)

Arquivo_Excel = pd.read_excel(r'SEI2022.xlsx', engine='openpyxl')

Locais = Arquivo_Excel['Local'].drop_duplicates(keep=False)

print("SALAS:")
print(Locais)


janela = QWidget()
janela.resize(500,400)
janela.setWindowTitle(Locais)
janela.show()

app.exec()