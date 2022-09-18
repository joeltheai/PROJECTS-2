
// 2140232
// joel varghese

#include <stdlib.h>
#include <stdio.h>

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
void clean_stdin(void);
void func();
node *insert(node *);

int main()
{

  char ch, ch1, ch4, ch3;
  int c, h;
  node *head;
  ch = 'y';
  ch1 = 'y';
  ch4 = 'y';
  ch3 = 'y';
  do
  {
    func();
    system("clear");
    printf("...........Linked list Program...........\n");
    head = (node *)malloc(sizeof(node));
    if (head != NULL)
    {
      create(head);
      display(head);
      do
      {
        printf("\nMENU\n1.Search\n2.Insert");
        printf("\n\nEnter choice (1,2) : ");
        scanf("%d", &h);
        switch (h)
        {
        case 1:
        {
          search(head);
          break;
        }
        case 2:
        {
          do
          {
            head = insert(head);
            display(head);
            printf("\nDo you wish insert again: ");
            clean_stdin();
            ch3 = getchar();

          } while (ch3 == 'y');
          break;
        }
        }

        printf("\nDo you wish to open menu again: ");
        fflush(stdin);
        scanf(" %c", &ch4);
      } while (ch4 == 'y');
    }
    printf("\nDo you wish to rerun the program : ");

    scanf(" %c", &ch);
  } while (ch == 'y');
  return 0;
}

void func()
{
  count = 0;
}

void clean_stdin(void)
{
  int c;
  do
  {
    c = getchar();
  } while (c != '\n' && c != EOF);
}

void create(node *ptr)
{
  char ch;
  printf("\nEnter the element to add to array : ");
  scanf("%d", &ptr->info);

  count++;
  printf("Do you wish to add another element : ");
  fflush(stdin);
  scanf(" %c", &ch);
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
  printf("\nThe list ik : ");
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
    scanf(" %c", &ch);
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