#include <iostream>
#include "Simulation.h"

int main()
{
  // Simulation Initialize
  Simulation sim;

  while(sim.IsRunning())
    {
      //Update
      sim.update();
      sim.render();
    }
  return 0;
}
