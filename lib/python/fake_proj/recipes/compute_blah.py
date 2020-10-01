# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
cluster_tasks = dataiku.Dataset("cluster_tasks")
cluster_tasks_df = cluster_tasks.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

blah_df = cluster_tasks_df # For this sample code, simply copy input to output


# Write recipe outputs
blah = dataiku.Dataset("blah")
blah.write_with_schema(blah_df)
