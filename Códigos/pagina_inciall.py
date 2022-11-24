from PyQt5 import uic,QtWidgets
import mysql.connector
bd= mysql.connector.connect(
    host='localhost',
    user='root',
    passwd="",
    database='projeto_produtos'
)

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
    print('Preço',linha5)
    linha6=pagina_inicial.lineEdit_6.text()
    print('Quantidade',linha6)
# Definindo referencia para botões selecionaveis.
    categoria=''
#
    if pagina_inicial.radioButton.isChecked():
        print('Beleza')
        categoria='Beleza'
    elif pagina_inicial.radioButon_2.isChecked():
        print('Resfriado')
        categoria='resfriado'
    elif pagina_inicial.radioButon_3.isChecked():
        print('Higiene Pessoal')
        categoria='higiene Pessoal'
    # ligando bd com tela
    cursor=bd.cursor()
    comando_SQL='insert into produtos_variaveis(Nome,sexo,Idade,produto,preço,Quantidade,categoria) values(%s,%s,%s,%s,%s,%s,%s)'
    dados=(str(linha1),str(linha2),str(linha3),str(linha4),str(linha5),str(linha6), categoria)
    cursor.execute(comando_SQL,dados)
    bd.commit()

app=QtWidgets.QApplication([])
pagina_inicial=uic.loadUi('pagina_inicial.ui')
pagina_inicial.pushButton.clicked.connect(funcao_principal)

pagina_inicial.show()
app.exec()

# criando as tabelas:
# create table produtos_variaveis ( 
    #id INT NOT NULL AUTO_INCREMENT,
    #Nome VARCHAR(50),  
    #Sexo VARCHAR(50), 
    #Idade INT,
    #produto VARCHAR(30),
    #preço DOUBLE,
    #Quantidade INT,
    #Categoria VARCHAR(30),
    #primary key (id)
#);
#insert into produtos_variaveis (Nome,sexo,Idade,produto,preço,Quantidade,categoria)values ("Odair Dias","M",33,"creme dental",9,1,"saude");