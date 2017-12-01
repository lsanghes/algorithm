// package com.isograd.exercise;
import java.util.*;
import java.io.*;

public class IsoContest3 {
    public static void solution(String[] lines){
        String res = "";
        for (String line: lines)
            res += (char) Integer.parseInt(line, 2);
        System.out.println(res);
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
            String data_dir = "3"; //mod
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

