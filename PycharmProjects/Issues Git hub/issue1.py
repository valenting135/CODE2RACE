# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:52:29 2018

@author: Valentin
"""

#First, the user input the values

nbr_videos = int(input())
nbr_posts = int(input())
list_duration = []

for i in range(nbr_videos):
    list_duration.append(int(input()))

resultat = []

def resolution(nbr_videos,nbr_posts,list_duration,duration):
    """check (with recursive way) if there is a solution for a specific common duration"""
    global resultat
    if nbr_posts == 1 and sum(list_duration) == duration : #Basic case for 1 number_posts
        resultat = [nbr_videos]+resultat
        return True
    if nbr_posts == 1:
        return False
    
    for sj in range(1,len(list_duration)-nbr_posts+2): #sj is the size of the first post for this list_duration
        if resolution(nbr_videos - sj,nbr_posts-1,list_duration[sj:],duration):
            if sum(list_duration[:sj]) == duration:
                resultat = [sj]+resultat #you add the right size
                return True
    resultat = [] #here, there is no solution for those considered size so you delete the resultat
    return False

solution_found = False

print()

for duree in range(1,sum(list_duration)+1): #you check resolution for all durations
    if resolution(nbr_videos,nbr_posts,list_duration,duration):
        print("Yes")
        for k in resultat:
            print(k)
        solution_found = True

if not(solution_found):
    print("No")