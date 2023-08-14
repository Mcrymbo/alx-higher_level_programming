#include "lists.h"
#include <stdlib.h>

/**
 * rev - reverses second half of list
 * @h_s: head of second half of the list
 * Return: no return
 */
void rev(listint_t **h_s)
{
	listint_t *prev, *curr, *nex;

	prev = NULL;
	curr = *h_s;
	while (curr != NULL)
	{
		nex = curr->next;
		curr->next = prev;
		prev = curr;
		curr = nex;
	}
	*h_s = prev;
}
/**
 * comp - compare integers of the list
 * @h1: head of first list
 * @h2: head of the second list
 * Return: 1 if equal, 0 otherwise
 */
int comp(listint_t *h1, listint_t *h2)
{
	listint_t *temp1, *temp2;

	temp1 = h1;
	temp2 = h2;
	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
			return (0);
	}
	if (temp1 == NULL && temp2 == NULL)
		return (1);
	return (0);
}

/**
 * is_palindrome - checks if singly linked list is a palindrome
 * @h: head
 * Return: 1 if it is a palindrom and 0 otherwise
 */
int is_palindrome(listint_t **h)
{
	listint_t *s1, *s2, *prev, *half, *middle;
	int pal;

	s1 = s2 = prev = *h;
	middle = NULL;
	pal = 1;
	if (*h && (*h)->next)
	{
		while (s2 && s2->next)
		{
			s2 = s2->next->next;
			prev =  s1;
			s1 = s1->next;
		}
		if (s2)
		{
			middle = s1;
			s1 = s1->next;
		}
		half = s1;
		prev->next = NULL;
		rev(&half);
		pal = comp(*h, half);
		if (middle)
		{
			prev->next = middle;
			middle->next = half;
		}
		else
			prev->next = half;
	}
	return (pal);
}
