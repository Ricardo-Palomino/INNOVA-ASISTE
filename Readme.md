## 🧠 INNOVA-ASISTE

**INNOVA-ASISTE** es una herramienta desarrollada en Python para gestionar la asistencia de estudiantes de forma eficiente y sencilla. Diseñado con fines educativos o institucionales, este sistema permite registrar, editar, eliminar, buscar y listar asistencias, así como administrar información de estudiantes de forma centralizada.

---

### 🚀 Características Principales

- 🔐 **Sistema de autenticación** con nombre de usuario y contraseña.
- 👨‍🎓 **Registro de estudiantes** mediante datos personales.
- 🕒 **Control de asistencia diario**, con almacenamiento en formato JSON.
- 🛠️ **Funciones CRUD** completas: buscar, editar, eliminar y listar registros.
- 🔑 **Generador automático de contraseñas** seguras.
- 💾 Almacenamiento local en archivos `.json` para fácil portabilidad.

---

### 📁 Estructura del Proyecto

```
INNOVA-ASISTE/
│
├── Arranque.py                  # Menú principal de interacción con el usuario
├── Sign_in.py                   # Lógica de inicio de sesión
├── generador_contras.py        # Generador de contraseñas automáticas
│
├── funcionalidad_buscar.py     # Buscar estudiante por ID
├── funcionalidad_editar.py     # Editar información de estudiantes
├── funcionalidad_eliminar.py   # Eliminar registros de estudiantes
├── funcionalidad_listar.py     # Listar todos los estudiantes
├── funcionalidad_registrar.py  # Registrar nuevos estudiantes
│
├── estudiantes.json            # Base de datos de estudiantes
├── asistencias.json            # Registro de asistencias
```

---

### ⚙️ ¿Cómo Usarlo?

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/INNOVA-ASISTE.git
   cd INNOVA-ASISTE
   ```

2. **Ejecutar el sistema desde el archivo principal:**
   ```bash
   python Arranque.py
   ```

3. **Explorar el menú interactivo**, donde puedes:
   - Iniciar sesión
   - Registrar estudiantes
   - Tomar asistencia
   - Buscar y editar registros
   - Ver el listado completo
   - Generar contraseñas seguras

---

### 💡 Tecnologías Utilizadas

- **Python 3**
- **JSON** como base de datos local
- Interfaz de línea de comandos (CLI)

---

### 🎯 Casos de Uso

- Instituciones educativas pequeñas o medianas
- Control de asistencia en talleres o seminarios
- Proyectos de aprendizaje en Python

---

### 🧩 Mejoras Futuras

- Exportación de datos a Excel o PDF
- Interfaz gráfica con Tkinter o PyQt
- Implementación de roles (admin, docente)
- Integración con bases de datos SQL

---

### 📜 Licencia

Este proyecto está bajo la Licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.
