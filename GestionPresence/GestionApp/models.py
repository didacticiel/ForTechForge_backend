from django.db import models

# Classe Employé
class Employe(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

   

    def __str__(self):
        return self.nom

# Classe Présence
class Presence(models.Model):
    date = models.DateField()
    heure_arrivee = models.DateTimeField(null=True, blank=True)
    heure_sortie = models.DateTimeField(null=True, blank=True)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)



    def __str__(self):
        return f"{self.employe.nom} - {self.date}"

# Classe Administrateur (hérite d'Employé)
class Administrateur(Employe):
    role = models.CharField(max_length=50)



# Classe Rapport
class Rapport(models.Model):
    TYPE_CHOICES = [
        (1, 'Journalier'),
        (2, 'Hebdomadaire'),
        (3, 'Mensuel'),
        (4, 'Personnalisé'),
    ]

    type = models.IntegerField(choices=TYPE_CHOICES)
    date_debut = models.DateField()
    date_fin = models.DateField()
    contenu = models.TextField()

    

    def __str__(self):
        return f"Rapport {self.get_type_display()} - {self.date_debut} à {self.date_fin}"
