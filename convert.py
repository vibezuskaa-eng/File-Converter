from pathlib import Path
import os

FORMATS = {
    1: "JPEG", 2: "PNG", 3: "WEBP", 4: "GIF", 5: "BMP", 6: "TIFF",
    7: "HEIC", 8: "PDF", 9: "DOCX", 10: "DOC", 11: "TXT", 12: "RTF",
    13: "ODT", 14: "XLSX", 15: "XLS", 16: "CSV", 17: "ODS", 18: "PPTX",
    19: "PPT", 20: "ODP", 21: "EPUB", 22: "ZIP", 23: "RAR", 24: "7Z",
}


def list_items(directory="."):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"Directory not found: {directory}")

        items = []

        for name in os.listdir(directory):
            path = os.path.join(directory, name)

            if os.path.isfile(path) or os.path.isdir(path):
                items.append(path)

        return items

    except Exception as e:
        print(f"Error while listing: {e}")
        return []


def print_items(items):
    for i, item in enumerate(items):
        name = os.path.basename(item)

        if os.path.isdir(item):
            print(f"{i}: [FOLDER] {name}")
        else:
            print(f"{i}: {name}")


def browse(start="."):
    current = os.path.abspath(start)

    while True:
        items = list_items(current)

        print(f"\nCurrent folder: {current}\n")

        if items:
            print_items(items)
        else:
            print("This folder is empty.")

        answer = input(
            "\nWhich file/folder do you want to select? (b = back, q = quit) "
        ).strip().lower()

        if answer == "q":
            return None

        if answer == "b":
            current = os.path.dirname(current)
            continue

        try:
            choice = int(answer)

            if choice < 0:
                raise IndexError

            chosen = items[choice]

        except ValueError:
            print("Enter a number.")
            continue

        except IndexError:
            print("That number doesn't exist.")
            continue

        # IF IT IS A FOLDER, GO INSIDE IT AND REPEAT
        if os.path.isdir(chosen):
            current = os.path.abspath(chosen)
        else:
            return os.path.abspath(chosen)


def ask_format():
    print("\nWhat's the conversion?\n")

    for number, name in FORMATS.items():
        print(f"[{number}] {name}")

    while True:
        raw = input("\nChoose a number: ").strip()

        try:
            number = int(raw)
        except ValueError:
            print("Enter a number.")
            continue

        if number in FORMATS:
            return FORMATS[number]

        print("That number doesn't exist.")


def search(path):
    try:
        if not os.path.exists(path):
            print(f"{path} was not found.")
            return None

        return ask_format()

    except Exception as e:
        print(f"Error while checking path: {e}")
        return None


if __name__ == "__main__":
    chosen_file = browse(".")

    if not chosen_file:
        print("\nNo file chosen.")
    else:
        print("\nChosen file:")
        print(chosen_file)

        target_format = search(chosen_file)

        if target_format:
            print(f"\nConvert {os.path.basename(chosen_file)} to {target_format}")