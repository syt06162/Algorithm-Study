#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 5

void printMatrix(int[][SIZE]);
void rotateMatrix(int[][SIZE]);

int main() {
	srand(time(NULL));

	int matrix[SIZE][SIZE];
	for (int i = 0; i < SIZE; i++) {
		for (int j = 0; j < SIZE; j++) {
			matrix[i][j] = rand() % 100 + 1; // 1~100 random int
		}
	}

	printf("initial: \n");
	printMatrix(matrix);

	rotateMatrix(matrix);
	printf("rotate 1 time: \n");
	printMatrix(matrix);

	rotateMatrix(matrix);
	printf("rotate 2 times: \n");
	printMatrix(matrix);

	rotateMatrix(matrix);
	printf("rotate 3 times: \n");
	printMatrix(matrix);

	rotateMatrix(matrix);
	printf("rotate 4 times: \n");
	printMatrix(matrix);

}

void printMatrix(int matrix[][SIZE]) {
	for (int i = 0; i < SIZE; i++) {
		for (int j = 0; j < SIZE; j++) {
			printf("%3d ", matrix[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

void rotateMatrix(int matrix[][SIZE]) {
	int newMatrix[SIZE][SIZE];

	for (int i = 0; i < SIZE; i++) {
		for (int j = 0; j < SIZE; j++) {
			newMatrix[j][SIZE - i - 1] = matrix[i][j];
		}
	}
	
	// copy to the origin
	for (int i = 0; i < SIZE; i++) {
		for (int j = 0; j < SIZE; j++) {
			matrix[i][j] = newMatrix[i][j];
		}
	}
}