#include <iostream>
#include <string>

using namespace std;

string encryptROT13(string message) {
    string encMessage = "";
    // character == c
    for (char c : message) {
        if (isalpha(c)) {
            char base = islower(c) ? 'a' : 'A';
            c = ((c - base + 13) % 26) + base;
        }
        encMessage += c;
    }

    return encMessage;
}

string decryptROT13(string message) {
    return encryptROT13(message);
    // ROT13 là phép mã hóa tự đối xứng, nên để giải mã, chỉ cần mã hóa lại
}

int main() {
    string message;
    cout << "Enter the message to be encrypted: ";
    getline(cin, message);

    string enMessage = encryptROT13(message);
    cout << "Encrypted message: " << encMessage << endl;

    string decMessage = decryptROT13(encMessage);
    cout << "Decrypted message: " << decMessage << endl;

    return 0;
}
