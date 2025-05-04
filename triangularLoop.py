def triangular_loop(nth):    # Get the nth triangular number using a loop
    total = 0                # Keep a total of all the columns
    for n in range(nth, 0, -1): # Start at nth and go back to 1
        total += n           # Return the total of all the columns
    return total

def triangular(nth):         # Get the nth triangular number recursively
    if nth < 1: return 0     # For anything less than 1, it's 0
    return (nth +            # Otherwise add this column to the preceding
            triangular(nth - 1))    # triangular number

def show_triangular(nth):    # Print the recursive execution steps of
    print('Computing triangular number #', nth)    # computing the nth
    if nth < 1:              # triangular number. Base case
        print('Base case. Returning 0')    # Print the return information
        return 0
    value = nth + show_triangular(nth - 1) # Non-base case, get value
    print('Returning', value, 'for #', nth)    # Print the return information
    return value

def factorial(n):       # Get factorial of n
    if n < 1: return 1  # It's 1 for anything < 1
    return (n *         # Otherwise, multiply n
            factorial(n-1)) # by preceding factorial

def anagrams(word):             # Return a list of anagrams for word
    if len(word) <= 1:          # Empty words and single letters
        return[word]            # have a single anagram, themselves
    result = []                 # Start with an empty list
    for part in anagrams(word[1:]):     # Loop over smaller anagrams
        for i in range(len(part)+1):    # For each index in smaller word
            result.append(      # Add a new anagram with
                part[:i] +      # the smaller word up to the index
                word[0] +       # plus the 1st character of this word
                part[i:])       # plus the rest of the smaller word
    return result               # Return the list of bigger anagrams

print(triangular(5))
show_triangular(5)
print(factorial(4))

print(anagrams(''))
print(anagrams('c'))
print(anagrams('cat'))

print(anagrams('play'))