import json

def handle_tree_item(tree_item):
    # if tree item has a type
    if 'type' in tree_item:
        tree_item_type = tree_item['type']
        if tree_item_type == 'file':
            handle_tree_file(tree_item)
        elif tree_item_type == 'directory':
            handle_tree_directory(tree_item)
        elif tree_item_type == 'link':
            handle_tree_link(tree_item)
        else:
            raise Exception("it's not a file or directory! ah!")
    else:
        raise Exception("i dunno")

def handle_tree_file(tree_file):
    # TODO(Denver): actually implement this
    print("it's a file!")

def handle_tree_directory(tree_dir):
    # TODO(Denver): actually implement this
    print("it's a dir!")
    print(f"name: {tree_dir['name']}")
    tree_dir_contents = tree_dir['contents']
    print(f"contents: {len(tree_dir_contents)}")
    for tree_item in tree_dir_contents:
        handle_tree_item(tree_item)

def handle_tree_link(tree_link):
    # TODO(Denver): actually implement this
    print(tree_link)

with open('./.cache/tree.json') as f:
    data = json.load(f)
    # get directories reported on in report
    dirs = [item for item in data if item["type"] == "directory"]
    # for each directory
    for item in dirs:
        handle_tree_item(item)
