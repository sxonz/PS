#include <bits/stdc++.h>
using namespace std;

int bit[2000001];
int sz;

void update(int x) {
    for (;x <= sz;x += x & -x) {
        bit[x]++;
    }
}

int query(int x) {
    int ret = 0;
    for (;x;x -= x & -x) {
        ret += bit[x];
    }
    return ret;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    
    vector<int> a(n);
    for (int i = 0;i < n;i++) {
        cin >> a[i];
    }

    vector<int> v = a;
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());
    
    for (int i = 0; i < n; i++) {
        a[i] = lower_bound(v.begin(), v.end(), a[i]) - v.begin() + 1;
    }
    
    sz = v.size();
    
    for (int i = 0;i < n;i++) {
        update(a[i]);
        cout << i + 1 - query(a[i] - 1) << '\n';
    }
    
    return 0;
}