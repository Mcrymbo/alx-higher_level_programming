#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints info on python list
 * @obj: python object
 * Return: no return
 */
void print_python_list_info(PyObject *obj)
{
	PyListObject *lst;
	PyObject *item;
	long int size, i;

	size = Py_SIZE(obj);
	printf("[*] size of  the Python List = %ld\n", size);
	lst = (PyListObject *)obj;
	printf("[*] Allocated = %ld\n", lst->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(obj, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
