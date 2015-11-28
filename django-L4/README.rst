====
L4
====

L4 es una tarea de la materia de Programación 2 que lista los paises del mundo.

Inicio Rapido
-------------
1. Añada "L4" a tus INSTALLED_APPS, de esta manera:

	INSTALLED_APPS = (
	...
	'L4',
	)
	
2. Incluya L4 al URLconf en tu proyecto busca urls.py asi:
	 url(r'^L4/', include('L4.urls')),
	 
3. Corra 'python manage.py migrate' para crear los modelos de L4.

4. Inicia el develompment server y visita http://127.0.0.1:8000/admin/ para crear L4 (necesitas tener el Admin app habilitada).

5. Visita http://127.0.0.1:8000/L4/ para participar en L4.

