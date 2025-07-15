# Gestor de Tareas en Python

[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PEP8](https://img.shields.io/badge/PEP8-compliant-brightgreen)](https://peps.python.org/pep-0008/)

Un gestor de tareas en terminal con prioridades, persistencia en JSON y logs, escrito siguiendo **PEP 8**, **PEP 257** y el **Zen de Python**.

##  Características
- Agregar, completar y eliminar tareas con prioridad (alta/media/baja).
- Persistencia de datos en JSON.
- Registro de logs (para auditoría).
- Interfaz enriquecida con `rich`.

---

## Configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/gestor-tareas-python.git
cd gestor-tareas-python




## Entorno virutal

# Crear entorno (Windows/Linux/macOS)
python -m venv .venv

# Activar (Windows)
.venv\Scripts\activate

# Activar (Linux/macOS)
source .venv/bin/activate




## Dependencias

pip install -r requirements.txt  # Dependencias principales
pip install -r requirements-dev.txt  # Desarrollo (black, flake8, mypy)
