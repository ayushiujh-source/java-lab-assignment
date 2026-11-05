// Name: Ayushi | Roll No.: BCS2025414 | Assignment: 12 | Question: 3
public class Main{public static void main(String[]x){int[] a={6,5,4,3,2,1};int shifts=0;for(int i=1;i<a.length;i++){int key=a[i],j=i-1;while(j>=0&&a[j]>key){a[j+1]=a[j];j--;shifts++;}a[j+1]=key;}System.out.println("Shifts: "+shifts);}}
