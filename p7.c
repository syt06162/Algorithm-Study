
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define L 1024
#define M 1024
#define N 1024

void printMatrix(int**, int, int);
void mul_ordinary(int** a, int** b, int** c, int _L, int _M, int _N);

void mul_strassen(int** a, int** b, int** c, int size);

void matrix_add(int size, int** a, int ia, int ja, int** b, int ib, int jb, int** c, int ic, int jc);
void matrix_sub(int size, int** a, int ia, int ja, int** b, int ib, int jb, int** c, int ic, int jc);
void matrix_copy(int size, int** a, int ia, int ja, int** c, int ic, int jc);

int main() {
	srand(time(NULL));

	double ordiTime, straTime;
	clock_t startTime, endTime;

	// max(L,M,N) is 50,
	// and the smallest square number of 2 which is greater than or equal to 50 is 64
	// so, const value STS is 64 (in this test case)
	int ma = max(max(L, M),N);
	int mi;
	for (mi = 1; mi < ma; mi *= 2);
	const int STS = mi;

	// a, b: original matrix

	// c1: result of ordinary multiplication
	// c2: result of strassen's idea
	// a_STS, b_STS: in strassen, we change matrices (A, B)'s size to 2^n X 2^n

	int** matrix_a = (int**)malloc(sizeof(int*) * L);
	int** matrix_b = (int**)malloc(sizeof(int*) * M);
	int** matrix_c1 = (int**)malloc(sizeof(int*) * L);
	int** matrix_c2 = (int**)malloc(sizeof(int*) * STS);
	int** matrix_a_STS = (int**)malloc(sizeof(int*) * STS);
	int** matrix_b_STS = (int**)malloc(sizeof(int*) * STS);

	if (matrix_a && matrix_b && matrix_c1 && matrix_c2 && matrix_a_STS && matrix_b_STS) {
		for (int i = 0; i < L; i++) {
			matrix_a[i] = (int*)malloc(sizeof(int) * M);
		}
		for (int i = 0; i < M; i++) {
			matrix_b[i] = (int*)malloc(sizeof(int) * N);
		}
		for (int i = 0; i < L; i++) {
			matrix_c1[i] = (int*)malloc(sizeof(int) * N);
		}
		for (int i = 0; i < STS; i++) {
			matrix_c2[i] = (int*)malloc(sizeof(int) * STS);
			matrix_a_STS[i] = (int*)malloc(sizeof(int) * STS);
			matrix_b_STS[i] = (int*)malloc(sizeof(int) * STS);
		}
	}
	else {
		printf("insufficient memory, the function ended with error!\n");
	}



	// matrix_a initialize
	for (int i = 0; i < L; i++) {
		for (int j = 0; j < M; j++) {
			matrix_a[i][j] = rand() % 10 + 1; // 1~10 random int
		}
	}
	printf("¡ámatrix_a :\n");
	printMatrix(matrix_a, L, M);

	// matrix_b initialize
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			matrix_b[i][j] = rand() % 10 + 1; // 1~10 random int
		}
	}
	printf("¡ámatrix_b :\n");
	printMatrix(matrix_b, M, N);




	// matrix_c1, with ordinary multiplication
	startTime = clock();
	mul_ordinary(matrix_a, matrix_b, matrix_c1, L, M, N);
	endTime = clock();
	ordiTime = (double)(endTime - startTime);
	printf("¡ámatrix_c1, with ordinary multiplication:\n");
	printMatrix(matrix_c1, L, N);


	// matrix_c2, with strassen
	// first, make a, b to size(STS x STS),
	// if matrix[i][j] does not have any value, fill with 0
	for (int i = 0; i < STS; i++) {
		for (int j = 0; j < STS; j++) {
			matrix_a_STS[i][j] = 0;
			matrix_b_STS[i][j] = 0;
		}
	}
	for (int i = 0; i < L; i++) {
		for (int j = 0; j < M; j++)
			matrix_a_STS[i][j] = matrix_a[i][j];
	}
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++)
			matrix_b_STS[i][j] = matrix_b[i][j];
	}

	startTime = clock();
	mul_strassen(matrix_a_STS, matrix_b_STS, matrix_c2, STS);
	endTime = clock();
	straTime = (double)(endTime - startTime);
	printf("¡ámatrix_c2, with strassen:\n");
	printMatrix(matrix_c2, L, N);

	// execution time compare
	printf("¡áexecution time - ordinary : %f\n", ordiTime);
	printf("¡áexecution time - strassen : %f\n", straTime);

}

