#include <unistd.h>

void ft_putchar(char c)
{
  write(1, &c, 1);
}

void  ft_print_comb(void)
{
  int a;
  int b;
  int c;

  a = '0' - 1;
  while(a <= '7')
  {
    a++;
    b = a;
    while(b <= '8')
    {
      b++;
      c = b + 1;
      while(c <= '9')
      {
        ft_putchar(a);
        ft_putchar(b);
        ft_putchar(c);
        if(a != '7')
        {
          ft_putchar(',');
          ft_putchar(' ');
        }
        c++;
      }
    }
  }
}