# manual-backup-assistant
Tool to help you keep track during the process of manually backing up your system.

For instance, instead of just backing up everything, you may want to **manually cut out any bloat or unnecessary files from your system before creating a backup** in preperation to move to a new OS. Alternatively, you may be looking for something to help you keep track as you move a subset of your media to cloud services so that it's available across all your devices instead of just the one.

## Getting started (Development)

1. Ensure you have the [prerequisites](#prerequisites) installed
2. Run the following
    ```bash
    cd <path_to_local_copy_of_repo> # navigate to your local copy of this repo
    poetry install # install project dependencies in isolated environment
    tree ~ -afsDJ --dirsfirst --sort="size" > ./.cache/tree.json # generate dir tree report
    ```
3. Create a `.config/labelled_dirs.json` file (you can use `.config/labelled_dirs.example.json` as a template)
4. Run the script
    ```bash
    poetry run python ./print_tree_from_json.py
    ```

### Prerequisites

| Prerequisite | Version | Install with   |
| ------------ | ------- | -------------- |
| Poetry       | >1.5.1  | Pipx           |
| Tree         | >1.8.0  | Apt            |
| Python       | >3.8    | Apt (or pyenv) |

## Limitations

- Cannot handle parsing JSON if the output from `tree` contains filenames with invalid encoding
- Cannot handle parsing JSON if the output from `tree` contains weird filenames with illegal chars like `\` bc the JSON parser tries to handle it like an escaped character
  - e.g. The Linux native version of the game 'Speedrunners' had created a directory named `[...]/Ghost\Replay/` on my machine that needed to be deleted before I could successfully parse the JSON output from `tree`)
