#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream inStream;
	inStream.open("passphrase.txt");

	ofstream outStream;
	outStream.open("NewPassphrase.txt", ios::app);

	string passPhrase;
	int i = 1;
	int userGuess;
	
	if (!inStream.fail())
	{
		while (inStream >> passPhrase)
		{
			cout << "The " << i << ". passphrase is: " << passPhrase << endl;
			i++;
			cout << "What is your answer? \n";
			cin >> userGuess;
			if (userGuess == passPhrase.length())
			{
				cout << "Congratulations\n";
			}
			else
			{
				cout << "Sorry try again\n";
				outStream << passPhrase << endl;
			}
			
		}
	}
	inStream.close();
	outStream.close();
}