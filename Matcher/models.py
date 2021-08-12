from typing import DefaultDict
from django.db import models

class Skill(models.Model):
    title =  models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Candidate(models.Model):
    title =  models.CharField(max_length=100)
    skils = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title

class Job(models.Model):
    title =  models.CharField(max_length=100)
    skils = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title

    # retuns best candidates objects 
    def CandidateFinder(self):
        max_skills = 0 
        all_candidates = {}
        best_users = []
        for c in Candidate.objects.filter(title=self.title):
            candidate_skills = []
            # add all candidate skills titles to the list
            for s in c.skils.all():
                candidate_skills.append(s)
            # iterate all job's skills and find matches 
            for s in self.skils.all():
                if s in candidate_skills:

                    if c in all_candidates.keys():
                         all_candidates[c] = all_candidates.get(c)+1
                    else:
                        all_candidates[c] = 1
        max_skills = max(all_candidates.values())
        best_users = [k for k,v in all_candidates.items() if v == max_skills]
        return best_users


