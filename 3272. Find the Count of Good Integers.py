# You are given two positive integers n and k.

# An integer x is called k-palindromic if:

# x is a palindrome.
# x is divisible by k.
# An integer is called good if its digits can be rearranged to form a k-palindromic integer. For example, for k = 2, 2020 can be rearranged to form the k-palindromic integer 2002, whereas 1010 cannot be rearranged to form a k-palindromic integer.

# Return the count of good integers containing n digits.

# Note that any integer must not have leading zeros, neither before nor after rearrangement. For example, 1010 cannot be rearranged to form 101.
def countGoodIntegers(self, n: int, k: int) -> int:
        from collections import Counter
        from math import factorial
        from itertools import product
        valid_digit_frequencies = set()

        def frequency_to_tuple(freq_dict):
            return tuple(freq_dict.get(str(digit), 0) for digit in range(10))

        def construct_palindrome(left_half, middle_digit=""):
            return "".join(left_half) + middle_digit + "".join(reversed(left_half))

        if n == 1:
            for single_digit in range(1, 10):
                if single_digit % k == 0:
                    valid_digit_frequencies.add(frequency_to_tuple(Counter(str(single_digit))))
        else:
            half_length = n // 2
            all_digits = '0123456789'

            left_half_combinations = product(all_digits, repeat=half_length)

            if n % 2 == 0:
                for left_half in left_half_combinations:
                    if left_half[0] == '0':
                        continue  
                    palindrome_str = construct_palindrome(left_half)
                    palindrome_value = int(palindrome_str)
                    if palindrome_value % k == 0:
                        valid_digit_frequencies.add(frequency_to_tuple(Counter(palindrome_str)))
            else:

                for left_half in left_half_combinations:
                    if left_half[0] == '0':
                        continue 
                    for middle_digit in all_digits:
                        palindrome_str = construct_palindrome(left_half, middle_digit)
                        palindrome_value = int(palindrome_str)
                        if palindrome_value % k == 0:
                            valid_digit_frequencies.add(frequency_to_tuple(Counter(palindrome_str)))


        res = 0
        for freq_tuple in valid_digit_frequencies:
            digit_counts = list(freq_tuple)


            total_permutations = factorial(n)
            for count in digit_counts:
                total_permutations //= factorial(count)

            invalid_permutations = 0
            if digit_counts[0] > 0:
                remaining_counts = digit_counts.copy()
                remaining_counts[0] -= 1
                invalid_permutations = factorial(n - 1)
                for count in remaining_counts:
                    invalid_permutations //= factorial(count)

            valid_permutations = total_permutations - invalid_permutations
            res += valid_permutations

        return res