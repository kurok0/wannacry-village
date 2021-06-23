#include <unistd.h>

void  ft_print_alphabet(void)
{
  int a;

  a = 97;
  while(a >= 'a' && a <= 'z')
  {
    write(1, &a, 1);
    a++;
  }
}