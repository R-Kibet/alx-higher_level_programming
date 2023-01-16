#!/usr/bin/python3
""" base class"""
import json
import csv
import os.path
import turtle


class Base:
    """ base class """
    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ convert to json """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to csv """
        if list_objs is None:
            with open(cls.__name__ + ".json", "w") as f:
                f.write("[]")
        else:
            lst_inst = [i.to_dictionary() for i in list_objs]
            with open(cls.__name__ + ".json", "w") as f:
                f.write(cls.to_json_string(lst_inst))

    @staticmethod
    def from_json_string(json_string):
        """ json to string """
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """ instance of atttributes already set """
        if cls.__name__ == "Rectangle":
            a = cls(10, 10)
        else:
            a = cls(10)
        a.update(**dictionary)
        return a

    @classmethod
    def load_from_file(cls):
        """  returns a list of instances """
        lst_inst = []
        f = cls.__name__ + ".json"
        if os.path.isfile(f):
            with open(f, "r") as fl:
                a = cls.from_json_string(fl.read())
            for i in a:
                lst_inst.append(cls.create(**i))
            return lst_inst
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes and deserializes in CSV """
        f = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            lst_dic = [0, 0, 0, 0, 0]
            lst_k = ['id', 'width', 'height', 'x', 'y']
        else:
            lst_dic = ['0', '0', '0', '0']
            lst_k = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for i in list_objs:
                for j in range(len(lst_k)):
                    lst_dic[j] = i.to_dictionary()[lst_k[j]]
                matrix.append(lst_dic[:])

        with open(f, 'w') as wFile:
            writer = csv.writer(wFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """ deserialier """
        f = "{}.csv".format(cls.__name__)

        if os.path.exists(f) is False:
            return []

        with open(f, "r") as fl:
            rd = csv.reader(fl)
            csv_lst = list(rd)

        if cls.__name__ == "Rectangle":
            lst_k = ['id', 'width', 'height', 'x', 'y']
        else:
            lst_k = ['id', 'size', 'x', 'y']

        m = []

        for i in csv_lst:
            d = {}
            for j in enumerate(i):
                d[lst_k[j[0]]] = int(j[1])
            m.append(d)

        lst_inst = []

        for a in range(len(m)):
            lst_inst.append(cls.create(**m[a]))

        return lst_inst

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws sqaures and rectangles"""
        for i in list_rectangles + list_squares:
            tt = turtle.Turtle()
            tt.shape("turtle")
            turtle.bgcolor("black")
            tt.fillcolor("white")
            tt.begin_fill()
            tt.pen(fillcolor="white", pencolor="red", pensize=2)
            for _ in range(2):
                tt.forward(i.width)
                tt.right(90)
                tt.forward(i.height)
                tt.right(90)
            tt.end_fill()
            turtle.done()
