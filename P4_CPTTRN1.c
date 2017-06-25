/*http://www.spoj.com/problems/CPTTRN1/*/
#include <stdio.h>

int main(void) {
	// your code here
	int n,l,c,i,j;
	scanf("%d",&n);
	while(n--){
		scanf("%d%d",&l,&c);
		for(i=0;i<l;i++){
			for(j=0;j<c;j++){
				if((i+j)%2 == 0) printf("*");
				else printf(".");
			}
			printf("\n");
		}
	}
	return 0;
}
