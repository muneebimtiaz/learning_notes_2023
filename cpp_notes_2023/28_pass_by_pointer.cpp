#include <iostream>
using namespace std;
// n pass by pointer, you use pointers to the original variables. Any changes made to the parameters through pointers directly affect the original variables.
void profitCalc(float *s,float *p);
void lossCalc(float *s,float *p);
int main(){
		float sold,purchased;
		cout<<"how much the product cost:";
		cin>>purchased;
		cout<<"At what price you sold the product:";
		cin>>sold;
		if(sold>purchased){
			profitCalc(&sold,&purchased);
			
		}else if(sold<purchased){
			lossCalc(&sold,&purchased);
		}else{
			cout<<"no profit";
		}
	return 0;
}
void profitCalc(float *s,float *p){
	float profit;
	profit=*s-*p;
	cout<<"profit:"<<profit;
}
void lossCalc(float *s,float *p){
	float loss;
	loss=*p-*s;
	cout<<"loss:"<<loss;
}