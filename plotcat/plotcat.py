#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib import pylab
import random


class plotter:

    """plotter initiates a matplotlib plot. This plot is used to plot the
    serial input."""

    def __init__(self, number_of_samples=[100], total_plots=1, rows=1,
                 cols=1, y_low_lim=[0], y_high_lim=[1024],
                 plot_lines=[1], names=['serial-graph'], time_interval=10):

        """initializes the figure with the specified number of subplots
           (arg: total_plots)
        """
        self.fig = pylab.figure(1)
        self.currentAxis = []
        
        self.plots = []
        self.lines = []
        if not len(number_of_samples) == total_plots:
            number_of_samples = [100 for i in range(total_plots)]

        if not len(names) == total_plots:
            names = ['serial-graph' for i in range(total_plots)]

        if not len(y_low_lim) == total_plots:
            y_low_lim = [0 for i in range(total_plots)]

        if not len(y_high_lim) == total_plots:
            y_high_lim = [1024 for i in range(total_plots)]

        if not len(plot_lines) == total_plots:
            plot_lines = [1 for i in range(total_plots)]

        for i in range(total_plots):
            self.currentAxis.append(pylab.arange(0, number_of_samples[i], 1))

        count = 1
        for i in range(rows):
            for j in range(cols):

                new_plot = self.fig.add_subplot(((rows * 100) + (cols * 10)
                                                 + count))
                for k in range(plot_lines[count-1]):

                    #print(number_of_samples, y_low_lim, y_high_lim)
                    new_line = new_plot.plot(self.currentAxis[count-1],
                                         [random.randint(y_low_lim[count-1],
                                                         y_high_lim[count-1])
                                          for i in
                                          range(0, number_of_samples[count-1])])
                    self.lines.append(new_line)

                pylab.title(names[count-1])
                self.plots.append(new_plot) 
                if count == total_plots:
                    break
                count += 1
        self.manager = pylab.get_current_fig_manager()
        self.timer = self.fig.canvas.new_timer(interval=time_interval)

    def set_call_back(self, func):

        """sets callback function for updating the plot.
        in the callback function implement the logic of reading of serial input
        also the further processing of the signal if necessary has to be done
        in this
        callbak function."""

        self.timer.add_callback(func)
        self.timer.start()
        pylab.show()

    def plot_self(self, func):

        """define your callback function with the decorator @plotter.plot_self.
        in the callback function set the data of lines
        in the plot using self.lines[i][j].set_data(your data)"""

        def func_wrapper():

            func()

            try:

                self.manager.canvas.draw()

            except ValueError:
                pass

            except RuntimeError as RtE:
                pass

            except:
                pass

        return func_wrapper
