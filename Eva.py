import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from firstmenu import Ui_MainWindow

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_4.clicked.connect(lambda: self.change_page(1))
        self.pushButton_5.clicked.connect(lambda: self.close())
        self.pushButton_6.clicked.connect(lambda: self.change_page(0))
        self.pushButton_3.clicked.connect(lambda: self.change_page(2))
        self.pushButton_7.clicked.connect(lambda: self.change_page(0))
        self.comboBox.currentTextChanged.connect(self.on_selection_changed)

    def change_page(self, index):
        self.stackedWidget.setCurrentIndex(index)



    def keyPressEvent(self, event):
        k = event.key()
        if k == Qt.Key_Escape:
            if self.stackedWidget.currentIndex() == 0:
                self.change_page(1)
            elif self.stackedWidget.currentIndex() == 2:
                self.change_page(0)
            elif self.stackedWidget.currentIndex() == 1:
                self.change_page(0)


    def on_selection_changed(self):
        if self.comboBox.currentText() in ['ქართული', 'Georgian']:
            self.label_4.setText('ენა')
            self.label_3.setText('გრაფიკა')
            self.label_5.setText('სირთულე')
            self.label_6.setText('სუბტიტრები')
            self.pushButton_7.setText('მთავარ მენიუში დაბრუნება')
            self.comboBox.setItemText(1, 'ქართული')
            self.comboBox.setItemText(0, 'ინგლისური')
            self.comboBox_2.setItemText(0, 'დაბალი')
            self.comboBox_2.setItemText(1, 'საშუალო')
            self.comboBox_2.setItemText(2, 'მაღალი')
            self.comboBox_3.setItemText(0, 'დამწყები')
            self.comboBox_3.setItemText(1, 'საშუალო')
            self.comboBox_3.setItemText(2, 'რთული')
            self.checkBox_2.setText('ჩართული')
            self.label_2.setText('ნამდვილად გსურთ გათიშვა?')
            self.pushButton_5.setText('დიახ')
            self.pushButton_6.setText('გაუქმება')
            self.checkBox.setText('მუსიკა')
            self.label.setText('ევანგელიონი')
            self.pushButton.setText('თამაშის დაწყება')
            self.pushButton_2.setText('პერსონაჟები')
            self.pushButton_3.setText('პარამეტრები')
            self.pushButton_4.setText('გათიშვა')
        elif self.comboBox.currentText() in ['ინგლისური', 'English']:
            self.label_4.setText('Language')
            self.label_3.setText('Graphics')
            self.label_5.setText('Difficulty')
            self.label_6.setText('Subtitles')
            self.pushButton_7.setText('Quit to Main Menu')
            self.comboBox.setItemText(1, 'Georgian')
            self.comboBox.setItemText(0, 'English')
            self.comboBox_2.setItemText(0, 'Low')
            self.comboBox_2.setItemText(1, 'Normal')
            self.comboBox_2.setItemText(2, 'High')
            self.comboBox_3.setItemText(0, 'Begginer')
            self.comboBox_3.setItemText(1, 'Regular')
            self.comboBox_3.setItemText(2, 'Hardened')
            self.checkBox_2.setText('On')
            self.label_2.setText('Are you sure you want to quit?')
            self.pushButton_5.setText('Yes')
            self.pushButton_6.setText('Cancel')
            self.checkBox.setText('Music')
            self.label.setText('Evangelion')
            self.pushButton.setText('Play Game')
            self.pushButton_2.setText('Characters')
            self.pushButton_3.setText('Settings')
            self.pushButton_4.setText('Quit')

app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())