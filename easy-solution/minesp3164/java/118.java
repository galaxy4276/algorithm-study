import java.util.ArrayList;

class Solution {
    public List<List<Integer>> generate(int numRows) {

        //This list is the final answer to be obtained
        List<List<Integer>> list = new ArrayList<>();

        //For handling Row 1, which will include 0c0 = 1
        List<Integer> list1 = new ArrayList<>();
        list1.add(1);
        list.add(list1);
        if(numRows == 1) {
            return list;
        }

        for(int i = 1; i < numRows; i++) {
            List<Integer> temp = new ArrayList<>();

            temp.add(1);

            for(int j = 1; j < i; j++) {
                temp.add(list.get(i-1).get(j-1) + list.get(i-1).get(j));
            }

            temp.add(1);
            list.add(temp);
        }

        return list;
    }
}