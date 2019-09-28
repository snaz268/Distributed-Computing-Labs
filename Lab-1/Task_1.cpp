#include <iostream>
#include <chrono>
using namespace std;

static long nSteps = 100000;
double steps;

void main()
{
	auto start_time = std::chrono::high_resolution_clock::now();
	int i = 0;
	double x, pi, sum = 0.0;
	steps = 1 / (double)nSteps;

	for (int i = 0; i < nSteps; i++)
	{
		x = (i + 0.5) * steps;
		sum = sum + 4.0 / (1 + x * x);
	}
	pi = steps * sum;
	std::cout << "Pi " << pi << std::endl;
	auto end_time = std::chrono::high_resolution_clock::now();
	auto time = end_time - start_time;
	std::cout << "It ran for " <<
		std::chrono::duration_cast <std::chrono::microseconds>(time).count() << " ms.\n";
	system("pause");
}
