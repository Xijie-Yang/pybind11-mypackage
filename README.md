# A Minimum Example Running C++ Functions from Python Using pybind11

## Create Environment

```bash
conda create -y -n 250828-pybind11 python=3.11
conda activate 250828-pybind11

python --version
# Python 3.11.13
pip list
# Package    Version
# ---------- -------
# pip        25.1
# setuptools 78.1.1
# wheel      0.45.1
```

## Build This Package

```bash
pip install -r requirements.txt
pip list
# Package    Version
# ---------- -------
# pip        25.1
# pybind11   3.0.1
# setuptools 78.1.1
# wheel      0.45.1

pip install .
pip list
# Package    Version
# ---------- -------
# mypackage  0.0.1
# pip        25.1
# pybind11   3.0.1
# setuptools 78.1.1
# wheel      0.45.1
```

## Use This Package

In any folder, create a file called `main.py`:

```py
import mypackage_python

print(f"{mypackage_python.add(a=1, b=2)=}")
print(f"{mypackage_python.add(a=1)=}")
```

```sh
conda activate 250828-pybind11
python main.py
```

## References

- https://github.com/pybind/python_example/tree/master
