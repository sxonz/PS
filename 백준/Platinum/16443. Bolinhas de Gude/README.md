# [Platinum I] Bolinhas de Gude - 16443 

[문제 링크](https://www.acmicpc.net/problem/16443) 

### 성능 요약

메모리: 49244 KB, 시간: 728 ms

### 분류

게임 이론, 스프라그–그런디 정리

### 제출 일자

2025년 12월 11일 20:00:08

### 문제 설명

<p>Usar bolinhas de gude como moeda não deu muito certo em Cubicônia. Na tentativa de se redimir com seus amigos, depois de roubar suas bolinhas de gude, o imperador decidiu convidar todos para uma noite de jogos em seu palácio.</p>

<p>Naturalmente, os jogos utilizam bolinhas de gude, afinal agora o imperador precisa encontrar alguma utilidade para tantas bolinhas. N bolinhas de gude são espalhadas em um grande tabuleiro cujas linhas são numeradas de 0 a L e as colunas numeradas de 0 a C. Os jogadores alternam turnos e em cada turno o jogador da vez deve escolher uma das bolinhas de gude e movˆe-la. O primeiro jogador que mover uma bolinha para a posição (0, 0) é o vencedor. Para que o jogo seja interessante, os movimentos são limitados; do contrário, o primeiro jogador sempre moveria a bolinha para a posição (0, 0) e venceria. Um movimento consiste em escolher um inteiro u maior que 0 e uma bolinha, cuja localização denotaremos por (l, c), e movˆe-la para uma das seguintes posiç˜oes, desde que a mesma não saia do tabuleiro:</p>

<ul>
	<li>(l − u, c);</li>
	<li>(l, c − u); ou</li>
	<li>(l − u, c − u).</li>
</ul>

<p>Note que mais de uma bolinha de gude pode ocupar a mesma posição no tabuleiro.</p>

<p>Como o imperador não gosta de perder vocˆe deve ajudá-lo a determinar em quais partidas ele deve participar. Como é de se esperar, sempre que joga o imperador fica com o primeiro turno. Assumindo que todos jogam de forma ótima, seu programa deve analisar a distribuição inicial das bolinhas de gude no tabuleiro e informar se é possível ou não que o imperador vença caso ele jogue.</p>

### 입력 

 <p>A primeira linha contém um inteiro N (1 ≤ N ≤ 1000). Cada uma das N linhas seguintes contém dois inteiros l<sub>i</sub> e c<sub>i</sub> indicando em qual linha e coluna a i-ésima bolinha de gude se encontra no tabuleiro (1 ≤ l<sub>i</sub>, ci ≤ 100).</p>

### 출력 

 <p>Seu programa deve produzir uma única linha contendo o caractere Y caso seja possível para o imperador ganhar o jogo ou N caso contrário.</p>