void printMatrix(int** matrix, int row, int col) {
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			printf("%4d ", matrix[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

void mul_ordinary(int **a, int **b, int **c, int _L, int _M, int _N) {
	for (int i = 0; i < _L; i++) {
		for (int j = 0; j < _N; j++) {
			c[i][j] = 0;
			for (int k = 0; k < _M; k++)
				c[i][j] += a[i][k] * b[k][j];
		}
	}
}

void mul_strassen(int** a, int** b, int** c, int size) {
	// if size==2 : basic strassen
	// else (= size is more than 2) : strassen with recursion

	if (size == 2) {
		int p1 = (**a) * ((*(*b + 1)) - (*(*(b + 1) + 1)));
		int p2 = ((**a) + (*(*a + 1))) * (*(*(b + 1) + 1));
		int p3 = (**(a + 1) + (*(*(a + 1) + 1))) * (**b);
		int p4 = (*(*(a + 1) + 1)) * ((**(b + 1)) - (**b));
		int p5 = ((**a) + (*(*(a + 1) + 1))) * ((**b) + (*(*(b + 1) + 1)));
		int p6 = ((*(*a + 1)) - *(*(a + 1) + 1)) * ((**(b + 1)) + (*(* (b + 1) + 1)));
		int p7 = ((**a) - (**(a + 1))) * ((**b) + (*(*b + 1)));

		**c = p5 + p4 - p2 + p6;
		*(*c + 1) = p1 + p2;
		**(c + 1) = p3 + p4;
		*(*(c + 1)+1) = p5 + p1 - p3 - p7;
	}
	else {
		int hSize = size / 2;  // half size

		int** temp1 = (int**)malloc(sizeof(int*) * hSize);
		int** temp2 = (int**)malloc(sizeof(int*) * hSize);
		int** p1 = (int**)malloc(sizeof(int*) * hSize);
		int** p2 = (int**)malloc(sizeof(int*) * hSize);
		int** p3 = (int**)malloc(sizeof(int*) * hSize);
		int** p4 = (int**)malloc(sizeof(int*) * hSize);
		int** p5 = (int**)malloc(sizeof(int*) * hSize);
		int** p6 = (int**)malloc(sizeof(int*) * hSize);
		int** p7 = (int**)malloc(sizeof(int*) * hSize);
		int** r = (int**)malloc(sizeof(int*) * hSize);
		int** s = (int**)malloc(sizeof(int*) * hSize);
		int** t = (int**)malloc(sizeof(int*) * hSize);
		int** u = (int**)malloc(sizeof(int*) * hSize);

		if (temp1 && temp2 && p1 && p2 && p3 && p4 && p5
			&& p6 && p7 && r && s && t && u) {
			for (int i = 0; i < hSize; i++) {
				temp1[i] = (int*)malloc(sizeof(int) * hSize);
				temp2[i] = (int*)malloc(sizeof(int) * hSize);
				p1[i] = (int*)malloc(sizeof(int) * hSize);
				p2[i] = (int*)malloc(sizeof(int) * hSize);
				p3[i] = (int*)malloc(sizeof(int) * hSize);
				p4[i] = (int*)malloc(sizeof(int) * hSize);
				p5[i] = (int*)malloc(sizeof(int) * hSize);
				p6[i] = (int*)malloc(sizeof(int) * hSize);
				p7[i] = (int*)malloc(sizeof(int) * hSize);
				r[i] = (int*)malloc(sizeof(int) * hSize);
				s[i] = (int*)malloc(sizeof(int) * hSize);
				t[i] = (int*)malloc(sizeof(int) * hSize);
				u[i] = (int*)malloc(sizeof(int) * hSize);
			}
		}
		else {
			printf("insufficient memory, the function ended with error!\n");
		}


		// p1 calculate
		matrix_copy(hSize, a, 0, 0, temp1, 0, 0);
		matrix_sub(hSize, b, 0, hSize, b, hSize, hSize, temp2, 0, 0);
		mul_strassen(temp1, temp2, p1, hSize);

		// p2 calculate
		matrix_add(hSize, a, 0, 0, a, 0, hSize, temp1, 0, 0);
		matrix_copy(hSize, b, hSize, hSize, temp2, 0, 0);
		mul_strassen(temp1, temp2, p2, hSize);

		// p3 calculate
		matrix_add(hSize, a, hSize, 0, a, hSize, hSize, temp1, 0, 0);
		matrix_copy(hSize, b, 0, 0, temp2, 0, 0);
		mul_strassen(temp1, temp2, p3, hSize);

		// p4 calculate
		matrix_copy(hSize, a, hSize, hSize, temp1, 0, 0);
		matrix_sub(hSize, b, hSize, 0, b, 0, 0, temp2, 0, 0);
		mul_strassen(temp1, temp2, p4, hSize);

		// p5 calculate
		matrix_add(hSize, a, 0, 0, a, hSize, hSize, temp1, 0, 0);
		matrix_add(hSize, b, 0, 0, b, hSize, hSize, temp2, 0, 0);
		mul_strassen(temp1, temp2, p5, hSize);

		// p6 calculate
		matrix_sub(hSize, a, 0, hSize, a, hSize, hSize, temp1, 0, 0);
		matrix_add(hSize, b, hSize, 0, b, hSize, hSize, temp2, 0, 0);
		mul_strassen(temp1, temp2, p6, hSize);

		// p7 calculate
		matrix_sub(hSize, a, 0, 0, a, hSize, 0, temp1, 0, 0);
		matrix_add(hSize, b, 0, 0, b, 0, hSize, temp2, 0, 0);
		mul_strassen(temp1, temp2, p7, hSize);


		// r calculate
		matrix_add(hSize, p5, 0, 0, p4, 0, 0, temp1, 0, 0);
		matrix_sub(hSize, p6, 0, 0, p2, 0, 0, temp2, 0, 0);
		matrix_add(hSize, temp1, 0, 0, temp2, 0, 0, r, 0, 0);

		// s calculate
		matrix_add(hSize, p1, 0, 0, p2, 0, 0, s, 0, 0);

		// t calculate
		matrix_add(hSize, p3, 0, 0, p4, 0, 0, t, 0, 0);

		// u calculate
		matrix_sub(hSize, p5, 0, 0, p3, 0, 0, temp1, 0, 0);
		matrix_sub(hSize, p1, 0, 0, p7, 0, 0, temp2, 0, 0);
		matrix_add(hSize, temp1, 0, 0, temp2, 0, 0, u, 0, 0);

		// copy "r,s,t,u" to "matrix c"
		matrix_copy(hSize, r, 0, 0, c, 0, 0);
		matrix_copy(hSize, s, 0, 0, c, 0, hSize);
		matrix_copy(hSize, t, 0, 0, c, hSize, 0);
		matrix_copy(hSize, u, 0, 0, c, hSize, hSize);

	}

}


// martix add, sub, copy operation, with variable size(variable name)

void matrix_add(int size, int** a, int ia, int ja, 
	int** b, int ib, int jb, int** c, int ic, int jc) {
	for (int i = 0; i < size; i++)
		for (int j = 0; j < size; j++)
			c[i + ic][j + jc] = a[i + ia][j + ja] + b[i + ib][j + jb];
}

void matrix_sub(int size, int** a, int ia, int ja, 
	int** b, int ib, int jb, int** c, int ic, int jc) {
	for (int i = 0; i < size; i++)
		for (int j = 0; j < size; j++)
			c[i + ic][j + jc] = a[i + ia][j + ja] - b[i + ib][j + jb];
}

void matrix_copy(int size, int** a, int ia, int ja, int** c, int ic, int jc) {
	for (int i = 0; i < size; i++)
		for (int j = 0; j < size; j++)
			c[i + ic][j + jc] = a[i + ia][j + ja];
}
