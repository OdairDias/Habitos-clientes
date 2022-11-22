from PyQt5 import uic,QtWidgets

def funcao_principal():
    linha1=pagina_inicial.lineEdit.text()
    print('Nome:', linha1)
    linha2=pagina_inicial.lineEdit_2.text().upper()
    print('Sexo:', linha2)
    linha3=pagina_inicial.lineEdit_3.text()
    print('Idade:',linha3)
    linha4=pagina_inicial.lineEdit_4.text()
    print('Produto:',linha4)
    linha5=pagina_inicial.lineEdit_5.text()
    print('Quantidade',linha5)
    if pagina_inicial.radioButton.isChecked():
        print('Beleza')
    elif pagina_inicial.radioButon_2.isChecked():
        print('Resfriado')
    elif pagina_inicial.radioButon_3.isChecked():
        print('Higiene Pessoal')

app=QtWidgets.QApplication([])
pagina_inicial=uic.loadUi('pagina_inicial.ui')
pagina_inicial.pushButton.clicked.connect(funcao_principal)

pagina_inicial.show()
app.exec()