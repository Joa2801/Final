"""
Módulo principal para la gestión de tareas con persistencia en JSON.
Incluye funciones para agregar, completar, eliminar y mostrar tareas.
"""

import json
import logging

logging.basicConfig(filename='registro.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def normalizar_tareas():
    
    """
    Normaliza los nombres de campos de descripción en las tareas.
    Convierte 'descripcion' y 'Descripción' a 'descripción'.
    """
    
    tareas = cargar_tareas()
    for tarea in tareas:

        if "descripcion" in tarea:
            tarea["descripción"] = tarea.pop("descripcion")
        elif "Descripción" in tarea:
            tarea["descripción"] = tarea.pop("Descripción")
    guardar_tareas(tareas)


def cargar_tareas():
    
    """
    Carga las tareas desde el archivo JSON.

    Returns:
        list: Lista de tareas cargadas o lista vacía si el archivo no existe.
    """
    
    try:
        with open("tareas.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def guardar_tareas(tareas):
    
    """
    Guarda las tareas en el archivo JSON.

    Args:
        tareas (list): Lista de tareas a guardar.
    """
    
    with open("tareas.json", "w") as f:
        json.dump(tareas, f, indent=4)


def agregar_tarea(tareas, titulo, descripción, prioridad):
    
    """
    Agrega una nueva tarea a la lista.

    Args:
        tareas (list): Lista actual de tareas.
        titulo (str): Título de la tarea.
        descripción (str): Descripción detallada.
        prioridad (str): Nivel de prioridad (alta/media/baja).

    Returns:
        None: Modifica la lista in-place.
    """
    
    nueva_tarea = {
        "id": len(tareas) + 1,
        "título": titulo,
        "descripción": descripción,
        "prioridad": prioridad,
        "estado": "pendiente"
    }
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    logging.info(f"Tarea agregada: {titulo}")


def mostrar_tareas(tareas):
    
    """
    Muestra las tareas en una tabla formateada usando Rich.

    Args:
        tareas (list): Lista de tareas a mostrar.
    """
    
    from rich.table import Table
    table = Table(title="Listado de Tareas", show_header=True, header_style="bold blue")
    table.add_column("ID", style="cyan", width=4)
    table.add_column("Título", style="magenta", min_width=20)
    table.add_column("Descripción", style="dim", min_width=30)
    table.add_column("Prioridad", style="green", width=10)
    table.add_column("Estado", style="red", width=8)
    
    for tarea in tareas:
        desc = tarea.get("descripción") or tarea.get("Descripción") or tarea.get("descripcion", "Sin descripción")
        estado = "✓" if tarea.get("estado") == "completada" else "●"
        
        table.add_row(
            str(tarea["id"]),
            tarea["título"],
            desc,
            tarea["prioridad"].capitalize(),
            estado
        )
    print(table)


def completar_tarea(tareas, id_tarea):
    
    """
    Marca una tarea como completada.

    Args:
        tareas (list): Lista de tareas.
        id_tarea (int): ID de la tarea a completar.

    Returns:
        bool: True si se encontró y completó la tarea, False en caso contrario.
    """
    
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            tarea["estado"] = "completada"
            guardar_tareas(tareas)
            logging.info(f"Tarea completada: ID {id_tarea}")
            return True
    return False


def eliminar_tarea(tareas, id_tarea):
    
    """
    Elimina una tarea de la lista.

    Args:
        tareas (list): Lista de tareas.
        id_tarea (int): ID de la tarea a eliminar.

    Returns:
        bool: True si se encontró y eliminó la tarea, False en caso contrario.
    """
    
    for i, tarea in enumerate(tareas):
        if tarea["id"] == id_tarea:
            tareas.pop(i)
            guardar_tareas(tareas)
            logging.info(f"Tarea eliminada: ID {id_tarea}")
            return True
    return False