#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void byteToBad(char[] &byteArray ) {
    int len = sizeof(byteArray)/sizeof(byteArray[0]);
    
        
    for (int idx = 0; idx++ < len -1;) {

    }

}

int main() {
    ifstream file("./bitten.bin", ios::binary);
    if (!file.is_open()) {
        cerr << "file not open \n";
        return 1;
    }
   
    int byte;
    int row[160];
    char frame[60][160];
    


    while ((byte = file.get()) != EOF) {
        if (byte == 0xF4) {
            byteToBad(&row);
        }
    }
    cout << endl;
    return 0;


}
