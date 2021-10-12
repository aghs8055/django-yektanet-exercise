from django.db import models


class Advertiser(models.Model):
    name = models.CharField(max_length=50)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Ad(models.Model):
    approve = models.BooleanField(default=False)
    title = models.CharField(max_length=50)
    img_url = models.CharField('Image url', max_length=100)
    link = models.CharField(max_length=100)
    advertiser_id = models.ForeignKey(Advertiser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class BaseModel(models.Model):
    ad_id = models.ForeignKey(Ad, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    ip = models.GenericIPAddressField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.ad_id.__str__()


class Click(BaseModel):
    pass


class View(BaseModel):
    pass
