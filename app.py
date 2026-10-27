
import os
import subprocess
import sys

# ============================================================
# 1. CONFIGURACIÓN
# ============================================================

# Ruta de la tarjeta SD de tu PSP
RUTA_PSP = r"D:\ISO"
os.makedirs(RUTA_PSP, exist_ok=True)

# Rutas del ejecutable mCISO y directorio temporal
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
TEMP_DIR = os.environ.get("TEMP", DIRECTORIO_ACTUAL)
MCISO_EXE = os.path.join(DIRECTORIO_ACTUAL, "mciso.exe")

# Comprobar que mciso.exe está disponible
if not os.path.isfile(MCISO_EXE):
    print("ERROR: No se encuentra 'mciso.exe'.")
    print(f"Colócalo en la carpeta del script: {DIRECTORIO_ACTUAL}")
    sys.exit(1)

# Repositorios de Internet Archive
REPOS = [
    "psp_20220507",
    "psp_20220507_2",
]

# ============================================================
# 2. LISTA DE JUEGOS
# ============================================================

JUEGOS = [
    "Grand Theft Auto - Chinatown Wars (Europe) (En,Fr,De,Es,It).cso",
    "Virtua Tennis 3 (Europe) (En,Fr,De,Es,It).cso",
    "Simpson, Los - El Videojuego (Spain).cso",
    "Lumines - Puzzle Fusion (Europe) (En,Fr,De,Es,It).cso",
    "Grand Theft Auto - Liberty City Stories (Europe) (En,Fr,De,Es,It) (v3.00).cso",
    "Grand Theft Auto - Vice City Stories (Europe) (En,Fr,De,Es,It).cso",
    "Patapon (Europe) (En,Fr,De,Es,It).cso",
    "Tekken 6 (Europe) (En,Ja,Fr,De,Es,It,Ko,Ru).cso",
    "Monster Hunter Freedom Unite (Europe) (En,Fr,De,Es,It).cso",
    "Daxter (Europe) (En,Fr,De,Es,It).cso",
    "Metal Gear Solid - Peace Walker (Europe, Australia) (En,Fr,De,Es,It).cso",
    "Castlevania - The Dracula X Chronicles (Europe) (En,Fr,De,Es,It).cso",
    "LocoRoco 2 (Europe) (En,Fr,De,Es,It,Nl,Pt,Sv,No,Da,Fi,Ru).cso",
    "Gran Turismo (Europe) (En,Fr,De,Es,It,Nl,Pt,Ru) (v2.00).cso",
    "Silent Hill Origins (Europe) (En,Fr,De,Es,It).cso",
    "Resistance - Retribution (Europe) (En,Fr,De,Es,It).cso",
    "Dragon Ball Z - Tenkaichi Tag Team (Europe) (En,Fr,De,Es,It).cso",
    "Dante's Inferno (Spain).cso",
    "Crisis Core - Final Fantasy VII (Spain).cso",
    "Burnout Dominator (Europe) (En,Fr,De,Es,It).cso",
    "Assassin's Creed - Bloodlines (Europe) (En,Fr,De,Es,It,Ru).cso",
    "Need for Speed - Most Wanted - 5-1-0 (Europe) (En,Fr,De,Es,It).cso",
]


# ============================================================
# 3. CONVERSIÓN CSO A ISO
# ============================================================

def convertir_cso_a_iso(archivo_cso, archivo_iso):
    """
    Convierte un CSO a ISO usando mCISO.
    La ISO se genera primero en un archivo temporal
    para evitar dejar un resultado incompleto.
    """

    archivo_parcial = archivo_iso + ".partial"

    try:
        if os.path.exists(archivo_parcial):
            os.remove(archivo_parcial)

        comando = [
            MCISO_EXE,
            "0",
            archivo_cso,
            archivo_parcial,
        ]

        subprocess.run(comando, check=True)

        if (
            not os.path.isfile(archivo_parcial)
            or os.path.getsize(archivo_parcial) == 0
        ):
            raise RuntimeError(
                "mCISO no ha generado una ISO válida."
            )

        # No sobrescribir una ISO que ya exista
        if os.path.exists(archivo_iso):
            print(
                f"AVISO: La ISO ya existe y no se sobrescribirá: "
                f"{archivo_iso}"
            )
            return False

        os.replace(archivo_parcial, archivo_iso)
        return True

    except subprocess.CalledProcessError as error:
        print(f"ERROR de mCISO: {error}")
        return False

    except OSError as error:
        print(f"ERROR de archivos durante la conversión: {error}")
        return False

    except RuntimeError as error:
        print(f"ERROR de conversión: {error}")
        return False

    finally:
        if os.path.exists(archivo_parcial):
            try:
                os.remove(archivo_parcial)
            except OSError as error:
                print(
                    "AVISO: No se pudo eliminar el archivo parcial: "
                    f"{error}"
                )


