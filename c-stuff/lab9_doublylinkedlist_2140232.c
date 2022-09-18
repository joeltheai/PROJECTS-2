// 2140232
// joel varghese

#include <stdio.h>
#include <stdlib.h>

struct dlist
{
  int info;
  struct dlist *next;
  struct dlist *prev;
};

typedef struct dlist node;

node *last = NULL;

void create(node *);
void bdisplay(node *);
void fdisplay(node *);

int main()
{
  char ch;
  node *head = NULL;
  do
  {
    system("cls");
    printf("\nprogram to create and display doubly linked list");
    head = (node *)malloc(sizeof(node));
    head -> prev = NULL;
    create(head);
    fdisplay(head);
    bdisplay(last);

    printf("\nContinue ? ");
    fflush(stdin);
    ch = getchar();
  } while (ch == 'y' || ch == 'Y');
  return 0;
}

void create(node *ptr)
{
  char ch;
  node *temp;
  printf("\n\nEnter the info : ");
  scanf("%d", &ptr->info);
  printf("Do you wish to add another node : ");
  fflush(stdin);
  ch = getchar();
  if (ch == 'y')
  {
    ptr->next = (node *)malloc(sizeof(node));
    ptr->next->prev = ptr;
    create(ptr->next);
  }
  else
  {
    ptr->next = NULL;
    last = ptr;
  }
}

void fdisplay(node *ptr)
{
  printf("\nthe forward display \n");
  while (ptr != NULL)
  {
    printf("%d -> ", ptr->info);
    ptr = ptr->next;
  }
  printf("NULL");
}

void bdisplay(node *ptr)
{
  printf("\nthe backward display \n");
  while (ptr != NULL)
  {
    printf("%d -> ", ptr->info);
    ptr = ptr->prev;
  }
 printf("NULL");
}


