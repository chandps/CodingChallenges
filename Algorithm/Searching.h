#pragma once

#include <array>

static const int NOT_FOUND = -1;

/*
Linear search x in arr[] (time o(n), space o(n))
return index element of x, return -1 if not found
*/
int linearSearch(int arr[], unsigned int n, int x) {

	for (size_t i = 0; i < n; i++)
	{
		if (arr[i] == x)
		{
			return i;
		}
	}

	return NOT_FOUND;
}

/* Linear Search using STL array */
template <size_t size>
int linearSearch(std::array<int,size> arr, int x) {
	
	int index = 0;
	for each (auto val in arr)
	{
		if (val == x)
		{
			return index;
		}
		index++;
	}

	return NOT_FOUND;
}

/*
Binary Search x in sorted array A (time o(log n), space o(n))
return index element of x, return -1 if not found
*/
int binarySearch(int A[], int left, int right, int x) {
	// exception
	if ((right - left) < 0) return NOT_FOUND;
	// base case
	if ((right - left) < 2)
	{
		if (right == left) // array size = 1
		{
			return (A[right] == x) ? right : NOT_FOUND;
		}
		// array size = 2
		return (A[right] == x) ? right : 
			((A[left] == x) ? left : NOT_FOUND);
	}

	// check middle, if not match, go to left/right
	int middle = (left + right) / 2;
	if (A[middle] == x) return middle;
	
	if (A[middle] < x)
	{
		return binarySearch(A, middle + 1, right, x);
	}
	else
	{
		return binarySearch(A, left, middle - 1, x);
	}
}

/* Binary Search without offset */
int binarySearch(int A[], int x) {
	int left = 0, right = sizeof(A) / sizeof(A[0]);
	return binarySearch(A, left, right, x);
}

/* Binary Search using STL array */
template <size_t size>
int binarySearch(std::array<int, size> A, int left, int right, int x) {
	int a[size] = A;
	return binarySearch(a, left, right, x);
}
