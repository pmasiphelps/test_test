# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
ds_with_arrays = dataiku.Dataset("ds_with_arrays")
ds_with_arrays_df = ds_with_arrays.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
ds_with_arrays_df['array_col']

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

out_py_df = ds_with_arrays_df # For this sample code, simply copy input to output


# Write recipe outputs
out_py = dataiku.Dataset("out_py")
out_py.write_with_schema(out_py_df)