from PyQt6.QtWidgets import *
import random


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.line1 = QLineEdit(self)
        self.line1.setPlaceholderText('Введите символы: ')
        self.line2 = QLineEdit()
        self.line2.setPlaceholderText('Введите количество символов: ')
        btn = QPushButton('Сгенерировать')

        main_l = QVBoxLayout()
        main_l.addWidget(self.line1)
        main_l.addWidget(self.line2)
        main_l.addWidget(btn)
        self.setLayout(main_l)

        btn.clicked.connect(self.generate)

    def initUI(self):
        self.setWindowTitle('Генератор паролей')

    def generate(self):
        message = QMessageBox()
        message.setWindowTitle('Пароль')

        symbols = list(self.line1.text())  # преобразование строки в список
        number_of_symbols = len(symbols)  # подсчёт количества символов в списке
        password_lenth = int(self.line2.text())
        random.shuffle(symbols)  # перемешивание элементов списка
        del symbols[0:number_of_symbols - password_lenth]  # удаление элементов списка
        password = ''
        for i in symbols:  # цикл, используемый для преобразования каждого элемента списка в одну строку
            password += str(i)
        if password_lenth <= number_of_symbols:
            message.setText(f'Ваш пароль: {password}')
        else:
            message.setText(f'Длинна пароля больше количества символов!')
        message.exec()


def main():
    app = QApplication([])
    win = MainWin()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()
