from pathlib import Path
import subprocess,tempfile
from PIL import Image,ImageDraw,ImageFont

A = [
("Decisions and Loops with Numbers","Use if, else if and loops to make decisions and repeat steps with whole numbers.",[
("Even or odd",'public class Main{public static void main(String[]x){int n=27;if(n%2==0)System.out.println(n+" is even");else System.out.println(n+" is odd");}}',"Use the remainder operator and if-else to test whether n is even or odd."),
("Grade using else-if",'public class Main{public static void main(String[]x){int marks=83;if(marks>=90)System.out.println("Grade: A");else if(marks>=75)System.out.println("Grade: B");else System.out.println("Grade: C");}}',"Check the mark ranges from highest to lowest using an else-if ladder."),
("Leap year check",'public class Main{public static void main(String[]x){int year=2024;if((year%4==0&&year%100!=0)||year%400==0)System.out.println("Leap year");else System.out.println("Not a leap year");}}',"Apply the divisibility-by-four, century and divisibility-by-400 leap-year rule."),
("Factorial of 5",'public class Main{public static void main(String[]x){int f=1;for(int i=1;i<=5;i++)f*=i;System.out.println("Factorial of 5 is "+f);}}',"Multiply the integers from one through five using a for loop.")
]),
("Star and Number Patterns","Use a loop inside another loop to print stars and numbers in rows.",[
("4 by 4 star square",'public class Main{public static void main(String[]x){for(int i=1;i<=4;i++){for(int j=1;j<=4;j++)System.out.print("*");System.out.println();}}}',"Use an outer loop for rows and an inner loop for four stars per row."),
("Right triangle of stars",'public class Main{public static void main(String[]x){for(int i=1;i<=4;i++){for(int j=1;j<=i;j++)System.out.print("*");System.out.println();}}}',"Print i stars on row i using nested loops."),
("Number triangle",'public class Main{public static void main(String[]x){for(int i=1;i<=4;i++){for(int j=1;j<=i;j++)System.out.print(j+" ");System.out.println();}}}',"Print numbers from one through the current row number."),
("Upside-down star triangle",'public class Main{public static void main(String[]x){for(int i=4;i>=1;i--){for(int j=1;j<=i;j++)System.out.print("*");System.out.println();}}}',"Start with four stars and decrease the row length by one each time.")
]),
("Writing Functions","Write functions with parameters and return values, and call them from main.",[
("5C2 using fact and nCr",'public class Main{static int fact(int n){int f=1;for(int i=1;i<=n;i++)f*=i;return f;}static int nCr(int n,int r){return fact(n)/(fact(r)*fact(n-r));}public static void main(String[]x){System.out.println("5C2 = "+nCr(5,2));}}',"Implement factorial, then calculate nCr as n! divided by r!(n-r)!."),
("5P2 using fact and nPr",'public class Main{static int fact(int n){int f=1;for(int i=1;i<=n;i++)f*=i;return f;}static int nPr(int n,int r){return fact(n)/fact(n-r);}public static void main(String[]x){System.out.println("5P2 = "+nPr(5,2));}}',"Implement factorial, then calculate nPr as n! divided by (n-r)!."),
("maxOf for 14 and 9",'public class Main{static int maxOf(int a,int b){return a>b?a:b;}public static void main(String[]x){System.out.println("Larger: "+maxOf(14,9));}}',"Write maxOf with two integer parameters and return the larger value.")
]),
("Arrays: Traversal and Counting","Create an array, visit every element with a loop, and add up or count the values.",[
("Print array indices and elements",'public class Main{public static void main(String[]x){int[] arr={3,4,5};for(int i=0;i<arr.length;i++)System.out.println("Index "+i+": "+arr[i]);}}',"Traverse arr using a for loop and arr.length."),
("Find sum and largest value",'public class Main{public static void main(String[]x){int[] a={12,45,7,33,21};int sum=0,max=a[0];for(int v:a){sum+=v;if(v>max)max=v;}System.out.println("Sum: "+sum);System.out.println("Largest: "+max);}}',"Add each value to sum and update max when a larger value appears."),
("Count values greater than 10",'public class Main{public static void main(String[]x){int[] a={5,12,2,14,7};int c=0;for(int v:a)if(v>10)c++;System.out.println("Count greater than 10: "+c);}}',"Traverse the array and increment a counter for values greater than ten.")
]),
("Arrays: Reverse and Duplicates","Print an array in reverse order, find the smallest value, and check an array for repeated values.",[
("Print array in reverse",'public class Main{public static void main(String[]x){int[] a={10,20,30,40,50};for(int i=a.length-1;i>=0;i--)System.out.println(a[i]);}}',"Start at the final index and move backwards to zero."),
("Find smallest value and index",'public class Main{public static void main(String[]x){int[] a={2,5,1,8,3,4};int min=a[0],idx=0;for(int i=1;i<a.length;i++)if(a[i]<min){min=a[i];idx=i;}System.out.println("Smallest: "+min+" at index "+idx);}}',"Initialize the minimum with the first value and update its value and index."),
("Find repeated value",'public class Main{public static void main(String[]x){int[] a={4,9,2,9,7};boolean found=false;for(int i=0;i<a.length&&!found;i++)for(int j=i+1;j<a.length;j++)if(a[i]==a[j]){System.out.println("Repeated value: "+a[i]);found=true;break;}if(!found)System.out.println("No repeated value");}}',"Compare each element with later elements using nested loops.")
]),
("Counting Steps and Complexity","Count the steps a program takes, and write its time complexity as a comment.",[
("Count one loop",'public class Main{public static void main(String[]x){int steps=0;// Time complexity: O(n)\nfor(int i=1;i<=10;i++)steps++;System.out.println("Steps: "+steps);}}',"Count each iteration. A single loop has O(n) time complexity."),
("Count nested loops",'public class Main{public static void main(String[]x){int steps=0;// Time complexity: O(n^2)\nfor(int i=1;i<=10;i++)for(int j=1;j<=10;j++)steps++;System.out.println("Steps: "+steps);}}',"Count each execution of the inner loop body. Nested loops have O(n^2) complexity."),
("Count halving steps",'public class Main{public static void main(String[]x){int n=1024,steps=0;// Time complexity: O(log n)\nwhile(n>1){n/=2;steps++;}System.out.println("Halving steps: "+steps);}}',"Repeatedly halve n until it becomes one and count the divisions.")
]),
("Matrices: Transpose and Row Sums","Create two-dimensional arrays, visit them row by row, and build a new matrix from one.",[
("Fill and print 3 by 4 matrix",'public class Main{public static void main(String[]x){int[][] m=new int[3][4];int v=1;for(int i=0;i<3;i++)for(int j=0;j<4;j++)m[i][j]=v++;for(int[] row:m){for(int a:row)System.out.print(a+" ");System.out.println();}}}',"Fill the matrix row by row with nested loops and print each row."),
("Transpose 3 by 3 matrix",'public class Main{public static void main(String[]x){int[][] m={{1,2,3},{4,5,6},{7,8,9}},t=new int[3][3];for(int i=0;i<3;i++)for(int j=0;j<3;j++)t[j][i]=m[i][j];for(int[] row:t){for(int a:row)System.out.print(a+" ");System.out.println();}}}',"Copy each element to the transposed position by swapping row and column indices."),
("Sum each matrix row",'public class Main{public static void main(String[]x){int[][] m={{1,2,3},{4,5,6},{7,8,9}};for(int i=0;i<3;i++){int s=0;for(int j=0;j<3;j++)s+=m[i][j];System.out.println("Row "+(i+1)+" sum: "+s);}}}',"Add the three elements in each row and print its total.")
]),
("Matrices: Rows and Columns","Visit the rows and columns of a matrix with nested loops to print, add and count its values.",[
("Print first and last rows",'public class Main{public static void main(String[]x){int[][] m={{1,2,3},{4,5,6},{7,8,9}};System.out.print("First row: ");for(int v:m[0])System.out.print(v+" ");System.out.println();System.out.print("Last row: ");for(int v:m[2])System.out.print(v+" ");System.out.println();}}',"Print the first and last matrix rows with spaces between values."),
("Sum each column",'public class Main{public static void main(String[]x){int[][] m={{1,2,3},{4,5,6},{7,8,9}};for(int j=0;j<3;j++){int s=0;for(int i=0;i<3;i++)s+=m[i][j];System.out.println("Column "+(j+1)+" sum: "+s);}}}',"Add values column by column using nested loops."),
("Count matrix values greater than 5",'public class Main{public static void main(String[]x){int[][] m={{1,2,3},{4,5,6},{7,8,9}};int c=0;for(int[] row:m)for(int v:row)if(v>5)c++;System.out.println("Values greater than 5: "+c);}}',"Visit every matrix element and count values greater than five.")
]),
("Switch and ArrayList","Choose a branch with a switch statement, and store and change a list of numbers in an ArrayList.",[
("Switch day name",'public class Main{public static void main(String[]x){int day=3;switch(day){case 1:System.out.println("Monday");break;case 2:System.out.println("Tuesday");break;case 3:System.out.println("Wednesday");break;default:System.out.println("Invalid day");}}}',"Use switch cases for days one to three and a default case."),
("Create ArrayList and read size and index 2",'import java.util.ArrayList; public class Main{public static void main(String[]x){ArrayList<Integer> list=new ArrayList<>();list.add(10);list.add(20);list.add(30);list.add(40);System.out.println(list);System.out.println("Size: "+list.size());System.out.println("Item at index 2: "+list.get(2));}}',"Add four integers, then print the list, its size and the item at index two."),
("Update and remove ArrayList items",'import java.util.ArrayList; public class Main{public static void main(String[]x){ArrayList<Integer> list=new ArrayList<>();list.add(10);list.add(20);list.add(30);list.add(40);list.set(1,25);list.remove(3);System.out.println(list);System.out.println("Size: "+list.size());}}',"Use set to update index one and remove to delete index three.")
]),
("Bubble Sort and Selection Sort","Sort small arrays with bubble sort and selection sort, and count the swaps.",[
("Bubble sort array",'import java.util.Arrays; public class Main{public static void main(String[]x){int[] a={5,1,4,2,8};for(int i=0;i<a.length-1;i++)for(int j=0;j<a.length-1-i;j++)if(a[j]>a[j+1]){int t=a[j];a[j]=a[j+1];a[j+1]=t;}System.out.println("Sorted: "+Arrays.toString(a));}}',"Compare adjacent elements and swap out-of-order pairs."),
("Selection sort array",'import java.util.Arrays; public class Main{public static void main(String[]x){int[] a={64,25,12,22,11};for(int i=0;i<a.length-1;i++){int min=i;for(int j=i+1;j<a.length;j++)if(a[j]<a[min])min=j;int t=a[i];a[i]=a[min];a[min]=t;}System.out.println("Sorted: "+Arrays.toString(a));}}',"Find the smallest remaining element and swap it into the current position."),
("Count bubble sort swaps",'public class Main{public static void main(String[]x){int[] a={5,1,4,2,8};int swaps=0;for(int i=0;i<a.length-1;i++)for(int j=0;j<a.length-1-i;j++)if(a[j]>a[j+1]){int t=a[j];a[j]=a[j+1];a[j+1]=t;swaps++;}System.out.println("Swaps: "+swaps);}}',"Increment the swap counter whenever two adjacent values exchange places.")
]),
("Insertion Sort","Sort small arrays with insertion sort and count how many values are shifted.",[
("Insertion sort array 7 3 5 1",'import java.util.Arrays; public class Main{public static void main(String[]x){int[] a={7,3,5,1};for(int i=1;i<a.length;i++){int key=a[i],j=i-1;while(j>=0&&a[j]>key){a[j+1]=a[j];j--;}a[j+1]=key;}System.out.println("Sorted: "+Arrays.toString(a));}}',"Take each element as key, shift larger values right, then insert the key."),
("Insertion sort array 14 3 9 21 6",'import java.util.Arrays; public class Main{public static void main(String[]x){int[] a={14,3,9,21,6};for(int i=1;i<a.length;i++){int key=a[i],j=i-1;while(j>=0&&a[j]>key){a[j+1]=a[j];j--;}a[j+1]=key;}System.out.println("Sorted: "+Arrays.toString(a));}}',"Take each element as key, shift larger values right, then insert the key."),
("Count insertion sort shifts",'public class Main{public static void main(String[]x){int[] a={6,5,4,3,2,1};int shifts=0;for(int i=1;i<a.length;i++){int key=a[i],j=i-1;while(j>=0&&a[j]>key){a[j+1]=a[j];j--;shifts++;}a[j+1]=key;}System.out.println("Shifts: "+shifts);}}',"Count each time an existing value moves one position to the right.")
]),
("Strings: Methods and Palindromes","Use common String methods, reverse a word, check a palindrome and print substrings.",[
("String length position and uppercase",'public class Main{public static void main(String[]x){String s="Programming";System.out.println("Length: "+s.length());System.out.println("Position of g: "+s.indexOf(\'g\'));System.out.println("Upper case: "+s.toUpperCase());}}',"Use length(), indexOf('g') and toUpperCase() on Programming."),
("Reverse Java using charAt",'public class Main{public static void main(String[]x){String s="Java",r="";for(int i=s.length()-1;i>=0;i--)r+=s.charAt(i);System.out.println("Reversed: "+r);}}',"Visit characters from the final index to zero and append each to a new String."),
("Check racecar palindrome",'public class Main{public static void main(String[]x){String s="racecar",r="";for(int i=s.length()-1;i>=0;i--)r+=s.charAt(i);if(s.equals(r))System.out.println(s+" is a palindrome");else System.out.println(s+" is not a palindrome");}}',"Reverse the word and compare it with the original using equals()."),
("Print every substring of abc",'public class Main{public static void main(String[]x){String s="abc";for(int i=0;i<s.length();i++)for(int j=i+1;j<=s.length();j++)System.out.println(s.substring(i,j));}}',"Use nested loops to print each starting letter's substrings from shortest to longest.")
]),
("Characters: Counting and Positions","Use charAt to count vowels and a letter, and print each letter with its position.",[
("Count vowels in programming",'public class Main{public static void main(String[]x){String s="programming";int c=0;for(int i=0;i<s.length();i++)if("aeiou".indexOf(s.charAt(i))>=0)c++;System.out.println("Vowels: "+c);}}',"Use charAt to inspect each character and count a, e, i, o and u."),
("Count g in programming",'public class Main{public static void main(String[]x){String s="programming";int c=0;for(int i=0;i<s.length();i++)if(s.charAt(i)==\'g\')c++;System.out.println("Count of g: "+c);}}',"Use charAt in a loop and increment the counter whenever the character is g."),
("Print character positions in hello",'public class Main{public static void main(String[]x){String s="hello";for(int i=0;i<s.length();i++)System.out.println(i+": "+s.charAt(i));}}',"Loop through the String indices and print each zero-based index and character.")
]),
("StringBuilder Methods","Build and change text with StringBuilder, using append, insert and deleteCharAt.",[
("Append World to Hello",'public class Main{public static void main(String[]x){StringBuilder sb=new StringBuilder("Hello");sb.append(" World");System.out.println(sb);System.out.println("Length: "+sb.length());}}',"Create a StringBuilder with Hello, append World with its leading space, then print text and length."),
("Append numbers and remove final comma",'public class Main{public static void main(String[]x){StringBuilder sb=new StringBuilder();for(int i=1;i<=5;i++)sb.append(i).append(\',\');sb.deleteCharAt(sb.length()-1);System.out.println(sb);}}',"Append numbers one through five with commas, then remove the last comma."),
("Insert Hello before Java",'public class Main{public static void main(String[]x){StringBuilder sb=new StringBuilder("Java");sb.insert(0,"Hello ");System.out.println(sb);}}',"Insert Hello and a space at index zero of a StringBuilder containing Java.")
])
]

