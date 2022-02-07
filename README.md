# AirBnB Clone

The AirBnB Clone is the first stage in the process of recreating the AirBnB website. This repository contains python packages for creating User, State, City, Place, Amenity, and Review classes, inheriting from the BaseModel class, and storing objects created from these, able to be reloaded every time every time the program is run. As well as the classes, there is console program in which commands can be used to create, view, update, and remove objects.

# Usage

To use the console and craete classes, run the colsole.py file. The "(hbnb)" prompt will appear and commands can be entered.

The available built-in commands are listed below.

# Builtins
The AirBnb console is capable of:

* `create`: Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the id. Ex: `(hbnb) create BaseModel`.

* `show`: Prints the string representation of an instance based on the class name and `id`. Ex: `(bhnb) show BaseModel 1234-1234-1234`.

* `destroy`: Deletes an instance based on the class name and `id` (save the change into the JSON file). Ex: `(hbnb) destroy BaseModel 1234-1234-1234`.

* `all`: Prints all string representation of all instances based or not on the class name. Ex: `(hbnb) all BaseModel`or `all`.

* `update`: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: `(hbnb) aupdate BaseModel 1234-1234-1234 email "aibnb@mail.com"`.

# Example Console Usage

`(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"`

`(hbnb) all BaseModel`

`["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]`

`(hbnb) destoy BaseModel 49faff9a-6318-451f-87b6-910505c55907`

`show BaseModel 49faff9a-6318-451f-87b6-910505c55907`

`** no instance found **`


# Files

* `console.py`: The AirBnB console which can create, show, and destroy objects.

* `/models/`: Contains all the class models: BaseModel, User, State, City, Place, Review, Amenity

* `/models/engine/file_storage.py`: Contains the FileStorage class used to save and reload the object data from previous sessions.

* `/tests/`: Contains unittests for each file and class, following the same fodler structure as `/models/`.

* `/models/__init__.py`: Imports all the Classes for use of the globals() function as well as containing the `storage` variable.

# Authors

* James Williams
* Joseph Williams