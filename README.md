## Puntos Importantes del Programa

Este programa lo desarrollé para automatizar la búsqueda y análisis de vulnerabilidades web utilizando varias herramientas potentes. A continuación, detallo los puntos más importantes del programa:


### 1. Ejecución de Comandos
El programa utiliza la función `subprocess.run` para ejecutar comandos de las herramientas que utilizaremos y capturar sus salidas. Esto permite integrar los resultados de diferentes herramientas en un solo informe.

### 2. Funcionalidades Principales
El programa ofrece las siguientes funcionalidades principales:
- **Enumeración de Subdominios**: Utiliza `sublist3r` para enumerar subdominios de un dominio dado.
- **Escaneo de Vulnerabilidades SQL**: Utiliza `sqlmap` para escanear vulnerabilidades SQL en una URL dada.
- **Fuzzing de Rutas**: Utiliza `ffuf` para realizar fuzzing en las rutas de un sitio web utilizando un wordlist.
- **Escaneo de XSS**: Utiliza `XSStrike` para escanear vulnerabilidades XSS en una URL dada.
- **Verificación de SSL/TLS**: Utiliza `sslscan` para verificar la configuración SSL/TLS de un sitio web.

### 3. Generación de Informes
El programa genera un informe detallado con los resultados de las pruebas realizadas. El informe incluye la fecha y hora de generación y se guarda en un archivo con un nombre basado en la fecha y hora actuales.

### 4. Uso de Argumentos
El programa utiliza la biblioteca `argparse` para procesar los argumentos de la línea de comandos, permitiendo al usuario especificar la URL a escanear y las pruebas a realizar mediante opciones como `--subdomains`, `--vuln-scan`, `--fuzz`, `--xss`, y `--ssl`.

### 5. Entorno Aislado
Se recomienda ejecutar el programa en un entorno virtual de Python (`venv`) para evitar conflictos con el sistema principal y asegurar que todas las dependencias estén correctamente instaladas.

### 6. Dependencias
Las dependencias necesarias para ejecutar el programa están listadas en el archivo `requirements.txt` y se pueden instalar utilizando `pip`.

### 7. Advertencias y Responsabilidad
El programa está destinado a fines éticos y educativos. Se debe utilizar en entornos controlados y sin violar ninguna ley. El autor no se hace responsable del mal uso de la herramienta.


## PASOS:

LEE ATENTAMENTE:

## Paso 1: 
Debes tener Kali Linux con todas las herramientas instaladas, aunque en Kali ya vienen preinstaladas las herramientas que aquí usaremos, no está de más que lo revises y lo instales.
Además usaremos un entorno aislado para ejecutar Python3 sobre Kali y así no generar conflicto con el sistema principal más abajo detallo dichas herramientas y como ejecutar el main.py.

>[!NOTE]
>Las Herramientas que se usarán aquí son:
>'sublist3r', 
>'sqlmap',
>'ffuf', 
>'sslscan',
>'XSStrike'
>
>Pero las que debemos clonar dentro de la raíz de nuestro directorio de trabajo son XSStrike y sublist3r y las dependencias que están en el archivo requirements.txt que luego lo instalaremos.
>

## Paso 2:
Clona el repositorio dentro de Kali y ábrelo en tu editor favorito: 

## Paso 3: 
Debes instalar python3 y pip en el sistema principal (dentro de kali). Por lo general en kali ya vienen incorporados como mencioné. Pero en el caso de que no: 

```bash
sudo apt-get install pip
sudo apt-get install  python3
```

>[!IMPORTANT]
>RECUERDA CAMBIAR LAS RUTAS CON LAS TUYAS EN LAS 2 LÍNEAS xsstrike_path = "/home/kali/Documents/bugBounty/XSStrike/xsstrike.py" DENTRO DEL CÓDIGO main.py PARA QUE PUEDA LEER CORRECTAMENTE EL ARCHIVO.
>

## Paso 4:
Dentro de la terminal del mismo editor puedes abrir una consola y copia lo siguiente:

```bash
python3 -m venv venv
```
Eso crea una carpeta "venv" en la raíz del proyecto que es un entorno aislado para ejecutar python3 como mencioné al principio.

Luego copia:

```bash
source venv/bin/activate
```
Eso activa el VENV.
Se vé asi: ┌──(venv)─(kali㉿kali)-[path/hackingEtical]
                       └─$ |

Luego empezamos a instalar las herramientas y dependencias. Todos los "git clone" se deben hacer dentro de la misma raíz del proyecto, al clonar se crearan las carpetas correspondientes automáticamente.

Copia esto por separado en la consola:

```bash
git clone https://github.com/aboul3la/Sublist3r.git
cd Sublist3r
pip install -r requirements.txt
```

Volvemos atrás ya que nos manda a la carpeta de Sublist3r, entonces hacemos:
```bash
 cd ..
```

```bash
git clone https://github.com/s0md3v/XSStrike.git
cd XSStrike
pip install -r requirements.txt
```
Volvemos atrás: 
```bash
cd ..
```

Nos situamos en la raíz:

POR ÚLTIMO, PARA ASEGURAR, INSTALAMOS LAS DEPENDENCIAS:

```bash
pip install -r requirements.txt
```

 ## Debería quedar así toda la ESTRUCTURA:

```
📁HackingEtico/
    └── 📁Sublist3r
    └── 📁venv
    └── 📁XSStrike
    └── directory-list-2.3-medium.txt
    └── main.py
    └── requirements.txt
```
## Paso 5:
Para ejecutar el escaneo: 

```bash
python3 main.py --url "https://ejemplo.com" --subdomains --vuln-scan --fuzz --xss --ssl
```

Esperamos a que termine y listo. Con eso genera el informe con nombre y fecha dentro de la raíz donde veremos el resultado del análisis.

🚀⭐
