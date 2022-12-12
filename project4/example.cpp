#include <iostream>

int main()
{
int i;

i = 0;
while (i<10){
  std::cout << i << " , ";
  i = i + 1;
  }
std::cout << std::endl; 

//for loop (rewriting of the while loop)

for (i=0;i<10;i++){
  std::cout << i << " , ";
}
std::cout << std::endl;  
  
return 0;
}

