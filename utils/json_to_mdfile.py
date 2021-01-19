import json
from pathlib import Path

with open("/Users/silva.park/git-my/spider/resources/egloos_oniondev.json") as json_file:
    post_json = json.load(json_file)

counter = 1
path = "/Users/silva.park/git-my/spider/resources"
cate_dir_dic = {}

for elem in post_json:
    # print(f'# {elem["title"]}\n')
    # print(f"> 날짜: {elem['created'].split()[0]}\n")
    # print("```")
    # print(elem["content"])
    # print("```")

    if elem["category"] not in cate_dir_dic:
        cate_dir_dic[elem["category"]] = f"cate{len(cate_dir_dic)+1}"
        Path(f"{path}/{cate_dir_dic[elem['category']]}").mkdir(parents=True, exist_ok=True)

    file_name = f"{path}/{cate_dir_dic[elem['category']]}/post_{counter}_{elem['category']}.md"

    with open(file_name, "a") as output_file:
        output_file.write(f'# {elem["title"]}\n\n')
        output_file.write(f"> 날짜: {elem['created'].split()[0]}\n\n")
        output_file.write("```\n")
        output_file.write(elem["content"])
        output_file.write("\n```\n\n---\n\n[목록으로](https://shiwoo-park.github.io/blog/kor)\n\n")

    counter += 1
