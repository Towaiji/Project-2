"""CSC111 Project 2

This module contains the graph visualization function
which utilizes the graph created in Graph_Operation.py.


Copyright and Usage Information
===============================

This file is provided solely for the personal and private use for Ali Towaiji and Tanay langhe
and the CSC111 teaching team at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.

This file is Copyright (c) 2024 Ali Towaiji and Tanay Langhe
"""
import pandas as pd
import plotly.express as px


def visualize_businesses_on_map(graph):
    """
    visualizes the graph on a 3D map and pinpoints locations based on real world placement
    """
    # Make sure the scores are already computed in the graph
    graph.compute_scores()  # figure out proper score system

    # Extract data for DataFrame
    # Convert the vertex data (including the score) into a format suitable for creating a DataFrame
    data = [{
        'name': vertex['name'],
        'latitude': vertex['latitude'],
        'longitude': vertex['longitude'],
        'score': vertex['score']  # Score as computed by compute_scores
    } for vertex in graph.get_vertices_data()]

    df = pd.DataFrame(data)

    # Generate the map
    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", hover_name="name",
                            color="score", size="score",
                            color_continuous_scale=px.colors.cyclical.IceFire, size_max=15,
                            zoom=10, mapbox_style="carto-positron")
    fig.show()
