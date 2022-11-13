import json

ua_list = []
with open("data",encoding="utf-8") as f:
    for i in f.readlines():
        try:
            b = i.replace(r"\"","\"").replace(', ,', ",")
            a = json.loads(b)
            ua_list.append({"model":a["model"],"id":a["id"]})
        except Exception as e:
            print(b)
            print(e)


print(f"len(ua_list):{len(ua_list)}")
# a = 0
with open("android_data.json", 'w',encoding="utf-8") as write_f:
	json.dump(ua_list, write_f, indent=4, ensure_ascii=False)
#     if "Linux; U;" in i:
#         a = a + 1
# print(a)