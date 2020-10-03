#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

const int MAX_CHIPS = 100;
const double MAX_TURN = .5;

int main() {
    bool player1Turn = true;
    bool gameOver = false;
    int chipsInPile = 0;
    int chipsTaken = 0;
    int maxPerTurn = 0;
    string playerNames[2];
    string dec;

    //seed the random number generator
    srand(time(0));

    //ask the players for their names, then store in an array
    cout << "Player 1, please enter your name: ";
    cin >> playerNames[0];
    cout << "\nThanks and good luck!" << endl << "Player 2, please enter your name: ";
    cin >> playerNames[1];
    cout << "\nThanks and good luck! \n";

    //start the game with a random number of chips in the pile
    do {
        chipsInPile = (rand() % MAX_CHIPS) + 1;

        cout << "This round will start with " << chipsInPile << " chips in the pile\n";

        while (!gameOver) {
            maxPerTurn = (MAX_TURN * chipsInPile);
            cout << "You can take up to ";
            if (chipsInPile > 1) {
                cout << maxPerTurn;
            } else {
                cout << "1";
            }
            cout << " Chips!" << endl;

            do {
                if (player1Turn) {
                    cout << playerNames[0];
                } else {
                    cout << playerNames[1];
                }
                cout << " how many Chips do you want to take?\n";
                cin >> chipsTaken;
            } while ((chipsTaken > maxPerTurn) && (chipsInPile > 1));
            cout << "Number taken: " << chipsTaken << endl;
            chipsInPile -= chipsTaken;
            cout << "There are " << chipsInPile << " Chips left.\n";

            if (chipsInPile == 0) {
                gameOver = true;
            } else {
                player1Turn = !player1Turn;
            }
        }

        cout << "Player ";
        if (player1Turn) {
            cout << playerNames[1];
        } else {
            cout << playerNames[0];
        }
        cout << " has won!\n\n";
        cout << "Do you two play again? (yes/no)\n";
        cin >> dec;
        gameOver = false;
    } while (dec == "yes");
    return 0;
}
