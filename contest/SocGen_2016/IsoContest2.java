// package com.isograd.exercise;
import java.util.*;
import java.io.*;

public class IsoContest2 {
    public static void solution(String[] lines){
        int s = Integer.parseInt(lines[0]);
        int n = Integer.parseInt(lines[1]);
        int a = 0;
        int b = 0;
        for(int i=2; i<n+2; i++) {
            a += Integer.parseInt(lines[i].split(" ")[0]);
            b += Integer.parseInt(lines[i].split(" ")[1]);
            if (a >= s && b >= s) {
                System.out.println("NO WINNER");
                break;
            } else if (a >= s && b < s){
                System.out.println("A");
                break;
            } else if (b >= s && a < s){
                System.out.println("B");
                break;
            }
        }
    }

    public static void main( String[] args ) throws Exception {
        if (args.length == 0){ /* online submission */
            String content = "";
            Scanner sc = new Scanner(System.in);
            while(sc.hasNextLine())
                content += sc.nextLine() + "\n";
            String[] lines = content.split("\n");
            solution(lines);
        } else { /* local test*/
            System.out.println("Test Result");
            System.out.println("-----------------------------");
            String data_dir = "2"; //mod
            File folder = new File(data_dir);
            for (File file : folder.listFiles()) {
                if (file.getName().startsWith("input")) {
                    System.out.println(file.getName() + " : expected output");
                    File output = new File(data_dir +  File.separator + file.getName().replace("input","output"));
                    Scanner sc = new Scanner(output);
                    while(sc.hasNextLine())
                        System.out.println(sc.nextLine());
                    String content = "";
                    sc = new Scanner(file);
                    while(sc.hasNextLine())
                        content += sc.nextLine() + "\n";
                    System.out.println();
                    String[] lines = content.split("\n");
                    System.out.println(file.getName() + " : my output");
                    solution(lines);
                    System.out.println("-----------------------------");
                }
            }
        }
    }
}
