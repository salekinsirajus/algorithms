/* file: bubblesort.c - Implements bubble sort */

void swap(int *array, int x, int y){
	/* Swap element at array[x] and array[y] position */
	int tmp;
	tmp = array[x];
	array[x] = array[y];
	array[y] = tmp;
}

void bubble_sort(int *array, int n) {
	/* Bubble Sort implementation
	 * Arguments:
	 *   int *array: a pointer to an array containing ints
	 *   int      n: the elements you want to sort (e.g. when
	 *				 the array is partially full)
	 * Return:
	 *   None, it modfifies the array in place
   	 */
	int swapped = 1;
	int i = 0, j;

	while (i < n - 1 && swapped) {
		swapped = 0;
		
		for (j = n - 1; j > i; j--) {
			
			if (array[j] < array[j - 1]) {
				swap(array, j, j - 1);
				swapped = 1;
			}
		}
		i++;
	}
}
