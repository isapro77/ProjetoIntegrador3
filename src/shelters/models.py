from django.db import models
from django.urls import reverse


class Shelter(models.Model):
    nome = models.CharField(max_length=300)
    endereço = models.CharField(max_length=300)
    # número = models.IntegerField()
    CEP = models.CharField(max_length=30)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    pet = models.CharField(max_length=5, default="Não")
    total = models.IntegerField(default=0)
    vagas = models.IntegerField(default=0)
    vacância = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.vacância = ((self.vagas * 100) / self.total)
        super(Shelter, self).save(force_insert, force_update, *args, **kwargs)

    def get_absolute_url(self):
        return reverse("shelter_list")


class Sheltered(models.Model):
    nome = models.CharField(max_length=300)
    gênero = models.CharField(max_length=30)
    idade = models.IntegerField()
    etinia = models.CharField(max_length=30)
    abrigo = models.ForeignKey(Shelter, null=True, related_name='shelter', on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.id is None:
            self.abrigo.vagas -= 1
            self.abrigo.save()
        super(Sheltered, self).save(force_insert, force_update, *args, **kwargs)

    def get_absolute_url(self):
        return reverse("sheltered_list")


class Device(models.Model):
    código = models.CharField(max_length=10)
    endereço_dispositivo = models.CharField(max_length=300)
    # número = models.IntegerField()
    CEP = models.CharField(max_length=30)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    abrigo = models.ManyToManyField(Shelter, blank=True, related_name='shelterdevice')

    def __str__(self):
        return self.código

    def get_absolute_url(self):
        return reverse("device_list")


class ShelterDevice(models.Model):
    abrigo = models.ForeignKey(Shelter, null=True, related_name='shelter_device', on_delete=models.SET_NULL)
    dispositivo = models.ForeignKey(Device, null=True, related_name='device_shelter', on_delete=models.SET_NULL)
    distância = models.IntegerField()

    def __str__(self):
        return self.distância

    def get_absolute_url(self):
        return reverse("shelter_device_list")

