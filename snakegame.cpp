#include <iostream>
#include <windows.h> // windows api library
#include <conio.h> // non standard libray with console commands, used for user inputs
#include <typeinfo>

using namespace std;

// Height and weight of the boundary
const int width = 40;
const int height = 10;

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

    for (int i=0; i< height;i++){
        for (int j=0;j<=width;j++){
            // sidewalls '|'
            if (j==0||j==width)
                cout << "|";
            // head of snake 'O'
            if (i==y && j==x)
                cout << "O";
            // food
            else if (i==fruitCordy && j==fruitCordx)
                cout << "$";
            // snake head
            else{
                bool prTail=false;
                for (int k=0; k<snakeTailLen;k++){
                    if (snakeTailx[k]==j && snakeTaily[k]==i){
                        cout << "O";
                        prTail = true;
                    } 
                }
                if (!prTail)
                    cout << " ";
            }
        }
        cout << endl;
    }

    // bottom walls
    for (int i=0;i<width+2;i++)
        cout << "-";
    cout << endl;

    // display player score
    cout << playerName << "'s score: " << playerScore << endl;
}

void UpdateGame(){
    int prevx = snakeTailx[0];
    int prevy = snakeTaily[0];
    int prev2x, prev2y;
    snakeTailx[0]=x;
    snakeTaily[0]=y;

    for (int i =1;i<snakeTailLen;i++){
        prev2x = snakeTailx[i];
        prev2y = snakeTaily[i];
        snakeTailx[i] = prevx;
        snakeTaily[i] = prevy;
        prevx = prev2x;
        prevy = prev2y; 
    }

    switch (sDir)
    {
    case LEFT:
        x--;
        break;
    case RIGHT:
        x++;
        break;
    case UP:
        y--;
        break;
    case DOWN:
        y++;
        break;    
    }

    // colision with wall
    if (x>=width || x<0 || y>=height || y<0)
        isGameOver = true;

    // collision with tail
    for (int i =0; i < snakeTailLen;i++){
        if (snakeTailx[i] == x && snakeTaily[i] == y)
            isGameOver = true;
    }

    // eating food (collision)
    if ( x == fruitCordx && y == fruitCordy){
        playerScore+=10;
        fruitCordx = rand() % width;
        fruitCordy = rand() & height;
        snakeTailLen++;
    }
}

void UserInput(){
    if (_kbhit()){ // keyboardhit
        switch (_getch()) // get key pressed
        {
        case 'a':
            sDir = LEFT;
            break;
        case 'd':
            sDir = RIGHT;
            break;
        case 'w':
            sDir = UP;
            break;
        case 's':
            sDir = DOWN;
            break;
        case 'x':
            isGameOver = true;
            break;
        }
    }
}

int difficulty(){
    cout << "Choose difficulty:\n1) Easy\n2)Medium\n3)Hard\n";
    int diff;
    int speed;
    cin >> diff;
    switch (diff)
    {
    case 1:
        speed = 150;
        break;
    case 2:
        speed = 100;
        break;
    case 3:
        speed = 30;
        break;    
    default:
        cout << "Command not recognised, going with medium";
        break;
    }
    return speed;
}

int main(){
    string playerName;
    cout << "Enter your name: ";
    cin >> playerName;
    int speed;
    speed = difficulty();
    GameInit();
    while (!isGameOver){
        GameRender(playerName);
        UserInput();
        UpdateGame();
        Sleep(speed);
    }
    return 0;
}



