class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_moves = 0  # Counter for Alice's moves
        bob_moves = 0    # Counter for Bob's moves

        # Iterate through the string to find valid moves for Alice and Bob
        for i in range(1, len(colors) - 1):
            if colors[i - 1:i + 2] == "AAA":
                alice_moves += 1
            elif colors[i - 1:i + 2] == "BBB":
                bob_moves += 1

        # If Alice can make more moves than Bob, she wins; otherwise, Bob wins
        return alice_moves > bob_moves