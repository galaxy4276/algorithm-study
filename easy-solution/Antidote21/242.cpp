public class Solution
{
    public bool IsAnagram(string s, string t)
    {      
        char[] temp1 = s.ToCharArray();
        System.Array.Sort(temp1);
        //System.Array.Reverse(temp);
        string s1 =new string(temp1);
        
        char[] temp2 = t.ToCharArray();
        System.Array.Sort(temp2);
        string s2 = new string(temp2);
        
        if(s1.Equals(s2))return true;
        return false;
                
    }
}
