# Trabajo-final_Coder89385_Sardi-Rivera-Martina
# MI APP: ☕ Ruta cafetera Argentina

Un espacio diseñado para la comunidad de amantes del café de especialidad en Argentina. Los usuarios pueden explorar reseñas de cafeterías, filtrarlas por métodos de preparación, puntuar sus experiencias con estrellas, comentar publicaciones y gestionar un perfil personalizado con su propio avatar.

## 🎥 Video de demostración
Instalación, navegación y flujo completo de la aplicación en funcionamiento:
👉 **[Hacé clic acá para ver el video de la aplicación](PEGÁ_ACÁ_EL_LINK_DE_TU_VIDEO_DE_YOUTUBE_DRIVE_O_LOOM)**

## Orden de Prueba (Instalación Local)

Para ejecutar este proyecto en tu computadora, seguí estos pasos en tu terminal:

1. Clonar el repositorio:
   ```bash
   git clone https://github.com
   cd tu-repositorio
   ```
2. Crear y activar el entorno virtual:
   * En Windows:
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
   * En Mac/Linux:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
3. Instalar dependencias obligatorias:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecutar las migraciones de la base de datos:
   ```bash
   python manage.py migrate
   ```
5. Iniciar el servidor local:
   ```bash
   python manage.py runserver
   ```
   *Ingresá en tu navegador a: `http://127.0.0.1:8000/`*

Desarrollado por Martina Sardi - Curso de Python en Coderhouse.
