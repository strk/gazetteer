# -*- coding: utf-8 -*-
################################################################################
#
#  New Zealand Geographic Board gazetteer application,
#  Crown copyright (c) 2020, Land Information New Zealand on behalf of
#  the New Zealand Government.
#
#  This file is released under the MIT licence. See the LICENCE file found
#  in the top-level directory of this distribution for more information.
#
################################################################################


# Form implementation generated from reading ui file 'Ui_NameSearchWidget.ui'
#
# Created: Thu Feb 28 12:38:05 2013
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_NameSearchWidget(object):
    def setupUi(self, NameSearchWidget):
        NameSearchWidget.setObjectName(_fromUtf8("NameSearchWidget"))
        NameSearchWidget.resize(529, 373)
        NameSearchWidget.setWindowTitle(QtGui.QApplication.translate("NameSearchWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(NameSearchWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabs = QtGui.QTabWidget(NameSearchWidget)
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.tabSearch = QtGui.QWidget()
        self.tabSearch.setObjectName(_fromUtf8("tabSearch"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabSearch)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.uSearchText = QtGui.QLineEdit(self.tabSearch)
        self.uSearchText.setObjectName(_fromUtf8("uSearchText"))
        self.horizontalLayout.addWidget(self.uSearchText)
        self.uSearchButton = QtGui.QToolButton(self.tabSearch)
        self.uSearchButton.setText(QtGui.QApplication.translate("NameSearchWidget", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.uSearchButton.setObjectName(_fromUtf8("uSearchButton"))
        self.horizontalLayout.addWidget(self.uSearchButton)
        self.uClearSearch = QtGui.QToolButton(self.tabSearch)
        self.uClearSearch.setText(QtGui.QApplication.translate("NameSearchWidget", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.uClearSearch.setObjectName(_fromUtf8("uClearSearch"))
        self.horizontalLayout.addWidget(self.uClearSearch)
        self.uToggleAdvanced = QtGui.QToolButton(self.tabSearch)
        self.uToggleAdvanced.setText(QtGui.QApplication.translate("NameSearchWidget", "Advanced", None, QtGui.QApplication.UnicodeUTF8))
        self.uToggleAdvanced.setObjectName(_fromUtf8("uToggleAdvanced"))
        self.horizontalLayout.addWidget(self.uToggleAdvanced)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.uSearchAdvanced = QtGui.QFrame(self.tabSearch)
        self.uSearchAdvanced.setFrameShape(QtGui.QFrame.StyledPanel)
        self.uSearchAdvanced.setFrameShadow(QtGui.QFrame.Raised)
        self.uSearchAdvanced.setObjectName(_fromUtf8("uSearchAdvanced"))
        self.formLayout_3 = QtGui.QFormLayout(self.uSearchAdvanced)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_2 = QtGui.QLabel(self.uSearchAdvanced)
        self.label_2.setText(QtGui.QApplication.translate("NameSearchWidget", "Feature class/type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.uSearchAdvanced)
        self.label_3.setText(QtGui.QApplication.translate("NameSearchWidget", "Name status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.uSearchNameStatus = QtGui.QComboBox(self.uSearchAdvanced)
        self.uSearchNameStatus.setObjectName(_fromUtf8("uSearchNameStatus"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.uSearchNameStatus)
        self.uSearchMapExtent = QtGui.QCheckBox(self.uSearchAdvanced)
        self.uSearchMapExtent.setText(QtGui.QApplication.translate("NameSearchWidget", "Limit search to map area", None, QtGui.QApplication.UnicodeUTF8))
        self.uSearchMapExtent.setObjectName(_fromUtf8("uSearchMapExtent"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.uSearchMapExtent)
        self.uSearchUnpublished = QtGui.QCheckBox(self.uSearchAdvanced)
        self.uSearchUnpublished.setText(QtGui.QApplication.translate("NameSearchWidget", "Only names with \"Not published\" annotation", None, QtGui.QApplication.UnicodeUTF8))
        self.uSearchUnpublished.setObjectName(_fromUtf8("uSearchUnpublished"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.uSearchUnpublished)
        self.label_4 = QtGui.QLabel(self.uSearchAdvanced)
        self.label_4.setText(QtGui.QApplication.translate("NameSearchWidget", "Maximum matches", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.uSearchMaxResults = QtGui.QSpinBox(self.uSearchAdvanced)
        self.uSearchMaxResults.setMinimum(10)
        self.uSearchMaxResults.setMaximum(1000000)
        self.uSearchMaxResults.setSingleStep(100)
        self.uSearchMaxResults.setProperty("value", 100)
        self.uSearchMaxResults.setObjectName(_fromUtf8("uSearchMaxResults"))
        self.horizontalLayout_2.addWidget(self.uSearchMaxResults)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.formLayout_3.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.uSearchFeatClass = QtGui.QComboBox(self.uSearchAdvanced)
        self.uSearchFeatClass.setObjectName(_fromUtf8("uSearchFeatClass"))
        self.horizontalLayout_4.addWidget(self.uSearchFeatClass)
        self.uSearchFeatType = QtGui.QComboBox(self.uSearchAdvanced)
        self.uSearchFeatType.setObjectName(_fromUtf8("uSearchFeatType"))
        self.horizontalLayout_4.addWidget(self.uSearchFeatType)
        self.formLayout_3.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.uSearchAdvanced)
        self.uSearchResults = ListModelTableView(self.tabSearch)
        self.uSearchResults.setObjectName(_fromUtf8("uSearchResults"))
        self.verticalLayout_2.addWidget(self.uSearchResults)
        self.uSearchStatus = QtGui.QLabel(self.tabSearch)
        self.uSearchStatus.setText(_fromUtf8(""))
        self.uSearchStatus.setObjectName(_fromUtf8("uSearchStatus"))
        self.verticalLayout_2.addWidget(self.uSearchStatus)
        self.tabs.addTab(self.tabSearch, _fromUtf8(""))
        self.tabRecent = QtGui.QWidget()
        self.tabRecent.setObjectName(_fromUtf8("tabRecent"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabRecent)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.uAllUsers = QtGui.QCheckBox(self.tabRecent)
        self.uAllUsers.setText(QtGui.QApplication.translate("NameSearchWidget", "Any user", None, QtGui.QApplication.UnicodeUTF8))
        self.uAllUsers.setObjectName(_fromUtf8("uAllUsers"))
        self.horizontalLayout_3.addWidget(self.uAllUsers)
        self.uEditOnly = QtGui.QCheckBox(self.tabRecent)
        self.uEditOnly.setText(QtGui.QApplication.translate("NameSearchWidget", "Edited only", None, QtGui.QApplication.UnicodeUTF8))
        self.uEditOnly.setObjectName(_fromUtf8("uEditOnly"))
        self.horizontalLayout_3.addWidget(self.uEditOnly)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label = QtGui.QLabel(self.tabRecent)
        self.label.setText(QtGui.QApplication.translate("NameSearchWidget", "Max count ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.uMaxRecent = QtGui.QSpinBox(self.tabRecent)
        self.uMaxRecent.setMinimum(10)
        self.uMaxRecent.setMaximum(1000)
        self.uMaxRecent.setProperty("value", 50)
        self.uMaxRecent.setObjectName(_fromUtf8("uMaxRecent"))
        self.horizontalLayout_3.addWidget(self.uMaxRecent)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.uRecentNames = ListModelTableView(self.tabRecent)
        self.uRecentNames.setObjectName(_fromUtf8("uRecentNames"))
        self.verticalLayout_4.addWidget(self.uRecentNames)
        self.tabs.addTab(self.tabRecent, _fromUtf8(""))
        self.tabFavourites = QtGui.QWidget()
        self.tabFavourites.setObjectName(_fromUtf8("tabFavourites"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabFavourites)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.uFavourites = ListModelTableView(self.tabFavourites)
        self.uFavourites.setObjectName(_fromUtf8("uFavourites"))
        self.verticalLayout_3.addWidget(self.uFavourites)
        self.tabs.addTab(self.tabFavourites, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabs)

        self.retranslateUi(NameSearchWidget)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(NameSearchWidget)

    def retranslateUi(self, NameSearchWidget):
        self.tabs.setTabText(self.tabs.indexOf(self.tabSearch), QtGui.QApplication.translate("NameSearchWidget", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tabRecent), QtGui.QApplication.translate("NameSearchWidget", "Recent", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tabFavourites), QtGui.QApplication.translate("NameSearchWidget", "Favourites", None, QtGui.QApplication.UnicodeUTF8))

from LINZ.Widgets.ListModelConnector import ListModelTableView
