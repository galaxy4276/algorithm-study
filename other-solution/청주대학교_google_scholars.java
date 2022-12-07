import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

class FormParser {
  private final String form;
  private final List<Map<String, String>> scholars;
  public FormParser(String form, List<Map<String, String>> scholars) { this.form = form; this.scholars = scholars; }
  public void print() {
    scholars.forEach(scholars -> {
      System.out.println(divergeToken(form, scholars));
    });
  }
  public String divergeToken(String s, Map<String, String> scholar) {
    s = s.replace("NM", scholar.getOrDefault("author", "null"));
    s = s.replace("TT", scholar.getOrDefault("title", "null"));
    s = s.replace("JN", scholar.getOrDefault("journal", "null"));
    s = s.replace("VL", scholar.getOrDefault("volume", "null"));
    s = s.replace("NB", scholar.getOrDefault("number", "null"));
    s = s.replace("PG", scholar.getOrDefault("pages", "null"));
    s = s.replace("YR", scholar.getOrDefault("year", "null"));
    s = s.replace("PB", scholar.getOrDefault("publisher", "null"));
    return s;
  }
}
class ScholarManager {
  private List<Map<String, String>> scholars;
  private final String authorDelimiter;
  public ScholarManager(List<String> refs, String authorForm) {
    this.authorDelimiter = authorForm.substring(authorForm.length() - 1);
    scholars = refs.stream().map(this::createMapInfo).collect(Collectors.toList());
  }
  public List<Map<String, String>> getScholars() { return scholars; }
  private Map<String, String> createMapInfo(String lineStrings) {
    List<String> lines = new ArrayList<>(List.of(lineStrings.split("\n")));
    Map<String, String> map = new HashMap<>();
    for (String line : lines) {
      if (line.length() > 1) {
        String property = parseProperty(line);
        if (property == null) continue;
        map.put(property.trim(), parseBracket(line));
      }
    }
    if (map.get("author") != null) {
      String author = map.get("author");
      String delimiter = authorDelimiter + " ";
      if (author.contains("and"))
        map.put("author", author.replace(" and ", delimiter));
    }

    return map;
  }
  private String parseProperty(String s) {
    int delimiter = s.indexOf("=");
    if (delimiter == -1) return null;
    return s.substring(0, delimiter);
  }
  private String parseBracket(String s) {
    int startIdx = s.indexOf("{");
    int endIdx = s.indexOf("}");
    return s.substring(startIdx+1, endIdx);
  }
}
public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String form = br.readLine();
    int refCount =  Integer.parseInt(br.readLine());
    List<String> refs = new ArrayList<>();
    int endCount = 0;
    StringBuilder sb = new StringBuilder();
    while (true) {
      String line = br.readLine();
      sb.append(line).append("\n");
      if (line.equals("}")) {
        endCount++;
        refs.add(sb.toString());
        sb = new StringBuilder();
      }
      if (endCount >= refCount) break;
    }
    String authorForm = Arrays.stream(form.split(" ")).filter(s -> s.contains("NM")).collect(Collectors.toList()).get(0);
    ScholarManager sm = new ScholarManager(refs, authorForm);
    FormParser formParser = new FormParser(form, sm.getScholars());
    formParser.print();
  }
}
