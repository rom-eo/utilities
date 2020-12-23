"""
@description:
This is an ad-hoc solution for producing attendance
sheet when the LMS gives you for each lecture a csv
file with the names in the first columns.
@arguments:
**input1: a directory where all csv files have been
downloaded
**input2: the name  of the file where you want the
result to be saved as csv file
@dependencies:
pandas
"""

# imports
import pandas as pd
import tkinter as tk
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import glob

# main window
root = tk.Tk()
# obtain the files as a list of dataframes
aPath= tk.filedialog.askdirectory(parent=root)
l_ist=glob.glob(aPath+'/*.csv')
dfs=[pd.read_csv(elem) for elem in l_ist]

# get all the first columns as a list
names=[elem for df in dfs for elem in df.iloc[:,0]]

# remove duplicates
d_ic={}
for elem in names:
 if elem in d_ic: d_ic[elem]=d_ic[elem]+1
 else:d_ic[elem]=1

# transform results in a csv file
names=list(d_ic.items())
names.sort()
names=pd.DataFrame(names)
names.to_csv(tk.filedialog.asksaveasfilename(parent=root,title="Save results as"))

# close main window
root.destroy()
