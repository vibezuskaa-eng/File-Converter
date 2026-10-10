import os
from pathlib import Path

import os


def listar_itens(diretorio="."):
    try:
        if not os.path.isdir(diretorio):
            raise FileNotFoundError(f"Diretório não encontrado: {diretorio}")

        itens = []

        for nome in os.listdir(diretorio):
            caminho = os.path.join(diretorio, nome)

            if os.path.isfile(caminho) or os.path.isdir(caminho):
                itens.append(caminho)

        return itens

    except Exception as e:
        print(f"Erro ao listar: {e}")
        return []


if __name__ == "__main__":
    caminho = "."

    itens = listar_itens(caminho)

    if not itens:
        print("Nenhum arquivo ou pasta encontrado.")

    else:
        print("Itens encontrados:\n")

        for i, item in enumerate(itens):
            nome = os.path.basename(item)

            if os.path.isdir(item):
                print(f"{i}: [PASTA] {nome}")
            else:
                print(f"{i}: {nome}")

        try:
            escolha = int(input("\nQual arquivo/pasta vc quer puxar? "))

            caminho_escolhido = itens[escolha]

            print("\nCaminho escolhido:")
            print(os.path.abspath(caminho_escolhido))

            # SE FOR UMA PASTA
            if os.path.isdir(caminho_escolhido):

                arquivos = listar_itens(caminho_escolhido)

                print("\nConteúdo da pasta:\n")

                for i, arquivo in enumerate(arquivos):
                    nome = os.path.basename(arquivo)

                    if os.path.isdir(arquivo):
                        print(f"{i}: [PASTA] {nome}")
                    else:
                        print(f"{i}: {nome}")

                try:
                    escolha_arquivo = int(
                        input("\nQual arquivo/pasta vc quer puxar? ")
                    )

                    arquivo_escolhido = arquivos[escolha_arquivo]

                    print("\nArquivo escolhido:")
                    print(os.path.abspath(arquivo_escolhido))

                except ValueError:
                    print("Digite um número.")

                except IndexError:
                    print("Esse número não existe.")

        except ValueError:
            print("Digite um número.")

        except IndexError:
            print("Esse número não existe.")

def listar_itens(diretorio="."):
    try:
        if not os.path.isdir(diretorio):
            raise FileNotFoundError(f"Diretório não encontrado: {diretorio}")

        itens = []

        for nome in os.listdir(diretorio):
            caminho = os.path.join(diretorio, nome)

            if os.path.isfile(caminho) or os.path.isdir(caminho):
                itens.append(caminho)

        return itens

    except Exception as e:
        print(f"Erro ao listar: {e}")
        return []


if __name__ == "__main__":
    caminho = "."

    itens = listar_itens(caminho)

    if not itens:
        print("Nenhum arquivo ou pasta encontrado.")

    else:
        print("Itens encontrados:\n")

        for i, item in enumerate(itens):
            nome = os.path.basename(item)

            if os.path.isdir(item):
                print(f"{i}: [PASTA] {nome}")
            else:
                print(f"{i}: {nome}")

        try:
            escolha = int(input("\nQual arquivo/pasta vc quer puxar? "))

            caminho_escolhido = itens[escolha]

            print("\nCaminho escolhido:")
            print(os.path.abspath(caminho_escolhido))

            # SE FOR UMA PASTA
            if os.path.isdir(caminho_escolhido):

                arquivos = listar_itens(caminho_escolhido)

                print("\nConteúdo da pasta:\n")

                for i, arquivo in enumerate(arquivos):
                    nome = os.path.basename(arquivo)

                    if os.path.isdir(arquivo):
                        print(f"{i}: [PASTA] {nome}")
                    else:
                        print(f"{i}: {nome}")

                try:
                    escolha_arquivo = int(
                        input("\nQual arquivo/pasta vc quer puxar? ")
                    )

                    arquivo_escolhido = arquivos[escolha_arquivo]

                    print("\nArquivo escolhido:")
                    print(os.path.abspath(arquivo_escolhido))

                except ValueError:
                    print("Digite um número.")

                except IndexError:
                    print("Esse número não existe.")

        except ValueError:
            print("Digite um número.")

        except IndexError:
            print("Esse número não existe.")
            
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