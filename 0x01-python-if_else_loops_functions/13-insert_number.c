#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts number into sorted singly linked list
 * @head: pointer to the head of the list
 * @number: number to be inserted
 * Return: address of the new node, or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	current = *head;
	while (current->next != NULL && number > current->next->n)
		current = current->next;

	new->next = current->next;
	current->next = new;

	return (new);
}
