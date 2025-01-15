from django.db import models
class Giornalista (models.Model):
     nome = models.CharField(max_length=20) 
     cognome = models.CharField(max_length=26) 
     def _str_(self): 
        return self.nome + " " +self.cognome
class Articolo (models.Model):
      models. CharField(max_length=100) 
      contenuto = models.CharTextField() 
      giornalista = models. ForeignKey (Giornalista, on_delete=models.CASCADE, related_name="articoli")
      def _str__(self):
        return self.titolo