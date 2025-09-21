# Required Python Packages
These can be installed with your favorite python package manager
```
numpy
matplotlib
numba
scipy
joblib
pandas
```

`airfoil_db` must be installed from its repository, which can be found [here](https://github.com/usuaero/AirfoilDatabase/tree/master)

To install it type these commands:
```bash
$ git clone https://github.com/usuaero/AirfoilDatabase.git
$ cd AirfoilDatabase
$ pip install .
```

# Required System Programs
To use the `airfoil_db` module you will need the xfoil program, you can get it [here](https://web.mit.edu/drela/Public/web/xfoil/)

To render LaTeX formatting you need to install LaTeX. You can get it [here](https://www.tug.org/texlive/)
- For windows you probably want MiKTeX
    - Follow [this guide](https://gist.github.com/Foadsf/768e6f023c45e3d078be7793cdb9e102)