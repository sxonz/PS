#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int distance[100000];
    int oil[100001];
    for (int i = 0; i < n - 1; i++) {
        scanf("%d", &distance[i]);
    }
    for (int i = 0; i < n; i++) {
        scanf("%d", &oil[i]);
    }
    long long min = 1000000001;
    long long ans = 0;
    
    for (int i = 0; i < n - 1; i++) {
        if (oil[i] < min) min = oil[i];
        ans += min * distance[i];
    }
    printf("%lld", ans);
    return 0;
}