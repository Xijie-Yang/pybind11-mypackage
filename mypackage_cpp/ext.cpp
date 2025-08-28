#include "src/add.h"

// https://pybind11.readthedocs.io/en/stable/basics.html
// https://pybind11.readthedocs.io/en/stable/classes.html
#include <pybind11/pybind11.h>

namespace py = pybind11;

// the name must be the same as the package name
PYBIND11_MODULE(mypackage_cpp, m) { m.def("add", &add); }
