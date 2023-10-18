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
        MainWindow.resize(1453, 778)
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
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_grph_viewer_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.lbl_grph_viewer_1.setFont(font)
        self.lbl_grph_viewer_1.setObjectName("lbl_grph_viewer_1")
        self.verticalLayout_2.addWidget(self.lbl_grph_viewer_1)
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.horz_playback_btns_viewer_1 = QtWidgets.QHBoxLayout()
        self.horz_playback_btns_viewer_1.setSpacing(10)
        self.horz_playback_btns_viewer_1.setObjectName("horz_playback_btns_viewer_1")
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horz_playback_btns_viewer_1.addItem(spacerItem1)
        self.btn_srt_begin__viewer_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_srt_begin__viewer_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/strt_frm_begin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_srt_begin__viewer_1.setIcon(icon)
        self.btn_srt_begin__viewer_1.setFlat(True)
        self.btn_srt_begin__viewer_1.setObjectName("btn_srt_begin__viewer_1")
        self.horz_playback_btns_viewer_1.addWidget(self.btn_srt_begin__viewer_1)
        self.btn_slow_viewer_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_slow_viewer_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imgs/imgs/slow_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_slow_viewer_1.setIcon(icon1)
        self.btn_slow_viewer_1.setFlat(True)
        self.btn_slow_viewer_1.setObjectName("btn_slow_viewer_1")
        self.horz_playback_btns_viewer_1.addWidget(self.btn_slow_viewer_1)
        self.btn_zoom_out_viewer_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zoom_out_viewer_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/imgs/imgs/aoom_out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_zoom_out_viewer_1.setIcon(icon2)
        self.btn_zoom_out_viewer_1.setFlat(True)
        self.btn_zoom_out_viewer_1.setObjectName("btn_zoom_out_viewer_1")
        self.horz_playback_btns_viewer_1.addWidget(self.btn_zoom_out_viewer_1)
        self.btn_play_pasuse_viewer_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_play_pasuse_viewer_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/imgs/imgs/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play_pasuse_viewer_1.setIcon(icon3)
        self.btn_play_pasuse_viewer_1.setFlat(True)
        self.btn_play_pasuse_viewer_1.setObjectName("btn_play_pasuse_viewer_1")
        self.horz_playback_btns_viewer_1.addWidget(self.btn_play_pasuse_viewer_1)
        self.btn_zoom_in_viewer_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zoom_in_viewer_1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/imgs/imgs/zoom_in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_zoom_in_viewer_1.setIcon(icon4)
        self.btn_zoom_in_viewer_1.setFlat(True)
        self.btn_zoom_in_viewer_1.setObjectName("btn_zoom_in_viewer_1")
        self.horz_playback_btns_viewer_1.addWidget(self.btn_zoom_in_viewer_1)
        self.btn_fast_viewer_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fast_viewer_1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/imgs/imgs/speed_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_fast_viewer_1.setIcon(icon5)
        self.btn_fast_viewer_1.setFlat(True)
        self.btn_fast_viewer_1.setObjectName("btn_fast_viewer_1")
        self.horz_playback_btns_viewer_1.addWidget(self.btn_fast_viewer_1)
        spacerItem2 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horz_playback_btns_viewer_1.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horz_playback_btns_viewer_1)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_grph_viewer_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.lbl_grph_viewer_2.setFont(font)
        self.lbl_grph_viewer_2.setObjectName("lbl_grph_viewer_2")
        self.verticalLayout_3.addWidget(self.lbl_grph_viewer_2)
        self.graphicsView_2 = PlotWidget(self.centralwidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_3.addWidget(self.graphicsView_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horz_playback_btns_viewer_2 = QtWidgets.QHBoxLayout()
        self.horz_playback_btns_viewer_2.setSpacing(10)
        self.horz_playback_btns_viewer_2.setObjectName("horz_playback_btns_viewer_2")
        spacerItem4 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horz_playback_btns_viewer_2.addItem(spacerItem4)
        self.btn_srt_begin__viewer_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_srt_begin__viewer_2.setText("")
        self.btn_srt_begin__viewer_2.setIcon(icon)
        self.btn_srt_begin__viewer_2.setFlat(True)
        self.btn_srt_begin__viewer_2.setObjectName("btn_srt_begin__viewer_2")
        self.horz_playback_btns_viewer_2.addWidget(self.btn_srt_begin__viewer_2)
        self.btn_slow_viewer_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_slow_viewer_2.setText("")
        self.btn_slow_viewer_2.setIcon(icon1)
        self.btn_slow_viewer_2.setFlat(True)
        self.btn_slow_viewer_2.setObjectName("btn_slow_viewer_2")
        self.horz_playback_btns_viewer_2.addWidget(self.btn_slow_viewer_2)
        self.btn_zoom_out_viewer_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zoom_out_viewer_2.setText("")
        self.btn_zoom_out_viewer_2.setIcon(icon2)
        self.btn_zoom_out_viewer_2.setFlat(True)
        self.btn_zoom_out_viewer_2.setObjectName("btn_zoom_out_viewer_2")
        self.horz_playback_btns_viewer_2.addWidget(self.btn_zoom_out_viewer_2)
        self.btn_play_pasuse_viewer_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_play_pasuse_viewer_2.setText("")
        self.btn_play_pasuse_viewer_2.setIcon(icon3)
        self.btn_play_pasuse_viewer_2.setFlat(True)
        self.btn_play_pasuse_viewer_2.setObjectName("btn_play_pasuse_viewer_2")
        self.horz_playback_btns_viewer_2.addWidget(self.btn_play_pasuse_viewer_2)
        self.btn_zoom_in_viewer_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zoom_in_viewer_2.setText("")
        self.btn_zoom_in_viewer_2.setIcon(icon4)
        self.btn_zoom_in_viewer_2.setFlat(True)
        self.btn_zoom_in_viewer_2.setObjectName("btn_zoom_in_viewer_2")
        self.horz_playback_btns_viewer_2.addWidget(self.btn_zoom_in_viewer_2)
        self.btn_fast_viewer_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fast_viewer_2.setText("")
        self.btn_fast_viewer_2.setIcon(icon5)
        self.btn_fast_viewer_2.setFlat(True)
        self.btn_fast_viewer_2.setObjectName("btn_fast_viewer_2")
        self.horz_playback_btns_viewer_2.addWidget(self.btn_fast_viewer_2)
        spacerItem5 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horz_playback_btns_viewer_2.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horz_playback_btns_viewer_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 1, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.grp_bx_ctrls_viewer_1 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.grp_bx_ctrls_viewer_1.sizePolicy().hasHeightForWidth())
        self.grp_bx_ctrls_viewer_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.grp_bx_ctrls_viewer_1.setFont(font)
        self.grp_bx_ctrls_viewer_1.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.grp_bx_ctrls_viewer_1.setCheckable(False)
        self.grp_bx_ctrls_viewer_1.setObjectName("grp_bx_ctrls_viewer_1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.grp_bx_ctrls_viewer_1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.combo_rename_grph_1 = QtWidgets.QComboBox(self.grp_bx_ctrls_viewer_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_rename_grph_1.sizePolicy().hasHeightForWidth())
        self.combo_rename_grph_1.setSizePolicy(sizePolicy)
        self.combo_rename_grph_1.setStyleSheet(" border: 2px solid rgb(89, 118, 199);\n"
"border-radius:6px")
        self.combo_rename_grph_1.setObjectName("combo_rename_grph_1")
        self.horizontalLayout_7.addWidget(self.combo_rename_grph_1)
        self.btn_rename_sig_1 = QtWidgets.QPushButton(self.grp_bx_ctrls_viewer_1)
        font = QtGui.QFont()
        font.setBold(True)
        self.btn_rename_sig_1.setFont(font)
        self.btn_rename_sig_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_rename_sig_1.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(89, 118, 199);\n"
"    color: black;\n"
"    border-radius: 3px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: lightblue;\n"
"}")
        self.btn_rename_sig_1.setObjectName("btn_rename_sig_1")
        self.horizontalLayout_7.addWidget(self.btn_rename_sig_1)
        spacerItem8 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 2, 1, 1, 1)
        self.horz_btns_ctrl__viewer_1 = QtWidgets.QHBoxLayout()
        self.horz_btns_ctrl__viewer_1.setObjectName("horz_btns_ctrl__viewer_1")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horz_btns_ctrl__viewer_1.addItem(spacerItem9)
        self.btn_add_sig_viewer_1 = QtWidgets.QPushButton(self.grp_bx_ctrls_viewer_1)
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
        self.btn_clear_viewer_1 = QtWidgets.QPushButton(self.grp_bx_ctrls_viewer_1)
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
        self.btn_snap_grph_1 = QtWidgets.QPushButton(self.grp_bx_ctrls_viewer_1)
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
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horz_btns_ctrl__viewer_1.addItem(spacerItem10)
        self.gridLayout_2.addLayout(self.horz_btns_ctrl__viewer_1, 3, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comb_sig_apperance_viewer_1 = QtWidgets.QComboBox(self.grp_bx_ctrls_viewer_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comb_sig_apperance_viewer_1.sizePolicy().hasHeightForWidth())
        self.comb_sig_apperance_viewer_1.setSizePolicy(sizePolicy)
        self.comb_sig_apperance_viewer_1.setStyleSheet(" border: 2px solid rgb(89, 118, 199);\n"
"border-radius:6px")
        self.comb_sig_apperance_viewer_1.setObjectName("comb_sig_apperance_viewer_1")
        self.horizontalLayout.addWidget(self.comb_sig_apperance_viewer_1)
        spacerItem11 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.btn_chng_colr_grpbox_viewer_1 = QtWidgets.QPushButton(self.grp_bx_ctrls_viewer_1)
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
        spacerItem12 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)
        self.chk_bx_sig_show_1 = QtWidgets.QCheckBox(self.grp_bx_ctrls_viewer_1)
        font = QtGui.QFont()
        font.setBold(True)
        self.chk_bx_sig_show_1.setFont(font)
        self.chk_bx_sig_show_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_bx_sig_show_1.setObjectName("chk_bx_sig_show_1")
        self.horizontalLayout.addWidget(self.chk_bx_sig_show_1)
        spacerItem13 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem13)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.lbl_move_viewer_1 = QtWidgets.QLabel(self.grp_bx_ctrls_viewer_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lbl_move_viewer_1.setFont(font)
        self.lbl_move_viewer_1.setObjectName("lbl_move_viewer_1")
        self.gridLayout_2.addWidget(self.lbl_move_viewer_1, 1, 0, 1, 1)
        self.lbl_colr_viewer_1 = QtWidgets.QLabel(self.grp_bx_ctrls_viewer_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lbl_colr_viewer_1.setFont(font)
        self.lbl_colr_viewer_1.setStyleSheet("")
        self.lbl_colr_viewer_1.setObjectName("lbl_colr_viewer_1")
        self.gridLayout_2.addWidget(self.lbl_colr_viewer_1, 0, 0, 1, 1)
        self.lbl_move_viewer_3 = QtWidgets.QLabel(self.grp_bx_ctrls_viewer_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lbl_move_viewer_3.setFont(font)
        self.lbl_move_viewer_3.setObjectName("lbl_move_viewer_3")
        self.gridLayout_2.addWidget(self.lbl_move_viewer_3, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comb_move_viewer_1 = QtWidgets.QComboBox(self.grp_bx_ctrls_viewer_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comb_move_viewer_1.sizePolicy().hasHeightForWidth())
        self.comb_move_viewer_1.setSizePolicy(sizePolicy)
        self.comb_move_viewer_1.setStyleSheet(" border: 2px solid rgb(89, 118, 199);\n"
"border-radius:6px")
        self.comb_move_viewer_1.setObjectName("comb_move_viewer_1")
        self.horizontalLayout_2.addWidget(self.comb_move_viewer_1)
        self.btn_move_viewer_1 = QtWidgets.QPushButton(self.grp_bx_ctrls_viewer_1)
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
        spacerItem14 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.grp_bx_ctrls_viewer_1)
        spacerItem15 = QtWidgets.QSpacerItem(30, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem15)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem16)
        self.btn_link_graphs = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_link_graphs.setFont(font)
        self.btn_link_graphs.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_link_graphs.setObjectName("btn_link_graphs")
        self.horizontalLayout_5.addWidget(self.btn_link_graphs)
        self.btn_repo = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_repo.setFont(font)
        self.btn_repo.setObjectName("btn_repo")
        self.horizontalLayout_5.addWidget(self.btn_repo)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem17)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem18 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem18)
        self.grp_bx_ctrls_viewer_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.grp_bx_ctrls_viewer_2.sizePolicy().hasHeightForWidth())
        self.grp_bx_ctrls_viewer_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.grp_bx_ctrls_viewer_2.setFont(font)
        self.grp_bx_ctrls_viewer_2.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.grp_bx_ctrls_viewer_2.setCheckable(False)
        self.grp_bx_ctrls_viewer_2.setObjectName("grp_bx_ctrls_viewer_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.grp_bx_ctrls_viewer_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.comb_sig_apperance_viewer_2 = QtWidgets.QComboBox(self.grp_bx_ctrls_viewer_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comb_sig_apperance_viewer_2.sizePolicy().hasHeightForWidth())
        self.comb_sig_apperance_viewer_2.setSizePolicy(sizePolicy)
        self.comb_sig_apperance_viewer_2.setStyleSheet(" border: 2px solid rgb(89, 118, 199);\n"
"border-radius:6px")
        self.comb_sig_apperance_viewer_2.setObjectName("comb_sig_apperance_viewer_2")
        self.horizontalLayout_6.addWidget(self.comb_sig_apperance_viewer_2)
        spacerItem19 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem19)
        self.btn_chng_colr_grpbox_viewer_2 = QtWidgets.QPushButton(self.grp_bx_ctrls_viewer_2)
        font = QtGui.QFont()
        font.setBold(True)
        self.btn_chng_colr_grpbox_viewer_2.setFont(font)
        self.btn_chng_colr_grpbox_viewer_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_chng_colr_grpbox_viewer_2.setStyleSheet("QPushButton {\n"
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
        self.btn_chng_colr_grpbox_viewer_2.setObjectName("btn_chng_colr_grpbox_viewer_2")
        self.horizontalLayout_6.addWidget(self.btn_chng_colr_grpbox_viewer_2)
        spacerItem20 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem20)
        self.chk_bx_sig_show_2 = QtWidgets.QCheckBox(self.grp_bx_ctrls_viewer_2)
        font = QtGui.QFont()
        font.setBold(True)
        self.chk_bx_sig_show_2.setFont(font)
        self.chk_bx_sig_show_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chk_bx_sig_show_2.setObjectName("chk_bx_sig_show_2")
        self.horizontalLayout_6.addWidget(self.chk_bx_sig_show_2)
        spacerItem21 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem21)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)
        self.horz_btns_ctrl__viewer_2 = QtWidgets.QHBoxLayout()
        self.horz_btns_ctrl__viewer_2.setObjectName("horz_btns_ctrl__viewer_2")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horz_btns_ctrl__viewer_2.addItem(spacerItem22)
        self.btn_add_sig_viewer_2 = QtWidgets.QPushButton(self.grp_bx_ctrls_viewer_2)
        font = QtGui.QFont()
        font.setBold(True)
        self.btn_add_sig_viewer_2.setFont(font)
        self.btn_add_sig_viewer_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add_sig_viewer_2.setStyleSheet("QPushButton {\n"
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
        self.btn_add_sig_viewer_2.setObjectName("btn_add_sig_viewer_2")
        self.horz_btns_ctrl__viewer_2.addWidget(self.btn_add_sig_viewer_2)
        self.btn_clear_viewer_2 = QtWidgets.QPushButton(self.grp_bx_ctrls_viewer_2)
        font = QtGui.QFont()
        font.setBold(True)
        self.btn_clear_viewer_2.setFont(font)
        self.btn_clear_viewer_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_clear_viewer_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(89, 118, 199);\n"
"    color: black;\n"
"    border-radius: 3px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: lightblue;\n"
"}")
        self.btn_clear_viewer_2.setObjectName("btn_clear_viewer_2")
        self.horz_btns_ctrl__viewer_2.addWidget(self.btn_clear_viewer_2)
        self.btn_snap_grph_2 = QtWidgets.QPushButton(self.grp_bx_ctrls_viewer_2)
        font = QtGui.QFont()
        font.setBold(True)
        self.btn_snap_grph_2.setFont(font)
        self.btn_snap_grph_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_snap_grph_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(89, 118, 199);\n"
