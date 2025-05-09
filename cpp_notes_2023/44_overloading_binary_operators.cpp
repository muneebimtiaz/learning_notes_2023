#include <iostream>
using namespace std;
class marks{
	 int ninth;
	 int tenth;
	public:
		marks(): ninth(0),tenth(0){}
		marks(int n,int t): ninth(n),tenth(t){}
		void print(){
			cout<<"ninth:"<<ninth<<endl;
			cout<<"tenth:"<<tenth<<endl;
		}
		void print1(){
			cout<<"total: "<<ninth<<endl;
			cout<<"total: "<<tenth<<endl;
		}
        
		marks operator +(marks m){
			marks temp;
			temp.ninth=m.ninth+m.ninth;
			temp.tenth=m.tenth+m.tenth;
			return temp;
		}
		
};
int main(){
	marks m1(412,413),m2(444,363);
	marks m3;
	m1.print();
	m2.print();
	
	m3=m1+m2;
	
	m3.print1();

	return 0; 
}


