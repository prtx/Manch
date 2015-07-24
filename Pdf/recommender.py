#!/usr/bin/python

from math import sqrt


def manhattan_distance(ratings1,ratings2):
	
	distance = 0.0
	total = 0

	for key in ratings1:
		if key in ratings2:
			distance += abs(ratings1[key]-ratings2[key])
			total += 1
	
	if total>0:
		return distance/total
	else:
		return -1


def closest_user(username,user_ratings):

	user_distances = []
	for user in user_ratings:
		if user != username:
			distance = manhattan_distance(user_ratings[user],user_ratings[username])
			if distance>=0:
				user_distances.append( ( distance, user ) )
	user_distances.sort()

	return user_distances


def recommend(username,user_ratings):
	
	recommendations = []

	closest_rating = user_ratings[closest_user(username,user_ratings)]

	user_rating = user_ratings[username]
	
	for series in closest_rating:
		if series not in user_rating:
			recommendations.append( (series,closest_rating[series]) )

	return sorted(recommendations, key=lambda seriesTuple: seriesTuple[1], reverse = True)
