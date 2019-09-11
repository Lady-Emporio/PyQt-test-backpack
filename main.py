#SET PATH=%PATH%;C:\Users\Иванова\Desktop\НУЖНОЕ\1\We\source\p\fd\fd\myq
#python main.py

from PyQt5.QtWidgets import (QMainWindow,QWidget,QHBoxLayout,QVBoxLayout,
QListView,QLabel,QPushButton,QGraphicsView,
QSpinBox)
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication,QLayout,QStyle
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGraphicsScene,QGraphicsEllipseItem,QGraphicsLineItem,QListWidget ,QSizePolicy , QGraphicsRectItem,QListWidgetItem
from PyQt5.QtCore import QTimer,Qt,QMimeData
from PyQt5.QtGui import QColor,QBrush,QPen,QTransform ,QPixmap,QCursor,QIcon

class Cell(QGraphicsRectItem):
	def __init__(self,row,col):
		QGraphicsRectItem.__init__(self)
		self.row=row
		self.col=col
		self.setRect(0, 0, 20, 20)
		
		self.setBrush(QColor(0,128,0))
		
		self.setX(self.row*20)
		self.setY(self.col*20)
		
class Scene(QGraphicsScene):
	def __init__(self):
		QGraphicsScene.__init__(self)
		self.table=[]
		self.createTable()
		self.isClickLeftButtonMouse=False;
		self.cell=None
		
	def createTable(self):
		for row in range(5):
			colArray=[]
			for col in range(4):
				cell=Cell(row,col)
				colArray.append(cell)
				self.addItem(cell)
		self.table.append(colArray)
		
	def mousePressEvent(self, event):
		self.isClickLeftButtonMouse=True;
	def mouseReleaseEvent(self,event):
		self.isClickLeftButtonMouse=False;
		x=event.scenePos().x()
		y=event.scenePos().y()
		row=int(x/20)
		col=int(y/20)
		self.cell.setX(row*20)
		self.cell.setY(col*20)
	def mouseMoveEvent(self,event):
		if not self.isClickLeftButtonMouse:
			return;
		x=event.scenePos().x();
		y=event.scenePos().y();
		self.cell.setX(x)
		self.cell.setY(y)
class MainWindow(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle("Table true")
	
		mainLayout=QHBoxLayout(self)
		rightLayout=QVBoxLayout()
		rightLayout.setAlignment(Qt.AlignTop)
		runButton=QPushButton("run")
		rightLayout.addWidget(runButton)
		
		self.view=QGraphicsView()
		self.scene=Scene()
		self.view.setScene(self.scene)
		self.view.setMouseTracking(True)
		
		mainLayout.addWidget(self.view)
		mainLayout.addLayout(rightLayout)
		
		self.cell=Cell(1,2)
		self.cell.setBrush(QColor(255,0,0))
		#self.cell.setZValue(2)
		self.scene.addItem(self.cell)
		self.scene.cell=self.cell;
		

app = QApplication([])
livePleaseDontDelete=MainWindow()
livePleaseDontDelete.show()
app.exec_()