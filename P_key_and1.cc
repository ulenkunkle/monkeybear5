#include <iostream>
#include <cstdlib>
#include <stdio.h>
using namespace std;

#define ranf() \
  ((double)random()/(1.0+(double)RAND_MAX)) // Uniform from interval [0,1) */

int main(int argc, char* argv[])


{
  int outcome, N=10, count_in=0 ;
  long seed=123 ;
  double fraction_in ;
  char *position , in[]="IN", out[]="OUT" ; 
  printf("%s \n\n\n","--------------START------------");
  if(argc>1) {
    sscanf( argv[1], "%d", &N ) ; // put the first command-line argument in N
  }
  if(argc>2) {
    sscanf( argv[2], "%ld", &seed ) ; // put the 2nd argument in seed
  }
  // Write out a summary of what's going to happen
  cout << "# " << argv[0] << " N=" << N << " seed=" << seed << endl ;
  
  // Initialise random number generator 
  srandom(seed);
  
  // Perform N experiments. 
  for(int n=1; n<=N; n++)
    {
      double x = ranf();
      double y = ranf();
      
      outcome = ( x*x + y*y > 1.0 ) ? 0 : 1 ; 
      position = ( x*x + y*y > 1.0 ) ? out : in ; 
      printf("out---%d   pos----%f  ", x,y);
      if(outcome==1) count_in++;
      cout << position << "\t" << x << "\t" << y << "\t"
	   << count_in << "\t" << n << endl;
    }
  
  //Integer variables must be converted (cast) for correct division
  fraction_in = static_cast<double>(count_in)/N;

  // Output results
  cout << "# Proportion of outcomes 'in' " 
       << fraction_in << endl;
  // Output results
  cout << "# pi-hat = " 
       << 4.0 * fraction_in << endl;
  printf("\n\n\n\n your public key is now figured at :: %f\n\n\n\n", ranf()*10000000000000000);
  return 0;
}

