import numpy as np
from scipy import  stats

from dash import dcc
import plotly.graph_objs as go


def get_data(raw_data: list) -> dict:
    """Implement the function that extracts aLogP quantity per molecule from raw ChEMBL data
       Computes mean, median and standard deviation 
       
    Hints:
       - aLogP quantity is located in attribute `alogp` of `molecule_properties`
       - Make sure to exclude None values
       - When input is empty, the method should return an empty dictionary

    Args:
        raw_data (list): ChEMBL output: see callbacks/data_schema.py for description
        
    Returns:
        dict: the following attributes have to be included in the output
                - component (str): name of the component
                - data (list): array of integers, actual values
                - mean (float): average value
                - median (float): median
                - std (float): standard deviation
                - min_value (float): minimum value
                - max_value (float): maximum value
                - irq (float): interquartile range (stats.iqr(data))
                - quartiles (list): 0.25th, 0.5th and 0.75th quantiles (np.quantile(data, [0.25, 0.5, 0.75]))
    """
    return {}
    
def draw_component(data_array: list) -> dcc.Graph:
    """[OPTIONAL]
       Method drawing a histogram of aLogP.
       You can use plotly tutorial: https://plotly.com/python/histograms/#histograms-with-gohistogram 
       to style the histogram as you like it or to replace it by other object, e.g. BoxPlot.
       To style graph layout, use reference manual: https://plotly.com/python/reference/index/
    Args:
        data_array (list): list of floats

    Returns:
        dcc.Graph: dash graph object that will be shown on the dashboard
    """
    plot = [go.Histogram(x=data_array,
                         marker={"color": "#FF0000",
                                 "line": {"width": 3,
                                          "color": "#D30202"}}
                         ),
            ]
    layout = go.Layout(xaxis={"title": "aLogP"},
                       yaxis={"title": "Frequency"},
                       margin={"t": 5})
    fig = go.Figure(data=plot,
                    layout=layout)
    
    return dcc.Graph(figure=fig)
    