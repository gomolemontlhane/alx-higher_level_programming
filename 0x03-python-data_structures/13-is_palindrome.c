#include "lists.h"
#include <stddef.h>
/**
 *reverse_list - reverses a linked list
 *@head: pointer to the head of the list
 *
 *Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}

/**
 *is_palindrome - checks if a linked list is a palindrome
 *@head: pointer to the head of the list
 *
 *Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	slow = reverse_list(&slow);
	fast = *head;

	while (slow != NULL)
	{
		if (slow->n != fast->n)
			return (0);

		slow = slow->next;
		fast = fast->next;
	}

	return (1);
}

