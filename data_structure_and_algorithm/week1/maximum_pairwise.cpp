#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
long long maxPairWise(vector<int> x){
    vector<int>::iterator max1 = max_element(x.begin(), x.end());
    long long max_num1 = max1[0];
    size_t index = distance(x.begin(), max1);
    x.erase(x.begin() + index);
    vector<int>::iterator max2 = max_element(x.begin(), x.end());
    long long max_num2 = max2[0];
    long long max = max_num1 * max_num2;
    return max; 
}

int main() {
    int a;
    int b;
    std::cin >> a;
    std::vector<int> input;
    for(int i=0;i<a; ++i){
        std::cin >> b;
        input.push_back(b);
    }
   long long ret = maxPairWise(input);
   cout << ret;
}