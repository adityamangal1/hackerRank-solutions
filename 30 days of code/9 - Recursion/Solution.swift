let n = Int(readLine()!)!

func factorial(_ n: Int) -> Int {
    if n == 1 {
        return 1
    }
    
    return factorial(n - 1) * n;
}

print(factorial(n))
