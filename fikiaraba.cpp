#include<iostream>
#include<fstream>

using namespace std;

#define hassasiyet 0.25
#define pin 0
int main(){
	ofstream 	fid;
	int x=99;
	float y=30;
	fid.open("/dev/servoblaster",ios::out);	
	if(!fid){
		printf("blaster dosyası açılamadı\n");
		return 1;
	}
	while(x != 0){
		flush(fid);
		cout<<"arrtır: 1\nazalt: 2\nçıkış: 0\n";
		cin>>x;
		cout<<y<<endl;
		if(x==0){
			return 0;
		}else if(x == 1){
			y = y + hassasiyet;
		}else if(x == 2){
			y = y - hassasiyet;
		}
		fid<<pin<<"="<<y<<"\%\n";		
	}
	return 0;
}

