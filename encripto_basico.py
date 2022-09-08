from PyQt5 import uic,QtWidgets

def crip():
    print('criptoi')
    line_text = crip_screen.lineEdit_1.text() # linha do texto a ser criptografado
    line_crip = crip_screen.lineEdit_2.text() # recebe o texto já encriptado
    
    idea = ''

    for i in line_text:
        idea = idea + chr (ord(i)+5)

    crip_screen.lineEdit_1.setText("") # limpa a caixa que recebe o texto a ser criptografado
    crip_screen.lineEdit_2.setText(idea) # mostra o texto encriptado na caixa 2


app=QtWidgets.QApplication([])
crip_screen=uic.loadUi("criptotela.ui")
crip_screen.pushButton_1.clicked.connect(crip)

crip_screen.show()
app.exec()