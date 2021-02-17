const compress = (chars) => {
  let lastIndex = 0;
  let index = 0;

  while (index < chars.length) {
    let count = 0;
    while (chars[index] === chars[index + count]) {
      count++;
    }
    if (count > 1) {
      chars[lastIndex] = chars[index];
      if (count > 10) {
        chars[lastIndex + 1] = String(1);
        chars[lastIndex + 2] = String(count - 10);
        lastIndex += 3;
      } else {
        chars[lastIndex + 1] = String(count);
        lastIndex += 2;
      }
    } else {
      lastIndex++;
    }
    index = index + count;
  }
  return lastIndex
};
