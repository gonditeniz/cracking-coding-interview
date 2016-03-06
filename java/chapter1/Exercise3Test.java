import static org.junit.Assert.assertEquals;
import org.junit.Test;
import org.junit.Before;

public class Exercise3Test { 

    private String input_data1;
    private String input_data2;
    private boolean expected_output;
    private Exercise3 exercise3;

    @Before
    public void setUp() {
        this.exercise3 = new Exercise3();
    }

    @Test
    public void test1()  {
        input_data1 = "god";
        input_data2 = "dog";
        expected_output = true;
        assertEquals(exercise3.run(this.input_data1, this.input_data2), this.expected_output);
    }

    @Test
    public void test2()  {
        input_data1 = "god";
        input_data2 = "doga";
        expected_output = false;
        assertEquals(exercise3.run(this.input_data1, this.input_data2), this.expected_output);
    }

    @Test
    public void test3()  {
        input_data1 = "godo";
        input_data2 = "doga";
        expected_output = false;
        assertEquals(exercise3.run(this.input_data1, this.input_data2), this.expected_output);
    }
}
