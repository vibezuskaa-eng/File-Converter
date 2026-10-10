import os
from pathlib import Path
n1 = str(input("What's the path to the file:  "))
def seach(path):
    try:
        if not os.path.exists:
            print("error")
            return f"{n1} is not found"
        else:    
            question = int(input("What's the conversation?" \
            "[1] JPEG"
            "[2] PNG"
            "[3] WEBP"
            "[4] GIF"
            "[5] BMP"
            "[6] TIFF"
            "[7] HEIC"
            "[8] PDF"
            "[9] DOCX"
            "[10] DOC"
            "[11] TXT"
            "[12] RTF"
            "[13] ODT"
            "[14] XLSX"
            "[15] XLS"
            "[16] CSV"
            "[17] ODS"
            "[18] PPTX"
            "[19] PPT"
            "[20] ODP"
            "[21] EPUB"
            "[22] ZIP"
            "[23] RAR"
            "[24] 7Z"
            ))
    except Exception as e:
        print(f"Erro ao verificar caminho: {e}")
        return False
resultado = seach(n1)
print(resultado)