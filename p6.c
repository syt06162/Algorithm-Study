#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 10

void pairSum(int arr[], int target);

int main() {
	int arr[SIZE] = { 2,4,3,5,6,-2,4,7,8,9 };
	int givenNumber = 7;

	pairSum(arr, givenNumber);
}

void pairSum(int arr[], int target) {
	int size = SIZE;
	char result[100][100];
	int resultNum = 0;
	char buf1[100];

	for (int i = 0; i < size - 1; i++) {
		for (int j = i + 1; j < size; j++) {
			if (arr[i] + arr[j] == target) {
				// add to result
				char temp[100] = "";
				strcat(temp, _itoa(arr[i], buf1, 10));
				strcat(temp, "+");
				strcat(temp, _itoa(arr[j], buf1, 10));

				strcpy(result[resultNum++], temp);
			}
		}
	}

	for (int i = 0; i < resultNum; i++) {
		for (int j = 0; result[i][j]; j++)
			printf("%c", result[i][j]);
		if (i!=resultNum-1) {
			printf(", ");
		}
	}
	printf("\n");
}