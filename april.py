import os, sys

APPLICATION_ID = "15DQ4FEwTwxxXOTwjDKwDsyyZGLfTTZS9WTQlWaN"
REST_API_KEY = "RIVWH59VFaPUqER09SjeJbxYA8NwDW1yOisuvBuv"

from parse_rest.connection import register, ParseBatcher
from parse_rest.datatypes import Object as ParseObject
register(APPLICATION_ID, REST_API_KEY)

anyObject = ParseObject()

name = raw_input("Enter your name: ")
zipcode = raw_input("Enter your zip code: ")
userObject = ParseObject()
userObject.name = name
userObject.zipcode = int(zipcode)
hates = []
while True:
  hate = raw_input("Tell me something you hate: ")
  if(hate == "nothing"):
    break
  else:
      hates.append(hate)

userObject.hates = hates
def saveToParse(anyObject):
    print "Saving..."

    anyObject.save()

    print "Done!"
    
saveToParse(userObject)

local = list(ParseObject.Query.filter(zipcode=userObject.zipcode))
for person in local:
  for item in userObject.hates:
    if item in person.hates and person.name != userObject.name:
      print person.name, "also hates" , item , "!"
