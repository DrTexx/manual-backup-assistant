# manual-backup-assistant
Tool to help you keep track during the process of manually back up your system (for instance, to cut bloat before moving to a new OS)

## Getting started (Development)

1. Ensure you have the [prerequisites](#prerequisites) installed
2. Run the following
    ```bash
    cd <path_to_local_copy_of_repo> # navigate to your local copy of this repo
    poetry install # install project dependencies in isolated environment
    tree ~ -afshDJ --dirsfirst --sort="size" > ./.cache/tree.json # generate dir tree report
    ```
3. Create a `.config/labelled_dirs.json` file (you can use `.config/labelled_dirs.example.json` as a template)
4. Run the script
    ```bash
    poetry run python ./print_tree_from_json.py
    ```

### Prerequisites

| Prerequisite | Version | Install with |
| ------------ | ------- | ------------ |
| Poetry       | >1.5.1  | Pipx         |
| Tree         | >1.8.0  | Apt          |

## Limitations

- Cannot handle parsing JSON if the output from `tree` contains filenames with invalid encoding
- Cannot handle parsing JSON if the output from `tree` contains weird files that contain illegal chars like `\` bc the JSON parser tries to handle it like an escaped character
