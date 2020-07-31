from django.db import models
from crags.models import Crag
from grades.models import Grade
from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comment


class Route(models.Model):
    rname = models.CharField(max_length=500, verbose_name='Route Name')
    rdescription = models.TextField(verbose_name='Route Description')
    ropener = models.CharField(max_length=500, verbose_name='Route Opener')
    rcrag = models.ForeignKey(Crag, on_delete=models.CASCADE, null=True, verbose_name='Crag')
    #In case of multipitch, the highest grade of all pitches
    grade = models.ForeignKey(Grade, on_delete=models.DO_NOTHING, verbose_name='Pitch Grade', null=True)
    
    # equal to pitch length if one pitch, otherwise sum of pitch length
    length = models.FloatField(verbose_name='Route Length', default=0)
    # this should be set once and never changed.
    base_unit = models.CharField(max_length=50, verbose_name='R Base_unit')
    rtype = models.CharField(max_length=50, verbose_name="Type of route")
    numpitch = models.CharField(max_length=500, verbose_name='Single or Multi')
    avg_rating = models.FloatField(verbose_name='Average rating', default=0)

    comments = GenericRelation(Comment)


    def __str__(self):
        return self.rname

    #function to add rating object to route
    def add_rating(self, user, rating):
        if user.is_authenticated:
            #get users eisting ratings for the route
            existing_ratings = self.rating_set.filter(user=user).count()
            #if there is already a rating
            if existing_ratings == 1:
                #delete that rating
                self.rating_set.get(user=user).delete()
            #If more than 1 rating exists, then something is wrong.
            elif existing_ratings > 1:
                print("errormode")

            #save the current rating.
            rating.save()
            self.rating_set.add(rating)
            ratings_count = self.rating_set.count()
            running_total = 0

            for i in self.rating_set.all():
                running_total+= i.score

            if ratings_count > 0 :
                self.avg_rating = running_total / ratings_count
                self.save()
            else:
                self.avg_rating = 0.0

            return self.avg_rating

    # I need this method for route rating    
    def get_absolute_url(self):
        from django.urls import reverse
        # return the string URL for route-view (in urls.py) using self.id as arg
        return reverse('route-view', args=[str(self.id)])

    #Needed for API
    def get_api_rate_url_1(self):
        from django.urls import reverse
        return reverse('rate-route-api-1', args=[str(self.id)])

    def get_api_rate_url_2(self):
        from django.urls import reverse
        return reverse('rate-route-api-2', args=[str(self.id)])

    def get_api_rate_url_3(self):
        from django.urls import reverse
        return reverse('rate-route-api-3', args=[str(self.id)])

    def get_api_rate_url_4(self):
        from django.urls import reverse
        return reverse('rate-route-api-4', args=[str(self.id)])

    def get_api_rate_url_5(self):
        from django.urls import reverse
        return reverse('rate-route-api-5', args=[str(self.id)])

    def get_api_rate_url(self, score):
        from django.urls import reverse
        return reverse('rate-route-api', args=[str(self.id), score])


    def get_highest_grade(self):        
        all_grades = []
        highest_grade_index = 0
        for pitch in self.pitch_set.all():
            all_grades.append(pitch.grade)
        for i, grade in enumerate(all_grades): 
            if all_grades[highest_grade_index].id > grade.id:
                print("all good")
            elif all_grades[highest_grade_index].id <= grade.id:
                highest_grade_index = i
        print("highest grade is", all_grades[highest_grade_index])
        self.grade = all_grades[highest_grade_index]
        self.save()
        return            


        



        
        


















