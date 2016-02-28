import static org.junit.Assert.assertEquals;
import org.junit.Test;
import org.junit.Before;

public class TemplateTest { 

    private int input_data;
    private int expected_output;
    private Template template;

    @Before
    public void setUp() {
        this.template = new Template();
    }

    @Test
    public void test1()  {
        input_data = 1;
        expected_output = 2;
        assertEquals(template.run(this.input_data), this.expected_output);
    }
}
