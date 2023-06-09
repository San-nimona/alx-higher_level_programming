#include "lists.h"
/**
 * insert_node - adds a no to a sorted linked list
 * @head: head
 * @number: number
 * Return: pointer to the new list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *list, *temp2;

	list = malloc(sizeof(listint_t));
	if (!list)
		return (NULL);

	list->n = number;

	if (!(*head))
	{
		list->next = NULL;
		*head = list;
		return (list);
	}

	if (temp->n >= number)
	{
		temp2 = *head;
		*head = list;
		list->next = temp2;
		return (list);
	}

	while (temp->next)
	{
		if (temp->next->n >= number)
		{
			temp2 = temp->next;
			temp->next = list;
			list->next = temp2;
			return (list);
		}
		temp = temp->next;
	}

	temp->next = list;
	list->next = NULL;

	return (list);
}
