# Trabajo-final_Coder89385_Sardi-Rivera-Martina
# MI APP: ☕ Ruta cafetera Argentina

Un espacio diseñado para la comunidad de amantes del café de especialidad en Argentina. Los usuarios pueden explorar reseñas de cafeterías, filtrarlas por métodos de preparación, puntuar sus experiencias con estrellas, comentar publicaciones y gestionar un perfil personalizado con su propio perfil.

## Aplicación Desplegada en Vivo
El proyecto se encuentra activo y accesible públicamente a través del siguiente enlace:
👉 **[https://ruta-cafetera-argentina.onrender.com]**

## Credenciales de Acceso para la Evaluación (Demo de Prueba)
Para probar los flujos interactivos de autenticación, CRUD y comentarios sin necesidad de registrarse, puede utilizar el siguiente usuario de pruebas:
*   **Usuario:** `tester_cafe`
*   **Contraseña:** `password123`

# Vista del Producto (Flujo de la Aplicación)
A continuación se detalla el recorrido visual de la plataforma paso a paso para facilitar la evaluación del producto final sin depender de la URL en línea:

### 1. Inicio / Landing Page
*Vista de la página principal donde se cargan las últimas reseñas de café de especialidad publicadas por la comunidad.*
![1. Inicio](imagenes/home.png)

### 2. Autenticación de Usuarios
*Formulario de ingreso para usuarios registrados. Permite habilitar los permisos de escritura para crear posts y comentar.*
![2. Login](imagenes/login.png)

### 3. Formulario de Creación de Reseñas (CRUD)
*Panel de interfaz exclusiva para usuarios donde se completan los campos de título, descripción, selección de estrellas y método de preparación.*
![3. Crear Post](imagenes/crear_post.png)

### 4. Detalle del Registro y Comentarios
*Vista ampliada de una cafetería específica donde se despliega la información completa, la puntuación del autor y la sección interactiva de comentarios.*
![4. Detalle y Comentarios](imagenes/detalle.png)

## 🎥 Video de demostración
Instalación, navegación y flujo completo de la aplicación en funcionamiento:
 **[[Hacé clic acá para ver el video de la aplicación](https://1drv.ms/v/c/e4823c21059fec3c/IQCSou-esplcR659m75bVE9BAQXTnPl7UK6zY_BasG4cf0A?e=eplxAj)]**

## Criterios de Aceptación Cumplidos (Para el Evaluador)
Para facilitar la revisión del proyecto, se detallan las correcciones funcionales implementadas con éxito:

*   **CRUD Completo (Create/Read/Update/Delete):** La aplicación permite listar y leer reseñas de café, crear nuevos registros mediante formularios protegidos, y ofrece opciones exclusivas para que los autores editen o eliminen sus publicaciones. *(Evidencia: Ver Capturas #1, #2, #3, #4 y archivos blog/views.py y blog/urls.py)*.
*   **Persistencia y Relaciones en Base de Datos:** Los posts se vinculan con un Usuario (Autor) y un Método de Preparación (V60, Prensa Francesa, etc.). Los cambios e inserciones se guardan de forma permanente utilizando `BigAutoField` para optimizar las claves primarias.
*   **Autenticación y Restricción de Accesos:** El sistema valida las credenciales de ingreso. Solo los usuarios que hayan iniciado sesión tienen permitido comentar publicaciones o acceder a las operaciones de creación, edición y eliminación de posts.
*   **Seguridad de Claves:** Se refactorizó `core/settings.py`. La `SECRET_KEY` y el modo `DEBUG` se gestionan de forma oculta a través de variables de entorno con `python-dotenv`.
*   **Estandarización de Dependencias:** El archivo `requirements.txt` está limpio, fijado en una versión estable de Django (`5.1.5`) y codificado estrictamente en **UTF-8**.

## Orden de Prueba (Uso local)
Para ejecutar este proyecto en tu computadora, seguí estos pasos en tu terminal:
1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com
   cd Trabajo-final_Coder89385_Sardi-Rivera-Martina
   ```

2. **Configurar el entorno y las claves:**
   * Crear y activar el entorno virtual:
     * **En Windows:**
       ```bash
       python -m venv venv
       .\venv\Scripts\activate
     ```
     * **En Mac/Linux:**
       ```bash
       python3 -m venv venv
       source venv/bin/activate
       ```
   * Crear un archivo `.env` en la raíz del proyecto y agregar las siguientes variables:
     ```env
     SECRET_KEY=tu_clave_secreta_aqui
     DEBUG=True
     ```

3. **Instalar dependencias obligatorias:**
   ```bash
   python -m pip install -r requirements.txt
   ```

4. **Ejecutar las migraciones de la base de datos:**
   ```bash
   python manage.py migrate
   ```
5. **Crear usuario Administrador:**
   Para acceder al panel administrativo de Django (`/admin`) y gestionar los métodos de café, ejecute el siguiente comando:
   ```bash
      python manage.py createsuperuser
   ```
6. Iniciar el servidor local:
   ```bash
   python manage.py runserver
   ```
   *Ingresá en tu navegador a: `http://127.0.0.1:8000/`*

## Pruebas Automatizadas
Para validar el correcto funcionamiento y la lógica de creación de posts de café, ejecute:
```bash
python manage.py test
```

Desarrollado por Martina Sardi - Curso de Python en Coderhouse.
