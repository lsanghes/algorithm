// package com.isograd.exercise;
import java.util.*;
import java.io.*;

public class IsoContest7 {
    public static void solution(String[] lines){
        String depart_city = lines[1];
        Map<String, Set<String>> flight_graph = new HashMap<>();
        Map<String, Integer> flight_cost = new HashMap<>();
        for (int i = 2; i < lines.length ; i++){
            String from_city = lines[i].split(" ")[0];
            String to_city = lines[i].split(" ")[1];
            int cost = Integer.parseInt(lines[i].split(" ")[2]);

            if (!flight_graph.containsKey(from_city))
                flight_graph.put(from_city, new HashSet<>());
            flight_graph.get(from_city).add(to_city);

            String key = from_city +  ">" + to_city;
            flight_cost.put(key, cost);
        }

        String[] final_city = {depart_city};
        int[] final_cost = {Integer.MAX_VALUE};
        List<String> path = new ArrayList<>(Arrays.asList(depart_city));
        dfs(flight_graph, flight_cost, depart_city, depart_city, 0, path, final_city, final_cost);
        System.out.println(final_city[0] + " " + final_cost[0]);
    }

    public static void dfs(Map<String, Set<String>> graph, Map<String, Integer> flight_cost, String depart_city, String cur_city, int cost, List<String> path, String[] final_city, int[] final_cost){
        if (cost < final_cost[0] && !cur_city.equals(depart_city)){
            final_cost[0] = cost;
            final_city[0] = cur_city;
        }
        Set<String> neighbours = graph.getOrDefault(cur_city, new HashSet<>());
        neighbours.removeAll(new HashSet<>(path));
        for (String next_city : neighbours){
            String key = cur_city +  ">" + next_city;
            int next_cost = cost + flight_cost.get(key);
            List<String> next_path = new ArrayList<>(path);
            next_path.add(next_city);
            dfs(graph, flight_cost, depart_city, next_city, next_cost, next_path, final_city, final_cost);
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
            String data_dir = "7"; //mod
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
