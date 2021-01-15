#include "integrate.hpp"

double integrate(int N, double * eps, double sigma, double G_max)
{
    double sum = 0.0;
 
    for (int ix = 0; ix < N; ++ix)
    {
        double kx = -G_max + ix * 2.0 * G_max / double(N);
        for (int iy = 0; iy < N; ++iy)
        {
            double ky = -G_max + iy * 2.0 * G_max / double(N);
            for (int iz = 0; iz < N; ++iz)
            {
                double kz = -G_max + iz * 2.0 * G_max / double(N);
                sum = sum + function(kx, ky, kz, eps, sigma, G_max);
            }
        }
    }
    double volume_element = 2 * G_max / N * 2 * G_max / N * 2 * G_max / N;
    return sum * volume_element / 2.0 / M_PI / M_PI;
}

double function(double kx, double ky, double kz, double * eps, double sigma, double G_max)
{
    double k_mod = kx * kx + ky * ky + kz * kz;
 
    if (k_mod <= G_max * G_max && k_mod > 0.00001)
    {
        double k_eps_x = eps[0] * kx + eps[1] * ky + eps[2] * kz;
        double k_eps_y = eps[3] * kx + eps[4] * ky + eps[5] * kz;
        double k_eps_z = eps[6] * kx + eps[7] * ky + eps[8] * kz;
        double exponent = kx * k_eps_x + ky * k_eps_y + kz * k_eps_z;
        return exp(-sigma * sigma * exponent) / exponent;
    }
    return 0.0;
}
	