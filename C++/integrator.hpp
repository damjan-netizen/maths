#ifndef INTEGRATOR_HPP
#define INTEGRATOR_HPP

#include <math.h>

extern "C"
double function(double kx, double ky, double kz, double *epsilon, double sigma, double G_max);

extern "C"
double integrate(int N, double sigma, double * epsilon, double G_max);

#endif

 