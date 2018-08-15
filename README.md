# Technical Assessment:

This repository is part of a Technical Assessment, all rights reserved to Author.

The main objective is the design and implementation of a Sorting Service Client (SSC).

# Source code organization:

The project folders is organized as folows:

- [x] source:

- `booksorter.py` -> public interface

- `sortingservice.py` -> main algorithm

- [x] tests:

- `ssc_test.py` -> The unit tests performing the described test cases

- `config.py` -> File with parameterized configurations


## Requirements:

- Docker>=18.0

- Python>= 3.6


## Setup instructions:
Clone this repo:

`$  git clone https://www.github.com/danielfloripa/assessment`

Go to dir:

`$  cd assessment`

Build the Docker:

`$  docker build -t mySSC .`

## Run command:

`$  docker run mySSC`

## Results:

Is performed the five use cases described, and the unit tests compare the results and output the message:

`
-----
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
`

For any help. please feel free to contact me
