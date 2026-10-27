# 🎮 PSP Auto Downloader & CSO Converter

[🇪🇸 Español](#español) · [🇬🇧 English](#english)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Windows-blue.svg)](#)

> **¡Automatiza la descarga y conversión de tus juegos de PSP a formato ISO!** 🚀
>
> Un script automatizado en Python que busca archivos de PSP en los repositorios configurados de Internet Archive, descarga los archivos comprimidos `.cso`, los convierte a formato `.iso` utilizando `mciso.exe` y guarda los resultados directamente en la carpeta de destino de tu Memory Stick o tarjeta SD.
>
> **¡Ahora `mciso.exe` viene incluido en el proyecto!** No necesitas buscarlo ni descargarlo por separado.

---

## Español

## 🌟 Características

- 🔍 **Búsqueda Multi-Repo:** Busca archivos en los repositorios `psp_20220507` y `psp_20220507_2`.
- ⚡ **Conversión Automática:** Utiliza `mciso.exe` para convertir archivos `.cso` a `.iso`.
- 💾 **Destino Configurable:** Guarda las ISO en la carpeta que elijas, por ejemplo, `D:\ISO`.
- 🔄 **Detección de ISO Existentes:** Omite los juegos que ya tienen una ISO en la carpeta de destino.
- 🧹 **Limpieza Automática:** Elimina los archivos CSO temporales según el flujo de procesamiento del script.
- 🛡️ **Conversión Más Segura:** Utiliza un archivo temporal durante la conversión para reducir el riesgo de dejar una ISO incompleta con el nombre definitivo.
- 📦 **Conversor Incluido:** `mciso.exe` se distribuye junto al script para facilitar la instalación.
- 📊 **Seguimiento del Proceso:** Muestra información sobre los juegos que se procesan y el resultado final.

---

## 🛠️ Requisitos Previos

Antes de empezar, asegúrate de tener lo siguiente:

1. **Windows 10 o Windows 11.**
2. **Python 3.8 o superior**, necesario para ejecutar el script.
3. **Una tarjeta Memory Stick o SD de PSP**, o una carpeta de destino con espacio suficiente.
4. **Conexión a Internet** para descargar los archivos.

No necesitas descargar `mciso.exe` por separado: viene incluido en el repositorio.

---

## 🚀 Instalación y Configuración Paso a Paso

### 1. Instalar Python

Si ya tienes Python 3.8 o superior instalado, puedes saltarte este paso.

1. Entra en la página oficial: [Descargar Python](https://www.python.org/downloads/).
2. Descarga una versión compatible con Windows.
3. Abre el instalador.
4. **Importante:** marca la casilla **“Add Python to PATH”** antes de continuar.
5. Pulsa **Install Now** y espera a que termine la instalación.

Para comprobar que se ha instalado correctamente:

1. Abre el menú Inicio de Windows.
2. Escribe `cmd` y abre el símbolo del sistema.
3. Ejecuta:

   ```bash
   python --version
   ```

Deberías ver una versión de Python, por ejemplo, `Python 3.12.x`.

Si el comando no funciona, prueba:

```bash
py --version
```

### 2. Descargar el proyecto

Tienes dos opciones. Si eres principiante, te recomendamos la primera.

#### Opción A: Descargar el proyecto como ZIP (recomendada)

1. Abre la página del repositorio en GitHub.
2. Pulsa el botón verde **Code**.
3. Selecciona **Download ZIP**.
4. Cuando termine la descarga, haz clic derecho sobre el archivo ZIP y selecciona **Extraer todo**.
5. Abre la carpeta extraída.

Dentro encontrarás los archivos del proyecto, incluido `mciso.exe`.

#### Opción B: Clonar el repositorio con Git

Si tienes Git instalado, abre una terminal y ejecuta los siguientes comandos:

```bash
git clone https://github.com/PepeXarli/PSP-Auto-Downloader.git
cd PSP-Auto-Downloader
```

### 3. Comprobar los archivos descargados

Después de descargar y extraer el proyecto, comprueba que la carpeta tenga una estructura parecida a esta:

```text
PSP-Auto-Downloader/
├── app.py
├── mciso.exe
├── README.md
├── LICENSE
├── LICENSE-mciso.txt
└── THIRD_PARTY_NOTICES.md
```

Los nombres pueden variar según cómo hayas llamado a tu script.

- `app.py`: el script de Python.
- `mciso.exe`: la herramienta de conversión incluida.
- `README.md`: este archivo de instrucciones.
- `LICENSE`: la licencia de tu propio proyecto, si corresponde.
- `LICENSE-mciso.txt`: el texto de la licencia GPL-3.0 de mciso.
- `THIRD_PARTY_NOTICES.md`: los avisos de licencia y créditos del programa de terceros.

**Importante:** conserva los avisos de licencia que acompañan a `mciso`. No sustituyas su licencia por la MIT de tu propio código. Antes de publicar el ejecutable, comprueba que su redistribución cumple las condiciones de la licencia aplicable.

### 4. Instalar Internet Archive CLI

La herramienta `ia` permite al script solicitar archivos a Internet Archive.

1. Abre el menú Inicio de Windows.
2. Escribe `cmd` y abre el símbolo del sistema.
3. Ejecuta:

   ```bash
   python -m pip install --upgrade internetarchive
   ```

4. Espera a que finalice la instalación.

Comprueba que funciona con:

```bash
ia --version
```

Si Windows no reconoce el comando `ia`, cierra y vuelve a abrir la terminal. Si el problema continúa, revisa la instalación de Python y la configuración de PATH.

### 5. Configurar Internet Archive

Si necesitas autenticarte para acceder a los archivos, puedes configurar tus credenciales.

1. Crea una cuenta o inicia sesión en [Internet Archive](https://archive.org/).
2. Abre el símbolo del sistema.
3. Ejecuta:

   ```bash
   ia configure
   ```

4. Sigue las instrucciones que aparezcan en pantalla.

No compartas tus credenciales ni las publiques en GitHub. La autenticación no garantiza que todos los archivos estén disponibles; eso depende del repositorio y de sus permisos.

### 6. Configurar la carpeta de destino

Ahora debes indicarle al script dónde quieres guardar los archivos ISO.

1. Abre el archivo Python con un editor de texto, como el Bloc de notas o [Visual Studio Code](https://code.visualstudio.com/).
2. Busca la variable `RUTA_PSP`.
3. Cambia la ruta para que coincida con la carpeta de destino de tu ordenador.

Por ejemplo:

```python
RUTA_PSP = r"D:\ISO"
```

Si tu tarjeta utiliza la letra `E:`, podrías configurarla así:

```python
RUTA_PSP = r"E:\ISO"
```

La carpeta puede estar en tu ordenador o en la tarjeta de memoria de la PSP.

> 💡 **Consejo:** asegúrate de que la unidad correcta esté conectada y tenga suficiente espacio libre antes de comenzar.

### 7. Personalizar la lista de juegos (opcional)

El script contiene una lista llamada `JUEGOS` con los nombres de los archivos `.cso` que quieres descargar.

Puedes añadir o eliminar elementos de esa lista. Conserva los nombres exactos de los archivos, incluida la extensión `.cso`, para que coincidan con los almacenados en Internet Archive.

Si no quieres modificar la lista, puedes dejarla como está.

---

## 🎮 Cómo ejecutar el script

Una vez completados los pasos anteriores:

1. Abre la carpeta donde se encuentran el script Python y `mciso.exe`.
2. Haz clic en la barra de direcciones del Explorador de archivos, escribe `cmd` y pulsa Enter.
3. En la terminal que se abre, ejecuta:

   ```bash
   python app.py
   ```

   Si tu script tiene otro nombre, sustituye `app.py` por el nombre correspondiente. Por ejemplo:

   ```bash
   python psp_converter.py
   ```

4. Espera a que termine el procesamiento. El tiempo dependerá de la conexión, el tamaño de los archivos y la velocidad del ordenador.

### ¿Qué hará el programa?

- Buscará cada archivo en los repositorios configurados.
- Intentará descargar el archivo CSO.
- Convertirá el archivo descargado a ISO.
- Omitirá las ISO que ya existan en la carpeta de destino.
- Eliminará los archivos temporales según el flujo de procesamiento del script.
- Mostrará información sobre el resultado del proceso.

> ⚠️ No cierres la ventana mientras el programa esté descargando o convirtiendo archivos.

---

## ❓ Solución de problemas

### `python` no se reconoce como comando

Python puede no estar instalado correctamente o no estar añadido a PATH. Prueba:

```bash
py --version
```

Si funciona, intenta ejecutar el script con:

```bash
py app.py
```

### `ia` no se reconoce como comando

Comprueba que Internet Archive CLI esté instalado:

```bash
python -m pip install --upgrade internetarchive
```

Cierra y vuelve a abrir la terminal después de instalarlo.

### No se encuentra `mciso.exe`

Comprueba que `mciso.exe` esté en la misma carpeta que el script Python y que el nombre del archivo sea exactamente el esperado.

Si has descargado el proyecto como ZIP, comprueba que la descarga incluya el ejecutable.

### No se descarga un juego

Puede que el nombre del archivo no coincida exactamente, que el repositorio no esté disponible o que el archivo no pueda descargarse con los permisos actuales. Comprueba los mensajes de la terminal y la disponibilidad del archivo en Internet Archive.

### La conversión falla

Comprueba que el archivo CSO se haya descargado correctamente, que haya suficiente espacio libre y que `mciso.exe` esté presente y funcione correctamente.

---

## 📚 Fuentes de datos (repositorios)

El script busca automáticamente en los repositorios configurados:

- 📁 **Repositorio 1:** [psp_20220507](https://archive.org/download/psp_20220507)
- 📁 **Repositorio 2:** [psp_20220507_2](https://archive.org/download/psp_20220507_2)

La disponibilidad de los archivos y las condiciones de acceso pueden cambiar con el tiempo.

---

## 🤝 Agradecimientos y créditos

- [**sindastra / psp-mciso**](https://github.com/sindastra/psp-mciso): por la herramienta `mciso` utilizada para convertir archivos CSO.
- [**Internet Archive**](https://archive.org/): por sus servicios de preservación y alojamiento de archivos digitales.

`mciso.exe` es software de terceros y no ha sido creado por este proyecto. Consulta los avisos de terceros y la licencia original para conocer las condiciones aplicables.

---

## ⚖️ Aviso legal

Este proyecto se proporciona con fines educativos y de preservación de software.

El usuario es responsable de comprobar que tiene derecho a descargar, almacenar y convertir los archivos que utilice. Respeta los derechos de autor, las condiciones de uso de Internet Archive y la legislación aplicable en tu país.

Este proyecto no aloja ni incluye directamente archivos de juegos. El script utiliza la herramienta `ia` para solicitar archivos a los repositorios configurados.

El autor no se hace responsable del uso indebido del programa ni de las consecuencias derivadas de su utilización.

---

## 📄 Licencias

El código original de este proyecto puede distribuirse bajo la licencia MIT, siempre que seas titular de los derechos correspondientes y mantengas los avisos requeridos.

El ejecutable `mciso.exe` es un componente de terceros asociado al proyecto [sindastra/psp-mciso](https://github.com/sindastra/psp-mciso), que indica la licencia GPL-3.0. Su distribución está sujeta a los términos de esa licencia y a los avisos correspondientes.

Consulta la licencia original de `mciso` antes de redistribuirlo y conserva la información de copyright y licencia que corresponda a esa versión.

---

## English

# 🎮 PSP Auto Downloader & CSO Converter

A Python script that downloads PSP CSO files from configured Internet Archive repositories, converts them to ISO format using `mciso.exe`, and saves the results to your chosen destination folder.

**`mciso.exe` is included in the project files**, so users do not need to download it separately.

### 🌟 Features

- Automatic lookup across configured repositories.
- CSO-to-ISO conversion using `mciso.exe`.
- Configurable output folder.
- Skips ISO files that already exist.
- Temporary-file cleanup.
- Improved handling of conversion errors.
- Included converter for easier setup.

### 🛠️ Requirements

- Windows 10 or Windows 11.
- Python 3.8 or later.
- Internet Archive CLI (`ia`).
- An Internet connection.
- A PSP Memory Stick/SD card or another destination folder with enough free space.

You do not need to download `mciso.exe` separately when it is included in the project ZIP.

### 🚀 Step-by-step installation

#### 1. Install Python

1. Visit [python.org/downloads](https://www.python.org/downloads/).
2. Download Python 3.8 or later for Windows.
3. Run the installer.
4. **Enable “Add Python to PATH”** before installing.
5. Open Command Prompt and verify the installation:

   ```bash
   python --version
   ```

#### 2. Download the project

**Option A — ZIP download (recommended)**

1. Open the [GitHub repository](https://github.com/PepeXarli/PSP-Auto-Downloader).
2. Click **Code**, then **Download ZIP**.
3. Extract the ZIP file.
4. Open the extracted folder.

The project files should include the Python script, `mciso.exe`, and the README.

**Option B — Git clone**

If Git is installed, run these commands:

```bash
git clone https://github.com/PepeXarli/PSP-Auto-Downloader.git
cd PSP-Auto-Downloader
```

#### 3. Check the project files

The folder should look similar to this:

```text
PSP-Auto-Downloader/
├── app.py
├── mciso.exe
├── README.md
├── LICENSE
├── LICENSE-mciso.txt
└── THIRD_PARTY_NOTICES.md
```

The script filename may differ. Keep the third-party license notices applicable to `mciso.exe`.

#### 4. Install Internet Archive CLI

Open Command Prompt and run:

```bash
python -m pip install --upgrade internetarchive
```

Verify the installation:

```bash
ia --version
```

#### 5. Configure Internet Archive authentication

If authentication is required, sign in to [Internet Archive](https://archive.org/) and run:

```bash
ia configure
```

Follow the prompts. Never publish your credentials in your repository.

#### 6. Configure the output folder

Open the Python script and find `RUTA_PSP`. Change the path to match your destination folder, for example:

```python
RUTA_PSP = r"D:\ISO"
```

If your memory card uses drive `E:`, you could use:

```python
RUTA_PSP = r"E:\ISO"
```

#### 7. Customize the game list (optional)

Edit the `JUEGOS` list in the Python script. Use the exact filenames, including the `.cso` extension.

#### 8. Run the script

Open Command Prompt in the project directory and run:

```bash
python app.py
```

Replace `app.py` with your actual script filename if necessary.

The script will attempt to download the configured CSO files, convert them to ISO, skip existing ISO files, and clean up temporary files according to its processing flow.

### ❓ Troubleshooting

- **Python not recognized:** Check your Python installation and PATH settings, or try `py app.py`.
- **`ia` not recognized:** Reinstall the Internet Archive package and reopen Command Prompt.
- **`mciso.exe` not found:** Ensure it is present in the same directory as the Python script.
- **Download failure:** Verify the filename, repository availability, and access permissions.
- **Conversion failure:** Check the CSO file, available disk space, and `mciso.exe`.

### 📚 Data sources

- [psp_20220507](https://archive.org/download/psp_20220507)
- [psp_20220507_2](https://archive.org/download/psp_20220507_2)

### 🤝 Credits

- [sindastra / psp-mciso](https://github.com/sindastra/psp-mciso) — third-party CSO conversion tool.
- [Internet Archive](https://archive.org/) — digital preservation and file hosting.

### ⚖️ Disclaimer

This project is provided for educational and software-preservation purposes. Users are responsible for ensuring they have the legal right to download, store, and convert the files they use.

This project does not host or include game files. The author is not responsible for misuse of the script or any consequences arising from its use.

### 📄 Licenses

The original code of this project may be distributed under the MIT License if you hold the applicable rights and preserve the required notices.

The included `mciso.exe` is a third-party component associated with [sindastra/psp-mciso](https://github.com/sindastra/psp-mciso), which identifies GPL-3.0 as its license. Redistribution is subject to that license and its applicable notices.

Please consult the original license and preserve the relevant copyright and license information before redistributing the executable.