from __future__ import unicode_literals

from django.db import models

TYPES_RESTOS = (
    ('1', "Italien"),
    ('2', "Japonais"),
    ('3', "Chinois"),
    ('4', "Mexicain"),
    ('5', "Français"),
    ('6', "Traditionnel"),
    ('7', "Fast-food"),
    ('8', "Autre"),
)

JOUR_SEMAINE = (
    ('Mon', "Monday"),
    ('Tue', "Tuesday"),
    ('Wed', "Wednesday"),
    ('Thu', "Thursday"),
    ('Fri', "Friday"),
    ('Sat', "Saturday"),
    ('Sun', "Sunday"),
)

# Classe qui à une horaire d'ouverture associe une horaire de fermeture
class TrancheHoraire(models.Model):

    horaire_ouverture = models.DateTimeField(
        verbose_name="Ouverture",
        null=False, blank=False,
    )

    horaire_fermeture = models.DateTimeField(
        verbose_name="Fermeture",
        null=False, blank=False,
    )

# Classe qui à une chaine de caractère (jour) associe la liste des TrancheHoraire correspondantes
class Horaires(models.Model):

    jour_semaine = models.CharField(
        max_length=300,
        choices=TYPES_RESTO,
        verbose_name="jour",
        )

    ouverture = models.ForeignKey(
            TrancheHoraire,
            on_delete=models.CASCADE
        )

class Restaurants(models.Model):

            'name',
            'type_resto',
            'disponibility',
            'tel',
            'adress',

    name = models.CharField(
        max_length=100,
        verbose_name="Nom",
    )

    type_resto = models.CharField(
        max_length=300,
        choices=TYPES_RESTO,
        verbose_name="Type",
    )

    disponibility = models.ForeignKey(
        'Horaire',
        verbose_name="Horaires d'ouverture",
        null=True, blank= True,
    )

    tel = models.CharField(
        max_length=100,
        verbose_name="Telephone",
    )

    adress = models.CharField(
        max_length=300,
        verbose_name="Adresse",
    )

    # Champs pour traiter facilement les requètes géographiques
    # location = models.ForeignKey(
    #     'map.Location',
    #     verbose_name="Position géographique",
    #     null=True, blank=True,
    # )

    def to_dict(self):
        """ On revoie un JSON qui sera affiché """

        # Fields to be exported
        fields = [
            #'ID',
            'name',
            'type',
            'disponibility',
            'tel',
            'adress',
        ]

        # Serialize the values
        exp_dict = {field: self.serializable_value(field) for field in fields}
        exp_dict['name'] = self.name
        exp_dict['type'] = self.type_resto
        exp_dict['disponibility'] = self.disponibility
        exp_dict['tel'] = self.tel
        exp_dict['adress'] = self.adress
        #exp_dict['f_start_date'] = _date(self.start_date, "F Y")
        return exp_dict

