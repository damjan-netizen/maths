#include "integrator.hpp"

double function(double kx, double ky, double kz, double * epsilon, double sigma, double G_max)
{
	double k_mod = kx*kx + ky*ky + kz*kz;
	if(k_mod<=G_max*G_max && k_mod>0.00001)
	{
		double kx_eps = epsilon[0]*kx + epsilon[1]*ky + epsilon[2]*kz;
		double ky_eps = epsilon[3]*kx + epsilon[4]*ky + epsilon[5]*kz;
		double kz_eps = epsilon[6]*kx + epsilon[7]*ky + epsilon[8]*kz;
		double kek = kx*kx_eps + ky*ky_eps + kz*kz_eps;
		return exp(-sigma*sigma*kek)/kek;
	}
	return 0.0;
}

double integrate(int N, double sigma, double * epsilon, double G_max)
{
	double integral = 0;
	for(int ix=0;ix<N;ix++)
	{
		double kx = -G_max + ix*2.0*G_max/double(N);
		for(int iy=0;iy<N;iy++)
		{
			double ky = -G_max + iy*2.0*G_max/double(N);
			for(int iz=0;iz<N;iz++)
			{
				double kz = -G_max + iz*2.0*G_max/double(N);
				double value = function(kx, ky, kz, epsilon, sigma, G_max);
				integral +=value;
			}
		}
	}
	
	double volume_element = (2*G_max/double(N))*(2*G_max/double(N))*(2*G_max/double(N));
	return integral*volume_element/2.0/M_PI/M_PI;
}

	
	
	
				