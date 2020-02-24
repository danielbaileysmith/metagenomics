#Daniel Bailey Smith -- 2/23/2020

data_set = input("Enter file name: " )
ds = data_set

with open(ds, 'r') as ds:
    ds_analysis = {}
    for line in ds:
        raw_key = tuple(line.strip().split(":")[-1].split(","))
        if len(raw_key) >= 50:
            continue
        else:
            key = hash(raw_key)
            if key in ds_analysis:
                ds_analysis[key] += 1
            else:
                ds_analysis[key] = 1
    ds_key_legend = {}
    for key, key in zip (raw_key, ds_analysis.keys()):
        ds_key_legend[key] = raw_key

with open('output_file.txt', 'w') as of:
    of.write(str(ds_analysis) + '\n' * 3)
    of.write(str(ds_key_legend))

print(ds_analysis)
print('Check current directory for output_file.txt for more information.')
