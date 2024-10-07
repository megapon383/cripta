from PyQt5.QtWidgets import (QLabel,QPushButton,QLineEdit,QHBoxLayout,QComboBox,QVBoxLayout,QApplication,QWidget)
from PyQt5.QtCore import Qt

app = QApplication([])

uest_lb = QLabel("Оберіть скільки ви вибираїте крипто валюти")
spusok = QComboBox()
lenut = QLineEdit()
uest = QLabel("тут бути")
cnopca = QPushButton("Розрохувати")

layut = QVBoxLayout()
layut.addWidget(uest_lb)
layut.addWidget(spusok)
layut.addWidget(lenut)
layut.addWidget(uest)
layut.addWidget(cnopca)






cripta = {"BTC": 63126.50,
            "ETC": 18.96,
            "XRP": 0.54}
spusok.addItems(cripta.keys())

def dolar():
    a = float(cripta[spusok.currentText()])
    uest.setText(str (a* float (lenut.text())))




window = QWidget()
window.resize(400 , 300)
window.setWindowTitle("Vucislator3000")
window.setLayout (layut)
window.show()

cnopca.clicked.connect(dolar)




app.exec()
