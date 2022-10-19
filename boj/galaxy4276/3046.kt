import java.io.*;
import java.util.*;
import java.lang.Integer.*;

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val st = StringTokenizer(br.readLine())
    val R1 = parseInt(st.nextToken());
    val S = parseInt(st.nextToken());

    println(S * 2 - R1)
}
