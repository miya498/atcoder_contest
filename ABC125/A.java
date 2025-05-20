import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long A = sc.nextLong();
        long B = sc.nextLong();
        long T = sc.nextLong();
        sc.close();

        // 起動後 T+0.5 秒までに何回の生産が行われるか
        // 生産は A, 2A, 3A, ... の時刻に行われる
        // k * A <= T + 0.5 となる最大の整数 k を求める
        // → k <= (T + 0.5) / A
        // 整数演算で floor((T + 0.5) / A) を求めるには、
        // (2T + 1) / (2A) の整数除算が使える
        long k = (2 * T + 1) / (2 * A);

        // 合計生産枚数
        long result = k * B;
        System.out.println(result);
    }
}
