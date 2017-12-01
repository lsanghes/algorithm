// package com.isograd.exercise;
import java.util.*;
import java.io.*;

public class IsoContest5 {
    public static void solution(String[] lines){
        Map<String, Integer> counter = new HashMap<>();
        Map<String, List<String>> parent = new HashMap<>();
        for (int i = 1; i<lines.length; i++){
            String a = lines[i].split(" ")[0];
            String b = lines[i].split(" ")[1];
            if (!parent.containsKey(a)){
                List<String> list = new ArrayList<String>();
                parent.put(a, list);
            }
            if (!parent.containsKey(b)){
                List<String> list = new ArrayList<String>();
                list.add(a);
                parent.put(b, list);
            } else {
                parent.get(b).add(a);
            }
        }
        for (int i = 1; i<lines.length; i++){
            String a = lines[i].split(" ")[0];
            String b = lines[i].split(" ")[1];
            if (!counter.containsKey(b)){
                counter.put(b, 1);
            }
            if (!counter.containsKey(a)){
                counter.put(a, counter.get(b)+1);
            } else {
                counter.put(a, Math.max(counter.get(a), counter.get(b)+1));
                update_parent(a, counter, parent);
            }
        }
        System.out.println(Collections.max(counter.values()));
    }

    public static void update_parent(String node, Map<String, Integer> counter,  Map<String, List<String>> parent){
        for (String p : parent.get(node)){
            if (counter.containsKey(p)){
                counter.put(p, Math.max(counter.get(p), counter.get(node)+1));
            } else {
                counter.put(p, counter.get(node)+1);
            }
            update_parent(p, counter, parent);
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
            String data_dir = "5"; //mod
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
