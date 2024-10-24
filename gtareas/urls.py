from django.urls import path, re_path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('gtareas/lista_proyectos', views.lista_proyectos, name='lista_proyectos'),
    path('gtareas/proyecto/<int:proyecto_id>/', views.lista_tareas_proyecto, name='lista_tareas_proyecto'),
    path('gtareas/<int:tarea_id>/', views.lista_usuarios_asignados, name='lista_usuarios_asignados'),
    path('gtareas/buscar/<str:texto>/', views.lista_tareas_por_observacion, name='lista_tareas_por_observacion'),
    path('tareas/completadas/<int:anio_inicial>/<int:anio_final>/', views.dame_tareas_por_anio, name='dame_tareas_por_anio'),
    path('tareas/<int:tarea_id>/ultimo-comentario/', views.ultimo_usuario_comentario, name='ultimo_usuario_comentario'),

]