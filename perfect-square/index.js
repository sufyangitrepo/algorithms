function isPerfectSquare(num) {
    let l = 1;
    let r = num;

    while(l <= r) {
        let mid = Math.floor((l+r) / 2);
        const sq = mid * mid;
        if (sq === num) {
            return true;
        } else if(sq < num) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    return false;
}
console.log(isPerfectSquare(12));