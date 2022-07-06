#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define N1 1000
#define N2 5000
#define N3 10000
#define SWAP(x,y) {int t; t=x; x=y; y=t;}

void setDecresingInput(int arr[], int size) {
	for (int i = 0; i < size; i++)
		arr[i] = size - i;
	printf("¡áinput: [%d %d %d ... %d %d %d]\n", arr[0], arr[1], arr[2]
		, arr[size - 3], arr[size - 2], arr[size - 1]);
}

void checkCorrectAnswer(int arr[], int size) {
	printf("¡áoutput: [%d %d %d ... %d %d %d]\n", arr[0], arr[1], arr[2], 
		arr[size - 3], arr[size - 2], arr[size - 1]);
	for (int i = 0; i < size; i++) {
		if (arr[i] != i + 1) {
			printf("wrong answer, with size %d\n", size);
			return;
		}
	}
	printf("correct answer, with size %d\n", size);
	return;
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
// inner iteration, we can start with i+1,
// because for every iteration, the first one is sorted.


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
// In the while statement, Shift may be a little faster than SWAP


void mergeSort(int arr[], int size, int start, int end) {
	if (start == end) return;

	int mid = (start + end) / 2;
	mergeSort(arr, size, start, mid);
	mergeSort(arr, size, mid + 1, end);

	int* sortedArr = (int*)malloc(sizeof(int) * (end - start + 1));

	int l = start, r = mid + 1, s = 0;
	while (l <= mid && r <= end) {
		if (arr[l] < arr[r])
			sortedArr[s++] = arr[l++];
		else
			sortedArr[s++] = arr[r++];
	}
	while (l <= mid)
		sortedArr[s++] = arr[l++];

	while (r <= end)
		sortedArr[s++] = arr[r++];

	s = 0;
	for (int i = start; i <= end; i++, s++) {
		arr[i] = sortedArr[s];
	}

	free(sortedArr);

}

void quickSort(int arr[], int start, int end) {
	if (start >= end) return;

	int mid = (start + end) / 2;
	SWAP(arr[mid], arr[end]);

	int pivot = arr[end];
	int l = start, r = end - 1;
	while (l <= r) {
		while (arr[l] < pivot && l < end) // l can move start to end
			l++;
		while (arr[r] > pivot && r > start) // r can move end-1 to start
			r--;
		if (l < r) {
			SWAP(arr[l], arr[r]);
		}
		else if (l == r) {
			break;
		}
	}
	SWAP(arr[l], arr[end]);
	// now pivot index is 'l'

	quickSort(arr, start, l - 1);
	quickSort(arr, l + 1, end);
}

void radixSort(int arr[], int size) {
	int maxExp = 1;
	int max = arr[0];
	for (int i = 0; i < size; i++) {
		if (arr[i] > max)
			max = arr[i];
	}
	while (max != 0) {
		max /= 10;
		maxExp *= 10;
	}
	maxExp /= 10;

	int nowExp = 1;
	int* nowArr = (int*)malloc(sizeof(int) * size);

	// using counting sort
	while (nowExp <= maxExp) {
		int bucket[10] = { 0,0,0,0,0,0,0,0,0,0 };
		for (int i = 0; i < size; i++)
			bucket[arr[i] / nowExp % 10]++;
		for (int i = 1; i < 10; i++)
			bucket[i] += bucket[i - 1];
		for (int i = size - 1; i >= 0; i--) //to stable
			nowArr[--bucket[arr[i] / nowExp % 10]] = arr[i];
		for (int i = 0; i < size; i++)
			arr[i] = nowArr[i];
		nowExp *= 10;
	}
	free(nowArr);
}

void bucketSort(int arr[], int size) {
	int bucketNum = size / 20;
	int** bucket = (int**)malloc(sizeof(int**) * bucketNum);
	for (int i = 0; i < bucketNum; i++)
		bucket[i] = (int*)malloc(sizeof(int*) * size);

	int* bucketSize = (int*)malloc(sizeof(int*) * bucketNum);
	for (int i = 0; i < bucketNum; i++) {
		bucketSize[i] = 0; //each bucket's element count
	}

	int min = arr[0], max = arr[0];
	for (int i = 0; i < size; i++) {
		if (arr[i] < min)
			min = arr[i];
		else if (arr[i] > max)
			max = arr[i];
	}

	int place; // find the right bucket place
	for (int i = 0; i < size; i++) {
		place = (arr[i] - min) * bucketNum / (max - min);
		if (place == bucketNum) place--;

		bucket[place][bucketSize[place]++] = arr[i];
	}
	for (int i = 0; i < bucketNum; i++) {
		// in bucket, we use insertion sort
		insertionSort(bucket[i], bucketSize[i]);
	}

	int idx = 0;
	for (int i = 0; i < bucketNum; i++) {
		for (int j = 0; j < bucketSize[i]; j++) {
			arr[idx++] = bucket[i][j];
		}
	}

	for (int i = 0; i < bucketNum; i++) {
		free(bucket[i]);
	}
	free(bucket);
}


int main() {
	int arr1[N1];
	int arr2[N2];
	int arr3[N3];

	clock_t startTime, endTime;
	double times[18];
	int cnt = 0;
	
	// ---1. Bubble Sort
	printf("\n\n---1. Bubble Sort:\n");
	setDecresingInput(arr1, N1);
	startTime = clock();
	bubbleSort(arr1, N1);
	endTime = clock();
	checkCorrectAnswer(arr1, N1);
	times[cnt] = (double)(endTime - startTime)*1000 / CLOCKS_PER_SEC;
	printf("Execution Time: %f\n", times[cnt++]);
	printf("\n");

	setDecresingInput(arr2, N2);
	startTime = clock();
	bubbleSort(arr2, N2);
	endTime = clock();
	checkCorrectAnswer(arr2, N2); 
	times[cnt] = (double)(endTime - startTime)*1000 / CLOCKS_PER_SEC;
	printf("Execution Time: %f\n", times[cnt++]);
	printf("\n");

	setDecresingInput(arr3, N3);
	startTime = clock();
	bubbleSort(arr3, N3);
	endTime = clock();
	checkCorrectAnswer(arr3, N3);
	times[cnt] = (double)(endTime - startTime)*1000 / CLOCKS_PER_SEC;
	printf("Execution Time: %f\n", times[cnt++]);
	printf("\n");
	

	// ---2. Insertion Sort
	printf("\n\n---2. Insertion Sort:\n");
	setDecresingInput(arr1, N1);
	startTime = clock();
	insertionSort(arr1, N1);
	endTime = clock();
	checkCorrectAnswer(arr1, N1);
	times[cnt] = (double)(endTime - startTime)*1000 / CLOCKS_PER_SEC;
	printf("Execution Time: %f\n", times[cnt++]);
	printf("\n");

	setDecresingInput(arr2, N2);
	startTime = clock();
	insertionSort(arr2, N2);
	endTime = clock();
	checkCorrectAnswer(arr2, N2);
	times[cnt] = (double)(endTime - startTime)*1000 / CLOCKS_PER_SEC;
	printf("Execution Time: %f\n", times[cnt++]);
	printf("\n");

	setDecresingInput(arr3, N3);
	startTime = clock();
	insertionSort(arr3, N3);
	endTime = clock();
	checkCorrectAnswer(arr3, N3);
	times[cnt] = (double)(endTime - startTime)*1000 / CLOCKS_PER_SEC;
	printf("Execution Time: %f\n", times[cnt++]);
	printf("\n");


	// ---3. Merge Sort
	printf("\n\n---3. Merge Sort:\n");
	setDecresingInput(arr1, N1);
	startTime = clock();
	mergeSort(arr1, 0, 0, N1 - 1);
	endTime = clock();
	checkCorrectAnswer(arr1, N1);
	times[cnt] = (double)(endTime - startTime)*1000 / CLOCKS_PER_SEC;
	printf("Execution Time: %f\n", times[cnt++]);
	printf("\n");

	setDecresingInput(arr2, N2);
	startTime = clock();
	mergeSort(arr2, 0, 0, N2 - 1);
	endTime = clock();
	checkCorrectAnswer(arr2, N2);
	times[cnt] = (double)(endTime - startTime)*1000 / CLOCKS_PER_SEC;
	printf("Execution Time: %f\n", times[cnt++]);
	printf("\n");

	setDecresingInput(arr3, N3);
	startTime = clock();
	mergeSort(arr3, 0, 0, N3 - 1);
	endTime = clock();
	checkCorrectAnswer(arr3, N3);
	times[cnt] = (double)(endTime - startTime)*1000 / CLOCKS_PER_SEC;
	printf("Execution Time: %f\n", times[cnt++]);
	printf("\n");


	// ---4. Quick Sort
	printf("\n\n---4. Quick Sort:\n");
	setDecresingInput(arr1, N1);
	startTime = clock();
	quickSort(arr1, 0, N1 - 1);
	endTime = clock();
	checkCorrectAnswer(arr1, N1);
	times[cnt] = (double)(endTime - startTime)*1000 / CLOCKS_PER_SEC;
	printf("Execution Time: %f\n", times[cnt++]);
	printf("\n");

	setDecresingInput(arr2, N2);
	startTime = clock();
	quickSort(arr2, 0, N2 - 1);
	endTime = clock();
	checkCorrectAnswer(arr2, N2);
	times[cnt] = (double)(endTime - startTime)*1000 / CLOCKS_PER_SEC;
	printf("Execution Time: %f\n", times[cnt++]);
	printf("\n");

	setDecresingInput(arr3, N3);
	startTime = clock();
	quickSort(arr3, 0, N3 - 1);
	endTime = clock();
	checkCorrectAnswer(arr3, N3);
	times[cnt] = (double)(endTime - startTime)*1000 / CLOCKS_PER_SEC;
	printf("Execution Time: %f\n", times[cnt++]);
	printf("\n");


	// ---5. Radix Sort
	printf("\n\n---5. Radix Sort:\n");
	setDecresingInput(arr1, N1);
	startTime = clock();
	radixSort(arr1, N1);
	endTime = clock();
	checkCorrectAnswer(arr1, N1);
	times[cnt] = (double)(endTime - startTime)*1000 / CLOCKS_PER_SEC;
	printf("Execution Time: %f\n", times[cnt++]);
	printf("\n");

	setDecresingInput(arr2, N2);
	startTime = clock();
	radixSort(arr2, N2);
	endTime = clock();
	checkCorrectAnswer(arr2, N2);
	times[cnt] = (double)(endTime - startTime)*1000 / CLOCKS_PER_SEC;
	printf("Execution Time: %f\n", times[cnt++]);
	printf("\n");

	setDecresingInput(arr3, N3);
	startTime = clock();
	radixSort(arr3, N3);
	endTime = clock();
	checkCorrectAnswer(arr3, N3);
	times[cnt] = (double)(endTime - startTime)*1000 / CLOCKS_PER_SEC;
	printf("Execution Time: %f\n", times[cnt++]);
	printf("\n");


	// ---6. Bucket Sort
	printf("\n\n---6. Bucket Sort:\n");
	setDecresingInput(arr1, N1);
	startTime = clock();
	bucketSort(arr1, N1);
	endTime = clock();
	checkCorrectAnswer(arr1, N1);
	times[cnt] = (double)(endTime - startTime)*1000 / CLOCKS_PER_SEC;
	printf("Execution Time: %f\n", times[cnt++]);
	printf("\n");

	setDecresingInput(arr2, N2);
	startTime = clock();
	bucketSort(arr2, N2);
	endTime = clock();
	checkCorrectAnswer(arr2, N2);
	times[cnt] = (double)(endTime - startTime)*1000 / CLOCKS_PER_SEC;
	printf("Execution Time: %f\n", times[cnt++]);
	printf("\n");

	setDecresingInput(arr3, N3);
	startTime = clock();
	bucketSort(arr3, N3);
	endTime = clock();
	checkCorrectAnswer(arr3, N3);
	times[cnt] = (double)(endTime - startTime)*1000 / CLOCKS_PER_SEC;
	printf("Execution Time: %f\n", times[cnt++]);
	printf("\n");

	// time table
	printf("\n\n");
	printf("%10s %10s %10s %10s %10s %10s %10s", "", "Bubble", "Insertion", 
		"Merge", "Quick", "Radix", "Bucket");
	printf("\n%10s ", "N = 1000");
	for (int i = 0; i < 18; i = i + 3) printf("%10f ", times[i]);
	printf("\n%10s ", "N = 5000");
	for (int i = 1; i < 18; i = i + 3) printf("%10f ", times[i]);
	printf("\n%10s ", "N = 10000");
	for (int i = 2; i < 18; i = i + 3) printf("%10f ", times[i]);

	printf("\n\n");
}
