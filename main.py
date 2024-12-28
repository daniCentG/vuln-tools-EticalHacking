import subprocess
import shutil
from datetime import datetime
import os

# Verificar si las herramientas necesarias están instaladas
def check_tools():
    tools = [
        'sublist3r', 
        'sqlmap',
        'ffuf', 
        'sslscan'
    ]
    for tool in tools:
        if not shutil.which(tool):
            print(f"Error: {tool} no está instalado o no está en el PATH.")
            return False

    # Verificar XSStrike específicamente
    xsstrike_path = "/home/kali/Documents/bugBounty/XSStrike/xsstrike.py"
    if not os.path.isfile(xsstrike_path):
        print("Error: XSStrike no está instalado o la ruta es incorrecta.")
        return False

    return True

# Función para ejecutar un comando de subprocess y capturar la salida
def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando {' '.join(command)}: {e}")
        return None

# Función para realizar escaneo de subdominios
def enumerate_subdomains(url):
    print(f"Enumerando subdominios para {url}...")
    return run_command(['sublist3r', '-d', url, '-o', 'subdomains.txt'])

# Función para escanear vulnerabilidades SQL
def scan_vulnerabilities(url):
    print(f"Escaneando vulnerabilidades SQL para {url}...")
    return run_command(['sqlmap', '-u', url, '--batch', '--level=5', '--risk=3'])

# Función para realizar fuzzing en las rutas
def perform_fuzzing(url):
    print(f"Realizando fuzzing en {url}...")
    wordlist_path = './directory-list.txt'
    if not os.path.isfile(wordlist_path):
        print(f"Error: No se encontró el wordlist en {wordlist_path}.")
        return None
    return run_command(['ffuf', '-u', f"{url}/FUZZ", '-w', wordlist_path])

# Función para escanear XSS
def scan_xss(url):
    print(f"Escaneando XSS en {url}...")
    xsstrike_path = "/home/kali/Documents/bugBounty/XSStrike/xsstrike.py"
    return run_command(['python3', xsstrike_path, '-u', url, '--crawl'])

# Función para verificar SSL/TLS
def check_ssl(url):
    print(f"Verificando SSL/TLS para {url}...")
    return run_command(['sslscan', url])

# Función para realizar un análisis de seguridad completo
def security_scan(url, args):
    results = {}

    if args.subdomains:
        results['subdomains'] = enumerate_subdomains(url)
    if args.vuln_scan:
        results['vulnerabilities'] = scan_vulnerabilities(url)
    if args.fuzz:
        results['fuzzing'] = perform_fuzzing(url)
    if args.xss:
        results['xss'] = scan_xss(url)
    if args.ssl:
        results['ssl'] = check_ssl(url)

    return results

# Función principal para la ejecución
def main(args):
    if not check_tools():
        return

    url = args.url
    report_filename = f"report_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

    print(f"Generando informe de seguridad para {url}...")
    results = security_scan(url, args)

    with open(report_filename, 'w') as f:
        f.write(f"Informe de seguridad para {url}\n")
        f.write(f"Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("Resultados de las pruebas:\n")
        for key, value in results.items():
            f.write(f"{key.capitalize()}:\n{value}\n\n")

    print(f"Informe generado: {report_filename}")

# Función para procesar los argumentos
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Escaneo de seguridad en el sitio web.")
    parser.add_argument("--url", required=True, help="URL del sitio web a escanear")
    parser.add_argument("--subdomains", action="store_true", help="Escanear subdominios")
    parser.add_argument("--vuln-scan", action="store_true", help="Escanear vulnerabilidades SQL")
    parser.add_argument("--fuzz", action="store_true", help="Realizar fuzzing")
    parser.add_argument("--xss", action="store_true", help="Escanear vulnerabilidades XSS")
    parser.add_argument("--ssl", action="store_true", help="Verificar SSL/TLS")

    args = parser.parse_args()
    main(args)