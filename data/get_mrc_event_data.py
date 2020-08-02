import json

path_slot = "slot_descrip"
path_label_map = "vocab_all_slot_label_noBI_map.txt"
query_list = []
label_2_id = {}
labels_list = []
with open(path_slot,"r",encoding="utf-8") as fp:
    lines = fp.readlines()
    for line in lines:
        line = line.strip()
        if line not in query_list:
            query_list.append(line)
with open(path_label_map,"r",encoding="utf-8") as fp:
    lines = fp.readlines()
    for line in lines:
        line = line.strip()
        label,id = line.split("\t")
        if label not in label_2_id:
            labels_list.append(label)
            label_2_id[label]=id
print(query_list)
print(label_2_id)
print(labels_list)


#data_from_sample
# {"text": "美国“未来为”子公司大幅度裁员，这是为什么呢？任正非正式回应",
#  "id": "5aec2b5b759c5f8f42f9c0156eb3c924",
#  "event_list": [{"event_type": "组织关系-裁员", "trigger": "裁员", "trigger_start_index": 13,
#                  "arguments": [
#                        {"argument_start_index": 0, "role": "裁员方", "argument": "美国“未来为”子公司", "alias": []}
#                               ],
#                  "class": "组织关系"}
#                 ]
#  }

path_train ="train.json"
path_dev = "dev.json"
path = "mrc-ner.test"
mrc_fp = open(path,"w",encoding="utf-8")
with open(path_dev,"r",encoding="utf-8") as fp:
    lines = fp.readlines()
    for line in lines:
        line = json.loads(line)
        sample_id =line["id"]
        context = line["text"]
        events = line["event_list"]
        for event in events:
            event_type = event["event_type"]
            arguments = event["arguments"]
            for argument in arguments:
                sample={}
                end_pos_list = []
                start_pos_list = []
                role = argument["role"]
                arg = argument["argument"]
                start_pos  =argument["argument_start_index"]
                start_pos_list.append(start_pos)
                end_pos = start_pos+len(arg)-1
                end_pos_list.append(end_pos)
                span_pos = []
                span_pos.append(";".join([str(start_pos),str(end_pos)]))
                role_type = "-".join([event_type,role])
                query =label_2_id[role_type]
                sample["context"]=context
                sample["argument"]=arg
                sample["end_position"]=end_pos_list
                sample["role_type"]=role_type
                sample["query"]=str(query)
                sample["span_position"]=span_pos
                sample["start_position"]=start_pos_list
                json.dump(sample,mrc_fp,ensure_ascii=False)
                mrc_fp.write("\n")







#data_to_sample
# {
# "context": "begala dr . palmisano , again , thanks for staying with us through the break .",
# "end_position": [
#     2,
#     4,
#     12
#     ],
# "entity_label": "PER",
# "impossible": false,
# "qas_id": "4.3",
# "query": "3",
# "span_position": [
#     "1;2",
#     "1;4",
#     "11;12"],
# "start_position": [
#     1,
#     1,
#     11]
# }
