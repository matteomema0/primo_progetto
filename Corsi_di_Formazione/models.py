from django.db import models 


class corso(models.Model):
  titolo = models.CharField(max_length=100)
  descrizione = models.TextField()
  data_inizio = models.DateField( blank=True)
  data_fine=models.DateField( blank=True)
  posti_disponibili=models.IntegerField (default=0, blank=True)

  def __str__(self):
    return self.titolo
    
    
  class Meta:
    verbose_name = "Corso"
    verbose_name_plural = "Corsi"