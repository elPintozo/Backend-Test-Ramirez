# Django
from django.db import models

#Apps.menus
from apps.menus import models as views_menu

#Apps.employees
from apps.employees import utils

class Employee(models.Model):
    name = models.CharField(max_length=100, null=False, default='')
    phone = models.IntegerField(null=False, default=0) # wsp
    email = models.EmailField(max_length=254, null=False, default='') # email from account slack
    nationality = models.CharField(max_length=3, default='46', choices=utils.nationality)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def get_or_create_plate(self, type_plate):
        """

        :param type_plate (string):
        :return (Plate):
        """
        if not EmployeePreferences.objects.filter(employee=self, plate__type=type_plate).count():
            return views_menu.Plate.objects.create(name=' ', type=type_plate)
        else:
            return EmployeePreferences.objects.filter(employee=self, plate__type=type_plate).first().plate

class EmployeePreferences(models.Model):
    type_options = (
        ('1', 'Like'),
        ('2', 'Hate'),
    )
    type = models.CharField(max_length=1, choices=type_options, default='1')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    plate = models.ForeignKey(views_menu.Plate, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(views_menu.Ingredient, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['plate', 'ingredient']]

"""
Tips to load data: 

** You can use this command for load data 
$ python3 manage.py loaddata employees_06112020.json.json
"""