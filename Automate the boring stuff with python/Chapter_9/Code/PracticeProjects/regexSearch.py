#! python
# regexSearch.py - Searches for a user-supplied regular expression in all .txt files in a folder.

import os, re, argparse


def search_folder(directory):
    """Searches for a user-supplied regular expression in all .txt files in a folder."""

    txtFiles = [file for file in os.listdir(directory) if file.endswith(".txt")]

    regex = re.compile(rf"{args.regex}")

    for file in txtFiles:
        with open(f"{directory}/{file}") as f:
            content = f.read()
            matches = regex.findall(content)
            if matches:
                print(f"Found matches in {file}:")
                for match in matches:
                    print(match)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Searches for a user-supplied regular expression in all .txt files in a folder."
    )
    parser.add_argument("directory", help="The directory to search in.")
    parser.add_argument("regex", help="The regular expression to search for.")
    args = parser.parse_args()
    search_folder(args.directory)
