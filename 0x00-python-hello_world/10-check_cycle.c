#include "lists.h"

/**
 * check_cycle - check if a linked list has cycles
 * @list: pointer to the nxt node
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *s, *f;

	if (!list)
		return (0);

	s = list;
	f = list->next;

	while (f && s && f->next)
	{
		if (f == s)
			return (1);

		f = f->next->next;
		s = s->next;
	}
	return (0);
}

