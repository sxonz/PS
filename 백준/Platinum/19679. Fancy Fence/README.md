# [Platinum III] Fancy Fence - 19679 

[문제 링크](https://www.acmicpc.net/problem/19679) 

### 성능 요약

메모리: 80540 KB, 시간: 400 ms

### 분류

수학, 자료 구조, 조합론, 스택

### 제출 일자

2026년 3월 24일 11:11:11

### 문제 설명

<p>Everybody knows that Balázs has the fanciest fence in the whole town. It’s built up from <em>N</em> fancy sections. The sections are rectangles standing closely next to each other on the ground. The <em>i</em>th section has integer height <em>h<sub>i</sub></em> and integer width <em>w<sub>i</sub></em>.</p>

<p>We are looking for fancy rectangles on this fancy fence.</p>

<p>A rectangle is fancy if:</p>

<ul>
	<li>its sides are either horizontal or vertical and have integer lengths</li>
	<li>the distance between the rectangle and the ground is integer</li>
	<li>the distance between the rectangle and the left side of the first section is integer</li>
	<li>it’s lying completely on sections</li>
</ul>

<p>What is the number of fancy rectangles?</p>

<p>This number can be very big, so we are interested in it modulo 10<sup>9</sup> + 7.</p>

### 입력 

 <p>The first line contains <em>N</em>, the number of sections.</p>

<p>The second line contains <em>N</em> space-separated integers, the <em>i</em>th number is <em>h<sub>i</sub></em>.</p>

<p>The third line contains <em>N</em> space-separated integers, the <em>i</em>th number is <em>w<sub>i</sub></em>.</p>

### 출력 

 <p>You should print a single integer, the number of fancy rectangles modulo 10<sup>9</sup> + 7. So the output range is 0, 1, 2, . . . , 10<sup>9</sup> + 6.</p>

