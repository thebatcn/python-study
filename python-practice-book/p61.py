import os

def print_directory_tree(path, indent=0):
    if not os.path.isdir(path):
        print(" " * indent + "├── " + os.path.basename(path))
        return

    print(" " * indent + "├── " + os.path.basename(path))
    indent += 4

    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)
        if os.path.isfile(entry_path):
            print(" " * indent + "│   " + entry)
        else:
            print_directory_tree(entry_path, indent)

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    print_directory_tree(directory)


