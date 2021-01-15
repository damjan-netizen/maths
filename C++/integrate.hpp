#ifndef INTEGRATE_HPP
#define INTEGRATE_HPP

#include <math.h>

extern "C"
double function(double kx, double ky, double kz, double * eps, double sigma, double G_max);

extern "C"
double integrate(int N, double * eps, double sigma, double G_max);

#endif


