

"""
Given 50 randomly located drivers, map them to some random number of randomly located jobs such that
total distance to jobs is minimised. With only 50 jobs available, map the driver ids and job location ids
and print out the result in a key value pair

"""

# get a list of all the drivers list k []
# generate a random number for each driver in the list
# get user input to get the job(the randomly located job)
# generate a random number for the user input
# match the randomly generated number for the job to the closest number in the drivers random list
# try using random.randit method to generate the random numbers for the drivers and the jobs
# append the two lists to a dictionary

# first loops through all the driver ids.
# A new list is created for all the driver ids where they are stored
# Then Generates a random job location id in the range 1-50 for the 50 drivers.
# The job location ids are stored in another seperate list
# Checks whether the  driver ids and random job locations are in range
# A dictionary is then created to map each driver to the closest location and
# finally printed out to the console.

from random import randint

for id in range(1,51):
# create a new list to store the data from the driver_id
    driver_id = []
# adding data on to the list through the append method
    driver_id.append(id)
# create a new list to hold the randomly generated jobs
    jobs = []
# an inbuilt method that randomly allocates values to that number in the range of 1 - 51
    jobs_list = randint(1, 51)
# appending data onto the list
    jobs.append(jobs_list)
#Pring out that list
    if driver_id >= jobs_list <= 51:
        final = dict(zip(driver_id, jobs))
    print final



#from the above:
# find out how to use random.randint to generate random data
# to match keys and values of two different lists to one dictionary
# various ways to create a dictionary



