#include <iostream> //completed one extra
using namespace std;

void function(int a){
  a = 5*10;
  cout << a << endl;
  
}

int main() {
  for (int x=0;x<10;x++){
  std::cout << x << " , ";
}
std::cout << std::endl;  
  
  int x;
  cout << "Hello World!" << endl;
  cout << "My name is Anisha" << endl;
  if (50>45)
  cout << "50 is greater than 45" << endl; //Determine which of two numbers is greater
  function (x);

  return 0;
}