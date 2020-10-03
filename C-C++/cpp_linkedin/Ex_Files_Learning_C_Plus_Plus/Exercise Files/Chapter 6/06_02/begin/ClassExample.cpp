#include <iostream> 

using namespace std; 
 
class BankAccount
{
  private: 
	  float balance;

  public:    
    BankAccount();  
	  void Deposit(float);
    void WithDrawl();
    float GetBalance();
};

BankAccount::BankAccount()
{
  balance = 0;
}

void BankAccount::Deposit(float f)
{
  balance += f;
}

float BankAccount::GetBalance()
{
  return balance;
}

int main() 
{
  BankAccount checking;
  BankAccount savings;
  checking.Deposit(100);
  savings.Deposit(50);
	cout << checking.GetBalance() << endl;
  cout << savings.GetBalance() << endl;
}



