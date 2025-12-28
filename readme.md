# Entrega Final Django

Blog de Reviews sobre Tecnologia

Este es un desarrollo de una aplicación web estilo blog realizada con el framework Django. La plataforma permite gestionar entradas, usuarios y perfiles.

## Caracteristicas

* **Tecnologias:** Python, Django, CKEditor, Bootstrap5

* **Funcionalidades:**

1. Gestión de Contenido
Listado de páginas: Vista de todos los posts en /pages/.
Detalle de post: Visualización individual de cada entrada con su imagen.
CRUD Completo: Creación, edición y borrado de entradas (protegido por login).
Buscador: Filtrado de blogs por título.
CKEditor: Implementado en el cuerpo de los posts para permitir formato profesional.

2. Gestión de Usuarios
Autenticación: Login, Logout y Registro.
Perfil de Usuario: Visualización de datos y Avatar.
Edición de Perfil: Modificación de datos personales y cambio de contraseña.

3. Requisitos Técnicos
Vistas Basadas en Clases (CBV): Implementadas para el listado y detalle.
Mixins y Decoradores: Control de acceso mediante LoginRequiredMixin y @login_required.
Herencia de Templates: Uso de un base.html para la barra de navegación y estructura general.

## Autor - Bujakiewicz Joaquin