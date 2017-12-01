// package com.isograd.exercise;
import java.util.*;
import java.io.*;

public class IsoContest4 {
    public static void solution(String[] lines){
        int N = Integer.parseInt(lines[0].split(" ")[0]);
        int K = Integer.parseInt(lines[0].split(" ")[1]);
        double R = Float.parseFloat(lines[0].split(" ")[2]);
        Map<Integer, Integer> map = new HashMap<>();
        for (int i=1; i<lines.length; i++){
            for (int j=i+1; j<lines.length; j++){
                int x1 = Integer.parseInt(lines[i].split(" ")[0]);
                int y1 = Integer.parseInt(lines[i].split(" ")[1]);
                int x2 = Integer.parseInt(lines[j].split(" ")[0]);
                int y2 = Integer.parseInt(lines[j].split(" ")[1]);
                double d = Math.sqrt(Math.pow((x1-x2), 2) + Math.pow((y1-y2), 2));
                if (d <= R){
                    map.put(i, map.getOrDefault(i, 0) + 1);
                    map.put(j, map.getOrDefault(j, 0) + 1);
                }
            }
        }

        List<Integer> list = new ArrayList<Integer>();
        for (Integer k: map.keySet()){
            if (map.get(k) >= K)
                list.add(k);
        }
        Collections.sort(list);

        String res = "";
        for (Integer i: list)
            res += i + " ";

        if (list.size() > 0)
            System.out.println(res);
        else
            System.out.println("No danger");

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
            String data_dir = "4"; //mod
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
