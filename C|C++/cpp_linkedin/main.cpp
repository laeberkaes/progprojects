#include <iostream> 
#include <ctime>
#include <cstdlib>
#include <fstream>

using namespace std;

struct Player
{
	string name;
	int winCounter;
};
 
string FindPlayerName(Player names[], bool playerTurn);
int askMove(bool player1Turn, int chipsInPile, Player names[]);
void getUserNames (Player names[]);
void addWin (Player names[], bool player1Turn);

const float MAX_TURN = .5;
const int MAX_CHIPS = 100;

int main()  
{  
    ofstream outStream;
    outStream.open("winner.txt", ios::app);
	int counter = 0;

    bool player1Turn = true;  
    bool gameOver = false;    
    int chipsInPile = 0;  
    int chipsTaken = 0; 

    char userChoice;
    Player playerNames[2];
	Player winner;
  
  //seed the random number generator
    srand(time(0));
  
  //ask the players for their names, then store in an array
    getUserNames(playerNames);
 
  
  //start the game with a random number of chips in the pile
  do
  {
	chipsInPile = (rand() % MAX_CHIPS) + 1;

  	cout << "This round will start with " << chipsInPile << " chips in the pile\n";
    gameOver = false;
    while (!gameOver)
	{
     chipsTaken = askMove(player1Turn, chipsInPile, playerNames);
	 chipsInPile = chipsInPile - chipsTaken;
	 cout << "There are " << chipsInPile << " left in the pile\n";
	 player1Turn = !player1Turn;

	 if (player1Turn)
	 {
		 counter++;
	 }

	 if (chipsInPile == 0)
	 {
	 	gameOver = true;
		
		if (playerNames[0].name == FindPlayerName(playerNames, player1Turn))
		{
			winner = playerNames[0];
		}
		else
		{
			winner = playerNames[1];
		}
		
	    cout << winner.name << ", congratulations you won\n";
		outStream << "The player " << winner.name << " has won after " << counter << " turns.\n";
		addWin(playerNames, player1Turn);
		counter = 0;
	 }
 	}

  	cout << "Do you wish to play again? (Y/N)\n";
    cin >> userChoice;
    userChoice = toupper(userChoice);
   }while ( userChoice == 'Y');
    cout << playerNames[0].name << " won " << playerNames[0].winCounter << " times this round.\n";
    cout << playerNames[1].name << " won " << playerNames[0].winCounter << " times this round.\n";

    outStream.close();
    return 0; 
} 
////////////////////////////////////////////////////////////////////////////////////
void getUserNames (Player names[])
{
	cout << "Player 1, please enter your name: ";
	cin >> names[0].name;
	cout << "\nThanks and good luck!" << endl;
	cout << "Player 2, please enter your name \n (If you wish to play against the computer, enter AI): ";
	cin >> names[1].name;
	cout << "\nThanks and good luck! \n";
}
////////////////////////////////////////////////////////////////

string FindPlayerName(Player names[], bool playerTurn)
{
	if (playerTurn)
		return names[0].name;
	else
		return names[1].name;
}
 ///////////////////////////////////////////////////////////////////////////////////
int askMove(bool player1Turn, int chipsInPile, Player names[])
{
	int chipsTaken;
	int maxPerTurn = MAX_TURN * chipsInPile;
	do
     {	
  		cout << FindPlayerName(names, player1Turn) << " How many chips would  you like?\n";
		
    	cout << "You can take up to ";
		if (( maxPerTurn ) == 0)
		{
			cout << " 1\n";
		}
		else
		{
			cout << maxPerTurn << endl;
		}
		if (FindPlayerName(names, player1Turn) == "AI")
         {
          		if (maxPerTurn == 0)
          		{ 
          			chipsTaken = 1;
		  		}
		  		else
		  		{
		  			chipsTaken = (rand() % maxPerTurn) + 1;
				}
		 }
		else
		{
    	   cin >> chipsTaken;
	    }
     } while ((chipsTaken > maxPerTurn )  && (chipsInPile > 1));
     return chipsTaken;
}

void addWin(Player names[], bool player1Turn)
{
	if (player1Turn)
	{
		names[0].winCounter++;
	}
	else
	{
		names[1].winCounter++;
	}
}

