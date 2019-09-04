# A Colony Visualization Library

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

This library is being built to accelerate the screening of constructs and automate downstream picking of validated
colonies with robotics. 

### Built With

This program is built using the pandas and numpy python libraries.

* [Pandas](https://pandas.pydata.org/)
* [Numpy](https://numpy.org/)


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

You'll need the following things to get started:
* python 3.7
* virtualenv
* virtualenvwrapper
* clustalo 

```sh
pip install virtualenv virtualenvwrapper
```

### Installation

1. Set up your environment with virtualenvwrapper
```sh
mkvirtualenv colonyvisual
workon colonyvisual
```
2. Clone the repo
```sh
git clone https://github.com/kennyworkman/alignment-app
cd colony-visual
```
3. Install Python dependencies
```sh
pip install -r requirements.txt
```
4. 
Currently working on user friendly API. Right now, just mess with the values in
the main function defined in the `__init__ module.

<!-- USAGE EXAMPLES -->
## Usage

The idea here is to provide a directory of genomic alignment information to
cvisual. The output will be a pandas DataFrame that will validate a colony based
on a set of user defined parameters. This DataFrame can be easily exported to a
csv format for downstream robotics, or viewed as an excel spreadsheet.

<!-- ROADMAP -->
## Roadmap

    * Looking to improve the user API
    * Provide easy configurations as a **kwargs parameter in main usage function
    * Easy communication with downstream robotics
    * User interface populated in a Flask web app

Please [contribute](#contributing)!

See the [open issues]( https://github.com/kennyworkman/colony-visual/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Kenny Workman - kennybworkman@gmail.com

Project Link -
[https://github.com/kennyworkman/colony-visual](https://github.com/kennyworkman/colony-visual)
