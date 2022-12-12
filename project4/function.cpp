#include <iostream>

//void is a special function that doesn't need to return the value

void print_hello(){
  std::cout << "hello world\n";
}
int add_two_numbers(int a, int b){
  int c;
  std::cout << "in func a: " << a << "b: " << b << "\n";
  c = a + b;
  return c;
}

int main()
{
  print_hello();
  int result = add_two_numbers(5,8);
  int a,b;
  a = 30;
  b = 100;
  result = add_two_numbers(b,a);
  std::cout << "in func a: " << a << "b: " << b << "\n";
  std::cout << result << "\n";


return 0;
}