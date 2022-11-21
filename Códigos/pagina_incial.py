from PyQt5 import uic,QtWidgets


def funcao_principal():
    print('Testando')

app=QtWidgets.QApplication([])
pagina_inicial=uic.loadUi('pagina_inicial.ui')
pagina_inicial.pushButton.clicked.connect(funcao_principal)

pagina_inicial.show()
app.exec
