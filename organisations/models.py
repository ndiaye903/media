from random import randrange
from django.db import models

# Create your models here.

CHOICES_CIVILITE = (
        ('M.', 'M.'),
        ('Mme.', 'Mme.'),
        ('Dr.', 'Dr.'),
        ('Pr.', 'Pr.'),
    )

CHOICES_LANG = (
        ('Fr', 'Fr'),
        ('En', 'En'),
    )

class Participants (models.Model):
    reference = models.CharField(max_length= 50, unique=True)
    civilite = models.CharField(max_length= 5, choices = CHOICES_CIVILITE)
    lang = models.CharField(max_length= 5, choices = CHOICES_LANG)
    nom = models.CharField(max_length= 100)
    prenom = models.CharField(max_length= 100)
    deuxiemeprenom = models.CharField(max_length= 100, null=True, blank=True)
    organisme = models.CharField(max_length= 100)
    fonction = models.CharField(max_length= 100)
    email1 = models.CharField(max_length= 50, unique=True)
    email2 = models.CharField(max_length= 50, blank = True)
    telephone = models.CharField(max_length= 50, unique=True)
    adresse = models.CharField(max_length= 100)
    ville = models.CharField(max_length= 50)
    pays = models.CharField(max_length= 50)

    isRemercimentsSend = models.BooleanField(default=False)
    estPresent = models.BooleanField(default=False)
    enAttente = models.BooleanField(default=True)
    provenance = models.CharField(max_length= 50)
    #Forums
    forumDesJeunes = models.BooleanField(default=False)
    forumDesFemmes = models.BooleanField(default=False)
    forumScientifiques = models.BooleanField(default=False)

    #Documents
    autreDocument = models.BooleanField(default=False)
    lettreInvitation = models.BooleanField(default=False)
    #Prise en charge
    priseChargeBillet = models.BooleanField(default=False)
    priseChargeComplete = models.BooleanField(default=False)
    priseChargeHebergement = models.BooleanField(default=False)
    reservationHotel = models.BooleanField(default=False)
    priseChargetransUrbain = models.BooleanField(default=False)
    autrePrecision = models.TextField(max_length=1000, null=True, blank=True)
    autrePrecisionCharge = models.TextField(max_length=1000, null=True, blank=True)

    dateDepart = models.DateField(null=True, blank=True)
    dateRetour = models.DateField(null=True, blank=True)
    villeDepart = models.CharField(max_length= 100, null=True, blank=True)
    passport = models.TextField(null=True)
    #Specifique speakers
    biographie = models.TextField(max_length=1500,null=True, blank=True)
    photo = models.TextField(null=True, blank=True)
    #Booleans
    isSpeakers = models.BooleanField(default=False)
    isParticipants = models.BooleanField(default=False)
    isEtudiants = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
            db_table = 'participants'



class Presses (models.Model):
    reference = models.CharField(max_length= 50, unique=True)
    civilite = models.CharField(max_length= 5, choices = CHOICES_CIVILITE)
    lang = models.CharField(max_length= 5, choices = CHOICES_LANG)
    nom = models.CharField(max_length= 100)
    prenom = models.CharField(max_length= 100)
    deuxiemeprenom = models.CharField(max_length= 100, null=True, blank=True)
    email = models.CharField(max_length= 50, unique=True)
    telephone = models.CharField(max_length= 50, unique=True)

    #Presses
    organePresse = models.CharField(max_length= 100)
    lettreAutorisation = models.TextField()
    typeTv = models.BooleanField(default=False)
    typeRadio = models.BooleanField(default=False)
    typeEcrite = models.BooleanField(default=False)
    typeWeb = models.BooleanField(default=False)

    
    estPresent = models.BooleanField(default=False)
    enAttente = models.BooleanField(default=True)
    provenance = models.CharField(max_length= 50)
    #Documents
    autreDocument = models.BooleanField(default=False)
    lettreInvitation = models.BooleanField(default=False)
    #Prise en charge
    priseChargeBillet = models.BooleanField(default=False)
    priseChargeComplete = models.BooleanField(default=False)
    priseChargeHebergement = models.BooleanField(default=False)
    reservationHotel = models.BooleanField(default=False)
    priseChargetransUrbain = models.BooleanField(default=False)
    autrePrecision = models.TextField(max_length=1000, null=True, blank=True)
    autrePrecisionCharge = models.TextField(max_length=1000, null=True, blank=True)

    dateDepart = models.DateField(null=True, blank=True)
    dateRetour = models.DateField(null=True, blank=True)
    villeDepart = models.CharField(max_length= 100, null=True, blank=True)
    passport = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
            db_table = 'presses'


class Organisations (models.Model):
    reference = models.CharField(max_length= 50, unique=True)
    civilite = models.CharField(max_length= 5, choices = CHOICES_CIVILITE)
    lang = models.CharField(max_length= 5, choices = CHOICES_LANG)
    prenom = models.CharField(max_length= 100)
    deuxiemeprenom = models.CharField(max_length= 100, null=True)
    nom = models.CharField(max_length= 100)
    email = models.CharField(max_length= 100, unique=True)
    telephone = models.CharField(max_length= 50, unique=True)
    commission = models.CharField(max_length= 50)

    estPresent = models.BooleanField(default=False)
    enAttente = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
            db_table = 'organisations'
