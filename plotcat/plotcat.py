#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pylab
import sys
import time
import random

class plotter:

  """plotter initiates a matplotlib plot. This plot is used to plot the serial input."""

  def __init__(self, number_of_samples = 100, total_plots = 1,y_low_lim = 0, y_high_lim = 1024):

    """initializes the figure with the specified number of subplots (arg: total_plots)
    """
    self.fig = pylab.figure(1)
    self.currentAxis = pylab.arange(0, number_of_samples, 1)

    self.plots = []
    self.lines = []
    for i in range(total_plots):
      new_plot = self.fig.add_subplot(111)
      new_line = new_plot.plot(self.currentAxis, [random.randint(y_low_lim, y_high_lim)for i in range(0,100)])
      self.plots.append(new_plot)
      self.lines.append(new_line)


    self.manager = pylab.get_current_fig_manager()
    self.timer = self.fig.canvas.new_timer(interval = 10)

  def set_call_back(self, func):

    """sets callback function for updating the plot.
    in the callback function implement the logic of reading of serial input
    also the further processing of the signal if necessary has to be done in this
    callbak function."""
    self.timer.add_callback(func)
    self.timer.start()
    pylab.show()


  def plot_self(self, func):

    """define your callback function with the decorator @plotter.plot_self.
    in the callback function set the data of lines 
    in the plot using self.lines[i][j].set_data(your data)"""
    def func_wrapper():
      func(self)
      try:
        self.manager.canvas.draw()
      except ValueError:
        pass
      except RuntimeError as RtE:
        pass
      except:
        pass
    return func_wrapper
