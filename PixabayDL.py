import sys
import os
import subprocess
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QGroupBox, QPlainTextEdit, QToolButton, QFrame, QDesktopWidget, 
                             QCheckBox, QMessageBox, QFileDialog, QComboBox, QLineEdit)
from PyQt5.QtCore import Qt, QPoint, QRect, QDateTime, QTimer, QDate, QProcess
from PyQt5.QtGui import QFont, QCursor, QIntValidator
from PyQt5 import QtCore, QtGui, QtWidgets

class Form(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(0, 0, 779, 580)
        self.center()
        self.setWindowTitle("Form")
        self.setStyleSheet("background-color: rgb(0, 171, 107);")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        self.btnLogs = QPushButton("O", self)
        self.btnLogs.setGeometry(630, 20, 21, 21)
        self.btnLogs.setFont(QFont("MS PGothic", 12))
        self.btnLogs.setCursor(Qt.PointingHandCursor)
        self.btnLogs.setStyleSheet("color: rgb(255, 255, 255); font: 12pt 'MS PGothic'; background-color: rgb(0, 171, 107);")
        self.btnLogs.clicked.connect(self.showLogs)

        self.btnInfo = QPushButton("?", self)
        self.btnInfo.setGeometry(670, 20, 21, 21)
        self.btnInfo.setFont(QFont("MS PGothic", 12))
        self.btnInfo.setCursor(Qt.PointingHandCursor)
        self.btnInfo.setStyleSheet("color: rgb(255, 255, 255); font: 12pt 'MS PGothic'; background-color: rgb(0, 171, 107);")
        self.btnInfo.clicked.connect(self.showInfo)

        self.btnMinimize = QPushButton("-", self)
        self.btnMinimize.setGeometry(710, 20, 21, 21)
        self.btnMinimize.setFont(QFont("MS PGothic", 12))
        self.btnMinimize.setCursor(Qt.PointingHandCursor)
        self.btnMinimize.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(0, 171, 107); font: 12pt 'MS PGothic';")
        self.btnMinimize.clicked.connect(self.showMinimized)
        
        self.btnClose = QPushButton("X", self)
        self.btnClose.setGeometry(750, 20, 21, 21)
        self.btnClose.setFont(QFont("MS PGothic", 12))
        self.btnClose.setCursor(Qt.PointingHandCursor)
        self.btnClose.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(0, 171, 107); font: 12pt 'MS PGothic';")
        self.btnClose.clicked.connect(self.confirmClose)
        
        self.lbTitle = QLabel(self)
        self.lbTitle.setGeometry(10, 0, 291, 61)
        self.lbTitle.setLayoutDirection(Qt.LeftToRight)
        self.lbTitle.setStyleSheet("font: 18pt 'Khmer OS Muol Light';")
        self.lbTitle.setText("<html><head/><body><p><span style=' font-size:14pt; font-weight:600; color:#ffffff;'>កម្មវិធីទាញយក Pixabay</span></p></body></html>")
        self.lbTitle.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        
        self.gbMain = QGroupBox(self)
        self.gbMain.setGeometry(10, 60, 761, 361)
        self.gbMain.setFont(QFont('', 10))
        self.gbMain.setLayoutDirection(Qt.LeftToRight)
        self.gbMain.setStyleSheet("color: rgb(255, 255, 255);")
        
        self.lbKeyDown = QLabel(self.gbMain)
        self.lbKeyDown.setGeometry(10, 5, 181, 31)
        self.lbKeyDown.setLayoutDirection(Qt.RightToLeft)
        self.lbKeyDown.setText("<html><head/><body><p><span style=' font-size:12pt; font-weight:600; color:#ffffff;'>Keyword Download</span></p></body></html>")
        self.lbKeyDown.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        
        self.txtLinkKeywordDownload = QPlainTextEdit(self.gbMain)
        self.txtLinkKeywordDownload.setGeometry(10, 40, 741, 151)
        self.txtLinkKeywordDownload.setFont(QFont("Roboto", 11))
        self.txtLinkKeywordDownload.setCursor(Qt.IBeamCursor)
        self.txtLinkKeywordDownload.setToolTipDuration(0)
        self.txtLinkKeywordDownload.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.txtLinkKeywordDownload.setPlaceholderText("Ex. cat, dog, home, ...")
        self.txtLinkKeywordDownload.setFrameShape(QFrame.WinPanel)
        
        self.gbDownload = QGroupBox("Option | Phekdey | V.1", self.gbMain)
        self.gbDownload.setGeometry(10, 200, 741, 151)
        self.gbDownload.setFont(QFont('', 8))
        self.gbDownload.setLayoutDirection(Qt.LeftToRight)
        self.gbDownload.setStyleSheet("color: rgb(255, 255, 255);")
        self.gbDownload.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        
        self.lbPath = QLabel(self.gbDownload)
        self.lbPath.setGeometry(10, 20, 61, 31)
        self.lbPath.setLayoutDirection(Qt.RightToLeft)
        self.lbPath.setText("<html><head/><body><p><span style=' font-weight:600; color:#ffffff;'>Save Path</span></p></body></html>")
        self.lbPath.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        
        self.txtPathSave = QPlainTextEdit(self.gbDownload)
        self.txtPathSave.setGeometry(80, 21, 481, 71)
        self.txtPathSave.setFont(QFont("Roboto", 9))
        self.txtPathSave.setCursor(Qt.IBeamCursor)
        self.txtPathSave.setToolTipDuration(0)
        self.txtPathSave.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.txtPathSave.textChanged.connect(self.check_path)
        
        self.btnBrowsePath = QToolButton(self.gbDownload)
        self.btnBrowsePath.setGeometry(10, 50, 61, 31)
        self.btnBrowsePath.setCursor(Qt.PointingHandCursor)
        self.btnBrowsePath.setText("...")
        self.btnBrowsePath.clicked.connect(self.browse_directory)
        
        self.lineSave = QFrame(self.gbDownload)
        self.lineSave.setGeometry(80, 90, 651, 20)
        self.lineSave.setFrameShape(QFrame.HLine)
        
        self.btnDownload = QToolButton(self.gbDownload)
        self.btnDownload.setGeometry(630, 110, 101, 31)
        self.btnDownload.setCursor(Qt.PointingHandCursor)
        self.btnDownload.setStyleSheet("color: rgb(255, 255, 255);")
        self.btnDownload.setFont(QFont("Roboto", 11))
        self.btnDownload.setText("Download")
        
        self.btnStop = QToolButton(self.gbDownload)
        self.btnStop.setGeometry(520, 110, 101, 31)
        self.btnStop.setCursor(Qt.PointingHandCursor)
        self.btnStop.setStyleSheet("color: rgb(255, 255, 0);")
        self.btnStop.setFont(QFont("Roboto", 11))
        self.btnStop.setText("Stop")
        
        self.btnClear = QToolButton(self.gbDownload)
        self.btnClear.setGeometry(80, 110, 101, 31)
        self.btnClear.setCursor(Qt.PointingHandCursor)
        self.btnClear.setStyleSheet("color: rgb(170, 0, 0);")
        self.btnClear.setText("Clear")
        self.btnClear.setFont(QFont("Roboto", 11))
        self.btnClear.clicked.connect(self.clear_code)
        
        self.lbAmount = QLabel(self.gbDownload)
        self.lbAmount.setGeometry(590, 20, 61, 31)
        self.lbAmount.setLayoutDirection(Qt.RightToLeft)
        self.lbAmount.setText("<html><head/><body><p><span style=' font-weight:600; color:#ffffff;'>Amount</span></p></body></html>")
        self.lbAmount.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        
        # self.txtAmountNum = QPlainTextEdit(self.gbDownload)
        # self.txtAmountNum.setGeometry(650, 20, 81, 31)
        # self.txtAmountNum.setFont(QFont("Roboto", 9))
        # self.txtAmountNum.setCursor(Qt.IBeamCursor)
        # self.txtAmountNum.setToolTipDuration(0)
        # self.txtAmountNum.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")

        self.txtAmountNum = QLineEdit(self.gbDownload)
        self.txtAmountNum.setGeometry(650, 20, 81, 31)
        self.txtAmountNum.setFont(QFont("Roboto", 9))
        self.txtAmountNum.setCursor(Qt.IBeamCursor)
        self.txtAmountNum.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.txtAmountNum.setValidator(QIntValidator(0, 9999, self))
        self.txtAmountNum.textChanged.connect(self.validate_amount)
        
        self.lbDelay = QLabel(self.gbDownload)
        self.lbDelay.setGeometry(590, 60, 61, 31)
        self.lbDelay.setLayoutDirection(Qt.RightToLeft)
        self.lbDelay.setText("<html><head/><body><p><span style=' font-weight:600; color:#ffffff;'>Delay (s)</span></p></body></html>")
        self.lbDelay.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        
        # self.txtDelayNum = QPlainTextEdit(self.gbDownload)
        # self.txtDelayNum.setGeometry(650, 60, 81, 31)
        # self.txtDelayNum.setFont(QFont("Roboto", 9))
        # self.txtDelayNum.setCursor(Qt.IBeamCursor)
        # self.txtDelayNum.setToolTipDuration(0)
        # self.txtDelayNum.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")

        self.txtDelayNum = QComboBox(self.gbDownload)
        self.txtDelayNum.setGeometry(650, 60, 81, 31)
        self.txtDelayNum.setFont(QFont("Roboto", 9))
        self.txtDelayNum.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.txtDelayNum.setCursor(Qt.PointingHandCursor)
        self.txtDelayNum.addItems(["1", "5", "10", "15", "20", "25", "30"])
        self.txtDelayNum.setCurrentIndex(2)
        
        self.txtLogsConsole = QPlainTextEdit(self)
        self.txtLogsConsole.setGeometry(10, 430, 761, 141)
        self.txtLogsConsole.setFont(QFont("Roboto", 10))
        self.txtLogsConsole.setCursor(Qt.IBeamCursor)
        self.txtLogsConsole.setToolTipDuration(0)
        self.txtLogsConsole.setStyleSheet("background-color: rgb(36, 36, 36); color: rgb(255, 255, 255);")
        self.txtLogsConsole.setFrameShape(QFrame.WinPanel)
        
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.globalPos()
            self.mouse_drag_active = True

    def mouseMoveEvent(self, event):
        if self.mouse_drag_active and event.buttons() == Qt.LeftButton:
            delta = event.globalPos() - self.drag_start_position
            self.move(self.pos() + delta)
            self.drag_start_position = event.globalPos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_drag_active = False

    def confirmClose(self):
        message_box = QtWidgets.QMessageBox()
        message_box.setIcon(QtWidgets.QMessageBox.Question)
        message_box.setWindowTitle('បញ្ជាក់ការបិទ')
        message_box.setText('តើអ្នកពិតជាចង់បិទចោលកម្មវិធីមែនឬទេ?')

        yes_button = message_box.addButton('យល់ព្រម', QtWidgets.QMessageBox.YesRole)
        yes_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        no_button = message_box.addButton('បដិសេដ', QtWidgets.QMessageBox.NoRole)
        no_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        message_box.setDefaultButton(no_button)

        reply = message_box.exec_()

        if message_box.clickedButton() == yes_button:
            QtCore.QCoreApplication.instance().quit()

    def showInfo(self):
        info_text = """
        <html>
            <body style='font-size: 10pt; color: white; background-color: gray;'>
                <h1>Owner Info</h1>
                <hr>
                <p>កម្មវិធីឈ្មោះ: Pixaby Downloader</p>
                <p>សរសេរដោយ: Phekdey PHORN | ផន ភក្ដី</p>
                <p>ទំនាក់ទំនង: 089 755 770</p>
                <p>ភាសាកូដៈ Python</p>
                <p>បង្កើតថ្ងៃៈ 24-April-2024</p>
                <p>បច្ចុប្បន្នភាពចុងក្រោយៈ 06-Auguest-2024</p>
                <p>ការប្រើប្រាស់ៈ Free</p>
                <p>កំណែទម្រង់ៈ 1.0</p>
                <br>
                <h1>User Info</h1>
                <hr>
                <p>Machine ID: {current}</p>
                <p>License Key: {current}</p>
                <p>Create Key: {current}</p>
                <p>Expiry Key: {current}</p>
            </body>
        </html>
        """
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Info")
        msg_box.setText(info_text)
        msg_box.setStyleSheet("QLabel{min-width: 600px;}")
        return_button = msg_box.addButton("ត្រលប់", QMessageBox.AcceptRole)
        return_button.setStyleSheet("color: white;")
        return_button.setCursor(Qt.PointingHandCursor)
        msg_box.exec_()
        return_button.clicked.connect(msg_box.close)

    def browse_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.txtPathSave.setPlainText(directory)
    def check_path(self):
        path = self.txtPathSave.toPlainText().strip()
        if path and not os.path.isdir(path):
            warning_box = QMessageBox(self)
            warning_box.setWindowTitle('ទីតាំងមិនត្រឹមត្រូវ')
            warning_box.setText('សូមជ្រើសរើសទីតាំងដែលមានសុពលភាព ឬ ត្រឹមត្រូវ !')
            warning_box.setStyleSheet("""
                QLabel { color: white; }
                QPushButton { color: white; background-color: rgb(50, 50, 50); }
            """)
            warning_box.setStandardButtons(QMessageBox.Ok)
            warning_box.button(QMessageBox.Ok).setText('យល់ព្រម')
            warning_box.button(QMessageBox.Ok).setCursor(Qt.PointingHandCursor)
            warning_box.exec_()
            self.txtPathSave.clear()

    def validate_amount(self):
        text = self.txtAmountNum.text()
        if text and not text.isdigit():
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number.")
            self.txtAmountNum.clear()

    def clear_code(self):
        linkKeywordDownload = self.txtLinkKeywordDownload.toPlainText().strip()
        pathSave = self.txtPathSave.toPlainText().strip()
        amountNum = self.txtAmountNum.text().strip()
        
        if not linkKeywordDownload and not pathSave and not amountNum:
            warning_box = QMessageBox(self)
            warning_box.setWindowTitle('ការព្រមាន')
            warning_box.setText('មិនមានទិន្នន័យទេ!')
            warning_box.setStyleSheet("""
                QLabel { color: white; }
                QPushButton { color: white; background-color: rgb(50, 50, 50); }
            """)
            warning_box.setStandardButtons(QMessageBox.Ok)
            warning_box.button(QMessageBox.Ok).setText('យល់ព្រម')
            warning_box.button(QMessageBox.Ok).setCursor(Qt.PointingHandCursor)
            warning_box.exec_()
        elif linkKeywordDownload or pathSave or amountNum:
            confirmation_box = QMessageBox(self)
            confirmation_box.setWindowTitle('បញ្ជាក់ការសម្អាត')
            confirmation_box.setText('តើអ្នកពិតជាចង់សម្អាតទម្រង់វាចោលមែនទេ?')
            confirmation_box.setStyleSheet("""
                QLabel { color: white; }
                QPushButton { color: white; background-color: rgb(50, 50, 50); }
            """)
            confirmation_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            confirmation_box.button(QMessageBox.Yes).setText('យល់ព្រម')
            confirmation_box.button(QMessageBox.Yes).setCursor(Qt.PointingHandCursor)
            confirmation_box.button(QMessageBox.No).setText('បដិសេដ')
            confirmation_box.button(QMessageBox.No).setCursor(Qt.PointingHandCursor)
            
            reply = confirmation_box.exec_()
            if reply == QMessageBox.Yes:
                self.txtLinkKeywordDownload.clear()
                self.txtPathSave.clear()
                self.txtAmountNum.clear()
                self.txtDelayNum.setCurrentIndex(1)
                self.txtLogsConsole.clear()

    def showLogs(self):
        confirmation_box = QMessageBox(self)
        confirmation_box.setWindowTitle('បញ្ជាក់ការបើកមើល log')
        confirmation_box.setText('តើអ្នកពិតជាចង់មើល log មែនទេ?')
        confirmation_box.setStyleSheet("""
            QLabel { color: white; }
            QPushButton { color: white; background-color: rgb(50, 50, 50); }
        """)
        confirmation_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirmation_box.button(QMessageBox.Yes).setText('យល់ព្រម')
        confirmation_box.button(QMessageBox.Yes).setCursor(Qt.PointingHandCursor)
        confirmation_box.button(QMessageBox.No).setText('បដិសេដ')
        confirmation_box.button(QMessageBox.No).setCursor(Qt.PointingHandCursor)
        reply = confirmation_box.exec_()

        if reply == QMessageBox.Yes:
            log_dir = r"C:\Tools Data\Pixabay DL Logs"
            if os.path.exists(log_dir):
                try:
                    # Open the directory in file explorer
                    if os.name == 'nt':  # For Windows
                        os.startfile(log_dir)
                    elif os.name == 'posix':  # For Unix-like OS
                        subprocess.call(['xdg-open', log_dir])
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Unable to open log directory: {e}")
            else:
                QMessageBox.warning(self, "Path Not Found", "Log directory does not exist.")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    sys.exit(app.exec_())



