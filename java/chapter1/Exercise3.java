import java.util.Arrays;

public class Exercise3 {

    boolean run(String word1, String word2) {
        if (word1.length() != word2.length()) {
            return false;
        }
        char[] chars = word1.toCharArray();
        Arrays.sort(chars);
        String word1sorted = new String(chars);
        chars = word2.toCharArray();
        Arrays.sort(chars);
        String word2sorted = new String(chars);

        return word1sorted.equals(word2sorted);
        
    }
}
