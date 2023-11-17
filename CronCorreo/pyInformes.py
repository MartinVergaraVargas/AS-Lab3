import os
import subprocess
from datetime import datetime

def obtener_fecha_actual():
    return datetime.now().strftime('%a %b %d %H:%M:%S %z %Y')

def ejecutar_comando(comando):
    resultado = subprocess.run(comando, shell=True, text=True, capture_output=True)
    return resultado.stdout

def generar_informe():
    informe = []

    informe.append(f"Bienvenido al Informe del sistema, hoy es: {obtener_fecha_actual()}\n\n")

    informe.append("Uso de CPU con el comando 'top -b -n 1 | head -n 36':\n")
    informe.append("======================================\n\n")
    informe.append(ejecutar_comando("top -b -n 1 | head -n 36"))

    informe.append("\n\nUso de RAM con el comando 'free -h':\n")
    informe.append("====================================\n\n")
    informe.append(ejecutar_comando("free -h"))

    informe.append("\n\nEspacio en disco con el comando 'df -h':\n")
    informe.append("========================================\n\n")
    informe.append(ejecutar_comando("df -h"))

    informe.append("\n\nUsuarios conectados actualmente usando el comando 'w':\n")
    informe.append("======================================================\n\n")
    informe.append(ejecutar_comando("w"))

    informe.append("\n\nÚltimos registros del sistema, usando 'journalctl -n 30':\n")
    informe.append("===============================================================\n\n")
    informe.append(ejecutar_comando("journalctl -n 30"))

    return ''.join(informe)

def guardar_informe(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)

if __name__ == "__main__":
    nombre_archivo = "Informe_del_sistema.txt"
    informe = generar_informe()
    guardar_informe(nombre_archivo, informe)

    print(f"Informe generado y guardado en {nombre_archivo}")
