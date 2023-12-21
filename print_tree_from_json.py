# builtin
import json
# site
from colorama import Fore, Back, Style
from colorama import init as colorama_init

# ------------ #
# --- init --- #
# ------------ #

labelled_dirs = []
with open('./.config/labelled_dirs.json','r') as f:
    labelled_dirs = json.load(f)

skip_dirs = {}
todo_dirs = {}
for labelled_dir in labelled_dirs:
    label = labelled_dir['label']
    label_path = labelled_dir['path']
    if label == 'skip':
        skip_dirs[label_path] = labelled_dir
    elif label == 'todo':
        todo_dirs[label_path] = labelled_dir
    else:
        raise Exception(f"dirpath entry has an invalid label! ({label})")

# ------------- #
# --- funcs --- #
# ------------- #

def handle_tree_item(tree_item):
    # if tree item has a type
    if 'type' in tree_item:
        tree_item_type = tree_item['type']
        if tree_item_type == 'file':
            return handle_tree_file(tree_item)
        elif tree_item_type == 'directory':
            return handle_tree_directory(tree_item)
        elif tree_item_type == 'link':
            return handle_tree_link(tree_item)
        elif tree_item_type == 'socket':
            return handle_tree_socket(tree_item)
        elif tree_item_type == 'fifo':
            return handle_tree_fifo(tree_item)
        else:
            print(f"unknown type: {tree_item_type}")
            raise Exception("tree item type isn't a file, directory, link, socket or fifo! ah!")
    else:
        raise Exception("tree item is missing the 'type' key")

def handle_tree_file(tree_file):
    # TODO(Denver): actually implement this
    # print("it's a file!")
    
    # NOTE: below does work MVP, it's just disabled for now
    # print(f"[{tree_file.get('size','?'):<5}] {tree_file['name']}")
    return {"size": tree_file['size']}

def handle_tree_directory(tree_dir):
    # TODO(Denver): actually implement this
    tree_dir_name = tree_dir['name']
    tree_dir_contents = tree_dir['contents']

    is_skipped = tree_dir_name in skip_dirs
    is_todo = tree_dir_name in todo_dirs
    is_empty = len(tree_dir_contents) < 1

    print(
        "[ dir ] "
        + (
            Fore.YELLOW
            + "SKIPPED "
            + Style.RESET_ALL
            if is_skipped
            else ""
        )
        + (
            Fore.BLUE
            + "TODO "
            + Style.RESET_ALL
            if is_todo
            else ""
        )
        + (
            Fore.BLACK
            + Back.WHITE
            + "EMPTY"
            + Style.RESET_ALL
            + " "
            if is_empty
            else ""
        )
        + tree_dir_name
        + " ("
        + str(len(tree_dir_contents))
        + ") "
        + (
            "- "
            + Fore.YELLOW
            + skip_dirs[tree_dir_name]["note"]
            + Style.RESET_ALL
            if is_skipped and "note" in skip_dirs[tree_dir_name]
            else ""
        )
        + (
            "- "
            + Fore.BLUE
            + todo_dirs[tree_dir_name]["note"]
            + Style.RESET_ALL
            if is_todo and "note" in todo_dirs[tree_dir_name]
            else ""
        )
    )

    # if dirpath has skip label
    if is_skipped:
        return handle_skipped_dir(tree_dir)
    
    # if dirpath has todo label
    if is_todo:
        return handle_todo_dir(tree_dir)

    # if dirpath is empty
    if is_empty:
        return handle_empty_dir(tree_dir)

    outputs = []
    for tree_item in tree_dir_contents:
        outputs.append(handle_tree_item(tree_item))
    
    # list number of children skipped
    skipped_count = outputs.count('skipped')
    if skipped_count > 0:
        print("  (" + Fore.YELLOW + "skipped " + str(skipped_count) + Style.RESET_ALL + ")")
    

def handle_tree_link(tree_link):
    # TODO(Denver): actually implement this
    # print(tree_link)
    return
    
def handle_tree_socket(tree_socket):
    # TODO(Denver): actually implement this
    print(tree_socket)
    
def handle_tree_fifo(tree_fifo):
    # TODO(Denver): actually implement this
    print(tree_fifo)
    
def handle_skipped_dir(skipped_dir):
    # TODO(Denver): actually implement this
    # print("skipped!")
    return "skipped"

def handle_todo_dir(todo_dir):
    # TODO(Denver): actually implement this
    # print("todo!")
    return "todo"

def handle_empty_dir(empty_dir):
    # TODO(Denver): actually implement this
    # print("empty!")
    return "empty"

# -------------- #
# --- script --- #
# -------------- #

colorama_init()

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
