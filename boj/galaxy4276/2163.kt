import java.io.*;
import java.util.*;
import java.lang.Integer.*;

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val st = StringTokenizer(br.readLine())
    val N = parseInt(st.nextToken());
    val M = parseInt(st.nextToken());

    println(N * M - 1)
}
