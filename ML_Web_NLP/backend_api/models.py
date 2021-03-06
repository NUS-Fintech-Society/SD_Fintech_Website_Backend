from django.db import models

class companies(models.Model):
    #Serial ID automatically created by django
    company_name = models.CharField(max_length=500, blank = False, unique = True, primary_key = True)

    def __str__(self):
        return self.company_name

class headlines(models.Model):
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)]
    # company_id = models.OneToOneField(
    #     companies,
    #     primary_key=True,
    #     on_delete=models.CASCADE
    # )
    company_name = models.ForeignKey(companies, on_delete = models.CASCADE) #When company in companies table is deleted, we delete all the headlines corresponding to it
    #company_name = models.CharField(max_length=5000, blank = False) #When company in companies table is deleted, we delete all the headlines corresponding to it
    title = models.CharField(max_length=5000, blank = False)
    date_posted = models.DateField(blank = False)
    week = models.IntegerField(blank = False)
    year = models.IntegerField(blank = False)
    score = models.FloatField(blank = False)

    def __str__(self):
        return self.title


# Create your models here.