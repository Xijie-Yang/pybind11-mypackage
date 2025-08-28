# https://setuptools.pypa.io/en/latest/userguide/quickstart.html
import setuptools

# https://pybind11.readthedocs.io/en/stable/compiling.html#modules-with-setuptools
# To use pybind11 inside your `setup.py`, you have to have some system to ensure that `pybind11` is installed when you build your package.
# https://pybind11.readthedocs.io/en/stable/installing.html#include-with-pypi
# pip install pybind11
import pybind11.setup_helpers


# https://setuptools.pypa.io/en/latest/references/keywords.html
setuptools.setup(
    # A string specifying the name of the package.
    name="mypackage",
    # A string specifying the version number of the package.
    version="0.0.1",
    # A list of strings specifying the packages that setuptools will manipulate.
    packages=["mypackage_python"],
    # ---
    # A list of instances of `setuptools.Extension` providing the list of Python extensions to be built.
    # https://setuptools.pypa.io/en/stable/userguide/ext_modules.html
    ext_modules=[
        # https://pybind11.readthedocs.io/en/stable/compiling.html#modules-with-setuptools
        pybind11.setup_helpers.Pybind11Extension(
            # name (str) – the full name of the extension, including any packages – ie. not a filename or pathname, but Python dotted name
            name="mypackage_cpp",
            # sources (list[str|os.PathLike[str]]) – list of source filenames, relative to the distribution root (where the setup script lives), in Unix form (slash-separated) for portability. Source files may be C, C++, SWIG (.i), platform-specific resource files, or whatever else is recognized by the “build_ext” command as source for a Python extension.
            sources=["mypackage_cpp/ext.cpp", "mypackage_cpp/src/add.cpp"],
            # include_dirs (list[str]) – list of directories to search for C/C++ header files (in Unix form for portability)
            # include_dirs=
        ),
    ],
    # A dictionary providing a mapping of command names to `Command` subclasses.
    cmdclass={},
)
