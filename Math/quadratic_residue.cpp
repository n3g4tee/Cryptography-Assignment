#include<bits/stdc++.h>
using namespace std;
int p=29;
int a[3]={14,6,11};
int main()
{
    for(int i=1;i*i<=29*29;i++)
    {
        int  u= i*i;
            cout<<u%p<<" ";
        }
/*
In Quadratic Residues we learnt what it means to
take the square root modulo an integer. We also saw that taking a root
 isn't always possible.

In the previous case when p = 29, even the simplest method of
 calculating the square root was fast enough, but as p gets
 larger, this method becomes wildly unreasonable.
*/

    return 0;
}
