# [The Transparency Project](http://transparencyproject.tech/)
*Data Science Slugs @ Cruzhacks 2020* -
*Sean Breckenridge, Julian Lehrer, Oasys Okubo, Garrett Leising and Anders Poirel*

<img src="https://raw.githubusercontent.com/Jswig/dss-cruzhacks/master/.github/demo.gif">

## Awards

- 1st place winner overall at Cruzhacks 2020
- 2nd place for Google Cloud at Cruzhacks 2020

The number one source for transparency, brah

## Installation

Clone into an empty directory, and make sure to

✔ Use python3.7~

✔ Install [pipenv](https://github.com/pypa/pipenv)

✔ Install [screen](https://www.gnu.org/software/screen/)

✔ Run `pipenv install` in one of the app directories.

To run the server:

```
cd server
pipenv install
./restart_server
```

Requires the ports 8050, 8051, and 8052 to be open for the graph instances. The domain name was also hardcoded in a couple places. In [config](https://github.com/Jswig/dss-cruzhacks/blob/master/server/server/constants.py), and the `external_stylesheets` argument in each [dash](https://github.com/Jswig/dss-cruzhacks/tree/master/server/dash) instance.

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
