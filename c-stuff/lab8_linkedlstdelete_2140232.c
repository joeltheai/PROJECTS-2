// 2140232
// joel varghese

#include <stdio.h>
#include <stdlib.h>
int count = 0;
struct list
{
  int info;
  struct list *link;
};

typedef struct list node;

void create(node *);
void display(node *);
void search(node *);

node *delete (node *);

void func()
{
  count = 0;
}

node *insert(node *);

int main()
{

  char ch, ch1, ch4, ch3, ch5;
  int c, h, jj;
  node *head;
  ch = 'y';
  ch1 = 'y';
  ch4 = 'y';
  ch3 = 'y';
  ch5 = 'y';
  do
  {
    func();
    system("cls");
    printf("...........Linked list Program...........\n");
    head = (node *)malloc(sizeof(node));
    if (head != NULL)
    {
      create(head);
      display(head);
      do
      {
        printf("\n\nMENU");
        printf("\n1.insert");
        printf("\n2.delete\n");
        scanf("%d", &jj);
        switch (jj)
        {
        case 1:
        {
          head = insert(head);
          display(head);
          break;
        }
        case 2:
        {
          head = delete (head);
          break;
        }
        }
        printf("\nopen menu again ? ");
        fflush(stdin);
        ch5 = getchar();
      } while (ch5 == 'y');
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
  count++;
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

node *insert(node *ptr)
{
  int pos, i = 1;
  node *temp = ptr, *newnode;
  printf("\nEnter pos(1-%d) : ", count + 1);
  scanf("%d", &pos);

  if ((pos > 0) && (pos <= count + 1))
  {
    count++;
    newnode = (node *)malloc(sizeof(node));
    printf("\nEnter info : ");
    scanf("%d", &newnode->info);
    if (pos == 1)
    {
      newnode->link = ptr;
      ptr = newnode;
    }
    else
    {
      while (i < pos - 1)
      {
        temp = temp->link;
        i++;
      }
      newnode->link = temp->link;
      temp->link = newnode;
    }
  }
  else
  {
    printf("\n INVALID POS");
  }
  return ptr;
}

node *delete (node *ptr)
{
  int pos, i = 1;
  char ch, ch1;
  node *temp1 = ptr, *temp2 = ptr;

  do
  {
    printf("\nEnter position (1-%d)", count);
    scanf("%d", &pos);
    if ((pos > 0) && (pos < count + 1))
    {
      if (pos == 1)
      {
        temp1 = ptr;
        ptr = ptr->link;
        free(temp1);
      }
      else
      {
        while (i < pos - 1)
        {
          temp1 = temp1->link;
          i++;
        }
        temp2 = temp1->link;
        temp1->link = temp2->link;
        free(temp2);
      }
      count--;
      display(ptr);
    }
    else
    {
      printf("\ninvalid pos");
      break;
    }
    printf("\nContinue?");
    fflush(stdin);
    ch = getchar();
  } while (ch == 'y');
  return ptr;
}