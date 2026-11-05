// Name: Ayushi | Roll No.: BCS2025414 | Assignment: 12 | Question: 2
import java.util.Arrays; public class Main{public static void main(String[]x){int[] a={14,3,9,21,6};for(int i=1;i<a.length;i++){int key=a[i],j=i-1;while(j>=0&&a[j]>key){a[j+1]=a[j];j--;}a[j+1]=key;}System.out.println("Sorted: "+Arrays.toString(a));}}
