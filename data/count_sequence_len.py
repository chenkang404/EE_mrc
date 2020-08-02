import json

path_ = "slot_descrip"
fs = open(path_,"r",encoding="utf-8")
qurys = [qury.strip() for qury in fs.readlines()]
qury_dic = {idx:qury for idx,qury in enumerate(qurys)}
path = "mrc-ner.train"
f = open(path,"r",encoding="utf-8")
lines = f.readlines()
sequence_count = {}
for sample in lines:
    sample = json.loads(sample)
    context = sample["context"]
    qury = qury_dic[int(sample["query"])]
    sequence = context+qury
    len_seq = len(sequence)
    if len_seq not in sequence_count:
        sequence_count[len_seq]= 1
    else :
        sequence_count[len_seq]+=1

print("sequence_len:count",sequence_count)
print("按照sequence_len排序",sorted(sequence_count.items(), key=lambda x:x[0], reverse=True))
print("按照count排序",sorted(sequence_count.items(), key=lambda x:x[1], reverse=False))