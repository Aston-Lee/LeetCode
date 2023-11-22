class Solution {
    public int scoreOfParentheses(String s) {
        /*
            ; at ending 
            s.charAt(i)
            s.length()
            &&
        */
        int mult = 1;
        int score = 0;
        
        for (int i=0; i<s.length(); i++){
            if (s.charAt(i) == '('){
                if (i+1 < s.length() && s.charAt(i+1) == '(' ){
                    mult *= 2;
                }else{
                    score += mult;
                    i += 1;
                }
            }else{
                mult /= 2;
            }
                
        }
        return score;
    }
}