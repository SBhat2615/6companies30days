class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cows, bulls = 0, 0
        count_secret = dict()
        count_guess = dict()
        for i in range(10):
            count_secret[str(i)] = secret.count(str(i))
            count_guess[str(i)] = guess.count(str(i))
            
        for i, num in enumerate(secret):
            if secret[i] == guess[i]:
                bulls += 1
                count_secret[num] -= 1
                count_guess[num] -= 1
        
        for keys in count_guess.keys():
            if count_secret[keys] == count_guess[keys]:
                cows += count_secret[keys]
            else:
                if count_secret[keys] > count_guess[keys] and count_guess[keys] != 0:
                    cows += count_guess[keys]
                elif count_secret[keys] < count_guess[keys] and count_guess[keys] != 0:
                    cows += count_secret[keys]
        print(count_secret)
        print(count_guess)
        return (str(bulls)+'A'+str(cows)+'B')