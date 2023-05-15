#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
import console
import inspect
import io
import pep8
import unittest
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")

    def test_unknown(self):
        """ Command that does not exist """
        msg = "*** Unknown syntax: asd\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("asd")
            _st = f.getvalue()
            self.assertEqual(msg, _st)

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except Exception:
            pass

    def test_help_help(self):
        """  Test for help of quit command """
        msg = "List available commands with \"help\" or " \
              "detailed help with \"help cmd\".\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help help")
            _st = f.getvalue()
            self.assertEqual(msg, _st)

    def test_help_quit(self):
        """  Test for help of quit command """
        msg = "Quit command to exit the program\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            _st = f.getvalue()
            self.assertEqual(msg, _st)

    def test_help_EOF(self):
        """  Test for help of EOF command """
        msg = "EOF command to exit the program\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            _st = f.getvalue()
            self.assertEqual(msg, _st)

    def test_help_create(self):
        """  Test for help of create command """
        msg = "Create an instance if the Model exists\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help create")
            _st = f.getvalue()
            self.assertEqual(msg, _st)

    def test_help_show(self):
        """  Test for help of show command """
        msg = "Print dict of a instance in base of it's ID\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help show")
            _st = f.getvalue()
            self.assertEqual(msg, _st)

    def test_help_destroy(self):
        """  Test for help of destroy command """
        msg = "Deletes an instance based on it's ID and save the changes\n \
        Usage: destroy <class name> <id>\n"

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            _st = f.getvalue()
            self.assertEqual(msg, _st)

    def test_help_all(self):
        """  Test for help of all command """
        msg = "Print all the instances saved in file.json\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help all")
            _st = f.getvalue()
            self.assertEqual(msg, _st)

    def test_help_update(self):
        """  Test for help of update command """
        msg = "Usage: update <class name> <id> <attribute name> " \
              "<attribute value>\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help update")
            _st = f.getvalue()
            self.assertEqual(msg, _st)

    def test_help_count(self):
        """  Test for help of count command """
        msg = "Usage: count <class name> or <class name>.count()\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help count")
            _st = f.getvalue()
            self.assertEqual(msg, _st)

    class Test_create(unittest.TestCase):
        """ Tests the create commands """

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except Exception:
            pass

    def test_create_no_class(self):
        """  Test for create with class missing """
        msg = "** class name missing **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create")
            _st = f.getvalue()
            self.assertEqual(msg, _st)

    def test_create_invalid_class(self):
        """  Test for create with invalid class """
        msg = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            _st = f.getvalue()
            self.assertEqual(msg, _st)

    def test_create_valid_class(self):
        """  Test for create with existing id  """
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("create " + i)
                id_st = f.getvalue()
                all_dic = storage.all()
                self.assertTrue((i + '.' + id_st[:-1]) in all_dic.keys())
        self.assertEqual(len(all_dic), len(classes))

    class Test_destroy(unittest.TestCase):
        """ Tests the destroy commands """
    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except Exception:
            pass

    def test_destroy_no_class(self):
        """  Test for destroy with class missing """
        msg = "** class name missing **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            _st = f.getvalue()
            self.assertEqual(msg, _st)

    def test_new_destroy_no_class(self):
        """  Test for destroy with class missing by second method """
        msg = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            pre_cmd = HBNBCommand().precmd("MyModel.destroy()")
            HBNBCommand().onecmd(pre_cmd)
            _st = f.getvalue()
            if st[0] == "\n":
                msg = "\n" + msg
            self.assertEqual(msg, _st)

    def test_destroy_invalid_class(self):
        """  Test for destroy with invalid class """
        msg = "** class doesn't exist **\n"

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            _st = f.getvalue()
            self.assertEqual(msg, _st)

    def test_destroy_no_id(self):
        """  Test for destroy with id missing """
        msg = "** instance id missing **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("destroy " + i)
                _st = f.getvalue()
                self.assertEqual(msg, _st)

    def test_new_destroy_no_id(self):
        """  Test for destroy with id missing """
        msg = "** instance id missing **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                pre_cmd = HBNBCommand().precmd(i + ".destroy()")
                HBNBCommand().onecmd(pre_cmd)
                _st = f.getvalue()
                if _st[0] == "\n":
                    msg = "\n" + msg
                self.assertEqual(msg, _st)

    def test_destroy_no_existent_id(self):
        """  Test for destroy with non-existent id """
        msg = "** no instance found **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("destroy " + i + " 123")
                st = f.getvalue()
                self.assertEqual(msg, st)

    def test_new_destroy_no_existent_id(self):
        """  Test for destroy with non-existent id """
        msg = "** no instance found **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                pre_cmd = HBNBCommand().precmd(i + ".destroy(123)")
                HBNBCommand().onecmd(pre_cmd)
                _st = f.getvalue()
                if _st[0] == "\n":
                    msg = "\n" + msg
                self.assertEqual(msg, _st)

    def test_destroy_valid_class(self):
        """  Test for destroy with existing id  """
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        class_length = len(classes)
        id_cl = []
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("create " + i)
                id_st = f.getvalue()
                id_cl.append(id_st)
                all_dic = storage.all()
                self.assertTrue((i + '.' + id_st[:-1]) in all_dic.keys())
        self.assertEqual(len(all_dic), class_length)
        for i, j in zip(classes, id_cl):
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("destroy " + i + " " + j)
                all_dic = storage.all()
                self.assertFalse((i + '.' + id_st[:-1]) in all_dic.keys())
                class_length -= 1
                self.assertEqual(len(all_dic), class_length)
