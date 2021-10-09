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

    @staticmethod
    def get_total_clicks():
        return sum([advertiser.clicks for advertiser in Advertiser.objects.all()])

    def __str__(self):
        return self.name


class Ad(BaseModel):
    title = models.CharField(max_length=50)
    img_url = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    advertiser_id = models.ForeignKey(Advertiser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def inc_clicks(self):
        super().inc_clicks()
        self.advertiser_id.inc_clicks()

    def inc_views(self):
        super().inc_views()
        self.advertiser_id.inc_views()
