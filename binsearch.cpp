#include <iostream>
#include <stdio.h>
#include <cmath>
using namespace std;

int main()
{
	int arrsize;
	cin >> arrsize;
	int *arr = new int[arrsize];
	for(int i = 0; i < arrsize; i++)
	{
		cin >> arr[i];
	}
	int searchsize;
	cin >> searchsize;
	for(int i = 0; i < searchsize; i++)
	{
		int tosearch = 0;
		cin >> tosearch;
		int left = 0;
		int right = arrsize;
		while(1)
		{
			if(tosearch == arr[(left + right) / 2])
			{
				cout << ((left + right) / 2) << endl;
				break;
			}
			else if(abs(right - left) == 1)
			{
				cout << -1 << endl;
				break;
			}
			else if(tosearch > arr[(left + right) / 2])
			{
				left = (right + left) / 2;
			}
			else if(tosearch < arr[(left + right) / 2])
			{
				right = (right + left) / 2;
			}
			else
			{
				cout << -1 << endl;
				break;
			}
		}
	}
}
