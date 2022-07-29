import glob


def main():
    matched_files = glob.glob("*.txt")
    pattern = "nigga"
    replacement = "REDACTED"
    change_map = {}

    # the read operation for each file
    for file in matched_files:
        f = open(file, "r")
        change_map[file] = f.readlines()

        # loop through all the lines in the file to find the pattern
        for x in range(len(change_map[file])):
            if pattern in change_map[file][x]:
                change_map[file][x] = change_map[file][x].replace(pattern, replacement)

        f.close()

    # the write operation
    for file in matched_files:
        f = open(file, "w")
        f.writelines(change_map[file])
        f.close()


if __name__ == '__main__':
    main()
