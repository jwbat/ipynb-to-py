Helper for the course `A Deep Understanding of Deep Learning` by Mike Cohen

The purpose of this repo is to convert `.ipynb` files to `.py` files for local readability,  
copy-and-paste-ability, and as an overall convenient reference.  
The converted files cannot be run as modules it should be noted.  


To recursively convert all `.ipynb` to `.py` files  
in `DUDL_PythonCode` into a new directory, `PythonCode`,  
run the following module in the dir where DUDL_PythonCode is.    
DUDL_PythonCode itself will be unchanged.
```sh
python ipynb_to_py.py
```

Dependency
```sh
Python >= 3.9
pip install jupyter
```

---

To convert any single `.ipynb` file to `.py`, run the following,   
leaving off the .py extension in the destination name.
```sh
jupyter nbconvert --to python <src-filename> --output <dst-filename>
```
