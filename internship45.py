# Daniel Bailey Smith -- 4/5/2020

import pandas as pd
import hashlib
import json

data_set = input("Enter file name: ")
ds = data_set

with open(ds, 'r') as ds:
    ds_analysis = {}
    ds_key_legend = {}
    taxids = set()
    for line in ds:
        raw_key = tuple(line.strip().split(":")[-1].split(","))
        taxids.update(list(raw_key))
        if len(raw_key) >= 50:
            continue
        else:
            key = hash(raw_key)
            if key in ds_analysis:
                ds_analysis[key] += 1
            else:
                ds_analysis[key] = 1
            if key not in ds_key_legend:
                ds_key_legend[key] = raw_key

df = pd.DataFrame.from_dict(ds_analysis, orient="index", columns=['counts'])
def fullprint_dataframe(df):
    def optional_fullprint(df):
        """
        This is optional for writing the df to output file.
        """
        pd.set_option('display.max_rows', len(df))
        print(df)
        pd.reset_option('display.max_rows')


with open('output_file.txt', 'w') as of:
    of.write(fullprint_dataframe(df))
    
    
# --- below is commented out because it's broken -- planning on using hashmap to fix this in the future ---
# with open('output_file2.txt', 'w') as of:
    # of.write(str(ds_key_legend))

#print(ds_analysis) # old checkpoint
print('Check current directory for output_file.txt for more information.')