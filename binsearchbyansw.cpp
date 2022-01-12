#include <iostream>
#include <stdio.h>
#include <cmath>
using namespace std;

int check(int length, int amount, int* arr, int arrsize)
{
	int count = 0;
	int i = 0;
	while(i < arrsize)
	{
		int dist = arr[i] + length;
		count++;
		if(dist >= arr[arrsize-1])
		{
			break;
		}
		for(int n = i + 1; n < arrsize; n++)
		{
			if(arr[n] > dist)
			{
				i = n;
				break;
			}
		}
	}
	if(amount >= count)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

int main()
{
	int arrsize;
	cin >> arrsize;
	int number;
	cin >> number;
	int *arr = new int[arrsize];
	for(int i = 0; i < arrsize; i++)
	{
		cin >> arr[i];
	}

	int tosearch = 0;
	cin >> tosearch;
	int left = 0;
	int right = arr[arrsize-1] - arr[0];
	int last = -1;

	while(1)
	{
		if(abs(right - left) == 1)
		{
			cout << last << endl;
			break;
		}
		else if(!check(((left + right) / 2), number, arr, arrsize))
		{
			left = (right + left) / 2;
		}
		else
		{
			last = (right + left) / 2;
			right = (right + left) / 2;
		}
	}
}
