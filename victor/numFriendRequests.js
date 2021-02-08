const numFriendRequests = (ages) => {
  let requestCount = 0;
  for(let i = 0; i < ages.length; i++) {
    for(j = 0; j < ages.length - 1; j++) {
      if(canRequest(ages[j], ages[i])){
        console.log(canRequest(ages[j], ages[i]), ages[i], ages[j])
       requestCount++;
      }
    }
  }
  return requestCount;
}

const canRequest = (a, b) => {
 if(b <= (a*0.5)+7 || (b > a) || (b > 100 && a < 100)){
    return false;
  }
  return true
}
