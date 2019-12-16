from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    color = models.CharField(max_length=7)
    foto_usuario = models.ImageField(upload_to='usuario/%Y/%m/%d', default='usuario/default.png')

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    fullname = models.CharField(max_length=200)
    sigla = models.CharField(max_length=10)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_anulacion = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.fullname

class Nota(models.Model):
    ESTADO_CHOICES = [
        ('PDTE', 'Pendiente'),
        ('TERM', 'Terminada'),
        ('ANUL', 'Anulada'),
    ]
    IMPORTANCIA_CHOICES = [
        ('MAX', 'Prioridad Máxima'),
        ('ALT', 'Prioridad Alta'),
        ('MED', 'Prioridad Media'),
        ('BAJ', 'Prioridad Baja'),
    ]
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=80)
    texto_nota = models.TextField()
    imagen = models.ImageField(upload_to='notas/%Y/%m/%d', default='notas/default.png')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_vencimiento = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
    )
    importancia = models.CharField(
        max_length=20,
        choices=IMPORTANCIA_CHOICES,
    )

    def __str__(self):
        return self.titulo
