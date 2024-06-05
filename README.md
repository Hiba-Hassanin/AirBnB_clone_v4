# AirBnB Clone - The Console

The console is the first part of the AirBnB project at Holberton School, focusing on key concepts of higher-level programming. The project's goal is to eventually create a simple version of the AirBnB website (HBnB). This part involves creating a command interpreter to manage objects for the HBnB website.

## Command Interpreter Features
* Create a new object (e.g., a new User or Place)
* Retrieve an object from a file or database
* Perform operations on objects (e.g., count, compute stats)
* Update an object's attributes
* Delete an object

## Table of Contents
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Usage](#usage)
* [Examples](#examples)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## Environment
This project is tested on Ubuntu 14.04 LTS using Python 3 (version 3.4.3).

## Installation
1. Clone this repository: `git clone "https://github.com/alexaorrico/AirBnB_clone.git"`
2. Go to the AirBnB directory: `cd AirBnB_clone`
3. Run the console interactively: `./console` and enter commands
4. Run the console non-interactively: `echo "<command>" | ./console.py`

## File Descriptions
### [console.py](console.py)
The entry point of the command interpreter. It supports commands like:
* `EOF` - exits the console
* `quit` - exits the console
* `<emptyline>` - does nothing when an empty line is entered
* `create` - creates a new instance of `BaseModel`, saves it to the JSON file, and prints the id
* `destroy` - deletes an instance based on the class name and id, saving the change to the JSON file
* `show` - prints the string representation of an instance based on the class name and id
* `all` - prints all string representations of all instances, optionally filtered by class name
* `update` - updates an instance based on the class name and id by adding or updating attributes, saving the change to the JSON file

### `/models` Directory
Contains classes used in the project:
* [base_model.py](/models/base_model.py) - The `BaseModel` class, from which future classes will be derived.
* Classes that inherit from `BaseModel`: [amenity.py](/models/amenity.py), [city.py](/models/city.py), [place.py](/models/place.py), [review.py](/models/review.py), [state.py](/models/state.py), [user.py](/models/user.py)

### `/models/engine` Directory
Contains the `FileStorage` class for JSON serialization and deserialization:
* [file_storage.py](/models/engine/file_storage.py) - Manages JSON file storage.

### `/tests` Directory
Contains unit tests for the project:
* [test_base_model.py](/tests/test_models/test_base_model.py) - Tests for the `BaseModel` class
* [test_amenity.py](/tests/test_models/test_amenity.py) - Tests for the `Amenity` class
* [test_city.py](/tests/test_models/test_city.py) - Tests for the `City` class
* [test_file_storage.py](/tests/test_models/test_file_storage.py) - Tests for the `FileStorage` class
* [test_place.py](/tests/test_models/test_place.py) - Tests for the `Place` class
* [test_review.py](/tests/test_models/test_review.py) - Tests for the `Review` class
* [test_state.py](/tests/test_models/test_state.py) - Tests for the `State` class
* [test_user.py](/tests/test_models/test_user.py) - Tests for the `User` class

## Usage
Run the command interpreter using `./console.py` and enter commands as needed. The interpreter supports commands for creating, reading, updating, and deleting objects.

## Examples
```sh
vagrant@AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}]
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}
(hbnb) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(hbnb) quit
```

## Bugs
No known bugs at this time.

## Authors
Alexa Orrico 
Jennifer Huang 
Jhoan Zamora 
David Ovalle
Joann Vuong
Hiba Hassanin


## License
Public Domain. No copy write protection.
