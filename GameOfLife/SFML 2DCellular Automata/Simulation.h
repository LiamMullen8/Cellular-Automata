#pragma once

#include <iostream>
#include <SFML/Graphics.hpp>
#include <SFML/System.hpp>
#include <SFML/Window.hpp>

/*
  Wrapper Class for entire Simulation
*/

class Simulation
{

private:

  // Window/init setup
  sf::RenderWindow* window;
  sf::VideoMode videoMode;
  sf::Event event;

  //Grid and Cells
  std::vector<sf::RectangleShape> Cells;
  
  sf::Vector2i mousePosWindow;

  //Game Logic
  int LiveCells;
  int DeadCells;

  // Priv Functions
  void initVars();
  void initWindow();
  void initCells();
  
public:

  //Con/De -structors
  Simulation();
  virtual ~Simulation();

  
  const bool IsRunning() const;

  
  void EventPoll();
  int countNeighbors(int i, int j);
  void updateMousePos();
  void updateGrid();
  void update();
  void render();
  void renderGrid();
  
};
