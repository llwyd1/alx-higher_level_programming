#include "lists.h"

/**
 * insert_node - inserts a number into a singly linked list
 * @head: a double pointer to the list
 * @number: number to insert to the list
 *
 * Return: address of the new node, or NULL if it failed
 **/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp = *head;
	int i;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;

	for (i = 0; i < 4; i++)
		temp = temp->next;

	new->next = temp->next;
	temp->next = new;

	return (temp->next);

}
