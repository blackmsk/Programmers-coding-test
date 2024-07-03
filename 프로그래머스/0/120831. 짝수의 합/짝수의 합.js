function solution(n) {
    var answer = 0;
    for (let a=0; a<=n; a=a+2){
        answer += a;
    }
    return answer;
}