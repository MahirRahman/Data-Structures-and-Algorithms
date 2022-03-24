// class Solution {
//     public String[] findRestaurant(String[] list1, String[] list2) {
//         Map<String, Integer> map = new HashMap<>();
//         LinkedList<String> fin = new LinkedList<>();
//         for (int i = 0; i < list1.length; i++) {
//             map.put(list1[i], i);
//         }
//         int min = 2001;
//         for (int i = 0; i < list2.length; i++) {
//             if (map.containsKey(list2[i])) {
//                 if (map.get(list2[i]) + i <= min) {
//                     if (map.get(list2[i]) + i < min) fin.clear();
//                     min = map.get(list2[i]) + i;
//                     fin.add(list2[i]);
//                 }
//             }
//         }
//         return fin.toArray(new String[fin.size()]);
//     }
// }
public class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        HashMap < Integer, List < String >> map = new HashMap < > ();
        for (int i = 0; i < list1.length; i++) {
            for (int j = 0; j < list2.length; j++) {
                if (list1[i].equals(list2[j])) {
                    if (!map.containsKey(i + j))
                        map.put(i + j, new ArrayList < String > ());
                    map.get(i + j).add(list1[i]);
                }
            }
        }
        int min_index_sum = Integer.MAX_VALUE;
        for (int key: map.keySet())
            min_index_sum = Math.min(min_index_sum, key);
        String[] res = new String[map.get(min_index_sum).size()];
        return map.get(min_index_sum).toArray(res);
    }
}
