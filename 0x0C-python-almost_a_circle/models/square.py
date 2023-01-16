#!/usr/bin/python3
""" square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialize attributes  """
        super().__init__(size, size, x, y, id,)

    def __str__(self):
        """String method """
        str_res = ("[Square] ({}) {}/{} - {}"
                   .format(self.id, self.x, self.y, self.width))
        return str_res

    @property
    def size(self):
        """ getter """
        return self.width

    @size.setter
    def size(self, value):
        """ setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update """
        if args is not None and len(args) != 0:
            lst = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if lst[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, lst[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ to dictionary """
        lst = ['id', 'size', 'x', 'y']
        dic = {}

        for key in lst:
            if key == 'size':
                dic[key] = getattr(self, 'width')
            else:
                dic[key] = getattr(self, key)

        return dic
