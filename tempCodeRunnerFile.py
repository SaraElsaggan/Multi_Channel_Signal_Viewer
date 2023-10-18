_changed = self.ui.comb_sig_apperance_viewer_1.currentText()
            for signal in self.signals_1 :
                if signal["name"] == signal_to_be_changed:
                    signal["color"] = color
            
                    for data_line in signal["data_lines"]:
                    