#include "sum.hpp"

int sum(double *x, int n)
{
	int i;
	double counter = 0;
	for(i=0;i<n;i++)
	{
		counter += x[i];
	}
	return counter;
}

int increment(int i)
{
	return i+2;
}


