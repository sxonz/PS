#include <stdio.h>
#include <math.h>
#include <stdlib.h>

long long back(int d[], int a[], int b[], int aidx, int bidx, int idx, int len) {
    if (idx == len) {
        if (aidx == 0 || bidx == 0)
            return 0;
        long long asum = 0, bsum = 0;
        for (int i = 0; i < aidx; i++) {
            asum = asum * 10 + a[i];
        }
        for (int i = 0; i < bidx; i++) {
            bsum = bsum * 10 + b[i];
        }
        return asum * bsum;
    }
    long long tmp = 0, tmp2 = 0;
    a[aidx] = d[idx];
    tmp = back(d, a, b, aidx + 1, bidx, idx + 1, len);
    b[bidx] = d[idx];
    tmp2 = back(d, a, b, aidx, bidx + 1, idx + 1, len);
    return tmp > tmp2 ? tmp : tmp2;
}

int compare(const void* a, const void* b) {
    return (*(int*)b - *(int*)a);
}

int main() {
    int n;
    scanf("%d", &n);
    for (int test = 0; test < n; test++) {
        char num[20];
        scanf("%s", num);

        int d[18];
        int len = 0;

        for (int i = 0; num[i] != '\0'; i++) {
            int digit = num[i] - '0';
            if (digit == 6)
                digit = 9;
            d[len++] = digit;
        }

        qsort(d, len, sizeof(int), compare);

        int a[18] = { 0 }, b[18] = { 0 };
        printf("%lld\n", back(d, a, b, 0, 0, 0, len));
    }
    return 0;
}