from django.test import TestCase
from django.template.defaultfilters import slugify
from apps.Registro.models import Portico
from apps.Registro.forms import Portico

class PorticoTestCase(TestCase):
    def setUp(self):
        Portico.objects.create(id_portico=11111, ubicacion= "AAAAAA")
        Portico.objects.create(id_portico=22222, ubicacion= "BBBBBB")

    def test_ingresar_porticos(self):
        """Los porticos se registran correctamente en la BD"""
        Portico_1 = Portico.objects.get(id_portico=11111)
        Portico_2 = Portico.objects.get(id_portico=22222)
        self.assertEqual(Portico_1.ubicacion, "AAAAAA")
        self.assertEqual(Portico_2.ubicacion, "BBBBBB")