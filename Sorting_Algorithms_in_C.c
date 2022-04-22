#include <stdio.h>
#define N1 100
#define N2 500
#define N3 1000
#define SWAP(x,y) {int t; t=x; x=y; y=t;}

void setDecresingInput(int arr[], int size) {
	for (int i = 0; i < size; i++)
		arr[i] = size - i;
}

void checkCorrectAnswer(int arr[], int size) {
	for (int i = 0; i < size; i++) {
		if (arr[i] != i + 1) {
			printf("wrong answer, with size %d\n", size);
			return;
		}
	}
	printf("correct answer, with size %d\n", size);
	return;
}

void printArray(int arr[], int size) {
	for (int i = 0; i < size; i++)
		printf("%3d ", arr[i]);
	printf("\n");
}

// Assume that the size of all input arrays is greater than 1.
void bubbleSort(int arr[], int size) {
	for (int i = 0; i < size - 1; i++) {
		for (int j = i + 1; j < size; j++) {
			if (arr[i] > arr[j]) 
				SWAP(arr[i], arr[j]);
		}
	}
}

void insertionSort(int arr[], int size) {
	for (int i = 1; i < size; i++) {
		for (int j = i + 1; j < size; j++) {
			if (arr[i] > arr[j])
				SWAP(arr[i], arr[j]);
		}
	}
}


int main() {
	int arr1[N1];
	int arr2[N2];
	int arr3[N3];

	setDecresingInput(arr1, N1);
	printArray(arr1, N1);

	bubbleSort(arr1, N1);
	printArray(arr1, N1);

}