def render_output(text,path):
    im=Image.new("RGB",(1100,300),(30,30,30)); d=ImageDraw.Draw(im)
    f=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",22)
    d.text((25,18),"Java Lab - Program Output",font=f,fill=(120,190,255))
    d.line((25,58,1075,58),fill=(90,90,90),width=2)
    y=82
    for line in text.splitlines()[:8]:
        d.text((25,y),line,font=f,fill=(240,240,240)); y+=30
    im.save(path)

for anum,(title,aim,qs) in enumerate(A,start=2):
    folder=Path(f"Assignment{anum}"); folder.mkdir(exist_ok=True)
    parts=[]
    for qnum,(qtitle,code,procedure) in enumerate(qs,start=1):
        qdir=folder/f"Question{qnum}"; qdir.mkdir(exist_ok=True)
        (qdir/"Main.java").write_text(f"// Name: Ayushi | Roll No.: BCS2025414 | Assignment: {anum} | Question: {qnum}\n{code}\n")
        with tempfile.TemporaryDirectory() as td:
            src=Path(td)/"Main.java"; src.write_text(code)
            c=subprocess.run(["javac",str(src)],capture_output=True,text=True)
            if c.returncode: raise RuntimeError(f"A{anum} Q{qnum} compile error: {c.stderr}")
            r=subprocess.run(["java","-cp",td,"Main"],capture_output=True,text=True)
            if r.returncode: raise RuntimeError(f"A{anum} Q{qnum} run error: {r.stderr}")
            output=r.stdout.rstrip("\n")
        render_output(output,qdir/"output.png")
        parts.append((qtitle,procedure,output))
    md=[f"# Assignment {anum}: {title}","","## 1. Experiment Title",title,"","## 2. Aim",aim,"","## 3. Software / Tools Required","- Java Development Kit (JDK)","- IntelliJ IDEA (IDE shown in the supplied Assignment 1 – Question 1 reference screenshot)","- Git and GitHub","","## 4. Theory",aim+" Each question is an independent Java program using the Main class and main method.","","## 5. Algorithm / Procedure"]
    for i,(qt,proc,out) in enumerate(parts,1): md += [f"### Question {i}",f"**{qt}**",f"1. {proc}",""]
    md += ["## 6. Input"]
    for i,(qt,proc,out) in enumerate(parts,1): md += [f"### Question {i}","No runtime input is required. Values are initialized in the program as specified in the lab assignment.",""]
    md += ["## 7. Output"]
    for i,(qt,proc,out) in enumerate(parts,1): md += [f"### Question {i}","~~~text",out,"~~~",""]
    md += ["## 8. Result",f"All {len(parts)} programs compiled and executed successfully; the outputs are shown above.",""]
    (folder/"README.md").write_text("\n".join(md))
print("Compiled and generated",sum(len(x[2]) for x in A),"Java programs.")
