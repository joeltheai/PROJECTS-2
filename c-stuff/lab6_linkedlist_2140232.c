
// 2140232
// joel varghese

#include <stdio.h>
#include <stdlib.h>

struct list
{
  int info;
  struct list *link;
};

typedef struct list node;

void create(node *);
void display(node *);
void search(node *);

int main()
{
  char ch, ch1;
  int c;
  node *head;
  ch = 'y';
  ch1 = 'y';
  do
  {
    system("cls");
    printf("...........Linked list Program...........\n");
    head = (node *)malloc(sizeof(node));
    if (head != NULL)
    {
      create(head);
      display(head);
      search(head);
      
    }
    printf("\nDo you wish to rerun the program : ");
    fflush(stdin);
    ch = getchar();
  } while (ch == 'y');
  return 0;
}

void create(node *ptr)
{
  char ch;
  printf("\nEnter the element to add to array : ");
  scanf("%d", &ptr->info);
  printf("Do you wish to add another element : ");
  fflush(stdin);
  ch = getchar();
  if (ch == 'y')
  {
    ptr->link = (node *)malloc(sizeof(node));
    create(ptr->link);
  }
  else
  {
    ptr->link = NULL;
  }
}

void display(node *ptr)
{
  printf("\nThe list is : ");
  while (ptr != NULL)
  {
    printf("%d -> ", ptr->info);
    ptr = ptr->link;
  }
  printf("NULL");
}

void search(node *ptr)
{
  int data;
  char ch;
  node *temp = ptr;
  int flag;
  do
  {
    int cc = 0;
    flag = 0;
    ptr = temp;
    printf("\n\nEnter the element to be searched : ");
    scanf("%d", &data);
    while (ptr != NULL)
    {
      cc++;
      if (data == ptr->info)
      {
        printf("\nElement found at position %d", cc);
        flag = 1;
        break;
      }
      ptr = ptr->link;
    }
    if (flag == 0)
    {
      printf("\nElement not found");
    }
    printf("\nsearch again ? : ");
    fflush(stdin);
    ch = getchar();
  } while (ch == 'y');
}