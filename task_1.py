import random

ORIGINAL_FILE = "file.txt"
FILE_COPY = ORIGINAL_FILE.replace(".", "_copy.")
SEPARATOR = " "


def write_to_file(f, word: str, last_index: int, sep: bool) -> None:
    if word == "\n":
        f.write("\n")

    else:
        if sep:
            f.write(
                word[0]
                + "".join(random.sample(word[1:last_index], len(word[1:last_index])))
                + word[last_index:]
                + SEPARATOR
            )
        else:
            f.write(
                word[0]
                + "".join(random.sample(word[1:last_index], len(word[1:last_index])))
                + word[last_index:]
            )


with open(ORIGINAL_FILE, "r", encoding="utf-8") as of:
    with open(FILE_COPY, "w", encoding="utf-8") as fc:
        for line in of:
            words = line.strip(" ").split(SEPARATOR)
            for word in words:
                if word.isalpha():
                    write_to_file(fc, word, -1, True)
                else:
                    if "\n" in word:
                        write_to_file(fc, word, -2, False)
                    else:
                        write_to_file(fc, word, -2, True)
