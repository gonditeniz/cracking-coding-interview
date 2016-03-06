import static org.junit.Assert.assertEquals;
import org.junit.Test;
import org.junit.Before;

public class Exercise1Test { 

    private String input_data;
    private boolean expected_output;
    private Exercise1 exercise1;

    @Before
    public void setUp() {
        this.exercise1 = new Exercise1();
    }

    @Test
    public void test1_1()  {
        input_data = "hola";
        expected_output = true;
        assertEquals(exercise1.uniqueCharacters(this.input_data), this.expected_output);
    }

    @Test
    public void test1_2()  {
        input_data = "holo";
        expected_output = false;
        assertEquals(exercise1.uniqueCharacters(this.input_data), this.expected_output);
    }

    @Test
    public void test2_1()  {
        input_data = "hola";
        expected_output = true;
        assertEquals(exercise1.uniqueCharacters2(this.input_data), this.expected_output);
    }

    @Test
    public void test2_2()  {
        input_data = "holo";
        expected_output = false;
        assertEquals(exercise1.uniqueCharacters2(this.input_data), this.expected_output);
    }
}
