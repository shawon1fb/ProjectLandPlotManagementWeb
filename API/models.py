from django.db import models


# Create your models here.


class Plot(models.Model):
    plotNo = models.TextField()
    plotId = models.TextField()
    plotName = models.TextField()
    plotSize = models.TextField()
    plot_RsLine = models.TextField()
    plotOwner = models.TextField()
    plotStatus = models.TextField()
    plotPic = models.ImageField()

    def __str__(self):
        return self.plotName


class Favorite(models.Model):
    PlotNo = models.ForeignKey(Plot, on_delete=models.CASCADE)


class User(models.Model):
    userId = models.IntegerField()
    userPhoneNo = models.TextField()
    Favorites = models.ManyToManyField(Favorite, blank=True)

    def __str__(self):
        return self.userPhoneNo
