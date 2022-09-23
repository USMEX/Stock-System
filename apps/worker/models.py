from django.db import models
from django.contrib.auth.models import User
import random

# Create your models here.

# |-----| cIUDADES REGISTRADAS
POSICIONES = [
    ('QUQU', 'Quarterbacks'),
    ('RURU', 'Running backs'),
    ('WIWI', 'Wide receivers'),
    ('TITI', 'Tight ends'),
    ('DEDE', 'Defensive linemen'),
    ('LILI', 'Linebackers'),
    ('DEDE', 'Defensive backs'),
    ('SPSP', 'Special teams'),
    ('PRPR', 'Practice squad'),
]
# |-----| Método de búsqueda de fotos
def get_worker_image_filepath(instance, filename):
    filebase, extension = filename.split('.')
    return 'worker/worker_%s/profile_picture.%s' % (instance.workerUsername, extension)

def get_default_worker_image():
    pictures = [
        'worker_worker_image0.png',
        'worker_worker_image1.png',
        'worker_worker_image2.png',
        'worker_worker_image3.png',
        ]
    return "worker/" + random.choice(pictures)

# |-----| Models para workeradores
class worker(models.Model):
    workerNameFirst = models.CharField(
        max_length=64, verbose_name=u"Firstname", null=False)
    workerNameLast = models.CharField(
        max_length=64, verbose_name=u"Lastname", null=False)
    workerNickname = models.CharField(
        max_length=64, verbose_name=u"Nickname", null=False)
    workerEmail = models.EmailField(
        max_length=60, verbose_name=u"Email", unique=True)
    workerDateRegistered = models.DateField(auto_now_add=True)
    workerDateBirth = models.DateField(
        verbose_name=u"BirthDate", null=True)
    workerIsActive = models.BooleanField(default=False, verbose_name=u"Usuario activo")

    # Fotografía del trabajador
    workerPhoto = models.ImageField(max_length=255, 
        upload_to=get_worker_image_filepath, 
        blank=True, default=get_default_worker_image,
        verbose_name=u"Upload a picture of you")

    # Referencia del usuario
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.workerNameLast, self.workerNameFirst)
    
    class Meta:
        ordering = ['workerNameLast']
    