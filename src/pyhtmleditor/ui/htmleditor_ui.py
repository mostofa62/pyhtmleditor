# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'htmleditor.ui'
#
# Created: Fri Jan 27 12:40:04 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(659, 398)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.webView = QtWebKit.QWebView(self.tab)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout_2.addWidget(self.webView)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.tab_2)
        self.plainTextEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 659, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName(_fromUtf8("menu_Edit"))
        self.menuF_ormat = QtGui.QMenu(self.menubar)
        self.menuF_ormat.setObjectName(_fromUtf8("menuF_ormat"))
        self.menuSt_yle = QtGui.QMenu(self.menuF_ormat)
        self.menuSt_yle.setObjectName(_fromUtf8("menuSt_yle"))
        self.menu_Align = QtGui.QMenu(self.menuF_ormat)
        self.menu_Align.setObjectName(_fromUtf8("menu_Align"))
        MainWindow.setMenuBar(self.menubar)
        self.standardToolBar = QtGui.QToolBar(MainWindow)
        self.standardToolBar.setObjectName(_fromUtf8("standardToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.standardToolBar)
        self.formatToolBar = QtGui.QToolBar(MainWindow)
        self.formatToolBar.setObjectName(_fromUtf8("formatToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.formatToolBar)
        MainWindow.insertToolBarBreak(self.formatToolBar)
        self.actionFileNew = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/document-new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFileNew.setIcon(icon)
        self.actionFileNew.setObjectName(_fromUtf8("actionFileNew"))
        self.actionFileOpen = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/document-open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFileOpen.setIcon(icon1)
        self.actionFileOpen.setObjectName(_fromUtf8("actionFileOpen"))
        self.actionFileSave = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/document-save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFileSave.setIcon(icon2)
        self.actionFileSave.setObjectName(_fromUtf8("actionFileSave"))
        self.actionFileSaveAs = QtGui.QAction(MainWindow)
        self.actionFileSaveAs.setObjectName(_fromUtf8("actionFileSaveAs"))
        self.actionEditUndo = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/edit-undo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEditUndo.setIcon(icon3)
        self.actionEditUndo.setObjectName(_fromUtf8("actionEditUndo"))
        self.actionEditRedo = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/edit-redo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEditRedo.setIcon(icon4)
        self.actionEditRedo.setObjectName(_fromUtf8("actionEditRedo"))
        self.actionEditCut = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/edit-cut.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEditCut.setIcon(icon5)
        self.actionEditCut.setObjectName(_fromUtf8("actionEditCut"))
        self.actionEditCopy = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/edit-copy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEditCopy.setIcon(icon6)
        self.actionEditCopy.setObjectName(_fromUtf8("actionEditCopy"))
        self.actionEditPaste = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/edit-paste.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEditPaste.setIcon(icon7)
        self.actionEditPaste.setObjectName(_fromUtf8("actionEditPaste"))
        self.actionEditSelectAll = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/edit-select-all.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEditSelectAll.setIcon(icon8)
        self.actionEditSelectAll.setObjectName(_fromUtf8("actionEditSelectAll"))
        self.actionFormatBold = QtGui.QAction(MainWindow)
        self.actionFormatBold.setCheckable(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/format-text-bold.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFormatBold.setIcon(icon9)
        self.actionFormatBold.setObjectName(_fromUtf8("actionFormatBold"))
        self.actionFormatItalic = QtGui.QAction(MainWindow)
        self.actionFormatItalic.setCheckable(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/format-text-italic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFormatItalic.setIcon(icon10)
        self.actionFormatItalic.setObjectName(_fromUtf8("actionFormatItalic"))
        self.actionFormatUnderline = QtGui.QAction(MainWindow)
        self.actionFormatUnderline.setCheckable(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/format-text-underline.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFormatUnderline.setIcon(icon11)
        self.actionFormatUnderline.setObjectName(_fromUtf8("actionFormatUnderline"))
        self.actionFormatStrikethrough = QtGui.QAction(MainWindow)
        self.actionFormatStrikethrough.setCheckable(True)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/format-text-strikethrough.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFormatStrikethrough.setIcon(icon12)
        self.actionFormatStrikethrough.setObjectName(_fromUtf8("actionFormatStrikethrough"))
        self.actionFormatAlignLeft = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/format-justify-left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFormatAlignLeft.setIcon(icon13)
        self.actionFormatAlignLeft.setObjectName(_fromUtf8("actionFormatAlignLeft"))
        self.actionFormatAlignCenter = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/format-justify-center.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFormatAlignCenter.setIcon(icon14)
        self.actionFormatAlignCenter.setObjectName(_fromUtf8("actionFormatAlignCenter"))
        self.actionFormatAlignRight = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/format-justify-right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFormatAlignRight.setIcon(icon15)
        self.actionFormatAlignRight.setObjectName(_fromUtf8("actionFormatAlignRight"))
        self.actionFormatAlignJustify = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/format-justify-fill.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFormatAlignJustify.setIcon(icon16)
        self.actionFormatAlignJustify.setObjectName(_fromUtf8("actionFormatAlignJustify"))
        self.actionFormatIncreaseIndent = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/format-indent-more.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFormatIncreaseIndent.setIcon(icon17)
        self.actionFormatIncreaseIndent.setObjectName(_fromUtf8("actionFormatIncreaseIndent"))
        self.actionFormatDecreaseIndent = QtGui.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/format-indent-less.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFormatDecreaseIndent.setIcon(icon18)
        self.actionFormatDecreaseIndent.setObjectName(_fromUtf8("actionFormatDecreaseIndent"))
        self.actionFormatBulletedList = QtGui.QAction(MainWindow)
        self.actionFormatBulletedList.setCheckable(True)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/bulleted-list.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFormatBulletedList.setIcon(icon19)
        self.actionFormatBulletedList.setObjectName(_fromUtf8("actionFormatBulletedList"))
        self.actionFormatNumberedList = QtGui.QAction(MainWindow)
        self.actionFormatNumberedList.setCheckable(True)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/numbered-list.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFormatNumberedList.setIcon(icon20)
        self.actionFormatNumberedList.setObjectName(_fromUtf8("actionFormatNumberedList"))
        self.actionInsertImage = QtGui.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/image-x-generic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInsertImage.setIcon(icon21)
        self.actionInsertImage.setObjectName(_fromUtf8("actionInsertImage"))
        self.actionCreateLink = QtGui.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/text-html.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreateLink.setIcon(icon22)
        self.actionCreateLink.setObjectName(_fromUtf8("actionCreateLink"))
        self.actionZoomOut = QtGui.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/list-remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomOut.setIcon(icon23)
        self.actionZoomOut.setObjectName(_fromUtf8("actionZoomOut"))
        self.actionZoomIn = QtGui.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/list-add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomIn.setIcon(icon24)
        self.actionZoomIn.setObjectName(_fromUtf8("actionZoomIn"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionStyleParagraph = QtGui.QAction(MainWindow)
        self.actionStyleParagraph.setObjectName(_fromUtf8("actionStyleParagraph"))
        self.actionStyleHeading1 = QtGui.QAction(MainWindow)
        self.actionStyleHeading1.setObjectName(_fromUtf8("actionStyleHeading1"))
        self.actionStyleHeading2 = QtGui.QAction(MainWindow)
        self.actionStyleHeading2.setObjectName(_fromUtf8("actionStyleHeading2"))
        self.actionStyleHeading3 = QtGui.QAction(MainWindow)
        self.actionStyleHeading3.setObjectName(_fromUtf8("actionStyleHeading3"))
        self.actionStyleHeading4 = QtGui.QAction(MainWindow)
        self.actionStyleHeading4.setObjectName(_fromUtf8("actionStyleHeading4"))
        self.actionStyleHeading5 = QtGui.QAction(MainWindow)
        self.actionStyleHeading5.setObjectName(_fromUtf8("actionStyleHeading5"))
        self.actionStyleHeading6 = QtGui.QAction(MainWindow)
        self.actionStyleHeading6.setObjectName(_fromUtf8("actionStyleHeading6"))
        self.actionStylePreformatted = QtGui.QAction(MainWindow)
        self.actionStylePreformatted.setObjectName(_fromUtf8("actionStylePreformatted"))
        self.actionStyleAddress = QtGui.QAction(MainWindow)
        self.actionStyleAddress.setObjectName(_fromUtf8("actionStyleAddress"))
        self.actionFormatFontName = QtGui.QAction(MainWindow)
        self.actionFormatFontName.setObjectName(_fromUtf8("actionFormatFontName"))
        self.actionFormatTextColor = QtGui.QAction(MainWindow)
        self.actionFormatTextColor.setObjectName(_fromUtf8("actionFormatTextColor"))
        self.actionFormatBackgroundColor = QtGui.QAction(MainWindow)
        self.actionFormatBackgroundColor.setObjectName(_fromUtf8("actionFormatBackgroundColor"))
        self.actionFormatFontSize = QtGui.QAction(MainWindow)
        self.actionFormatFontSize.setObjectName(_fromUtf8("actionFormatFontSize"))
        self.actionInsertHtml = QtGui.QAction(MainWindow)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/insert-html.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInsertHtml.setIcon(icon25)
        self.actionInsertHtml.setObjectName(_fromUtf8("actionInsertHtml"))
        self.menu_File.addAction(self.actionFileNew)
        self.menu_File.addAction(self.actionFileOpen)
        self.menu_File.addAction(self.actionFileSave)
        self.menu_File.addAction(self.actionFileSaveAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionExit)
        self.menu_Edit.addAction(self.actionEditUndo)
        self.menu_Edit.addAction(self.actionEditRedo)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.actionEditCut)
        self.menu_Edit.addAction(self.actionEditCopy)
        self.menu_Edit.addAction(self.actionEditPaste)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.actionEditSelectAll)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.actionInsertImage)
        self.menu_Edit.addAction(self.actionCreateLink)
        self.menu_Edit.addAction(self.actionInsertHtml)
        self.menuSt_yle.addAction(self.actionStyleParagraph)
        self.menuSt_yle.addAction(self.actionStyleHeading1)
        self.menuSt_yle.addAction(self.actionStyleHeading2)
        self.menuSt_yle.addAction(self.actionStyleHeading3)
        self.menuSt_yle.addAction(self.actionStyleHeading4)
        self.menuSt_yle.addAction(self.actionStyleHeading5)
        self.menuSt_yle.addAction(self.actionStyleHeading6)
        self.menuSt_yle.addAction(self.actionStylePreformatted)
        self.menuSt_yle.addAction(self.actionStyleAddress)
        self.menu_Align.addAction(self.actionFormatAlignLeft)
        self.menu_Align.addAction(self.actionFormatAlignCenter)
        self.menu_Align.addAction(self.actionFormatAlignRight)
        self.menu_Align.addAction(self.actionFormatAlignJustify)
        self.menuF_ormat.addAction(self.menuSt_yle.menuAction())
        self.menuF_ormat.addAction(self.menu_Align.menuAction())
        self.menuF_ormat.addSeparator()
        self.menuF_ormat.addAction(self.actionFormatBold)
        self.menuF_ormat.addAction(self.actionFormatItalic)
        self.menuF_ormat.addAction(self.actionFormatUnderline)
        self.menuF_ormat.addAction(self.actionFormatStrikethrough)
        self.menuF_ormat.addSeparator()
        self.menuF_ormat.addAction(self.actionFormatIncreaseIndent)
        self.menuF_ormat.addAction(self.actionFormatDecreaseIndent)
        self.menuF_ormat.addSeparator()
        self.menuF_ormat.addAction(self.actionFormatNumberedList)
        self.menuF_ormat.addAction(self.actionFormatBulletedList)
        self.menuF_ormat.addSeparator()
        self.menuF_ormat.addAction(self.actionFormatFontName)
        self.menuF_ormat.addAction(self.actionFormatFontSize)
        self.menuF_ormat.addSeparator()
        self.menuF_ormat.addAction(self.actionFormatTextColor)
        self.menuF_ormat.addAction(self.actionFormatBackgroundColor)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menuF_ormat.menuAction())
        self.standardToolBar.addAction(self.actionFileNew)
        self.standardToolBar.addAction(self.actionFileOpen)
        self.standardToolBar.addAction(self.actionFileSave)
        self.standardToolBar.addSeparator()
        self.standardToolBar.addAction(self.actionEditUndo)
        self.standardToolBar.addAction(self.actionEditRedo)
        self.standardToolBar.addSeparator()
        self.standardToolBar.addAction(self.actionEditCut)
        self.standardToolBar.addAction(self.actionEditCopy)
        self.standardToolBar.addAction(self.actionEditPaste)
        self.standardToolBar.addSeparator()
        self.standardToolBar.addAction(self.actionZoomOut)
        self.standardToolBar.addAction(self.actionZoomIn)
        self.formatToolBar.addAction(self.actionFormatBold)
        self.formatToolBar.addAction(self.actionFormatItalic)
        self.formatToolBar.addAction(self.actionFormatUnderline)
        self.formatToolBar.addAction(self.actionFormatStrikethrough)
        self.formatToolBar.addSeparator()
        self.formatToolBar.addAction(self.actionFormatAlignLeft)
        self.formatToolBar.addAction(self.actionFormatAlignCenter)
        self.formatToolBar.addAction(self.actionFormatAlignRight)
        self.formatToolBar.addAction(self.actionFormatAlignJustify)
        self.formatToolBar.addSeparator()
        self.formatToolBar.addAction(self.actionFormatDecreaseIndent)
        self.formatToolBar.addAction(self.actionFormatIncreaseIndent)
        self.formatToolBar.addSeparator()
        self.formatToolBar.addAction(self.actionFormatNumberedList)
        self.formatToolBar.addAction(self.actionFormatBulletedList)
        self.formatToolBar.addSeparator()
        self.formatToolBar.addAction(self.actionInsertImage)
        self.formatToolBar.addAction(self.actionCreateLink)
        self.formatToolBar.addAction(self.actionInsertHtml)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "HTML Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuF_ormat.setTitle(QtGui.QApplication.translate("MainWindow", "F&ormat", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSt_yle.setTitle(QtGui.QApplication.translate("MainWindow", "St&yle", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Align.setTitle(QtGui.QApplication.translate("MainWindow", "&Align", None, QtGui.QApplication.UnicodeUTF8))
        self.standardToolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Standard", None, QtGui.QApplication.UnicodeUTF8))
        self.formatToolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Formatting", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileNew.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileNew.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileOpen.setText(QtGui.QApplication.translate("MainWindow", "&Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileSave.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileSaveAs.setText(QtGui.QApplication.translate("MainWindow", "Save &As...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditUndo.setText(QtGui.QApplication.translate("MainWindow", "&Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditUndo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditRedo.setText(QtGui.QApplication.translate("MainWindow", "&Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditRedo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Y", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditCut.setText(QtGui.QApplication.translate("MainWindow", "Cu&t", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditCut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditCopy.setText(QtGui.QApplication.translate("MainWindow", "&Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditCopy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditPaste.setText(QtGui.QApplication.translate("MainWindow", "&Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditPaste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditSelectAll.setText(QtGui.QApplication.translate("MainWindow", "Select A&ll", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditSelectAll.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatBold.setText(QtGui.QApplication.translate("MainWindow", "&Bold", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatBold.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+B", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatItalic.setText(QtGui.QApplication.translate("MainWindow", "&Italic", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatItalic.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatUnderline.setText(QtGui.QApplication.translate("MainWindow", "&Underline", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatUnderline.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+U", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatStrikethrough.setText(QtGui.QApplication.translate("MainWindow", "&Strikethrough", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatAlignLeft.setText(QtGui.QApplication.translate("MainWindow", "Align &Left", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatAlignCenter.setText(QtGui.QApplication.translate("MainWindow", "Align &Center", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatAlignRight.setText(QtGui.QApplication.translate("MainWindow", "Align &Right", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatAlignJustify.setText(QtGui.QApplication.translate("MainWindow", "Align &Justify", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatIncreaseIndent.setText(QtGui.QApplication.translate("MainWindow", "I&ncrease Indent", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatDecreaseIndent.setText(QtGui.QApplication.translate("MainWindow", "&Decrease Indent", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatBulletedList.setText(QtGui.QApplication.translate("MainWindow", "Bulle&ted List", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatNumberedList.setText(QtGui.QApplication.translate("MainWindow", "&Numbered List", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsertImage.setText(QtGui.QApplication.translate("MainWindow", "Insert &Image...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreateLink.setText(QtGui.QApplication.translate("MainWindow", "Create Link...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom Out", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom In", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStyleParagraph.setText(QtGui.QApplication.translate("MainWindow", "&Paragraph", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStyleHeading1.setText(QtGui.QApplication.translate("MainWindow", "Heading &1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStyleHeading2.setText(QtGui.QApplication.translate("MainWindow", "Heading &2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStyleHeading3.setText(QtGui.QApplication.translate("MainWindow", "Heading &3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStyleHeading4.setText(QtGui.QApplication.translate("MainWindow", "Heading &4", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStyleHeading5.setText(QtGui.QApplication.translate("MainWindow", "Heading &5", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStyleHeading6.setText(QtGui.QApplication.translate("MainWindow", "Heading &6", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStylePreformatted.setText(QtGui.QApplication.translate("MainWindow", "Pre&formatted", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStyleAddress.setText(QtGui.QApplication.translate("MainWindow", "&Address", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatFontName.setText(QtGui.QApplication.translate("MainWindow", "&Font Name...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatTextColor.setText(QtGui.QApplication.translate("MainWindow", "Text &Color...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatBackgroundColor.setText(QtGui.QApplication.translate("MainWindow", "Bac&kground Color...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFormatFontSize.setText(QtGui.QApplication.translate("MainWindow", "Font Si&ze...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsertHtml.setText(QtGui.QApplication.translate("MainWindow", "Insert HTML...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsertHtml.setToolTip(QtGui.QApplication.translate("MainWindow", "Insert HTML", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
import htmleditor_rc
