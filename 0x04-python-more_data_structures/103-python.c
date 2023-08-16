#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - print byte information
 * @obj: python object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int i, size, lim;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject * )(p))->ob_size;
	str = ((PyBytesObject * )(p))->ob_sval;
	printf(" size: %ld\n", size);
	printf(" trying string: %s\n", str);
	if (size >= 10)
		lim = 10;
	else
		lim = size + 1;
	printf(" first %ld bytes:", lim);
	for (i = 0; i < lim; i++)
	{
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);
	}
	printf("\n");
}
/**
 * print_python_list - print list information
 * @p: python object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	PyObject *p1;
	PyListObject *lst;
	long int i, size;

	lst = (PyListObject *)p;
	size = ((PyVarObject *)p)->ob_size;
	printf("[*] Python List info\n");
	printf("[*] Size of Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", lst->allocated);
	for (i = 0; i < size; i++)
	{
		p1 = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((p1)->ob_type)->tp_name);
		if (PyBytes_Check(p1))
			print_python_bytes(p1);
	}
}
