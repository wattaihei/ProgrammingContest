import json

basejsonpath = "/Users/taihei/Library/Application Support/Code/User/snippets/"

info = {
    "code_path" : "./cpp/combination.cpp",
    "write_file" : "cpp.json",
    "prefix" : "combination",
    "description" : "combination"
}


def read_snippet_file(filename):
    with open(basejsonpath+filename, "r") as f:
        js = json.load(f)
    return js

def write_snippet_file(filename, js):
    with open(basejsonpath+filename, "w") as f:
        json.dump(js, f, ensure_ascii=False, indent=4)

def file_to_list(filepath):
    contents = []
    with open(filepath, "r") as f:
        for row in f:
            contents.append(row.rstrip())
    return contents

def main():
    js = read_snippet_file(info["write_file"])
    js[info["description"]] = {
        "prefix" : info["prefix"],
        "body" : file_to_list(info["code_path"]),
        "description" : info["description"]
    }
    write_snippet_file(info["write_file"], js)


if __name__ == "__main__":
    main()