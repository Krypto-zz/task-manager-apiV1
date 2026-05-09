# Task Manager API - V1

# Esta es la primera version de una API robusta para la gestion de tareas para que el usuario pueda agregar una nueva tarea, editarla, eliminarla, esta API esta construida con **FastAPI** , este proyecto cuenta con un sitema completo de autenticación y persistencia en la base de datos relacional

# Tecnologias Utilizadas:
-   **FastAPI**
-   **SQLite**
-   **Bcrypt**
-   **Pydantic**

## Características Principales:
-   **Registro de Usuarios**
-   **Autenticacion(Login)**
-   **Encriptación de Contraseñas**
-   **Base de datos relacional**
-   **Documentacion integrada**
-   **Arquitectura en capas(Separacion total, en Rutas, Sevicios y Base de datos)**

## Instalación y uso:
1. **Clonar el repositorio**
    '''bash
    git clone https://github.com/Krypto-zz/task-manager-apiV1.git'''

2. **Instalar dependencias**
    pip install fasapi uvicorn bcrypt pydantic

3. **Ejecutar la API**
    '''bash
    uvicorn main:app_task --reload'''
    Ir a la ducomentacion que nos proporciona FastAPI con: 
    Abre tu navegador en http://127.0.0.1:8000/docs

## Proximos pasos
- **Inplementar generacion de tokens JWT para las sesiones**
- **Mejorar el manejo de errores con HTTPException**
