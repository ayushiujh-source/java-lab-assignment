// Name: Ayushi | Roll No.: BCS2025414 | Assignment: 4 | Question: 1
public class Main{static int fact(int n){int f=1;for(int i=1;i<=n;i++)f*=i;return f;}static int nCr(int n,int r){return fact(n)/(fact(r)*fact(n-r));}public static void main(String[]x){System.out.println("5C2 = "+nCr(5,2));}}
