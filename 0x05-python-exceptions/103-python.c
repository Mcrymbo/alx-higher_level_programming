#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
/**
 * print_python_list - used for printing information abouth the list
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
	PyListObject *lst;
	PyObject *obj;
	long int len, i;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf(" [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}
	len = ((PyVarObject *)(p))->ob_size;
	lst = (PyListObject *)p;
	printf("[*] Size of Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", lst->allocated);

	for (i = 0; i < len; i++)
	{
		obj = lst->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
		if (PyFloat_Check(obj))
			print_python_float(obj);
	}
	setbuf(stdout, NULL);
}
/**
 * print_python_float - printing information about float
 * @p: PyObject
 */
void print_python_float(PyObject *p)
{
	char *ch;
	double value;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf(" [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}
	value = ((PyFloatObject *)(p))->ob_fval;
	ch = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);
	printf(" value: %s\n", ch);
	setbuf(stdout, NULL);
}
/**
 * print_python_bytes - printing information about bytes
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int lim, len, i;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}
	len = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	printf(" size: %ld\n", len);
	printf(" trying string: %s\n", str);
	if (len >= 10)
		lim = 10;
	else
		lim = len + 1;
	printf(" first %ld bytes:", lim);
	for (i = 0; i < lim; i++)
	{
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", str[i] + 256);
	}
	printf("\n");
	setbuf(stdout, NULL);
}
