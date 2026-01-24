#include <python3.13/Python.h>

static PyObject* pyWindowHandler_test(PyObject* self, PyObject* args)
{
    return PyLong_FromLong(13);
}

static PyMethodDef pyWindowHandler_methods[] =
{
    {"test", pyWindowHandler_test, METH_VARARGS, "test function"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef pyWindowHandler_module =
{
    .m_methods = pyWindowHandler_methods
};

PyMODINIT_FUNC
PyInit_pyWindowHandler(void)
{
    return PyModuleDef_Init(&pyWindowHandler_module);
}
