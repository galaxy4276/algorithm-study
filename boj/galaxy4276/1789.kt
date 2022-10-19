import java.io.*;
import java.util.*;
import java.lang.Integer.*;

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val N: Long = br.readLine().toLong()
    var sum = 0L
    var inc = 1
    while (true) {
        sum += inc
        if (sum > N) break
        inc++
    }
    println(inc - 1)
}
