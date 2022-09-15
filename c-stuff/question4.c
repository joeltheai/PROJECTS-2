//2140232
//joel varghese

// 4. Write a C program to accept a set of integers by dynamically allocating memory [use malloc()] and
// then sort the numbers in ascending order using selection sort.

#include <stdio.h>
#include <stdlib.h>

int main()
{
  int ch = 1;
  do
  {
  int *ptr;
  int n, i, k, minindex, j, temp;
  system("cls");
  printf("\n\nEnter number of elements : ");
  scanf("%u", &n);
  fflush(stdin);

  ptr = (int *)malloc(n * sizeof(int));

  if (ptr == NULL)
  {
    printf("Memory not allocated.\n\n");
  }
  else
  {

    printf("Memory successfully allocated for %d elements using malloc at %u.\n\n", n,ptr);

    for (i = 0; i < n; ++i)
    {
      printf("Enter  element #%d : ", i + 1);
      scanf("%d", &k);
      ptr[i] = k;
    }

    printf("\nThe elements of the array are: \n");
    for (i = 0; i < n; ++i)
    {
      printf("%d\t", ptr[i]);
    }

    for (i = 0; i < n - 1; i++)
    {

      minindex = i;
      for (j = i + 1; j < n; j++)
      {
        if (ptr[j] < ptr[minindex])
          minindex = j;
      }

      temp = ptr[minindex];
      ptr[minindex] = ptr[i];
      ptr[i] = temp;
    }
    printf("\n\nThe array after selection sort: \n");
    for (i = 0; i < n; ++i)
    {
      printf("%d\t", ptr[i]);
    }
  }printf("\n\nDo you wish to rerun program? (1 for yes) : ");
  scanf("%d",&ch);

  } while (ch == 1);
  printf("\n\nProgram ended");
  return 0;
}
