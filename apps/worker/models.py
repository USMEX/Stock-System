from django.db import models
from django.contrib.auth.models import User
from random import randint

from colorfield.fields import ColorField

# |-----| |-----| |-----| METODOS PARA MODELS   |-----| |-----| |-----|
def get_worker_image_filepath(instance, filename):
    filebase, extension = filename.split('.')
    return 'worker/worker_%s/profile_picture.%s' % (instance.workerNickname, extension)

def get_default_worker_image():
    return "worker/worker_worker_image" + str(randint(0, 5)) + ".png"

# |-----| |-----| |-----| |----| |----| |----|  |-----| |-----| |-----|

# |-----| |-----| |--| ELEMENTOS PARA TRABAJADORES |--| |-----| |-----|
class worker(models.Model):
    workerNameFirst = models.CharField(
        max_length=32, verbose_name=u"Firstname", null=False)
    workerNameLast = models.CharField(
        max_length=32, verbose_name=u"Lastname", null=False)
    workerNickname = models.CharField(
        max_length=32, verbose_name=u"Nickname", null=False)
    workerEmail = models.EmailField(
        max_length=32, verbose_name=u"Email", unique=True)
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
    
# |-----| |-----| |--| ELEMENTOS PARA LOS DEPARTAMENTOS |-----| |-----|
# Departamento
class department(models.Model):
    dptoNameLong = models.CharField(
        max_length=32, verbose_name=u"Department name", null=False)
    dptoNameShort = models.CharField(
        max_length=8, verbose_name=u"Department code", null=False)
    dptoEmail = models.EmailField(
        max_length=32, verbose_name=u"Department email", unique=True)
    dptoColor = ColorField(default='#1cc88a')
    
    def __str__(self):
        return "[%s] - %s" % (self.dptoNameShort, self.dptoNameLong)
    
# Puestos de trabajo
class jobTittle(models.Model):
    jobtName = models.CharField(
        max_length=32, verbose_name=u"Job tittle", null=False)
    jobtEmail = models.EmailField(
        max_length=32, verbose_name=u"Job email group", unique=True, null=True)
    jobtSalary = models.DecimalField(
        max_digits=11,  verbose_name=u"Job salary", decimal_places=2, null=False)
    
    # ForeignKey with deparment
    jobtDepartment = models.ForeignKey(
        department, 
        on_delete=models.CASCADE, 
        verbose_name=u"Department on charge", 
        null=False)
    
    def __str__(self):
        return "%s %s" % (self.jobtDepartment, self.jobtName)
    
# Asociación entre trabajador y un puesto de trabajo
class job(models.Model):
    jobWorker = models.ForeignKey(
        worker, 
        on_delete=models.CASCADE, 
        verbose_name=u"Worker", 
        null=False)
    jobJobTittle = models.ForeignKey(
        jobTittle,
        on_delete=models.CASCADE, 
        verbose_name=u"Job assignment", 
        null=False)
    
    def __str__(self):
        return "%s - %s" % (self.jobWorker, self.jobJobTittle)