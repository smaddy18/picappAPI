# from django.db import models
# import json

# class RoomInfo(models.Model):
#     registrationNo = models.CharField(max_length=64)
#     images = models.JSONField()
#     length = models.FloatField()
#     width = models.FloatField()
#     height = models.FloatField()

#     def save(self, *args, **kwargs):
#         # Convertir la liste d'images en JSON avant de l'enregistrer
#         self.images = json.dumps(self.images)
#         super().save(*args, **kwargs)

#     def get_images(self):
#         # Convertir le JSON en liste d'images lors de la récupération
#         return json.loads(self.images)