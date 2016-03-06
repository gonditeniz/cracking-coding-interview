import java.util.HashMap;
import java.lang.Integer;

public class Exercise1 {

    boolean uniqueCharacters(String str) {
    
        HashMap charsHashMap = new HashMap();        
        for(int i = 0; i < str.length(); i++) {
            Integer strVal = new Integer(str.charAt(i));
            Integer numOccurrences = (Integer)charsHashMap.get(strVal);
            if (numOccurrences != null && numOccurrences.intValue() > 0) {
                return false;
            } else {
                charsHashMap.put(strVal, new Integer(1)); 
            }
        }
        return true;
    }

    boolean uniqueCharacters2(String str) {
    
        int charsChecker = 0;       
        for(int i = 0; i < str.length(); i++) {
            int strVal = str.charAt(i);
            if ((charsChecker & (1 << strVal)) != 0) {
                return false;
            } else {
                charsChecker |= (1 << strVal);
            }
        }
        return true;
    }
}
