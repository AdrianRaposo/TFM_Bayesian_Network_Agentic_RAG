import os
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from config import *
import shutil

# Para que los resultados sean consistentes
DetectorFactory.seed = 0

# Carpeta raíz donde buscar archivos relacionados
CARPETA_RAIZ = r"C:\Users\adria\OneDrive\Documentos\TFM\TFM_Bayesian_Network_Agentic_RAG"

# Carpeta con los archivos a analizar
CARPETA_ARCHIVOS = RAW_DATA_PATH_MD_MISTRAL

# Carpeta donde mover los archivos no válidos
CARPETA_DESTINO = r"C:\Users\adria\OneDrive\Documentos\TFM\Extra\NoValidFiles"

LOG_FILE = r"C:\Users\adria\OneDrive\Documentos\TFM\Extra\NoValidFiles\resultado_log.txt"

# Idiomas permitidos: 'es' = español, 'en' = inglés
IDIOMAS_PERMITIDOS = {"es", "en"}


def detectar_idioma_archivo(ruta_archivo):
    """Detecta el idioma de un archivo de texto plano"""
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            texto = f.read()
            if not texto.strip():
                return "vacio"
            return detect(texto)
    except LangDetectException:
        return "indetectable"
    except Exception as e:
        return f"error: {e}"


def listar_archivos_relacionados(nombre_base, carpeta_raiz):
    """Lista todos los archivos en la carpeta raíz y subcarpetas que tengan el mismo nombre base"""
    relacionados = []
    for root, _, files in os.walk(carpeta_raiz):
        for archivo in files:
            if os.path.splitext(archivo)[0] == nombre_base:
                relacionados.append(os.path.join(root, archivo))
    return relacionados


def mover_archivo(ruta_archivo, carpeta_destino):
    """Mueve un archivo a la carpeta destino, manteniendo estructura de carpetas"""
    os.makedirs(carpeta_destino, exist_ok=True)
    try:
        nombre = os.path.basename(ruta_archivo)
        destino = os.path.join(carpeta_destino, nombre)
        # Si ya existe, renombrar para evitar sobrescritura
        if os.path.exists(destino):
            base, ext = os.path.splitext(nombre)
            contador = 1
            while os.path.exists(destino):
                destino = os.path.join(carpeta_destino, f"{base}_{contador}{ext}")
                contador += 1
        shutil.move(ruta_archivo, destino)
        return destino
    except Exception as e:
        return f"ERROR moviendo {ruta_archivo}: {e}"


def revisar_carpeta(archivos_carpeta, raiz_carpeta, carpeta_destino, log_file):
    """Revisa los archivos en 'archivos_carpeta', mueve los no válidos y guarda un log"""
    resultados = []

    with open(log_file, "w", encoding="utf-8") as log:
        for root, _, files in os.walk(archivos_carpeta):
            for archivo in files:
                ruta = os.path.join(root, archivo)
                if os.path.isfile(ruta):
                    idioma = detectar_idioma_archivo(ruta)
                    if idioma not in IDIOMAS_PERMITIDOS:
                        nombre_base = os.path.splitext(archivo)[0]
                        relacionados = listar_archivos_relacionados(nombre_base, raiz_carpeta)

                        # Guardar en resultados
                        resultados.append((ruta, idioma, relacionados))

                        # Escribir en log
                        log.write(f"- {ruta} → {idioma}\n")
                        log.write(f"  Archivos relacionados en la carpeta raíz ({len(relacionados)} encontrados):\n")
                        for rel in relacionados:
                            log.write(f"    * {rel}\n")
                        log.write("\n")

                        # Mover archivos
                        archivos_a_mover = [ruta] + relacionados
                        for file in set(archivos_a_mover):  # set() para evitar duplicados
                            if os.path.exists(file):  # evitar mover dos veces
                                mover_archivo(file, carpeta_destino)

    return resultados


if __name__ == "__main__":
    resultados = revisar_carpeta(CARPETA_ARCHIVOS, CARPETA_RAIZ, CARPETA_DESTINO, LOG_FILE)

    if resultados:
        print(f"Archivos movidos a '{CARPETA_DESTINO}' y log guardado en '{LOG_FILE}' ✅")
    else:
        print("Todos los archivos están en español o inglés ✅")
