# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)

music = {
            "Mitski" : [("Lush", 2009), ("Retired from business", 2015)],
            "The Garden" : [("Route 66",2024), ("Bootleg", 2026)],
            "Weezer": [("Pinkerton", 1999), ("weezer",2000)]
            }

# Pretty-print the data structure

pprint(music)

# Display details of one album recorded by a specific artist

print(music['Mitski'][0])