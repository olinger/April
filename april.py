import os, sys

APPLICATION_ID = "15DQ4FEwTwxxXOTwjDKwDsyyZGLfTTZS9WTQlWaN"
REST_API_KEY = "RIVWH59VFaPUqER09SjeJbxYA8NwDW1yOisuvBuv"

from parse_rest.connection import register, ParseBatcher
# Alias the Object type to make clear is not a normal python Object
from parse_rest.datatypes import Object as ParseObject
register(APPLICATION_ID, REST_API_KEY)

anyObject = ParseObject()

name = raw_input("Enter your name: ")
city = raw_input("Where do you live? ")
userObject = ParseObject()
userObject.name = name
userObject.city = city
hates = []
while True:
  hate = raw_input("Tell me something you hate: ")
  if(hate == "nothing"):
    break
  else:
      hates.append(hate)
  #also_hates(name, city, hate)
userObject.hates = hates
def saveToParse(anyObject):
    print "Saving..."

    anyObject.save()

    print "Done!"
    
saveToParse(userObject)