
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main() {
	
	int n;
	printf("input n: ");
	scanf("%d", &n);

	int k = 1;
	int mul = 2;
	for (; mul <= n; k++) {
		mul *= 2;
	}
	printf("output k: %d\n", k - 1);
	
	return 0;
}