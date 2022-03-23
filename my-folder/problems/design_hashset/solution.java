class MyHashSet {
    
    private LinkedList<Integer>[] arr;
    public MyHashSet() {
        arr = new LinkedList[97];        
    }
    
    private int hash(int key) {
        long r = Double.doubleToLongBits(key);
        r = 31 * Double.doubleToLongBits(r);
        return (int) ((((r >> 32) ^ r) % 97) + 97) % 97;
    }
    
    
    public void add(int key) {
        if (!contains(key)) {
        int h = hash(key);
        if (arr[h] == null) arr[h] = new LinkedList<Integer>();
        else System.out.println("Collision for key: " + key + " at " + arr[h]);
        arr[h].addFirst(key);
        }
    }
    
    public void remove(int key) {
        int h = hash(key);
        if (arr[h] != null) {
            arr[h].removeFirstOccurrence(key);
        }
    }
    
    public boolean contains(int key) {
         int loc = hash(key);
        if(arr[loc] != null) {
            return arr[loc].contains(key);
        }
        return false;
//     }
    }
}
// class MyHashSet {
//     private int m;
//     private LinkedList<Integer>[] arr;

//     /** Initialize your data structure here. */
//     public MyHashSet() {
//         m = 1009;
//         arr = new LinkedList[m];
//     }
    
//     private int hash(int key) {
//         long r = Double.doubleToLongBits(key);
//         r = 31 * Double.doubleToLongBits(r);
//         return (int) ((r >> 32) ^ r) % 1009;
//     }
//     public void add(int key) {
//        if(!contains(key)){
//         int loc = hash(key);
//         if(arr[loc] == null) {
//             arr[loc] = new LinkedList<Integer>();
//         }
//         arr[loc].addFirst(key);
//        }
//     }
    
//     public void remove(int key) {
//         int loc = hash(key);
//         if(arr[loc]!=null) {
//             arr[loc].removeFirstOccurrence(key);
//         }
//     }
    
//     /** Returns true if this set contains the specified element */
//     public boolean contains(int key) {
//         int loc = hash(key);
//         if(arr[loc] != null) {
//             return arr[loc].contains(key);
//         }
//         return false;
//     }
// }

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */