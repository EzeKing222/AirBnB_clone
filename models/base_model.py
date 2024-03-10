#!/usr/bin/python3
"""
Base model
"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """
    This class define all attributes and methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        class instance

        Args:

        id: string - assigned to uuid when instance is created.
        created_at: datetime - assigned with current datetime
        when instance is created.
        updated_at: datetime - assigned with current datetime
        when instance is created, it is updated every time object is changed
        """

        time_fmt = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, value in kwargs.items():
                if key == __class__:
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_fmt))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

        models.storage.new(self)

    def save(self):
        """
        update the created attribute
        """

        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        return a dictionary containing all key/value of __dict__
            of the instance
        """

        instance_dictionary = self.__dict__.copy()
        instance_dictionary["__class__"] = self.__class__.__name__
        instance_dictionary["created_at"] = self.created_at.isoformat()
        instance_dictionary["updated_at"] = self.updated_at.isoformat()

        return instance_dictionary

    def __str__(self):
        """
        print: [<class name>] (<self.id>) <self.__dict__>
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "king"
    my_model.my_number = 89
    print(my_model)
