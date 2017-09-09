import sys
from PyQt4 import QtGui
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from gui import gui, dlg1, dlg2

class Ui_Gui(QtGui.QMainWindow, gui.Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb_Plot_1.clicked.connect(lambda: self._plot(1))
        self.pb_Plot_2.clicked.connect(lambda: self._plot(2))
        self.edit_x.selectAll()
        self.show()
        
    def _plot(self, indx):
        try:
            x = eval(self.edit_x.text())
            y = eval(self.edit_y.text())
            if indx == 1:
                Plot = Ui_Plot_1(x, y)
            elif indx == 2:
                Plot = Ui_Plot_2(x, y)
            else:
                return
        except:
            QtGui.QMessageBox.critical(self, 'Fehler', 'Die eingegebenen Werte sind fehlerhaft')
            return
        Plot.show()
        Plot.exec_()

class Ui_Plot_1(QtGui.QDialog, dlg1.Ui_Dialog):

    def __init__(self, x, y):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        ax = self.Plotwidget.axes
        ax.plot(x, y, 'b-')
        ax.grid(True)
        self.show()

class Ui_Plot_2(QtGui.QDialog, dlg2.Ui_Dialog):

    def __init__(self, x, y):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        fig = Figure()
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot(x, y, 'b-')
        ax.grid(True)
        canvas = FigureCanvas(fig)
        nt = NavigationToolbar(canvas, self.toolbarWidget)
        nt.setMinimumWidth(600)
        self.plotLayout.addWidget(canvas)
        self.show()
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Gui = Ui_Gui()
    app.exec_()
    
# Ende