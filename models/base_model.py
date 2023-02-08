from datetime import datetime
from models import storage
from uuid import uuid4
    """Defines a rectangle class
    """


class BaseModel:
    """represents the base model class of the Airbnb project"""

    def __init__(self, *args, **kwargs):
        """initializes an instance attributes"""

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(
                uuid4()
            )  # the goal of using the module uuid4 is to have a unique id for each Base module object
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """prints a string representation of a object"""
        return "[self.__name__] ({}) <{}>".format(self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict

