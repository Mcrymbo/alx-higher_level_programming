#include "lists.h"

/**
 * insert_note - inserts node to a sorted singly linked list
 * @head: leading node
 * @number: number to insert
 * Return: address of new node or null if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *prev, *curr = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	while (curr != NULL)
	{
		if (curr->n > number)
			break;
		prev = curr;
		curr = curr->next;
	}
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = curr;
		if (curr == *head)
			*head = new;
		else
			prev->next = new;
	}
	return (new);
}
