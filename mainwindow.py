# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1741, 805)
        font = QtGui.QFont()
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setStyleSheet("QGroupBox  {\n"
"    border: 1px solid gray;\n"
"    border-color: #FF17365D;\n"
"    margin-top: 27px;\n"
"    font-size: 14px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 5px 8000px 5px 8000px;\n"
"    background-color:rgb(78, 82, 145);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid rgb(89, 118, 199);\n"
"    color: black;\n"
"    border-radius: 3px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: lightblue;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_grph_viewer_1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_grph_viewer_1.setGeometry(QtCore.QRect(20, 10, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.lbl_grph_viewer_1.setFont(font)
        self.lbl_grph_viewer_1.setObjectName("lbl_grph_viewer_1")
        self.grp_bx_ctrls_viewer_1 = QtWidgets.QGroupBox(self.centralwidget)
        self.grp_bx_ctrls_viewer_1.setGeometry(QtCore.QRect(930, 90, 511, 221))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.grp_bx_ctrls_viewer_1.setFont(font)
        self.grp_bx_ctrls_viewer_1.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.grp_bx_ctrls_viewer_1.setCheckable(False)
        self.grp_bx_ctrls_viewer_1.setObjectName("grp_bx_ctrls_viewer_1")
        self.formLayoutWidget_5 = QtWidgets.QWidget(self.grp_bx_ctrls_viewer_1)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(0, 30, 511, 191))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.form_ctrls_viewer_1 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.form_ctrls_viewer_1.setContentsMargins(6, 6, 6, 6)
        self.form_ctrls_viewer_1.setVerticalSpacing(6)
        self.form_ctrls_viewer_1.setObjectName("form_ctrls_viewer_1")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.form_ctrls_viewer_1.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.lbl_colr_viewer_1 = QtWidgets.QLabel(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lbl_colr_viewer_1.setFont(font)
        self.lbl_colr_viewer_1.setStyleSheet("")
        self.lbl_colr_viewer_1.setObjectName("lbl_colr_viewer_1")
        self.form_ctrls_viewer_1.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_colr_viewer_1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comb_sig_apperance_viewer_1 = QtWidgets.QComboBox(self.formLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comb_sig_apperance_viewer_1.sizePolicy().hasHeightForWidth())
        self.comb_sig_apperance_viewer_1.setSizePolicy(sizePolicy)
        self.comb_sig_apperance_viewer_1.setStyleSheet(" border: 2px solid rgb(89, 118, 199);\n"
"border-radius:6px")
        self.comb_sig_apperance_viewer_1.setObjectName("comb_sig_apperance_viewer_1")
        self.horizontalLayout.addWidget(self.comb_sig_apperance_viewer_1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_chng_colr_grpbox_viewer_1 = QtWidgets.QPushButton(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        self.btn_chng_colr_grpbox_viewer_1.setFont(font)
        self.btn_chng_colr_grpbox_viewer_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_chng_colr_grpbox_viewer_1.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(89, 118, 199);\n"
"    color: black;\n"
"    border-radius: 3px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: lightblue;\n"
"}\n"
" ")
        self.btn_chng_colr_grpbox_viewer_1.setObjectName("btn_chng_colr_grpbox_viewer_1")
        self.horizontalLayout.addWidget(self.btn_chng_colr_grpbox_viewer_1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.chk_bx_sig_show_1 = QtWidgets.QCheckBox(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        self.chk_bx_sig_show_1.setFont(font)
        self.chk_bx_sig_show_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_bx_sig_show_1.setObjectName("chk_bx_sig_show_1")
        self.horizontalLayout.addWidget(self.chk_bx_sig_show_1)
        spacerItem3 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.form_ctrls_viewer_1.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.form_ctrls_viewer_1.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        self.lbl_move_viewer_1 = QtWidgets.QLabel(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lbl_move_viewer_1.setFont(font)
        self.lbl_move_viewer_1.setObjectName("lbl_move_viewer_1")
        self.form_ctrls_viewer_1.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_move_viewer_1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comb_move_viewer_1 = QtWidgets.QComboBox(self.formLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comb_move_viewer_1.sizePolicy().hasHeightForWidth())
        self.comb_move_viewer_1.setSizePolicy(sizePolicy)
        self.comb_move_viewer_1.setStyleSheet(" border: 2px solid rgb(89, 118, 199);\n"
"border-radius:6px")
        self.comb_move_viewer_1.setObjectName("comb_move_viewer_1")
        self.horizontalLayout_2.addWidget(self.comb_move_viewer_1)
        self.btn_move_viewer_1 = QtWidgets.QPushButton(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        self.btn_move_viewer_1.setFont(font)
        self.btn_move_viewer_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_move_viewer_1.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(89, 118, 199);\n"
"    color: black;\n"
"    border-radius: 3px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: lightblue;\n"
"}")
        self.btn_move_viewer_1.setObjectName("btn_move_viewer_1")
        self.horizontalLayout_2.addWidget(self.btn_move_viewer_1)
        spacerItem5 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.form_ctrls_viewer_1.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.horz_btns_ctrl__viewer_1 = QtWidgets.QHBoxLayout()
        self.horz_btns_ctrl__viewer_1.setObjectName("horz_btns_ctrl__viewer_1")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horz_btns_ctrl__viewer_1.addItem(spacerItem6)
        self.btn_add_sig_viewer_1 = QtWidgets.QPushButton(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        self.btn_add_sig_viewer_1.setFont(font)
        self.btn_add_sig_viewer_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add_sig_viewer_1.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(89, 118, 199);\n"
"    color: black;\n"
"    border-radius: 3px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: lightblue;\n"
"}\n"
"")
        self.btn_add_sig_viewer_1.setObjectName("btn_add_sig_viewer_1")
        self.horz_btns_ctrl__viewer_1.addWidget(self.btn_add_sig_viewer_1)
        self.btn_clear_viewer_1 = QtWidgets.QPushButton(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        self.btn_clear_viewer_1.setFont(font)
        self.btn_clear_viewer_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_clear_viewer_1.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(89, 118, 199);\n"
"    color: black;\n"
"    border-radius: 3px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: lightblue;\n"
"}")
        self.btn_clear_viewer_1.setObjectName("btn_clear_viewer_1")
        self.horz_btns_ctrl__viewer_1.addWidget(self.btn_clear_viewer_1)
        self.btn_snap_grph_1 = QtWidgets.QPushButton(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        self.btn_snap_grph_1.setFont(font)
        self.btn_snap_grph_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_snap_grph_1.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(89, 118, 199);\n"
"    color: black;\n"
"    border-radius: 3px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: lightblue;\n"
"}")
        self.btn_snap_grph_1.setObjectName("btn_snap_grph_1")
        self.horz_btns_ctrl__viewer_1.addWidget(self.btn_snap_grph_1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horz_btns_ctrl__viewer_1.addItem(spacerItem7)
        self.form_ctrls_viewer_1.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horz_btns_ctrl__viewer_1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.form_ctrls_viewer_1.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem8)
        self.btn_link_graphs = QtWidgets.QPushButton(self.centralwidget)
        self.btn_link_graphs.setGeometry(QtCore.QRect(1000, 360, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_link_graphs.setFont(font)
        self.btn_link_graphs.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_link_graphs.setObjectName("btn_link_graphs")
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(250, 350, 371, 41))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horz_playback_btns_viewer_1 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horz_playback_btns_viewer_1.setContentsMargins(0, 0, 0, 0)
        self.horz_playback_btns_viewer_1.setSpacing(10)
        self.horz_playback_btns_viewer_1.setObjectName("horz_playback_btns_viewer_1")
        self.btn_srt_begin__viewer_1 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.btn_srt_begin__viewer_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/strt_frm_begin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_srt_begin__viewer_1.setIcon(icon)
        self.btn_srt_begin__viewer_1.setFlat(True)
        self.btn_srt_begin__viewer_1.setObjectName("btn_srt_begin__viewer_1")
        self.horz_playback_btns_viewer_1.addWidget(self.btn_srt_begin__viewer_1)
        self.btn_slow_viewer_1 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.btn_slow_viewer_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imgs/imgs/slow_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_slow_viewer_1.setIcon(icon1)
        self.btn_slow_viewer_1.setFlat(True)
        self.btn_slow_viewer_1.setObjectName("btn_slow_viewer_1")
        self.horz_playback_btns_viewer_1.addWidget(self.btn_slow_viewer_1)
        self.btn_zoom_out_viewer_1 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.btn_zoom_out_viewer_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/imgs/imgs/aoom_out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_zoom_out_viewer_1.setIcon(icon2)
        self.btn_zoom_out_viewer_1.setFlat(True)
        self.btn_zoom_out_viewer_1.setObjectName("btn_zoom_out_viewer_1")
        self.horz_playback_btns_viewer_1.addWidget(self.btn_zoom_out_viewer_1)
        self.btn_play_pasuse_viewer_1 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.btn_play_pasuse_viewer_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/imgs/imgs/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play_pasuse_viewer_1.setIcon(icon3)
        self.btn_play_pasuse_viewer_1.setFlat(True)
        self.btn_play_pasuse_viewer_1.setObjectName("btn_play_pasuse_viewer_1")
        self.horz_playback_btns_viewer_1.addWidget(self.btn_play_pasuse_viewer_1)
        self.btn_zoom_in_viewer_1 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.btn_zoom_in_viewer_1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/imgs/imgs/zoom_in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_zoom_in_viewer_1.setIcon(icon4)
        self.btn_zoom_in_viewer_1.setFlat(True)
        self.btn_zoom_in_viewer_1.setObjectName("btn_zoom_in_viewer_1")
        self.horz_playback_btns_viewer_1.addWidget(self.btn_zoom_in_viewer_1)
        self.btn_fast_viewer_1 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.btn_fast_viewer_1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/imgs/imgs/speed_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_fast_viewer_1.setIcon(icon5)
        self.btn_fast_viewer_1.setFlat(True)
        self.btn_fast_viewer_1.setObjectName("btn_fast_viewer_1")
        self.horz_playback_btns_viewer_1.addWidget(self.btn_fast_viewer_1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(130, 50, 770, 300))
        self.widget.setObjectName("widget")
        self.layoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(250, 710, 371, 41))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horz_playback_btns_viewer_2 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horz_playback_btns_viewer_2.setContentsMargins(0, 0, 0, 0)
        self.horz_playback_btns_viewer_2.setSpacing(10)
        self.horz_playback_btns_viewer_2.setObjectName("horz_playback_btns_viewer_2")
        self.btn_srt_begin__viewer_2 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.btn_srt_begin__viewer_2.setText("")
        self.btn_srt_begin__viewer_2.setIcon(icon)
        self.btn_srt_begin__viewer_2.setFlat(True)
        self.btn_srt_begin__viewer_2.setObjectName("btn_srt_begin__viewer_2")
        self.horz_playback_btns_viewer_2.addWidget(self.btn_srt_begin__viewer_2)
        self.btn_slow_viewer_2 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.btn_slow_viewer_2.setText("")
        self.btn_slow_viewer_2.setIcon(icon1)
        self.btn_slow_viewer_2.setFlat(True)
        self.btn_slow_viewer_2.setObjectName("btn_slow_viewer_2")
        self.horz_playback_btns_viewer_2.addWidget(self.btn_slow_viewer_2)
        self.btn_zoom_out_viewer_2 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.btn_zoom_out_viewer_2.setText("")
        self.btn_zoom_out_viewer_2.setIcon(icon2)
        self.btn_zoom_out_viewer_2.setFlat(True)
        self.btn_zoom_out_viewer_2.setObjectName("btn_zoom_out_viewer_2")
        self.horz_playback_btns_viewer_2.addWidget(self.btn_zoom_out_viewer_2)
        self.btn_play_pasuse_viewer_2 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.btn_play_pasuse_viewer_2.setText("")
        self.btn_play_pasuse_viewer_2.setIcon(icon3)
        self.btn_play_pasuse_viewer_2.setFlat(True)
        self.btn_play_pasuse_viewer_2.setObjectName("btn_play_pasuse_viewer_2")
        self.horz_playback_btns_viewer_2.addWidget(self.btn_play_pasuse_viewer_2)
        self.btn_zoom_in_viewer_2 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.btn_zoom_in_viewer_2.setText("")
        self.btn_zoom_in_viewer_2.setIcon(icon4)
        self.btn_zoom_in_viewer_2.setFlat(True)
        self.btn_zoom_in_viewer_2.setObjectName("btn_zoom_in_viewer_2")
        self.horz_playback_btns_viewer_2.addWidget(self.btn_zoom_in_viewer_2)
        self.btn_fast_viewer_2 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.btn_fast_viewer_2.setText("")
        self.btn_fast_viewer_2.setIcon(icon5)
        self.btn_fast_viewer_2.setFlat(True)
        self.btn_fast_viewer_2.setObjectName("btn_fast_viewer_2")
        self.horz_playback_btns_viewer_2.addWidget(self.btn_fast_viewer_2)
        self.lbl_grph_viewer_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_grph_viewer_2.setGeometry(QtCore.QRect(30, 370, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.lbl_grph_viewer_2.setFont(font)
        self.lbl_grph_viewer_2.setObjectName("lbl_grph_viewer_2")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(130, 400, 770, 300))
        self.widget_2.setObjectName("widget_2")
        self.grp_bx_ctrls_viewer_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.grp_bx_ctrls_viewer_2.setGeometry(QtCore.QRect(930, 450, 511, 231))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.grp_bx_ctrls_viewer_2.setFont(font)
        self.grp_bx_ctrls_viewer_2.setObjectName("grp_bx_ctrls_viewer_2")
        self.formLayoutWidget_6 = QtWidgets.QWidget(self.grp_bx_ctrls_viewer_2)
        self.formLayoutWidget_6.setGeometry(QtCore.QRect(0, 30, 511, 201))
        self.formLayoutWidget_6.setObjectName("formLayoutWidget_6")
        self.form_ctrls_viewer_2 = QtWidgets.QFormLayout(self.formLayoutWidget_6)
        self.form_ctrls_viewer_2.setContentsMargins(6, 6, 6, 6)
        self.form_ctrls_viewer_2.setVerticalSpacing(6)
        self.form_ctrls_viewer_2.setObjectName("form_ctrls_viewer_2")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.form_ctrls_viewer_2.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem9)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comb_sig_apperance_viewer_2 = QtWidgets.QComboBox(self.formLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comb_sig_apperance_viewer_2.sizePolicy().hasHeightForWidth())
        self.comb_sig_apperance_viewer_2.setSizePolicy(sizePolicy)
        self.comb_sig_apperance_viewer_2.setStyleSheet(" border: 2px solid rgb(89, 118, 199);\n"
"border-radius:6px")
        self.comb_sig_apperance_viewer_2.setObjectName("comb_sig_apperance_viewer_2")
        self.horizontalLayout_3.addWidget(self.comb_sig_apperance_viewer_2)
        spacerItem10 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.btn_chng_colr_grpbox_viewer_2 = QtWidgets.QPushButton(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setBold(True)
        self.btn_chng_colr_grpbox_viewer_2.setFont(font)
        self.btn_chng_colr_grpbox_viewer_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_chng_colr_grpbox_viewer_2.setObjectName("btn_chng_colr_grpbox_viewer_2")
        self.horizontalLayout_3.addWidget(self.btn_chng_colr_grpbox_viewer_2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.chk_bx_sig_show_2 = QtWidgets.QCheckBox(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setBold(True)
        self.chk_bx_sig_show_2.setFont(font)
        self.chk_bx_sig_show_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_bx_sig_show_2.setStyleSheet("selection-background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 85, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.chk_bx_sig_show_2.setObjectName("chk_bx_sig_show_2")
        self.horizontalLayout_3.addWidget(self.chk_bx_sig_show_2)
        spacerItem12 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.form_ctrls_viewer_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.form_ctrls_viewer_2.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem13)
        self.lbl_move_viewer_2 = QtWidgets.QLabel(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lbl_move_viewer_2.setFont(font)
        self.lbl_move_viewer_2.setObjectName("lbl_move_viewer_2")
        self.form_ctrls_viewer_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_move_viewer_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.comb_move_viewer_2 = QtWidgets.QComboBox(self.formLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comb_move_viewer_2.sizePolicy().hasHeightForWidth())
        self.comb_move_viewer_2.setSizePolicy(sizePolicy)
        self.comb_move_viewer_2.setStyleSheet(" border: 2px solid rgb(89, 118, 199);\n"
"border-radius:6px")
        self.comb_move_viewer_2.setObjectName("comb_move_viewer_2")
        self.horizontalLayout_4.addWidget(self.comb_move_viewer_2)
        self.btn_move_viewer_2 = QtWidgets.QPushButton(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setBold(True)
        self.btn_move_viewer_2.setFont(font)
        self.btn_move_viewer_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_move_viewer_2.setObjectName("btn_move_viewer_2")
        self.horizontalLayout_4.addWidget(self.btn_move_viewer_2)
        spacerItem14 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.form_ctrls_viewer_2.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.form_ctrls_viewer_2.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem15)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.form_ctrls_viewer_2.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem16)
        self.horz_btns_ctrl__viewer_2 = QtWidgets.QHBoxLayout()
        self.horz_btns_ctrl__viewer_2.setObjectName("horz_btns_ctrl__viewer_2")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horz_btns_ctrl__viewer_2.addItem(spacerItem17)
        self.btn_add_sig_viewer_2 = QtWidgets.QPushButton(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setBold(True)
        self.btn_add_sig_viewer_2.setFont(font)
        self.btn_add_sig_viewer_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add_sig_viewer_2.setObjectName("btn_add_sig_viewer_2")
        self.horz_btns_ctrl__viewer_2.addWidget(self.btn_add_sig_viewer_2)
        self.btn_clear_viewer_2 = QtWidgets.QPushButton(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setBold(True)
        self.btn_clear_viewer_2.setFont(font)
        self.btn_clear_viewer_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_clear_viewer_2.setObjectName("btn_clear_viewer_2")
        self.horz_btns_ctrl__viewer_2.addWidget(self.btn_clear_viewer_2)
        self.btn_snap_grph_2 = QtWidgets.QPushButton(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setBold(True)
        self.btn_snap_grph_2.setFont(font)
        self.btn_snap_grph_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_snap_grph_2.setObjectName("btn_snap_grph_2")
        self.horz_btns_ctrl__viewer_2.addWidget(self.btn_snap_grph_2)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horz_btns_ctrl__viewer_2.addItem(spacerItem18)
        self.form_ctrls_viewer_2.setLayout(7, QtWidgets.QFormLayout.FieldRole, self.horz_btns_ctrl__viewer_2)
        self.lbl_colr_viewer_2 = QtWidgets.QLabel(self.formLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lbl_colr_viewer_2.setFont(font)
        self.lbl_colr_viewer_2.setObjectName("lbl_colr_viewer_2")
        self.form_ctrls_viewer_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_colr_viewer_2)
        self.btn_repo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_repo.setGeometry(QtCore.QRect(1260, 360, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_repo.setFont(font)
        self.btn_repo.setObjectName("btn_repo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1741, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.minu_add_sig = QtWidgets.QMenu(self.menufile)
        self.minu_add_sig.setObjectName("minu_add_sig")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionproperties = QtWidgets.QAction(MainWindow)
        self.actionproperties.setObjectName("actionproperties")
        self.act_add_sig_viewer_1 = QtWidgets.QAction(MainWindow)
        self.act_add_sig_viewer_1.setObjectName("act_add_sig_viewer_1")
        self.act_add_sig_viewer_2 = QtWidgets.QAction(MainWindow)
        self.act_add_sig_viewer_2.setObjectName("act_add_sig_viewer_2")
        self.actionchannel_3 = QtWidgets.QAction(MainWindow)
        self.actionchannel_3.setObjectName("actionchannel_3")
        self.actionreport = QtWidgets.QAction(MainWindow)
        self.actionreport.setObjectName("actionreport")
        self.minu_add_sig.addAction(self.act_add_sig_viewer_1)
        self.minu_add_sig.addAction(self.act_add_sig_viewer_2)
        self.menufile.addAction(self.minu_add_sig.menuAction())
        self.menufile.addAction(self.actionreport)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_grph_viewer_1.setText(_translate("MainWindow", "Graph viewer 1"))
        self.grp_bx_ctrls_viewer_1.setTitle(_translate("MainWindow", "Graph viewer 1"))
        self.lbl_colr_viewer_1.setText(_translate("MainWindow", "Signal"))
        self.btn_chng_colr_grpbox_viewer_1.setText(_translate("MainWindow", "Change color"))
        self.chk_bx_sig_show_1.setText(_translate("MainWindow", "Show"))
        self.lbl_move_viewer_1.setText(_translate("MainWindow", "Move signal"))
        self.btn_move_viewer_1.setText(_translate("MainWindow", "Move to graph 2"))
        self.btn_add_sig_viewer_1.setText(_translate("MainWindow", "Add signal"))
        self.btn_clear_viewer_1.setText(_translate("MainWindow", "Clear graph"))
        self.btn_snap_grph_1.setText(_translate("MainWindow", "Screenshot"))
        self.btn_link_graphs.setText(_translate("MainWindow", "Link graphs"))
        self.btn_srt_begin__viewer_1.setToolTip(_translate("MainWindow", "replay"))
        self.btn_srt_begin__viewer_1.setWhatsThis(_translate("MainWindow", "stast from beging\n"
""))
        self.btn_play_pasuse_viewer_1.setToolTip(_translate("MainWindow", "paly\n"
""))
        self.lbl_grph_viewer_2.setText(_translate("MainWindow", "Graph viewer 2"))
        self.grp_bx_ctrls_viewer_2.setTitle(_translate("MainWindow", "Graph viewer 2"))
        self.btn_chng_colr_grpbox_viewer_2.setText(_translate("MainWindow", "Change color"))
        self.chk_bx_sig_show_2.setText(_translate("MainWindow", "Show"))
        self.lbl_move_viewer_2.setText(_translate("MainWindow", "Move signal"))
        self.btn_move_viewer_2.setText(_translate("MainWindow", "Move to graph 1"))
        self.btn_add_sig_viewer_2.setText(_translate("MainWindow", "Add signal"))
        self.btn_clear_viewer_2.setText(_translate("MainWindow", "Clear graph"))
        self.btn_snap_grph_2.setText(_translate("MainWindow", "Screenshot"))
        self.lbl_colr_viewer_2.setText(_translate("MainWindow", "Signal"))
        self.btn_repo.setText(_translate("MainWindow", "Report"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.minu_add_sig.setTitle(_translate("MainWindow", "add signal"))
        self.actionproperties.setText(_translate("MainWindow", "properties"))
        self.act_add_sig_viewer_1.setText(_translate("MainWindow", "Graph viewer 1"))
        self.act_add_sig_viewer_2.setText(_translate("MainWindow", "Graph viewer 2"))
        self.actionchannel_3.setText(_translate("MainWindow", "channel 3"))
        self.actionreport.setText(_translate("MainWindow", "report"))
import imgs_rc
