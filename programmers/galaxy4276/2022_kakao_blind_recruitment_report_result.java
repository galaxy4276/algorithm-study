import java.util.*;

/**
 * @url https://school.programmers.co.kr/learn/courses/30/lessons/92334
 * @name 신고 결과 받기
 */
class Solution {
  public int[] solution(String[] id_list, String[] report, int k) {
    Map<String, List<String>> map = new HashMap();
    Map<String, Integer> reportMap = new HashMap();

    for (int i = 0; i < report.length; i++) {
      String[] info = report[i].split(" ");
      String reporter = info[0];
      String target = info[1];
      if (!map.containsKey(target)) {
        List<String> reportList = new ArrayList<>();
        reportList.add(reporter);
        map.put(target, reportList);
      } else {
        List<String> reportList = map.get(target);
        if (!reportList.contains(reporter)) {
          reportList.add(reporter);
          map.put(target, reportList);
        }
      }
    }

    int[] answer = new int[id_list.length];
    int answerHead = 0;

    for (int i = 0; i < id_list.length; i++) {
      if (map.containsKey(id_list[i])) {
        List<String> reportList = map.get(id_list[i]);

        if (reportList.size() >= k) {
          for (String reporter : reportList) {
            if (!reportMap.containsKey(reporter)) {
              reportMap.put(reporter, 1);
            } else {
              Integer reportResult = reportMap.get(reporter);
              reportMap.put(reporter, reportResult + 1);
            }
          }
        }
      }
    }

    for (int i = 0; i < id_list.length; i++) {
      if (reportMap.containsKey(id_list[i])) {
        Integer processedCount = reportMap.get(id_list[i]);
        answer[answerHead++] = processedCount;
      } else {
        answer[answerHead++] = 0;
      }
    }

    return answer;
  }

  public int[] refactoredSolution(String[] id_list, String[] report, int k) {
    List<String> list = Arrays.stream(report).distinct().toList();
    HashMap<String, Integer> count = new HashMap<>();
    for (String s : list) {
      String target = s.split(" ")[1];
      count.put(target, count.getOrDefault(target, 0) + 1);
    }
    return Arrays.stream(id_list).map(_user -> {
      final String user = _user;
      List<String> reportList = list.stream().filter(s -> s.startsWith(user + " ")).toList();
      // Debug On
      reportList.forEach(item -> {
        System.out.println("item: " + item + ", user: " + user);
      });
      // Debug Off
      return reportList.stream()
              .filter(s -> count.getOrDefault(s.split(" ")[1], 0) >= k)
              .count();
    }).mapToInt(Long::intValue).toArray();
  }
}

class Application {
  public static void main(String args[]) {
    String[] idList = {"muzi", "frodo", "apeach", "neo"};
    String[] report = {"muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"};
    // String[] idList = {"con", "ryan"};
    // String[] report = {"ryan con", "ryan con", "ryan con", "ryan con"};
    Solution s = new Solution();
    int[] result = s.refactoredSolution(idList, report, 2);
    Arrays.stream(result).forEach(System.out::print);
  }
}
