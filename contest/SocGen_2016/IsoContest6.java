// package com.isograd.exercise;
import java.util.*;
import java.io.*;

public class IsoContest6 {
    public static void solution(String[] lines){
        String begin = lines[1];
        String end = lines[2];
        Set<String> dict = new HashSet<String>();
        for (int i = 4; i < lines.length ; i++){
            dict.add(lines[i]);
        }
        List<List<String>> res = findladder(begin, end, dict);
        if (res.isEmpty()){
            System.out.println("IMPOSSIBLE");
        } else {
            List<String> outputs = new ArrayList<>();
            for (List<String> path: res){
                String output = "";
                for (String s : path){
                    output += s + " ";
                }
                outputs.add(output);
            }
            Collections.sort(outputs);
            System.out.println(outputs.get(0));
        }
    }

    public static List<List<String>> findladder(String beginWord, String endWord, Set<String> wordList){
        Map<String, Set<String>> graph = new HashMap<>();
        Set<String> level = new HashSet<String>(Arrays.asList(beginWord));
        while (!level.isEmpty() && !graph.containsKey(endWord)){
            Set<String> next_level = new HashSet<String>();
            for (String word : level){
                Set<String> new_words = mask_one_char(word);
                for (String new_word : new_words){
                    if (wordList.contains(new_word) && !graph.containsKey(new_word) && !level.contains(new_word)){
                        if (!graph.containsKey(word)){
                            graph.put(word, new HashSet<String>());
                        }
                        graph.get(word).add(new_word);
                        next_level.add(new_word);
                    }
                }
            }
            level = next_level;
        }

        List<List<String>> res = new ArrayList<>();
        List<String> path = new ArrayList<>(Arrays.asList(beginWord));
        dfs(graph, beginWord, endWord, path, res);
        return res;
    }

    public static void dfs(Map<String, Set<String>> graph, String start, String end, List<String> path, List<List<String>> res){
        if (start.equals(end))
            res.add(path);
        Set<String> neighbours = graph.getOrDefault(start, new HashSet<>());
        neighbours.removeAll(new HashSet<>(path));
        for (String v : neighbours){
            List<String> next_path = new ArrayList<>(path);
            next_path.add(v);
            dfs(graph, v, end, next_path, res);
        }
    }

    public static Set<String> mask_one_char(String word){
        Set<String> new_words = new HashSet<String>();
        String letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        for (int i = 0; i < word.length() ; i++ ){
            for(int j = 0; j < letters.length() ; j++) {
                char c = letters.charAt(j);
                if (word.charAt(i) != c){
                    String new_word = word.substring(0, i) + c + word.substring(i+1);
                    new_words.add(new_word);
                }
            }
        }
        return new_words;
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
            String data_dir = "6"; //mod
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
