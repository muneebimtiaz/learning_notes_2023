// Member Functions Accessed with Pointers
#include <iostream>
using namespace std;
class store{
	int itemId;
	float price;
	public:
		void set_data(int xx,float yy){
			itemId=xx;
			price=yy;
		}
		void print_data(){
			cout<<"Id of Item"<<itemId<<endl;
			cout<<"Price of Item:"<<price<<endl;
		}
};
int main(){
	//pointer to object
	store item1;
	store *ptr;
	ptr=&item1;
//	(*ptr).set_data(14,56.7);
//	(*ptr).print_data();

	ptr->set_data(14,56.7);
	ptr->print_data();
	
    return 0;
}

