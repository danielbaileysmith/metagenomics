# Daniel Bailey Smith -- 2/23/2020

data_file = 'example_data.clp'
df = data_file

taxid_analysis = {}
with open(df, 'r') as df:
    for line in df:
        key_raw = tuple(line.strip().split(":")[-1].split(","))
        if len(key_raw) >= 50:
            continue
        else:
            key = hash(key_raw)
            if key in taxid_analysis:
                taxid_analysis[key] += 1
            else:
                taxid_analysis[key] = 1


#append a key value to a set
#cat each output and combine them together
#run hash on all them to reverse

# hash functions? how to import/use
# figure out default dict
print(list(taxid_analysis.values()))
print(list(taxid_analysis.keys()))
print(taxid_analysis)