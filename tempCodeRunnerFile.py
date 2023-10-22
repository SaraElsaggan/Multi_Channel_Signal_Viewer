p += 20
        legend_1 = pg.LegendItem((10, 10), offset=(40 ,  p ))
        legend_1.setParentItem(self.ui.graphicsView.getPlotItem())
        legend_1.addItem(data_line, signal["name"])