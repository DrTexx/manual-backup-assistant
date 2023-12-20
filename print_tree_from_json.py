import json

# ----------------- #
# --- constants --- #
# ----------------- #

labelled_dirs = [
    {
        "path": "/home/denver/.zoom",
        "label": "skip"
    }
]

# ------------ #
# --- init --- #
# ------------ #

skip_dirs = []
for labelled_dir in labelled_dirs:
    label = labelled_dir['label']
    if label == 'skip':
        skip_dirs.append(labelled_dir['path'])

# ------------- #
# --- funcs --- #
# ------------- #

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
        elif tree_item_type == 'socket':
            handle_tree_socket(tree_item)
        elif tree_item_type == 'fifo':
            handle_tree_fifo(tree_item)
        else:
            print(f"unknown type: {tree_item_type}")
            raise Exception("tree item type isn't a file, directory, link, socket or fifo! ah!")
    else:
        raise Exception("tree item is missing the 'type' key")

def handle_tree_file(tree_file):
    # TODO(Denver): actually implement this
    # print("it's a file!")
    return

def handle_tree_directory(tree_dir):
    # TODO(Denver): actually implement this
    print("it's a dir!")
    tree_dir_name = tree_dir['name']
    print(f"name: {tree_dir_name}")

    # if dirpath matches the dirs labelled to be skipped
    if tree_dir_name in skip_dirs:
        handle_skipped_dir(tree_dir)
        return "skipped"

    tree_dir_contents = tree_dir['contents']
    print(f"contents: {len(tree_dir_contents)}")
    for tree_item in tree_dir_contents:
        handle_tree_item(tree_item)

def handle_tree_link(tree_link):
    # TODO(Denver): actually implement this
    print(tree_link)
    
def handle_tree_socket(tree_socket):
    # TODO(Denver): actually implement this
    print(tree_socket)
    
def handle_tree_fifo(tree_fifo):
    # TODO(Denver): actually implement this
    print(tree_fifo)
    
def handle_skipped_dir(skipped_dir):
    # TODO(Denver): actually implement this
    print("skipped!")

with open('./.cache/tree.json') as f:
    data = json.load(f)
    # get directories reported on in report
    dirs = [item for item in data if item["type"] == "directory"]
    # for each directory
    for item in dirs:
        handle_tree_item(item)

# ----------------- #
# --- Todo List --- #
# ----------------- #

# TODO(Denver): allow dirs and their children to be marked as "skipped", "backed up", "to back up"
