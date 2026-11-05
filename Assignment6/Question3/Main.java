// Name: Ayushi | Roll No.: BCS2025414 | Assignment: 6 | Question: 3
public class Main{public static void main(String[]x){int[] a={4,9,2,9,7};boolean found=false;for(int i=0;i<a.length&&!found;i++)for(int j=i+1;j<a.length;j++)if(a[i]==a[j]){System.out.println("Repeated value: "+a[i]);found=true;break;}if(!found)System.out.println("No repeated value");}}
