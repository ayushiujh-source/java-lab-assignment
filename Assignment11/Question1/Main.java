// Name: Ayushi | Roll No.: BCS2025414 | Assignment: 11 | Question: 1
import java.util.Arrays; public class Main{public static void main(String[]x){int[] a={5,1,4,2,8};for(int i=0;i<a.length-1;i++)for(int j=0;j<a.length-1-i;j++)if(a[j]>a[j+1]){int t=a[j];a[j]=a[j+1];a[j+1]=t;}System.out.println("Sorted: "+Arrays.toString(a));}}
