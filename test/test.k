const LAST = 30;
fun fib(n:int):int {
    if(n > 1){
        return fib(n-1) + fib(n-2);
    }
    else {
        return 1;
    }
}

fun main():int {
    var n:int = 0;
    while(n < LAST){
        print(fib(n));
        n = n + 1;
    }
    return 0;
}
