from pathlib import Path

def leer_headers(carpeta_base="."):
    base = Path(carpeta_base)
    if not base.exists():
        raise FileNotFoundError(f"No existe la ruta: {base}")

    hea_files = sorted(base.glob("*.hea"))
    if not hea_files:
        print(f"No se han encontrado archivos .hea en: {base.resolve()}")
        return

    for hea in hea_files:
        print("=" * 80)
        print(f"ARCHIVO: {hea.name}")
        print("=" * 80)

        try:
            with hea.open("r", encoding="utf-8", errors="replace") as f:
                contenido = f.read().splitlines()

            if not contenido:
                print("(Archivo vacío)")
                continue

            for i, linea in enumerate(contenido, start=1):
                print(f"{i:03d}: {linea}")

        except Exception as e:
            print(f"Error leyendo {hea.name}: {e}")

        print()

if __name__ == "__main__":
    leer_headers(".")