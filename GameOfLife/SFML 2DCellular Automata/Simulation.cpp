#include "Simulation.h"


void Simulation::initVars()
{
    this->window = nullptr;
    this->LiveCells = 0;
    this->DeadCells = 0;    
}

void Simulation::initWindow()
{
  this->videoMode.height = 256;
  this->videoMode.width = 256;
  
  this->window = new sf::RenderWindow(this->videoMode, "Cellular Automata",  sf::Style::Resize | sf::Style::Close);
  this->window->setFramerateLimit(144);
  this->window->setSize(sf::Vector2u(1024,1024));
}

void Simulation::initCells()
{
  std::vector<sf::RectangleShape> c;
  this->Cells = c;

  int width = this->videoMode.width;
  int height = this->videoMode.height;

  int i,j;
  for(i=0; i < height; i++){    
    for(j=0; j < width; j++){
      
      sf::RectangleShape cell;

      cell.setPosition(j, i);
      cell.setSize(sf::Vector2f(1.f,1.f));

      if (i==0 || i == width-1){
	cell.setFillColor(sf::Color::White);
      }
      else{
	if (rand() % 100 > 60){
	  cell.setFillColor(sf::Color::White);
	}
	else{
	  cell.setFillColor(sf::Color::Black);
	}
      }

      this->Cells.push_back( cell );
    }

    //border walls
    this->Cells[0 + i*height].setFillColor(sf::Color::White);
    this->Cells[width-1 + i*height].setFillColor(sf::Color::White);
  }
}

// Con-/De- structors
Simulation::Simulation()
{
  this->initVars();
  this->initWindow();
  this->initCells();
}

Simulation::~Simulation()
{
  delete this->window;  // prevent memory leaks
}

const bool Simulation::IsRunning() const
{
  return this->window->isOpen();
}

void Simulation::EventPoll()
{
  //Event polling
  while(this->window->pollEvent(this->event))
    {
      switch (this->event.type)
	{
	case sf::Event::Closed:
	  this->window->close();
	  break;
          
	case sf::Event::KeyPressed:
	  if(this->event.key.code == sf::Keyboard::Escape)
	    this->window->close();
	  else if(this->event.key.code == sf::Keyboard::G)
	    this->window->close();
	  break;
	}
    }
}

void Simulation::updateMousePos()
{
  this->mousePosWindow = sf::Mouse::getPosition(*this->window);
}

int Simulation::countNeighbors(int j, int i)
{

  int height = this->videoMode.height;
  std::vector<sf::RectangleShape> neighbors = {
    this->Cells[(j-1) + (i-1)*height],
    this->Cells[(j)   + (i-1)*height],
    this->Cells[(j+1) + (i-1)*height],
    this->Cells[(j-1) + (i)*height],
    this->Cells[(j+1) + (i)*height],
    this->Cells[(j-1) + (i+1)*height],
    this->Cells[(j)   + (i+1)*height],
    this->Cells[(j+1) + (i+1)*height]
  };
  
  int count = 0;
  
  for (auto& cell: neighbors)
  {    
    if(cell.getFillColor() == sf::Color::White)
    {
      count++;
    }
  }
  
  return count;
 
}

void Simulation::updateGrid()
{
  std::vector<sf::RectangleShape> newGrid = Cells;
  int width = this->videoMode.width;
  int height = this->videoMode.height;

  for(int i=1; i < height - 1; i++)
  {
    for( int j=1; j < width - 1; j++)
    {
      sf::Color c = Cells[j + i*height].getFillColor();
      int N = this->countNeighbors(j, i);
      
      if(c == sf::Color::White)
      {
	if(N<2 || N>3)
	{
	  newGrid[j + i*height].setFillColor(sf::Color::Black);
	}
      }
      else if(c == sf::Color::Black)
      {
	if (N==3)
	{
	  newGrid[j + i*height].setFillColor(sf::Color::White);
	}	    
      } 
    }
  }
  this->Cells = newGrid;
  newGrid.clear();
}
 
// logic / functions / math / anything non-rendering
void Simulation::update()
{
  this->EventPoll();
  this->updateMousePos();
  this->updateGrid();
}

void Simulation::renderGrid()
{  
  for(auto & cell: this->Cells)
  {
    this->window->draw(cell);
  }
  
}

void Simulation::render()
{
  this->window->clear();  

  this->renderGrid();
  
  this->window->display();
}
