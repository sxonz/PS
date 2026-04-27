T = int(input())
results = []

for t in range(T):
    N = int(input())
    deck = [input().strip() for _ in range(N)]
    
    cost = 0
    sorted_deck = []
    
    for card in deck:
        if not sorted_deck or card >= sorted_deck[-1]:
            sorted_deck.append(card)
        else:
            for i in range(len(sorted_deck)):
                if card < sorted_deck[i]:
                    sorted_deck.insert(i, card)
                    cost += 1
                    break
    
    results.append(f"Case #{t + 1}: {cost}")

for result in results:
    print(result)
