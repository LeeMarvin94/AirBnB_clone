#!/usr/bin/python3
""" python code that implements the base model of a Airbnb clone + } =  """
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ represents the base model class of the Airbnb project """
    def __init__(self,*args,**kwargs):
        """ initializes a instance attributes """
        self.id = str(uuid4())    # the goal of using the module uuid4 is to have a unique id for each Base module object
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ prints a string representation of a object """
        return "[self.__name__] ({}) <{}>".format(self.id,self.__dict__)
        

    def save(self):
        """ updates the public instance attribute with the current datetime """
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """ returns a dictionary containing all keys/values of the instance """
        
        
        

