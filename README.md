# Trabajo-final_Coder89385_Sardi-Rivera-Martina
# MI APP: ☕ Ruta cafetera Argentina

Un espacio diseñado para la comunidad de amantes del café de especialidad en Argentina. Los usuarios pueden explorar reseñas de cafeterías, filtrarlas por métodos de preparación, puntuar sus experiencias con estrellas, comentar publicaciones y gestionar un perfil personalizado con su propio perfil.

## Aplicación Desplegada en Vivo
El proyecto se encuentra activo y accesible públicamente a través del siguiente enlace:
👉 **[https://ruta-cafetera-argentina.onrender.com](https://onrender.cohttps://ruta-cafetera-argentina.onrender.comm)**

## 🎥 Video de demostración
Instalación, navegación y flujo completo de la aplicación en funcionamiento:
 **[[Hacé clic acá para ver el video de la aplicación](https://1drv.ms/v/c/e4823c21059fec3c/IQCSou-esplcR659m75bVE9BAQXTnPl7UK6zY_BasG4cf0A?e=eplxAj)]**
 LINK DEL VIDEO: https://1drv.ms/v/c/e4823c21059fec3c/IQCSou-esplcR659m75bVE9BAQXTnPl7UK6zY_BasG4cf0A?e=eplxAj

## Orden de Prueba
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
   python.exe -m pip install -r requirements.txt
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
