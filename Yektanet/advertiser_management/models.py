from django.db import models


class BaseModel(models.Model):
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def get_clicks(self):
        return self.clicks

    def get_views(self):
        return self.views

    def inc_clicks(self):
        self.clicks += 1

    def inc_views(self):
        self.views += 1


class Advertiser(BaseModel):
    name = models.CharField(max_length=50)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class Ad(BaseModel):
    title = models.CharField(max_length=50)
    img_url = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    advertiser_id = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
