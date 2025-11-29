# Bibites_Maker 🧬

**Bibites_Maker** es un proyecto desarrollado en **Python** que utiliza la potencia de **Google Gemini** para generar Bibites a partir de una descripción dada por el usuario.
El servidor se ejecuta utilizando **Uvicorn**.

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

* **Python 3.12** o superior ([Descargar aquí](https://www.python.org/downloads/)).
* Una **API KEY** válida de Google Gemini.

## Instalación y Configuración Local

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

### 1. Clonar el repositorio

```bash
git clone [https://github.com/tu-usuario/Bibites_Maker.git](https://github.com/tu-usuario/Bibites_Maker.git)
cd Bibites_Maker
```
### 2. Crear el Entorno Virtual
El proyecto incluye un script automatizado para crear el entorno virtual e instalar las dependencias necesarias.

Simplemente ejecuta el siguiente archivo por lotes:
```bash
start_server.bat
```

### 3. Configuración de Variables de Entorno (API Key)
El proyecto necesita conectarse con Gemini para funcionar.
Localiza el archivo llamado env.test en la raíz del proyecto.
Este archivo actúa como plantilla. Deberás crear un archivo .env (o editar el existente según tu configuración) basándote en él.

Asegúrate de definir tu clave de API:
```
API_KEY=tu_clave_de_gemini_aqui
```

### 4. Ejecutar el servidor
Para iniciar el servidor con Uvicorn, utiliza el script de arranque incluido:

```
start_server.bat
```

Una vez ejecutado, deberías ver en la consola que el servidor está corriendo, accesible en: http://localhost:30095
