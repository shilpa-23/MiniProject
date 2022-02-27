import argparse
from pathlib import Path
import hashlib


parser = argparse.ArgumentParser()
parser.add_argument("-c", "--directory", default=".")
# add_argument() method, which is what we use to specify which command-line options the program is willing to accept.

args = vars(parser.parse_args())


def hash_db(directory):
    db = {}
    for path in directory.iterdir():
        if path.is_file():
            with open(path, "rb") as f:
                hash = hashlib.sha1(f.read()).hexdigest()
                if hash in db:
                    db[hash].append(path)
                else:
                    db[hash] = [path]
    return db


def filter_duplicates(db):
    return {key: value for key, value in db.items() if len(value) > 1}


def remove_duplicates(duplicates):
    for _, value in duplicates.items():
        files_to_remove = value[:-1]
        for file in files_to_remove:
            file.unlink()
    print("Duplicates successfully removed!!")


def main():
    directory = Path(args["directory"])
    db = hash_db(directory)
    duplicates = filter_duplicates(db)
    remove_duplicates(duplicates)


if __name__ == "__main__":
    main()