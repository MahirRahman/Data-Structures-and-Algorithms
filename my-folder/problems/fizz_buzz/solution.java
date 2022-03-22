class Solution {
    public List<String> fizzBuzz(int n) {
    //     List<String> answer = new ArrayList<String>();
    //     for (int i = 1; i <= n; i++) {
    //         if (i % 3 == 0) {
    //             if (i % 5 == 0) 
    //                 answer.add("FizzBuzz");
    //             else
    //             answer.add("Fizz");
    //         }
    //         else if (i % 5 == 0) 
    //                 answer.add("Buzz");
    //         else answer.add("" + i);
    //         }
    //     return answer;
    //     }
    
//     //easy for gc
// private String FIZZ = "Fizz";
// private String BUZZ = "Buzz";
// private String FIZZ_BUZZ = "FizzBuzz";

// public List<String> fizzBuzz(int n) {
//     List<String> res = new ArrayList();
//     for(int i = 1; i <= n; i++){
//         //remove if else, make code shorter
//         String temp = i % 15 == 0 ? FIZZ_BUZZ : (i % 3 == 0 ? FIZZ : (i % 5 == 0 ?  BUZZ : String.valueOf(i)));
//         res.add(temp);
//     }
//     return res;
// }
    List<String> answer = new ArrayList<String>();
    for (int i = 1; i <= n; i++) {
        answer.add("" + i);
    }
    for (int i = 2; i < n; i += 3) answer.set(i, "Fizz");
    for (int i = 4; i < n; i+= 5) answer.set(i, "Buzz");
    for (int i = 14; i < n; i+= 15) answer.set(i, "FizzBuzz");
    
    return answer;
    }

}