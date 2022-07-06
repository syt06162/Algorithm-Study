#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int arr[] = { 12, 34, 37, 45, 57, 82, 99, 120, 134 };
	int size = sizeof(arr) / sizeof(int);
	int target;
	int flag = 0; // flag is false (not found yet)

	printf("input finding value: ");
	scanf("%d", &target);

	int left = 0;
	int right = size - 1;
	int mid;

	while (left <= right) {
		mid = (int)((left + right) / 2);
		if (arr[mid] == target) {
			flag = 1; // we find target index
			break;
		}
		else if (arr[mid] < target) {
			left = mid + 1;
		}
		else {
			right = mid - 1;
		}
	}

	if (flag == 1)
		printf("target index : %d\n", mid);
	else
		printf("there is no target value");

}