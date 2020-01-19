# The Transparency Project
*Data Science Slugs @ Cruzhacks 2020* -
*Sean Breckenridge, Julian Lehrer, Oasys Okubo, Garrett Leising and Anders Poirel*

![Website Snapshot](https://i.imgur.com/MWG9lS5.jpg)


The number one source for transparency, brah

## Installation

Clone into an empty directory, and make sure to

✔ Use python3.7~

✔ Install [pipenv](https://github.com/pypa/pipenv)

✔ Run `pipenv install` in one of the app directories.

To run the server:

```
cd server
pipenv install
pipenv shell
export FLASK_ENV=development
flask run
```

## Project Structure

Folder structure

```
 --|---- data 
   |
   |--- server-----|---- dash
   |               |
   |               |---- server---- |---- static
   |                                |
   |                                |---- template
   |---- wrangling
```
