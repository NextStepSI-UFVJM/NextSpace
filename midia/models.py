from django.db import models

class Midia(models.Model):

  Id = models.AutoField(primary_key=True)


  EVENTOS = 'Eventos'
  VIAGENS = 'Viagens'
  HAPPY_HOUR = 'Happy Hour'

  CATEGORIA_CHOICES = [
    (EVENTOS, 'Eventos'),
    (VIAGENS, 'Viagens'),
    (HAPPY_HOUR, 'Happy Hour'),
  ]

  Categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES)

  Legenda = models.TextField()

  Imagem = models.ImageField(upload_to='')

  Data_de_publicação= models.DateTimeField(auto_now_add=True)

  Autor = models.CharField(max_length=75)

  Curtidas = models.IntegerField(default=0)



  def __str__(self):
    return f"{self.id} - {self.caption}"
  


