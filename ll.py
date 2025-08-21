class F:
    def read(filename):
        with open(filename, "r", encoding="utf-8") as f:
            for linea in f:# iterar línea a línea (eficiente)
             print(linea.strip())

def write(filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Encabezado\n")
        f.writelines(["linea 1\n", "linea 2\n", "linea 3\n", "línea 4\n"])



F  = F()
F.read("note.txt")
F.write("note.txt")