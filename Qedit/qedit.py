#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Thanks to the ZetCode PyQt5 tutorial by Jan Bodnar at zetcode.com

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
"""

import sys
import os
from PyQt5.QtWidgets import (QMainWindow, 
	QAction, QFileDialog, QApplication, QTextEdit)
from PyQt5.QtGui import QIcon


class main(QMainWindow):
	
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
		self.curFile = ''
		self.openedFile = False
		
		
	def initUI(self):	   

		self.statusBar()
		
		self.textEdit = QTextEdit()
		self.setCentralWidget(self.textEdit)
		self.textEdit.setText('Start writing in this buffer and hit save to make a new document')
		
		openFile = QAction(QIcon('resources/open.png'), 'Open', self)
		openFile.setShortcut('Ctrl+O')
		openFile.setStatusTip('Open File')
		openFile.triggered.connect(self.openDialog)
		
		
		#exit button
		exitProgram = QAction(QIcon('resources/exit.png'), 'Exit', self)
		exitProgram.setShortcut('Alt+F4')
		exitProgram.setStatusTip('Exit the program')
		exitProgram.triggered.connect(self.exitButton)
		
		saveFile = QAction(QIcon('resources/save.png'), 'Save', self)
		saveFile.setShortcut('Ctrl+S')
		saveFile.setStatusTip('Save file')
		saveFile.triggered.connect(self.saveDialog)

		#add buttons to file menu
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(openFile)
		fileMenu.addAction(exitProgram)
		fileMenu.addAction(saveFile)
		
		#configure window
		self.setGeometry(300, 300, 640, 480)
		self.setWindowIcon(QIcon('resources/icon.png'))
		self.setWindowTitle('Qedit')
		self.show()
		
	
	#compression dialog
	def openDialog(self):

		fname = QFileDialog.getOpenFileName(self, 'Open File', '/home')
		
		if fname[0]:
			
			self.curFile = fname[0]
			self.openedFile = True
			
			f = open(fname[0], 'r+')

			with f:
				data = f.read()
				self.textEdit.setText(data)	
				
	def saveDialog(self):
	
		if self.openedFile:
			
			f = open(self.curFile, 'r+')
		
			with f:
				f.write(self.textEdit.toPlainText())
		else:
			fname = QFileDialog.getSaveFileName(self, 'Save File', '/home')
			
			if fname[0]:
				f = open(fname[0], 'w')
				
				with f:
					f.write(self.textEdit.toPlainText())
				

	#exit button
	def exitButton(self):
		sys.exit()
		
		
if __name__ == '__main__':
	#run app
	app = QApplication(sys.argv)
	ex = main()
	sys.exit(app.exec_())