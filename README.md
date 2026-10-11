# File Browser & Converter Menu | File Converter

A small Python terminal program that lets you browse your folders, pick a file, choose a format, and convert the file. The new file is saved next to the original one.

> **Project status:** work in progress. Images can be converted with Pillow. Documents, spreadsheets and presentations are converted with LibreOffice. Archives, HEIC and EPUB are not supported yet (see [Roadmap](#roadmap)).

## Features

- Browse folders and files directly in the terminal
- Go inside folders as deep as you want, and go back with `b`
- Quit at any time with `q`
- Input validation: wrong numbers or letters never crash the program
- Real conversion, organized by file families (image, document, spreadsheet, presentation)
- Rejects conversions that make no sense (for example, a photo to DOCX)
- Never overwrites a file that already exists
- The converted file is saved in the same folder as the original

## Requirements

- Python 3.8 or newer
- [Pillow](https://pypi.org/project/pillow/) for images:

  ```bash
  pip install pillow
  ```

- [LibreOffice](https://www.libreoffice.org/) for documents, spreadsheets and presentations (only needed for those types)

## How to run

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   cd YOUR-REPOSITORY
   ```

2. Install the requirements (see above).

3. Run the script:

   ```bash
   python browse_items.py
   ```

## How to use

1. The program lists the files and folders of the current folder. Folders are marked with `[FOLDER]`.
2. Type the number of a file or folder and press Enter.
   - If you pick a **folder**, the program opens it and lists its contents.
   - If you pick a **file**, the program shows its full path and moves on to the format menu.
3. Type `b` to go back one folder, or `q` to quit. Going back only changes the folder you are looking at. It does not create or move anything.
4. Choose a number from the format menu.
5. The program converts the file and creates the new one in the same folder.

### Example

```text
Current folder: /home/user/documents

0: [FOLDER] photos
1: report.docx
2: notes.txt

Which file/folder do you want to select? (b = back, q = quit) 1

Chosen file:
/home/user/documents/report.docx

What's the conversion?

[1] JPEG
[2] PNG
...
[24] 7Z

Choose a number: 8

Convert report.docx to report.pdf
Done!
```

## How the conversion works

Every file belongs to a **family**. Each family uses one method, so the program does not need one piece of code per format.

| Family | Source extensions | Target formats | Method |
|---|---|---|---|
| Image | JPG, JPEG, PNG, WEBP, GIF, BMP, TIF, TIFF | JPEG, PNG, WEBP, GIF, BMP, TIFF | Pillow |
| Document | DOCX, DOC, ODT, RTF, TXT | DOCX, DOC, ODT, RTF, TXT, PDF | LibreOffice |
| Spreadsheet | XLSX, XLS, ODS, CSV | XLSX, XLS, ODS, CSV, PDF | LibreOffice |
| Presentation | PPTX, PPT, ODP | PPTX, PPT, ODP, PDF | LibreOffice |

Steps inside the program:

1. Find the family of the chosen file from its extension.
2. Check that the chosen format is allowed for that family.
3. Build the new path and stop if the file already exists.
4. Send the file to the right method (Pillow or LibreOffice).

## Not supported yet

- HEIC (needs the `pillow-heif` package)
- EPUB
- ZIP, RAR and 7Z
- PDF as the **source** file

The menu still shows these options. If you choose one, the program says it is not supported yet and changes nothing.

## Project structure

```text
.
├── browse_items.py   # file browser, format menu and conversion
└── README.md
```

## Roadmap

- [x] Browse folders and pick a file
- [x] Convert images with Pillow (JPEG, PNG, WEBP, GIF, BMP, TIFF)
- [x] Convert documents, spreadsheets and presentations with LibreOffice
- [x] Save the converted file next to the original
- [x] Never overwrite an existing file
- [ ] Show only the formats that make sense for the selected file
- [ ] Support HEIC
- [ ] Handle archives (ZIP, RAR, 7Z)
- [ ] Support EPUB
- [ ] Convert PDF files
- [ ] Convert several files in one run

## Contributing

Suggestions and pull requests are welcome. Open an issue first to talk about what you would like to change.

## License

Add a license here (for example [MIT](https://choosealicense.com/licenses/mit/)).
