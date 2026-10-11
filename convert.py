import os
import shutil
import subprocess
 
from PIL import Image
from PIL import UnidentifiedImageError
 
FORMATS = {
    1: "JPEG", 2: "PNG", 3: "WEBP", 4: "GIF", 5: "BMP", 6: "TIFF",
    7: "HEIC", 8: "PDF", 9: "DOCX", 10: "DOC", 11: "TXT", 12: "RTF",
    13: "ODT", 14: "XLSX", 15: "XLS", 16: "CSV", 17: "ODS", 18: "PPTX",
    19: "PPT", 20: "ODP", 21: "EPUB", 22: "ZIP", 23: "RAR", 24: "7Z",
}
 
# Each family = a group of formats that are converted with the same method.
FAMILY_FORMATS = {
    "image": {"JPEG", "PNG", "WEBP", "GIF", "BMP", "TIFF"},
    "document": {"DOCX", "DOC", "TXT", "RTF", "ODT"},
    "spreadsheet": {"XLSX", "XLS", "CSV", "ODS"},
    "presentation": {"PPTX", "PPT", "ODP"},
}
 
# Extension of the chosen file -> its family.
SOURCE_EXTENSIONS = {
    ".jpg": "image", ".jpeg": "image", ".png": "image", ".webp": "image",
    ".gif": "image", ".bmp": "image", ".tif": "image", ".tiff": "image",
    ".docx": "document", ".doc": "document", ".odt": "document",
    ".rtf": "document", ".txt": "document",
    ".xlsx": "spreadsheet", ".xls": "spreadsheet", ".ods": "spreadsheet",
    ".csv": "spreadsheet",
    ".pptx": "presentation", ".ppt": "presentation", ".odp": "presentation",
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
 
 
# ---------------------------------------------------------------
# CONVERSION PART
# ---------------------------------------------------------------
 
def build_new_path(path, target_format):
    # splitext on the FULL path keeps the folder, so the new file
    # is created next to the original one.
    root, _ = os.path.splitext(path)
    return f"{root}.{target_format.lower()}"
 
 
def get_family(path):
    # Look at the extension of the file and say which family it is.
    _, extension = os.path.splitext(path)
    return SOURCE_EXTENSIONS.get(extension.lower())
 
 
def convert_image(path, new_path, target_format):
    # Pillow: open the image, adjust the colors if needed, save.
    try:
        image = Image.open(path)
 
        # JPEG has no transparency, so only JPEG needs this step.
        if target_format == "JPEG":
            image = image.convert("RGB")
 
        image.save(new_path, format=target_format)
        return True
 
    except UnidentifiedImageError:
        print("This file is not an image.")
        return False
 
    except OSError as e:
        print(f"Could not save the image: {e}")
        return False
 
 
def convert_with_libreoffice(path, new_path, target_format):
    # LibreOffice converts documents, spreadsheets and presentations.
    program = shutil.which("soffice") or shutil.which("libreoffice")
 
    if not program:
        print("LibreOffice was not found. Install it to convert this file.")
        return False
 
    folder = os.path.dirname(path)
 
    result = subprocess.run(
        [program, "--headless", "--convert-to", target_format.lower(),
         "--outdir", folder, path],
        capture_output=True,
        text=True,
    )
 
    if result.returncode != 0 or not os.path.exists(new_path):
        print(f"LibreOffice could not convert this file: {result.stderr.strip()}")
        return False
 
    return True
 
 
def convert(path, target_format):
    # 1. Which family is the chosen file?
    family = get_family(path)
 
    if family is None:
        print("This file type is not supported yet.")
        return False
 
    # 2. Can this family become the chosen format?
    allowed = set(FAMILY_FORMATS[family])
 
    if family != "image":
        allowed.add("PDF")  # LibreOffice can export all of these to PDF
 
    if target_format not in allowed:
        print(f"A {family} file can't be converted to {target_format} (yet).")
        return False
 
    # 3. Build the new path and protect an existing file.
    new_path = build_new_path(path, target_format)
 
    if os.path.exists(new_path):
        print(f"{os.path.basename(new_path)} already exists. Nothing was changed.")
        return False
 
    print(f"\nConvert {os.path.basename(path)} to {os.path.basename(new_path)}")
 
    # 4. Send the file to the right method.
    if family == "image":
        done = convert_image(path, new_path, target_format)
    else:
        done = convert_with_libreoffice(path, new_path, target_format)
 
    if done:
        print("Done!")
 
    return done
 
 
if __name__ == "__main__":
    chosen_file = browse(".")
 
    if not chosen_file:
        print("\nNo file chosen.")
    else:
        print("\nChosen file:")
        print(chosen_file)
 
        target_format = search(chosen_file)
 
        if target_format:
            convert(chosen_file, target_format)