"    color: black;\n"
"    border-radius: 3px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: lightblue;\n"
"}")
        self.btn_snap_grph_2.setObjectName("btn_snap_grph_2")
        self.horz_btns_ctrl__viewer_2.addWidget(self.btn_snap_grph_2)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horz_btns_ctrl__viewer_2.addItem(spacerItem23)
        self.gridLayout_3.addLayout(self.horz_btns_ctrl__viewer_2, 3, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.comb_move_viewer_2 = QtWidgets.QComboBox(self.grp_bx_ctrls_viewer_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comb_move_viewer_2.sizePolicy().hasHeightForWidth())
        self.comb_move_viewer_2.setSizePolicy(sizePolicy)
        self.comb_move_viewer_2.setStyleSheet(" border: 2px solid rgb(89, 118, 199);\n"
"border-radius:6px")
        self.comb_move_viewer_2.setObjectName("comb_move_viewer_2")
        self.horizontalLayout_9.addWidget(self.comb_move_viewer_2)
        self.btn_move_viewer_2 = QtWidgets.QPushButton(self.grp_bx_ctrls_viewer_2)
        font = QtGui.QFont()
        font.setBold(True)
        self.btn_move_viewer_2.setFont(font)
        self.btn_move_viewer_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_move_viewer_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(89, 118, 199);\n"
"    color: black;\n"
"    border-radius: 3px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: lightblue;\n"
"}")
        self.btn_move_viewer_2.setObjectName("btn_move_viewer_2")
        self.horizontalLayout_9.addWidget(self.btn_move_viewer_2)
        spacerItem24 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem24)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 1, 1, 1, 1)
        self.lbl_move_viewer_2 = QtWidgets.QLabel(self.grp_bx_ctrls_viewer_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lbl_move_viewer_2.setFont(font)
        self.lbl_move_viewer_2.setObjectName("lbl_move_viewer_2")
        self.gridLayout_3.addWidget(self.lbl_move_viewer_2, 1, 0, 1, 1)
        self.lbl_move_viewer_4 = QtWidgets.QLabel(self.grp_bx_ctrls_viewer_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lbl_move_viewer_4.setFont(font)
        self.lbl_move_viewer_4.setObjectName("lbl_move_viewer_4")
        self.gridLayout_3.addWidget(self.lbl_move_viewer_4, 2, 0, 1, 1)
        self.lbl_colr_viewer_2 = QtWidgets.QLabel(self.grp_bx_ctrls_viewer_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lbl_colr_viewer_2.setFont(font)
        self.lbl_colr_viewer_2.setStyleSheet("")
        self.lbl_colr_viewer_2.setObjectName("lbl_colr_viewer_2")
        self.gridLayout_3.addWidget(self.lbl_colr_viewer_2, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.combo_rename_grph_2 = QtWidgets.QComboBox(self.grp_bx_ctrls_viewer_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_rename_grph_2.sizePolicy().hasHeightForWidth())
        self.combo_rename_grph_2.setSizePolicy(sizePolicy)
        self.combo_rename_grph_2.setStyleSheet(" border: 2px solid rgb(89, 118, 199);\n"
"border-radius:6px")
        self.combo_rename_grph_2.setObjectName("combo_rename_grph_2")
        self.horizontalLayout_8.addWidget(self.combo_rename_grph_2)
        self.btn_rename_sig_2 = QtWidgets.QPushButton(self.grp_bx_ctrls_viewer_2)
        font = QtGui.QFont()
        font.setBold(True)
        self.btn_rename_sig_2.setFont(font)
        self.btn_rename_sig_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_rename_sig_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(89, 118, 199);\n"
"    color: black;\n"
"    border-radius: 3px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: lightblue;\n"
"}")
        self.btn_rename_sig_2.setObjectName("btn_rename_sig_2")
        self.horizontalLayout_8.addWidget(self.btn_rename_sig_2)
        spacerItem25 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem25)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 2, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.grp_bx_ctrls_viewer_2)
        spacerItem26 = QtWidgets.QSpacerItem(30, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_4.addItem(spacerItem26)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1453, 26))
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
        self.btn_srt_begin__viewer_1.setToolTip(_translate("MainWindow", "replay"))
        self.btn_srt_begin__viewer_1.setWhatsThis(_translate("MainWindow", "stast from beging\n"
""))
        self.btn_play_pasuse_viewer_1.setToolTip(_translate("MainWindow", "paly\n"
""))
        self.lbl_grph_viewer_2.setText(_translate("MainWindow", "Graph viewer 2"))
        self.btn_srt_begin__viewer_2.setToolTip(_translate("MainWindow", "replay"))
        self.btn_srt_begin__viewer_2.setWhatsThis(_translate("MainWindow", "stast from beging\n"
""))
        self.btn_play_pasuse_viewer_2.setToolTip(_translate("MainWindow", "paly\n"
""))
        self.grp_bx_ctrls_viewer_1.setTitle(_translate("MainWindow", "Graph viewer 1"))
        self.btn_rename_sig_1.setText(_translate("MainWindow", "rename"))
        self.btn_add_sig_viewer_1.setText(_translate("MainWindow", "Add signal"))
        self.btn_clear_viewer_1.setText(_translate("MainWindow", "Clear graph"))
        self.btn_snap_grph_1.setText(_translate("MainWindow", "Screenshot"))
        self.btn_chng_colr_grpbox_viewer_1.setText(_translate("MainWindow", "Change color"))
        self.chk_bx_sig_show_1.setText(_translate("MainWindow", "Show"))
        self.lbl_move_viewer_1.setText(_translate("MainWindow", "Move signal"))
        self.lbl_colr_viewer_1.setText(_translate("MainWindow", "Signal"))
        self.lbl_move_viewer_3.setText(_translate("MainWindow", "rename signal"))
        self.btn_move_viewer_1.setText(_translate("MainWindow", "Move to graph 2"))
        self.btn_link_graphs.setText(_translate("MainWindow", "Link graphs"))
        self.btn_repo.setText(_translate("MainWindow", "Report"))
        self.grp_bx_ctrls_viewer_2.setTitle(_translate("MainWindow", "Graph viewer 2"))
        self.btn_chng_colr_grpbox_viewer_2.setText(_translate("MainWindow", "Change color"))
        self.chk_bx_sig_show_2.setText(_translate("MainWindow", "Show"))
        self.btn_add_sig_viewer_2.setText(_translate("MainWindow", "Add signal"))
        self.btn_clear_viewer_2.setText(_translate("MainWindow", "Clear graph"))
        self.btn_snap_grph_2.setText(_translate("MainWindow", "Screenshot"))
        self.btn_move_viewer_2.setText(_translate("MainWindow", "Move to graph 1"))
        self.lbl_move_viewer_2.setText(_translate("MainWindow", "Move signal"))
        self.lbl_move_viewer_4.setText(_translate("MainWindow", "rename signal"))
        self.lbl_colr_viewer_2.setText(_translate("MainWindow", "Signal"))
        self.btn_rename_sig_2.setText(_translate("MainWindow", "rename"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.minu_add_sig.setTitle(_translate("MainWindow", "add signal"))
        self.actionproperties.setText(_translate("MainWindow", "properties"))
        self.act_add_sig_viewer_1.setText(_translate("MainWindow", "Graph viewer 1"))
        self.act_add_sig_viewer_2.setText(_translate("MainWindow", "Graph viewer 2"))
        self.actionchannel_3.setText(_translate("MainWindow", "channel 3"))
        self.actionreport.setText(_translate("MainWindow", "report"))
from pyqtgraph import PlotWidget
import imgs_rc
