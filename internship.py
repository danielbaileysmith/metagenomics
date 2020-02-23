# Daniel Bailey Smith -- 2/16/2020

data_file = 'example_data.clp'

taxid_analysis = {}
with open(data_file, 'r') as taxidf:
    for line in taxidf:
        key = tuple(line.strip().split(":")[-1].split(","))
        if len(key) >= 50:
            continue
        if key in taxid_analysis:
            taxid_analysis[key] += 1 #hashfunction wrap around this before += 1
        else:
            taxid_analysis[key] = 1
            #append a key value to a set
            #cat each output and combine them together
            #run hash on all them to reverse

# hash functions? how to import/use
# figure out default dict
# comment to check sync!
print(list(taxid_analysis.values()))

