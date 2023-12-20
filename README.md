# manual-backup-assistant
Tool to help you keep track during the process of manually back up your system (for instance, to cut bloat before moving to a new OS)

## Getting started (Development)

1. Run the following from the root of the repository
    ```bash
    poetry install
    ```
2. Create a `.config/labelled_dirs.json` file (you can use `.config/labelled_dirs.example.json` as a template)
3. Run the script
    ```bash
    poetry run python ./print_tree_from_json.py
    ```
