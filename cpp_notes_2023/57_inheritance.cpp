#include <iostream>
#include <string>
using namespace std;
class animal{
	private:
	protected:
	public:
		void walk(){
			cout<<"walking"<<endl;
		}
		void sleep(){
			cout<<"sleeping"<<endl;
		}
		void eat(){
			cout<<"eating"<<endl;
		}
};
class dog:public animal{
	public:
		void talk(){
			cout<<"bark"<<endl;
		}
};
class cat:public animal{
	public:
		void talk(){
			cout<<"meow"<<endl;
		}
};
class bear:public animal{
	public:
		void talk(){
			cout<<"growl"<<endl;
		}
};
int main(){
	dog d;
	cat c;
	bear b;
	
	cout<<"dog is ";
	d.walk();
	cout<<"dog sound ";
	d.talk();

	cout<<"bear is ";
	b.sleep();
	cout<<"bear sound ";
	b.talk();

	cout<<"cat is ";
	c.eat();
	cout<<"cat sound ";
	c.talk();
	return 0;	
}





