'''
Created on 2018年8月23日
可视界面
@author: woshiuu
'''
import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QApplication)
from PyQt5.QtCore import QCoreApplication
from wbspider.WeiboCrawler import Weibocrawler
from wbspider.analysis import analysis

result = ""
class FirstWindow(QWidget):
     
    def __init__(self):
        super(FirstWindow,self).__init__()
         
        self.initUI()
         
         
    def initUI(self):     
        
        lbl1 = QLabel('输入用户ID：')        
        lbl2 = QLabel('输入Cookie：')
        lbl3 = QLabel('数据分析：')
        
        self.lineEdit = QLineEdit()       
        self.textEdit1 = QTextEdit()
        self.textEdit2 = QTextEdit()
        
        okButton = QPushButton("获取数据并分析")
        okButton.clicked.connect(self.getInformation)
        cancelButton = QPushButton("取消")
        cancelButton.clicked.connect(QCoreApplication.instance().quit)
        
        grid = QGridLayout()
        grid.setSpacing(10)
        
        grid.addWidget(lbl1, 1, 0)
        grid.addWidget(self.lineEdit, 1, 1)
        
        grid.addWidget(lbl2, 2, 0)
        grid.addWidget(self.textEdit1, 2, 1, 3, 1)
        
        grid.addWidget(lbl3, 1, 2)
        grid.addWidget(self.textEdit2, 2, 2, 3, 2)
        
        grid.addWidget(cancelButton, 5, 0)
        grid.addWidget(okButton, 5, 1)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('用户信息获取')
        
         
    def getInformation(self):
         
        UserID = int(self.lineEdit.text())
        myCookie = self.textEdit1.toPlainText()
        
        text = Weibocrawler(UserID, myCookie)
        result = analysis(text)
        print('%s' % result)
        
        self.textEdit2.setText(result)
#         print('UserID:%s Cookie:%s ' % (UserID, myCookie))
                          
if __name__ == '__main__':

    app = QApplication(sys.argv)
    fir = FirstWindow()
    fir.show()
    sys.exit(app.exec_())