class Solution 
{
    public boolean isAnagram(String s, String t) 
    {
        if(s.length() != t.length())
            return false;

        char[] firstString = s.toCharArray();
        char[] secondString = t.toCharArray();

        Arrays.sort(firstString);
        Arrays.sort(secondString);

        if(Arrays.equals(firstString, secondString))
            return true;
    
        return false;
    }
}
