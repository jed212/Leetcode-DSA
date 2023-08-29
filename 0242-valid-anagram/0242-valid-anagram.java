class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
        {
            return false;
        }
        int[] counts = new int[26];
        
        for (int i = 0; i < s.length(); i++)
        {
            counts[s.charAt(i) - 'a']++;
            counts[t.charAt(i) - 'a']--;
        }

        for (int n: counts) if (n != 0) return false;

        return true;
    }  
}