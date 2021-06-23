#include <unistd.h>

void ft_print_reverse_alphabet(void)
{
  int a;

  a = 122;
  while(a >= 'a' && a <= 'z')
  {
    write(1, &a, 1);
    a--;
  }
}