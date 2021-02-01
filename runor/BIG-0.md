### Questions from Cracking The Coding Interview. Page 54

###### VI.1 The following code computes the product of a and b. What is its runtime?
```
int product(int a, int b) {
  int sum = 0;
  for (int i= 0; i < b; i++) {
    sum += a;
  }
  return sum;
}
```



_Answer: O(b) + O(1) = O(b)_

###### VI.2 The following code computes a b. What is its runtime?
```
int power(int a, int b) {
  if (b < 0) {
    return 0;
  } else if (b == 0) {
    return 1;
  } else {
    return a * power(a, b - 1);
  }
}
```
5, 6
5 * power(5, 5)
5 * power(5, 4)
5 * power(5, 3)
5 * power(5, 2)
5 * power(5, 1)
5 * power(5, 0)

_Answer: O(b)_


###### VI.3 The following code computes a % b. What is its runtime?
```
int mod(int a, int b) {
  if (b <= 0) { 
    return -1;
  }
  int div = a / b;
  return a - div * b;
}
```

_Answer: _
5, 6
5/6 = 0.xxx
5 - 0.xxx * 6
_Answer: O(1)_


###### VI.4 The following code performs integer division. What is its runtime (assume a and b are both positive)?
```
int div(int a, int b) { 
  int count = 0;
  int sum = b·,
  while (sum <= a) {
    sum += b; 
    count++;
  }
  return count; 
}
```

a = 15, b = 5
sum = 5

sum = 5 + 5 = 10
count = 1

sum = 10 + 5 = 15
count = 2

sum = 15 + 5 = 20
count = 3

_Answer: O(a/b)_

###### VI.5 The following code computes the [integer] square root of a number. If the number is not a perfect square (there is no integer square root), then it returns -1. It does this by successive guessing. If n is 100, it first guesses SO. Too high? Try something lower - halfway between 1 and 5O. What is its runtime?
```
int sqrt(int n) {
  return sqrt_helper(n, 1, n);
}

int sqrt_helper(int n, int min, int max) {
  if (max < min) return -1; // no square root
  int guess = (min + max) I 2·,
  if (guess *guess == n) { // found it!
    return guess;
  } else if (guess * guess < n) { // too low
    return sqrt_helper(n, guess max); // try higher
  } else { // too high
    return sqrt_helper(n, min, guess - l); // try lower 
  }
}
```

_Answer: O(log N)_

###### VI.6 The following code computes the [integer] square root of a number. If the number is not a perfect square (there is no integer square root), then it returns -1. It does this by trying increasingly large numbers until it finds the right value (or is too high). What is its runtime?
```
int sqrt(int n) {
  for (int guess = 1; guess * guess <= n; guess++) { 
    if (guess * guess == n) {
      return guess;
    }
  } 
  return -1;
}
```

36
1 * 1
2 * 2
3 * 3
4 * 4
5 * 5
6 * 6 = 36

_Answer: O( sqr(n) )_

###### VI.7 If a binary search tree is not balanced, how long might it take (worst case) to find an element in it?

_Answer: O(n)_

###### VI.8 You are looking for a specific value in a binary tree, but the tree is not a binary search tree.
What is the time complexity of this?

```
      10
    8     11
  6   9  10  13
```
_Answer: O(n)_

###### VI.9 The appendToNew method appends a value to an array by creating a new, longer array and returning this longer array. You've used the appendToNew method to create a copyArray function that repeatedly calls appendToNew. How long does copying an array take?
```
int[] copyArray(int[] array) {
  int[] copy = new int[0];
  for (int value : array) {
    copy= appendToNew(copy, value); 
  }
  return copy;
}

int[] appendToNew(int[] array, int value) {
  // copy all elements over to new array 
  int[] bigger = new int[array.length + 1]; 
  for (int i= 0; i < array.length; i++) {
    bigger[i] = array[i];
  }
  // add new element 
  bigger[bigger.length - 1] 
  return bigger;
}
```

_Answer: O(n^2)_

###### VI.10 The following code sums the digits in a number. What is its big O time?
```
int sumDigits(int n) {
  int sum = 0;
  while (n > 0) {
    sum += n % 10;
    n /= 10;
  } 
  return sum;
}
```
1000
loop
0 + (15 % 10) = 0 + 5 = 5
n = 15 / 10 = 1

---
sum = 5 + (1 % 10) = 5 + 1 = 6
n = 1 / 10 = 0
return sum = 6;

20 = 2
15 = 6
11 = 2


_Answer: O(n/10) || O(log N) _

###### VI.11 The following code prints all strings of length k where the characters are in sorted order. It does this by generating all strings of length k and then checking if each is sorted. What is its runtime?
```
int numChars = 26;
void printSortedStrings(int remaining) {
  printSortedStrings(remaining, "");
}
void printSortedStrings(int remaining, String prefix) {
  if (remaining== 0) {
    if (isinOrder(prefix)) {
      System.out.println(prefix);
    }
  } else {
    for (int i= 0; i < numchars; i++) {
      char c = ithletter(i);
      printSortedStrings(remaining - 1, prefix + c); }
    }
  }

boolean isinOrder(String s) {
  for (int i= 1; i < s.length(); i++) {
    int prev ithLetter(s.charAt(i - 1));
    int curr = ithLetter(s.charAt(i));
    if (prev > curr) {
      return false;
    } 
  }
  return true;
}

char ithLetter(int i) {
  return (char) (((int) 'a') + i); 
}
```

_Answer: 0(kck)_ **Needs review**

###### VI.12 The following code computes the intersection (the number of elements in common) of two arrays. It assumes that neither array has duplicates. It computes the intersection by sorting one array (array b) and then iterating through array a checking (via binary search) if each value is in b. What is its runtime?
```
int intersection(int[] a, int[] b) {
  mergesort(b);
  int intersect = 0;
  for (int x : a) {
    if (binarySearch(b, x) >= 0) {
    intersect++;
    }
  }
  return intersect;
}
```

_Answer: O(b * log b) + O(a * logb) = 0(b log b + a log b)_