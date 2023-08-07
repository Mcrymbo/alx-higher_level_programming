#include "lists.h"

/**
 * check_cycle - checks for a cycle if exist in singly linked list
 * @list: pointer to list
 * Return: 0 if no cycle, 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *curr;
	listint_t *prev;
	
	curr = list;
	prev = list;
	while (list && curr && curr->next)
	{
		curr = curr->next->next;
		list = list->next;

		if (list == curr)
		{
			list = prev;
			prev = curr;
			while (1)
			{
				curr = prev;
				while (curr->next != list && curr->next != prev)
					curr = curr->next;
				if (curr->next == list)
					break;
				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}
