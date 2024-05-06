#include <iostream>
#include <windows.h> // windows api library
#include <conio.h> // non standard libray with console commands
#include <typeinfo>

using namespace std;

// Height and weight of the boundary
const int width = 80;
const int height = 20;

// snake head coord
int x, y;

// coord of snake
int snakeTailx[100], snakeTaily[100];

// length of snake 
int snakeTailLen;

// snake's moving direction and snakesdirection variable
enum snakesDirection{STOP, LEFT, RIGHT, UP, DOWN};
enum snakesDirection sDir;

// food coord
int fruitCordx, fruitCordy;

// player score
int playerScore;

// bool var for gamer over
bool isGameOver;

void GameInit()
{
    isGameOver = false;
    sDir = STOP;
    x = width/2;
    y = height/2;
    fruitCordx = rand() % width;
    fruitCordy = rand() % height;
    playerScore = 0;
}

void GameRender(string playerName)
{
    system("cls"); //clear console

    // Creating top walls
    for (int i = 0 ; i<width+2 ;i++)
        cout << "-";
    cout << endl;

    //for (int)
}

int main(){
    //cout << typeid(snakesDirection).name() << endl;
    //srand(time(0)); // generate "random" seed
    //int i = 50;
    //cout << rand() % i;
    GameRender("bob");
    return 0;
}



