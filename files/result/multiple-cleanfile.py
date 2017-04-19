import glob

read_files = glob.glob("part-r*")

with open("diff_data.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

with open('diff_data.txt','r') as f:
        lines = f.read()
        lines = lines.replace('{}\n','')

with open('s_asset_xa-missing_row_id.txt','w') as f1:
        f1.writelines(lines)



