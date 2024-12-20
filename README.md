# Coffee Shop ☕️

**Coffee Shop** es una aplicación web en desarrollo construida con Django, diseñada para gestionar la venta de productos de una tienda de café. Actualmente, se están implementando nuevas funcionalidades y mejorando el diseño.

## Estado del Proyecto

🚧 **En desarrollo**: El proyecto está en una fase activa de desarrollo. Algunas funcionalidades pueden no estar completamente implementadas o podrían cambiar en versiones futuras.

## Funcionalidades Actuales

- **Gestión de productos**:
  - Añadir, editar y eliminar productos.
  - Visualizar una lista de productos disponibles.
- **Gestión de usuarios**:
  - Registro de usuarios.
  - Inicio de sesión.
  - Formularios estilizados con **Tailwind CSS** y **Crispy Forms**.

### Funcionalidades en Desarrollo

- Carrito de compras.
- Pasarela de pago.
- Panel de administración avanzado para la gestión de inventario.

## Tecnologías

- **Django** 
- **Python** 
- **Tailwind CSS**
- **Crispy Forms**
- **SQLite** 
- **Docker** 

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/coffee_shop.git
cd coffee_shop
```

### 2. Crear y activar el entorno virtual

Si no tienes `virtualenv` instalado, puedes hacerlo ejecutando:

```bash
pip install virtualenv
```

Crear el entorno virtual:

```bash
python3 -m venv coffee_shop
```

Activar el entorno virtual:

```bash
source ~/.envs/coffee_shop/bin/activate
```

### 3. Instalar las dependencias

Con el entorno activado, ejecuta:

```bash
pip install -r requirements.txt
```

### 4. Migrar la base de datos

```bash
python manage.py migrate
```

### 5. Cargar datos iniciales (opcional)

Si tienes un archivo de datos iniciales, puedes cargarlo con:

```bash
python manage.py loaddata initial_data.json
```

### 6. Ejecutar el servidor local

```bash
python manage.py runserver
```

Luego abre tu navegador y ve a `http://127.0.0.1:8000/`.

## Docker (Opcional)

Si prefieres utilizar Docker para ejecutar el proyecto, sigue estos pasos:

1. Asegúrate de tener Docker instalado y configurado en tu sistema.
2. Ejecuta el siguiente comando para levantar los servicios definidos en `docker-compose.yml`:

```bash
docker-compose up
```

El servidor estará disponible en `http://localhost:8000/`.

## Contribuir

Si deseas contribuir al proyecto, sigue estos pasos:

1. Crea un *fork* del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza los cambios necesarios y haz commits descriptivos.
4. Envía un *pull request*.

**Nota:** Dado que el proyecto está en desarrollo, asegúrate de comunicarte con el equipo antes de proponer grandes cambios.

## Licencia

Este proyecto está bajo la licencia MIT.

---

## Contacto

Si tienes preguntas o sugerencias, por favor contacta a [luisf_alfonsos@soy.sena.edu.co].

