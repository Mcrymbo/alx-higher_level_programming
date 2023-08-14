#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @obj_list: A PyObject list
 */
void print_python_list_info(PyObject *obj_list)
{
	int n, list, i;
	PyObject *obj;

	n = Py_SIZE(obj_list);
	list = ((PyListObject *)obj_list)->allocated;
	printf("[*] Size of the Python List = %d\n", n);
	printf("[*] Allocated = %d\n", list);
	for (i = 0; i < n; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(obj_list, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
