from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=200)
    time_in_canada = models.IntegerField(default=0)#moreThan1yr/lessThan1yr/planning
    status = models.CharField(max_length=200)#pr/student/refugee/temporaryworker/
    housing = models.CharField(max_length=200) # rent/buy/alreayRent/alreadyOwn
    documment_have = models.IntegerField(default=0)#pr/SIN/driverLic
    children_age  = models.IntegerField(default=0)#5-12/under5/13-18/pregnant/noChild
    current_english = models.CharField(max_length=200)#beginer/intermediate/fluent
    work_situation = models.CharField(max_length=200)#IT professional/services industry/finance
    country_origin = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Services(models.Model):

    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Categories,max_length=200)
    long = models.FloatField(null=True)
    lat = models.FloatField(null=True)

    def score_list(self):
        score_list=[]
        ease_of_transportation_score = 0
        cost_score = 0
        meet_need_score = 0
        time_spent_score = 0
        print(self.reviews_set.all())

        i=0
        for i,review in enumerate(self.reviews_set.all()):
            ease_of_transportation_score += review.ease_of_transportation
            cost_score += review.cost
            meet_need_score += review.meet_need
            time_spent_score += review.time_spent

        score_list = [ease_of_transportation_score/(i+1),cost_score/(i+1),meet_need_score/(i+1),time_spent_score/(i+1)]
        return score_list




    def __str__(self):
        return self.name

class Reviews(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    ease_of_transportation = models.IntegerField(default=0)  # rating
    cost = models.IntegerField(default=0)  # rating
    meet_need = models.IntegerField(default=0)  # rating
    time_spent = models.FloatField()
    comment = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "review1"



