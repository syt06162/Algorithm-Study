
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	char string[100];
	printf("input String: ");
	scanf("%s", string);

	int left = 0; // string's left position
	int right = 0; // string's right position
	for (; string[right]; right++); // right goes to the last of the string
	right--;

	int flag = 1; // 1: palindorme,  0: NOT

	for (; left < right; left++, right--) {
		if (string[left] != string[right])
		{
			flag = 0;
			break;
		}
	}

	if (flag == 1) {
		printf("It is a Palindrome\n");
	}
	else {
		printf("It is NOT Palindrome\n");
	}

	printf("\n\n");
}
