from Application.View import MagnifierWindow, MainWindow, PlotterWindow


class Controller(object):
    def __init__(self):
        # instantiate the QMainWindow objects
        self.mainWindow = MainWindow()
        self.plotterWindow = PlotterWindow()
        self.magnifierWindow = MagnifierWindow()

        # show the main window
        self.mainWindow.show()
