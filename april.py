import os, sys

APPLICATION_ID = "APPLICATION_ID_HERE"
REST_API_KEY = "REST_API_KEY_HERE"

from parse_rest.connection import register, ParseBatcher
# Alias the Object type to make clear is not a normal python Object
from parse_rest.datatypes import Object as ParseObject

register(APPLICATION_ID, REST_API_KEY)
anyObject.title = 'Hello world'
anyObject.score = 100


def saveToParse(anyObject):
    print "Saving..."

    anyObject.save()

    print "Done!"