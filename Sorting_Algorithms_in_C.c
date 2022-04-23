#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS
#define N1 100
#define N2 500
#define N3 1000
#define SWAP(x,y) {int t; t=x; x=y; y=t;}

void setDecresingInput(int arr[], int size) {
	for (int i = 0; i < size; i++)
		arr[i] = size - i;
	printf("■input: [%d %d %d ... %d %d %d]\n", arr[0], arr[1], arr[2], arr[size - 3], arr[size - 2], arr[size - 1]);
}

void checkCorrectAnswer(int arr[], int size) {
	for (int i = 0; i < size; i++) {
		if (arr[i] != i + 1) {
			printf("wrong answer, with size %d\n", size);
			return;
		}
	}
	printf("■output: [%d %d %d ... %d %d %d]\n", arr[0], arr[1], arr[2], arr[size - 3], arr[size - 2], arr[size - 1]);
	printf("correct answer, with size %d\n\n", size);
	return;
}

void printArray(int arr[], int size) {
	for (int i = 0; i < size; i++)
		printf("%3d ", arr[i]);
	printf("\n");
}

// Assume that the size of all input arrays is greater than 1,
// and also there is no same value ////
void bubbleSort(int arr[], int size) {
	for (int i = 0; i < size - 1; i++) {
		for (int j = i + 1; j < size; j++) {
			if (arr[i] > arr[j]) 
				SWAP(arr[i], arr[j]);
		}
	}
}
// 안에 반복문은 j=0부터 할 필요없이, i+1부터 하면된다. 왜냐하면 앞에서부터 1개씩은 정렬되기 때문.

void insertionSort(int arr[], int size) {
	int key, j;
	for (int i = 1; i < size; i++) {
		key = arr[i];
		j = i - 1;
		while (j >= 0 && arr[j] > key) {
			arr[j + 1] = arr[j];
			j--;
		}
		arr[j + 1] = key;
	}
}
// while문안에서 shift 하는것이 swap보다 약간 더 빠를거라 기대함.


int main() {
	int arr1[N1];
	int arr2[N2];
	int arr3[N3];

	setDecresingInput(arr1, N1);
	bubbleSort(arr1, N1);
	checkCorrectAnswer(arr1, N1);
}
