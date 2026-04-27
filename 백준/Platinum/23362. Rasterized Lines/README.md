# [Platinum I] Rasterized Lines - 23362 

[문제 링크](https://www.acmicpc.net/problem/23362) 

### 성능 요약

메모리: 116688 KB, 시간: 200 ms

### 분류

수학, 정수론, 소수 판정, 소인수분해, 오일러 피 함수, 폴라드 로, 밀러–라빈 소수 판별법

### 제출 일자

2026년 04월 27일 23:39:51

### 문제 설명

<p>Tomas is a computer graphics student. He has a homework which is very easy for him. He has to make a program that draws a line from point (0, 0) to (a, b), where integers <b>a, b (a>0, b> 0)</b> are the input of the program.</p>

<p>He uses the following algorithm. He divides the plane into squares 1x1 – these squares are pixels. When the line from (0, 0) to (a, b) intersects a square <b>in more than one point</b>, the square (pixel) will be black. Otherwise it will be white. Look at the example:</p>

<p style="text-align: center;"><img alt="" src=""></p>

<p>Tomas is a computer graphics student. He has a homework which is very easy for him. He has to make a program that draws a line from point (0, 0) to (a, b), where integers <b>a, b (a>0, b> 0)</b> are the input of the program.</p>

<p>He uses the following algorithm. He divides the plane into squares 1x1 – these squares are pixels. When the line from (0, 0) to (a, b) intersects a square <b>in more than one point</b>, the square (pixel) will be black. Otherwise it will be white. Look at the example:</p>

### 입력 

 <p>The first line of the input file contains an integer <b>T</b> specifying the number of test cases. Each test case is preceded by a blank line.</p>

<p>Each test case looks as follows: The one and only line contains a positive integer <b>N</b>. You can assume that number <b>N</b> has at most 47 divisors.</p>

### 출력 

 <p>For each test case output one line with one integer – the number of lines that use exactly <b>N</b> black pixels.</p>

