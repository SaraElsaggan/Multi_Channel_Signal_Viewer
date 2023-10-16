def cal_statistics(self,graph):
        data_item = graph.getPlotItem().listDataItems()[0]  
        x_values, y_values = data_item.getData()

        mean_value = mean(y_values)
        std_deviation = stdev(y_values)
        duration = len(y_values)
        min_value = min(y_values)
        max_value = max(y_values)

        statistics = {
            'mean': mean_value,
            'std': std_deviation,
            'duration': duration,
            'min': min_value,
            'max': max_value
        }

        return statistics