#include <bits/stdc++.h>
using namespace std;

bool check(int x) {
    for (int i = 2; i <= (int)sqrt((double)x); i++)
        if (x % i == 0) return false;
    return true;
}

vector<int> prime;
vector<vector<int>> d;
vector<int> subtree_sz, centroids, level;
long long ans = 0;
vector<int> collected, dist;
set<int> used;
int n;

void sub(int par, int x) {
    subtree_sz[x] = 1;
    for (int nx : d[x]) {
        if (nx == par || centroids[nx]) continue;
        sub(x, nx);
        subtree_sz[x] += subtree_sz[nx];
    }
}

int centroid_find(int par, int x, int size) {
    for (int nx : d[x]) {
        if (nx == par || centroids[nx]) continue;
        if (subtree_sz[nx] > size / 2)
            return centroid_find(x, nx, size);
    }
    return x;
}

int collect(int cur, int par, int depth) {
    used.insert(depth);
    collected[depth]++;
    int m = depth;
    for (int nx : d[cur]) {
        if (nx == par || centroids[nx]) continue;
        m = max(m, collect(nx, cur, depth + 1));
    }
    return m;
}

void solve(int cent) {
    int m = 0;
    for (int nx : d[cent]) {
        if (centroids[nx]) continue;
        m = max(m, collect(nx, cent, 1));
        for (int i : used) {
            for (int j : prime) {
                if (j - i > m) break;
                if (j >= i)
                    ans += (long long)dist[j - i] * collected[i];
            }
        }
        for (int i : used) {
            dist[i] += collected[i];
            collected[i] = 0;
        }
        used.clear();
    }
    for (int i = 1; i <= m; i++)
        dist[i] = 0;
}

void dnc(int cur) {
    sub(-1, cur);
    int cent = centroid_find(-1, cur, subtree_sz[cur]);
    centroids[cent] = 1;
    solve(cent);
    for (int nx : d[cent]) {
        if (!centroids[nx]) dnc(nx);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    for (int i = 2; i <= 100000; i++)
        if (check(i)) prime.push_back(i);

    cin >> n;
    d.resize(n + 1);
    subtree_sz.assign(n + 1, 1);
    centroids.assign(n + 1, 0);
    level.assign(n + 1, 0);
    collected.assign(100001, 0);
    dist.assign(100001, 0);
    dist[0] = 1;

    for (int i = 0; i < n - 1; i++) {
        int a, b;
        cin >> a >> b;
        d[a].push_back(b);
        d[b].push_back(a);
    }

    dnc(1);

    cout << fixed << setprecision(9)
         << (double)ans * 2.0 / ((long long)n * (n - 1)) << "\n";
    return 0;
}