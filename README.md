# AirBnB_clone
The console is the first segment of the AirBnB project at ALX that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Examples of use](#examples-of-use)
* [Authors](#authors)

## Environment
All these files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)

## Installation
* Clone this repository: 
```
    git clone "https://github.com/Ayom04/AirBnB_clone.git"
```
* Access AirBnb directory: 
```
cd AirBnB_clone
```
* Run hbnb(interactively): 
```
./console
``` 
and enter command
* Run hbnb(non-interactively): 
```
echo "<command>" | ./console.py
```

## File Descriptions
[console.py](console.py) - the console contains the entry point of the command interpreter. 
List of commands this console current supports:
* `create` - Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id
* `show` - Prints the string representation of an instance based on the class name and id.
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file).
* `all` - Prints all string representation of all instances based or not on the class name.
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 
* `quit` - exits console
* `EOF` - exits console
* `<emptyline>` - shouldn’t execute anything

#### `models/` directory contains classes used for this project:
[base_model](/models/base_model.py) - The BaseModel that defines all common attributes/methods for other classes
* `def __init__(self, *args, **kwargs)` - Initialization of the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - updates the public instance attribute with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys/values of the instance

#### `/models/engine` directory contains File Storage class that handles JSON serialization and deserialization :
[file_storage.py](/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* `def all(self)` -  returns the dictionary __objects
* `def new(self, obj)` - sets in __objects the obj with key <obj class name>.id
* `def save(self)` - serializes __objects to the JSON file (path: __file_path)
* `def reload(self)` -  deserializes the JSON file to __objects

