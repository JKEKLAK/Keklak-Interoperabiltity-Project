# jared keklak INFO 762 Interoperability Dr walter Grovers
import requests
import get as g
import put as p
import update as u

import INFOproj_GLOBALS as G
import INFOproj_YOUTUBE_API as Y
import INFOproj_CATFACTS_API as F
import INFOproj_CATCLASSIFIER_API as C

#getting a pre-existing cat name, and a youtube video about it
cat_name = g.get_(0)['name']
youtube_video = Y.get_youtube_videos(cat_name + " cat")

#posting the youtube video link to the db
u.update_(0, 'youtube', youtube_video)

#getting a cat name from db, then posting cat facts to the db
facts = F.get_cat_facts(cat_name)
u.update_(0, 'facts', facts)

print()
#getting those facts to display
catfacts = g.get_(0)['facts']
print(catfacts)

#lets ID an image in the DB then fill out the rest of the info
#getting and identifying the cat image
cat_image = g.get_(3)['image_url']

#sending that image to the cat classifier
cat_name = C.classify_cat(cat_image)

#getting youtube videos about the cat
cat_youtube = Y.get_youtube_videos(cat_name + " cat")

#getting facts about the cat
cat_facts = F.get_cat_facts(cat_name)

#updating the table
u.update_(3, 'name', cat_name)
u.update_(3, 'youtube', cat_youtube)
u.update_(3, 'facts', cat_facts)

print()
#lets get a link to that youtube video
print(g.get_(3)['youtube'])

#getting those new cat facts
print()
print(g.get_(3)['facts'])


#now lets put a new entry in the DB and do all the steps
new_cat_image = "https://cdn2.thecatapi.com/images/2N4PhyqTG.jpg"
p.put_new(new_cat_image, 5)

new_cat_name = C.classify_cat(new_cat_image)
new_cat_youtube = Y.get_youtube_videos(new_cat_name)
new_cat_facts = F.get_cat_facts(new_cat_name)

u.update_(5, 'name', new_cat_name)
u.update_(5, 'youtube', new_cat_youtube)
u.update_(5, 'facts', new_cat_facts)

#You should be able to see the changes in the DB