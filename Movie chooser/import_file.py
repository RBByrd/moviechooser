#import a csv file to 
import csv, random
#from operator import itemgetter, attrgetter

import os.path
# make an empty list
rawmovielist = [] 

#ask the user if they want to add a new file
Q1 = input('Do you want to import a new list? \n (Y/N) \n')

# if they do ask for the file name
if (Q1 == 'Y') or (Q1 == 'y'):
	Q1 = 'Y'
	while(Q1 == 'Y'):

		newfile = input('Enter the file Name of the new file. \n Enter C to cancel. \n')
		if (newfile == 'C') or (newfile == 'c'):
			break
		if os.path.isfile(newfile):

			# import the user input file (needs to be tested if a real file)
			with open(newfile, 'rt') as csvfile:
				input_file = csv.reader(csvfile, delimiter=',')
				for column in input_file:
					rawmovielist.extend(column)
			# remove spaces from in from of the movie names (needs to be clean data function)
			for i in range(len(rawmovielist)):
				word = list(rawmovielist[i])
				while word[0] == ' ':
					del(word[0])

					rawmovielist[i] = "".join(word)		



			# put the list in alphabetical order
			sortedmovielist = sorted(rawmovielist)


			# put the list into a file
			with open('list_of_movies.csv', 'wt') as csvfile:
				wr = csv.writer(csvfile)
				wr.writerow(sortedmovielist)

			break		  
		else:
			print('There was an error opening that file\n')



#empty list for the current movie list and watched movie list
currentmovielist = []
watchedmovies = []

#open the up to date movie list
with open('list_of_movies.csv', 'rt') as csvfile:
	input_file = csv.reader(csvfile, delimiter=',')
	for column in input_file:
		currentmovielist.extend(column)	

#open the most recently watch movie list
with open('watched_movies.csv', 'rt') as csvfile:
	input_file = csv.reader(csvfile, delimiter=',')
	for column in input_file:
		watchedmovies.extend(column)	

#set loop variables
watching = 'Y'

#choose a new movie
while(watching == 'Y'):

	watched = 0
	
	while (watched == 0):
		watched = 1
		# choose a random number from the list
		choice = random.randrange(0, len(currentmovielist), 1)

		#check if the movie is on the recent watched list
		for i in range(len(watchedmovies)):
			if currentmovielist[choice] == watchedmovies[i]:
				watched = 0


	#print the movie selected
	print(currentmovielist[choice])

	#ask the user if they watched the movie
	Q2 = input("Did you watch the movie\n (Y/N)\n")

	if (Q2 == 'Y') or (Q2 == 'y'):
		watching = 'n'
		watchedmovies.append(currentmovielist[choice])
		print(watchedmovies[len(watchedmovies) - 1])
		with open('watched_movies.csv', 'wt') as csvfile:
			wr = csv.writer(csvfile)
			wr.writerow(watchedmovies)