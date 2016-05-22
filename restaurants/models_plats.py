from __future__ import unicode_literals

from django.db import models

class Plats(models.Model):

            'name',
            'description',
            'url',
            'price',

    name = models.CharField(
        max_length=100,
        verbose_name="Nom",
    )

    description = models.CharField(
        max_length=1000,
        verbose_name="Description",
    )

    url = models.CharField(
        max_length=150,
        verbose_name="URL",
    )

    price = MoneyField(
        max_digits=10,
        decimal_places=2,
        default_currency='EUR')

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
            'description',
            'url',
            'price',
        ]

        # Serialize the values
        exp_dict = {field: self.serializable_value(field) for field in fields}
        exp_dict['name'] = self.name
        exp_dict['description'] = self.description
        exp_dict['url'] = self.url
        exp_dict['price'] = self.price
        #exp_dict['f_start_date'] = _date(self.start_date, "F Y")
        return exp_dict
