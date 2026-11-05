// Name: Ayushi | Roll No.: BCS2025414 | Assignment: 11 | Question: 2
import java.util.Arrays; public class Main{public static void main(String[]x){int[] a={64,25,12,22,11};for(int i=0;i<a.length-1;i++){int min=i;for(int j=i+1;j<a.length;j++)if(a[j]<a[min])min=j;int t=a[i];a[i]=a[min];a[min]=t;}System.out.println("Sorted: "+Arrays.toString(a));}}
