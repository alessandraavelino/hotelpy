from PyQt5 import uic, QtWidgets
import sqlite3

def fazerLogin():
    tela_login.label_4.setText("")
    usuario = tela_login.lineEdit.text()
    senha = tela_login.lineEdit_2.text()
    banco = sqlite3.connect("banco_cadastro.db")
    cursor = banco.cursor()
    try:
        cursor.execute("SELECT senha FROM cadastro WHERE usuario = '{}'".format(usuario))
        senha_bd = cursor.fetchall()
        print(senha_bd[0][0])
        banco.close()
    except:
        print("Erro ao validar o login!")
    

    if senha == senha_bd[0][0]:
        tela_login.close()
        tela_main.show()
    else:
        tela_login.label_4.setText("Dados de login incorretos.")

def logout():
    tela_main.close()
    tela_login.show()

def abrirTelaCadastro():
    tela_cadastro.show()



def cadastrar():
    nome = tela_cadastro.lineEdit.text()
    telefone = tela_cadastro.lineEdit_2.text()
    usuario = tela_cadastro.lineEdit_3.text()
    senha = tela_cadastro.lineEdit_4.text()
    c_senha = tela_cadastro.lineEdit_5.text()

    if (senha == c_senha):
        try:
            banco = sqlite3.connect("banco_cadastro.db")
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text, telefone text, usuario text, senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('"+nome+"', '"+telefone+"', '"+usuario+"', '"+senha+"')")

            banco.commit()
            banco.close()
            tela_cadastro.label_5.setText("Usuário cadastrado com sucesso.")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ", erro)

    else:
        tela_cadastro.label_7.setText("As senhas digitadas não coincidem.")

def abrirTelaCadastrarHospede():
    tela_cadastrohospede.show()

def cadastrarHospede():
    nomeCompleto = tela_cadastrohospede.lineEdit.text()
    telefone = tela_cadastrohospede.lineEdit_2.text()
    quarto = tela_cadastrohospede.lineEdit_3.text()
    dataCheckin = tela_cadastrohospede.dateEdit.text()
    dataCheckout = tela_cadastrohospede.dateEdit_2.text()
    totalDiarias = tela_cadastrohospede.spinBox_2.text()
    totalPag = tela_cadastrohospede.label_8.text()
    
    if quarto == "Suíte presidencial" and totalDiarias == 1:
        tela_cadastrohospede.label_8.setText("100,00")

        
    try:
        banco = sqlite3.connect("banco_cadastro.db")
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS hospede (nomeCompleto text, telefone text, quarto text, dataCheckin text, dataCheckout text)")
        cursor.execute("INSERT INTO hospede VALUES ('"+nomeCompleto+"', '"+telefone+"', '"+quarto+"', '"+dataCheckin+"', '"+dataCheckout+"')")
        banco.commit()
        banco.close()

    except sqlite3.Error as erro:
        print("Ocorreu um erro: ", erro)

def abrirTelaListarHospedes():
    tela_listarhospedes.show()
    banco = sqlite3.connect("banco_cadastro.db")
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM hospede")
    dados_lidos = cursor.fetchall()
    tela_listarhospedes.tableWidget.setRowCount(len(dados_lidos))
    tela_listarhospedes.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
            tela_listarhospedes.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    banco.close()



app = QtWidgets.QApplication([])
tela_login = uic.loadUi("tela_login.ui")
tela_main = uic.loadUi("tela_main.ui")
tela_cadastro = uic.loadUi("tela_cadastro.ui")
tela_listarhospedes = uic.loadUi("tela_listarhospedes.ui")
tela_cadastrohospede = uic.loadUi("tela_cadastrohospede.ui")
tela_login.pushButton.clicked.connect(fazerLogin)
tela_main.pushButton_4.clicked.connect(logout)
tela_login.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
tela_login.pushButton_2.clicked.connect(abrirTelaCadastro)
tela_cadastro.pushButton.clicked.connect(cadastrar)
tela_cadastrohospede.pushButton.clicked.connect(cadastrarHospede)
tela_main.pushButton.clicked.connect(abrirTelaCadastrarHospede)
tela_main.pushButton_3.clicked.connect(abrirTelaListarHospedes)


tela_login.show()
app.exec()