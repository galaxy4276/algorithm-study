import java.io.*;
import java.util.*;
import java.lang.Integer.*;

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val st = StringTokenizer(br.readLine())
    var H = parseInt(st.nextToken())
    var M = parseInt(st.nextToken())
    val CT = parseInt(br.readLine())

    M += CT
    H += M / 60
    M %= 60
    H %= 24

    println("$H $M")
}
