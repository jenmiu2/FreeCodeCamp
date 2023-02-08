function countDown(n){
    if (n < 1) {
        return [];
    }
    else {
        const countArr = countDown(n - 1);
        countArr.unshift(n);
        return countArr;
    }
}