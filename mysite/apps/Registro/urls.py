from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required


urlpatterns = [

    # listar las carreras de la bd
    path('listarPorticos', views.listar_porticos, name="listar_porticos"),
    path('listarBicicletas', views.listar_bicicletas, name="listar_bicicletas"),

    
    # agregar un pórtico
    path('agregar_portico', views.agregar_portico, name="agregar_portico"),

    # editar un pórtico
    path('editar_portico/<int:portico_id>', login_required(views.editar_portico), name="editar_portico"),

    # borrar un pórtico
    path('borrar_portico/<int:portico_id>', login_required(views.borrar_portico), name="borrar_portico"),

    # llamando a la clases 
    path('add_portico', views.PorticoCreate.as_view(), name="add_portico"),

    path('listarPorticos', views.PorticoList.as_view(), name='listar_porticos'),

    path('edit_portico/<int:pk>', views.PorticoUpdate.as_view(), name='edit_portico'),

    path('del_portico/<int:pk>', views.PorticoDelete.as_view(), name='del_portico'),


    # agregar un bicicleta
    path('agregar_bicicleta', views.agregar_bicicleta, name="agregar_bicicleta"),

    # editar un bicicleta
    path('editar_bicicleta/<int:bicicleta_id>', login_required(views.editar_bicicleta), name="editar_bicicleta"),

    # borrar un bicicleta
    path('borrar_bicicleta/<int:bicicleta_id>', login_required(views.borrar_bicicleta), name="borrar_bicicleta"),

    # llamando a la clases 
    path('add_bicicleta', views.BicicletaCreate.as_view(), name="add_bicicleta"),

    path('listarBicicletas', views.BicicletaList.as_view(), name='listar_bicicletas'),

    path('edit_bicicleta/<int:pk>', views.BicicletaUpdate.as_view(), name='edit_bicicleta'),

    path('del_bicicleta/<int:pk>', views.BicicletaDelete.as_view(), name='del_bicicleta'),
    
    # listar con filtros
    path('listar_porticos', views.ListPortico , name="list_portico"), 

    # api
    path('porticos/',  views.portico_collection , name='portico_collection'),
    path('porticos/<int:pk>/', views.portico_element ,name='portico_element')

]