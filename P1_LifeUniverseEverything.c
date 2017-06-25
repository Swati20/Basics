/*
Problem is : http://www.spoj.com/problems/EXPECT/ 
*/
#include <iostream>
using namespace std;

int main() {
	
	// your code here
	int n;
	while(true) {
		scanf("%d",&n);
		printf("%d\n",n);
		fflush(stdout);
		if(n==42) break;
	}

	return 0;
}
