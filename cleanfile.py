import pdb

with open('s_doc_quote-diff_data.txt','r') as f:
	lines = f.read()
	lines = lines.replace('{}\n','')

with open('siebel-s_doc_quote-missing_rowid.txt','w') as f1:
	f1.writelines(lines)
#pdb.set_trace()
