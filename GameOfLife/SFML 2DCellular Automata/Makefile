GXX = g++
LIBS = -lsfml-graphics -lsfml-window -lsfml-system
TARGET = Cellular

SOURCES = main.cpp Simulation.cpp
OBJECTS = $(SOURCES:.cpp=.o)

all: $(OBJECTS)
	$(GXX) $(OBJECTS) -o $(TARGET) $(LIBS)


$(OBJECTS): %o: %cpp
	$(GXX) -c $<

clean:
	$(RM) $(TARGET) $(OBJECTS)
