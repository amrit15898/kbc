from django.db import models

# Create your models here.
class Answers(models.Model):
    ans = models.CharField(max_length=200)
    is_status = models.BooleanField(default=False)

    def __str__(self):
        return self.ans

class Questiom(models.Model):
    ques = models.TextField()
    answers = models.ManyToManyField(Answers)

    def __str__(self) -> str:
        return self.ques
    