# ============================================================
# 4. BUCLE AUTOMATIZADO
# ============================================================

def main():
    total = len(JUEGOS)

    estadisticas = {
        "correctos": 0,
        "omitidos": 0,
        "fallidos": 0,
    }

    for indice, juego_cso in enumerate(JUEGOS, start=1):
        print("=" * 60)
        print(f"[{indice}/{total}] Procesando: {juego_cso}")

        tmp_cso_path = os.path.join(TEMP_DIR, juego_cso)
        destino_iso_path = os.path.join(
            RUTA_PSP,
            juego_cso[:-4] + ".iso",
        )

        # Comprobar si la ISO ya existe
        if os.path.exists(destino_iso_path):
            print(
                "--> ¡OMITIDO! El juego ya existe en tu tarjeta SD: "
                f"{destino_iso_path}"
            )
            estadisticas["omitidos"] += 1
            continue

        descargado = False

        try:
            # =================================================
            # DESCARGA ORIGINAL: SE MANTIENE SIN CAMBIOS
            # =================================================

            for repo in REPOS:
                print(
                    f"Intentando descargar desde '{repo}' con 'ia'..."
                )

                cmd_ia = [
                    "ia",
                    "download",
                    repo,
                    juego_cso,
                    "--dest",
                    TEMP_DIR,
                    "--no-directories",
                ]

                resultado = subprocess.run(cmd_ia)

                if os.path.exists(tmp_cso_path):
                    descargado = True
                    break

            # =================================================
            # COMPROBACIÓN DEL ARCHIVO DESCARGADO
            # =================================================

            if not descargado:
                print(
                    "ERROR: No se pudo encontrar o descargar "
                    f"'{juego_cso}' en ninguno de los repositorios."
                )
                estadisticas["fallidos"] += 1
                continue

            if os.path.getsize(tmp_cso_path) == 0:
                print("ERROR: El archivo descargado está vacío.")
                estadisticas["fallidos"] += 1
                continue

            # =================================================
            # CONVERSIÓN
            # =================================================

            print("Convirtiendo a ISO mediante mCISO...")

            if convertir_cso_a_iso(
                tmp_cso_path,
                destino_iso_path,
            ):
                print(
                    "--> ¡Guardado con éxito en tu PSP!: "
                    f"{destino_iso_path}"
                )
                estadisticas["correctos"] += 1
            else:
                estadisticas["fallidos"] += 1

        except KeyboardInterrupt:
            print("\nProceso interrumpido por el usuario.")
            raise

        except Exception as error:
            print(f"ERROR procesando '{juego_cso}': {error}")
            estadisticas["fallidos"] += 1

        finally:
            # Eliminar el CSO temporal, como en el código original
            if os.path.exists(tmp_cso_path):
                try:
                    os.remove(tmp_cso_path)
                    print("Archivo temporal eliminado.")
                except OSError as error:
                    print(
                        "AVISO: No se pudo eliminar el archivo "
                        f"temporal: {error}"
                    )

    # ========================================================
    # 5. RESUMEN FINAL
    # ========================================================

    print("=" * 60)
    print("¡Proceso finalizado!")
    print(f"Juegos procesados: {total}")
    print(f"Convertidos correctamente: {estadisticas['correctos']}")
    print(f"Omitidos porque ya existían: {estadisticas['omitidos']}")
    print(f"Fallidos: {estadisticas['fallidos']}")
    print(f"Destino: {RUTA_PSP}")
    print("=" * 60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma detenido.")
        sys.exit(130)
