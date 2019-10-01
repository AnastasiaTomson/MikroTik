#!/home/delker/PycharmProjects/MikRotik/venv/bin/python3.6
import paramiko
from PySide2.QtWidgets import QApplication, QMainWindow
import sys
from ui import Ui_MainWindow

# Create application
app = QApplication(sys.argv)

# Create form and init UI
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

host = '192.168.88.1'
login = 'admin'


# Hook logic
def bp():
    com = ui.pushButton_2.text()
    if com == 'Настроить':
        setup()
    else:
        clear()


def setup():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=login, password='\r')
    ssid = ui.lineEdit.text()
    password = ui.lineEdit_3.text()
    if ssid and password and len(password) >= 8:
        password2 = ui.lineEdit_5.text()
        if not password2:
            password2 = 52498

        def command(x):
            stdin, stdout, stderr = client.exec_command(x, 2)
            var = stdout.read() + stderr.read()
            return var.decode("UTF-8")

        # Count ether
        count_ether = command('/interface ethernet print count-only')

        # IP address last ether
        command('/ip address set interface=ether' + count_ether + ' numbers=0')

        # Interface-list -> all
        command('/tool mac-server set allowed-interface-list=all')
        command('/tool mac-server mac-winbox set allowed-interface-list=all')
        command('/ip neighbor discovery-settings set discover-interface-list=all')

        # Remove port with bridge
        command('/interface bridge port remove [find interface=ether' + count_ether + ']')

        # Firewall
        count = int(command('/ip firewall filter print count-only'))
        command((':for x from 1 to ' + str(count) + ' do={/ip firewall filter remove numbers=$x}'))

        # WIFI
        count_wifi = int(command('/interface wireless print count-only'))
        for i in range(count_wifi):
            command(('interface wireless set ssid="' + ssid + '" numbers=' + str(i)))
            command(('interface wireless security-profiles set numbers=' + str(i) +
                     ' mode=dynamic-keys authentication-types=wpa-psk,wpa2-psk'
                     ' wpa-pre-shared-key=' + password + ' wpa2-pre-shared-key=' + password))

        # Move port to bridge
        command('interface bridge port add interface=ether' + count_ether + ' bridge=bridge;'
                ' ip address set interface=bridge numbers=0')

        # IP service
        command('/ip service disable [find name=api]')
        command('/ip service disable [find name=ftp]')
        command('/ip service disable [find name=api-ssl]')
        command('/ip service set [find name=ssh] port=44522')
        command('/ip service set [find name=telnet] port=44523')
        command('/ip service set [find name=www] port=8111')

        # Change user password
        command('/user set [find name=admin] password=' + str(password2))
        ui.pushButton_2.setStyleSheet("background-color: rgb(196, 223, 208); font-weight: bold")
        ui.pushButton_2.setText('Настроено! / Очистить')
    else:
        ui.lineEdit.setStyleSheet("border: 2px solid rgb(170, 0, 0)")
        ui.lineEdit_3.setStyleSheet("border: 2px solid rgb(170, 0, 0)")
    client.close()


# SSH подключение / получение модели устройства
def connect():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=login, password='\r')
    # model
    client.exec_command('yes\r')
    client.exec_command('yes\r')

    stdin, stdout, stderr = client.exec_command('put [/system routerboard get model]', 2)
    model = stdout.read().decode("UTF-8")
    if model.split(' ')[0] != 'expected':
        ui.lineEdit_4.setText(model)
        ui.lineEdit_4.setStyleSheet("color: green")
        ui.pushButton.setStyleSheet("background-color: rgb(196, 223, 208); font-weight: bold")
        ui.pushButton.setText('Подключено!')
    else:
        ui.lineEdit_4.setText('Сбой')
        ui.lineEdit_4.setStyleSheet("color: red")
    client.close()


# Очистить поля для дальнейшего использования
def clear():
    ui.lineEdit_4.setText('')
    ui.lineEdit.setText('APEX')
    ui.lineEdit.setStyleSheet("border: 1px solid rgb(235, 235, 235);")
    ui.lineEdit_3.setStyleSheet("border: 1px solid rgb(235, 235, 235);")
    ui.lineEdit_3.setText('')
    ui.lineEdit_5.setText('')
    ui.pushButton.setText('Подключиться')
    ui.pushButton_2.setText('Настроить')
    ui.pushButton.setStyleSheet("QPushButton::hover{background-color: rgb(192, 225, 255);}\n"
                                "QPushButton{ background-color: rgb(230, 241, 255);"
                                " border-radius: 5px; border: 1px solid rgb(190, 220, 255)}")
    ui.pushButton_2.setStyleSheet("QPushButton::hover{background-color: rgb(192, 225, 255);}\n"
                                  "QPushButton{ background-color: rgb(230, 241, 255);"
                                  " border-radius: 5px; border: 1px solid rgb(190, 220, 255)}")


# Обработчик события нажатия на клавишу
ui.lineEdit.setText('APEX')
ui.pushButton.clicked.connect(connect)
ui.pushButton_2.clicked.connect(bp)


# Run main loop
sys.exit(app.exec_())