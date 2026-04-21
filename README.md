# 🛒 Tienda Online - Proyecto Django

Este es un proyecto web desarrollado con **Django**, que simula una tienda online con productos, vistas dinámicas y estructura MVC.

---

## 🚀 Tecnologías utilizadas

- Python 3
- Django
- HTML5
- CSS3
- Bootstrap (opcional según templates)
- SQLite (base de datos local)

---

## 📁 Estructura del proyecto

```
tiendaonline/
│
├── entidad/               # App principal (models, views, admin)
├── templates/             # Plantillas HTML
├── db.sqlite3             # Base de datos local (NO se sube a producción)
├── manage.py              # Script principal de Django
└── settings.py            # Configuración del proyecto
```

---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/mfernandacortes/tiendaonline.git
cd tiendaonline
```

### 2. Crear entorno virtual (recomendado)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Instalar dependencias

```bash
pip install django
```

O si existe requirements.txt:

```bash
pip install -r requirements.txt
```

### 4. Migraciones

```bash
python manage.py migrate
```

### 5. Ejecutar servidor

```bash
python manage.py runserver
```

Abrir en navegador:

```
http://127.0.0.1:8000/
```

---

## 📌 Funcionalidades

- Listado de productos
- Vistas dinámicas con Django
- Plantillas HTML organizadas
- Estructura MVC (Model - View - Template)
- Panel admin (si está habilitado)

---

## ⚠️ Notas importantes

- La base de datos `db.sqlite3` es local y no se sube a producción.
- Este proyecto es educativo y forma parte de portfolio.

---

## 👩‍💻 Autor

**María Fernanda Cortes**

Desarrolladora Full Stack en formación
Especializada en Python, Django, PHP y SQL

---

## 🎯 Objetivo del proyecto

Este proyecto forma parte de mi portfolio profesional para demostrar habilidades en desarrollo backend con Django, manejo de bases de datos y estructura de aplicaciones web.

