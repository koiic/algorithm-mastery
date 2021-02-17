const longestPalindrome = (str) => {
  let longest = str[0];
  const n = str.length;
  const isPalindrome = (string) => {
    if (string === string.split('').reverse().join('')) {
      return string;
    }
    return '';
  };
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      const substring = str.substring(i, j + 1);
      if (isPalindrome(substring) && substring.length > longest.length) {
        longest = substring;
      }
    }
  }
  return longest;
};
