from django.db import models


class UserProfileBasicQuerySet(models.QuerySet):

    def get_organization_status(self,user_id):
        return self.get(auth=user_id)