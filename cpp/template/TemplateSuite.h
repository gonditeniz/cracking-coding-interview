#include <cxxtest/TestSuite.h>
#include "Template.cpp"

class TemplateSuite : public CxxTest::TestSuite
{
public:
    void test1(void)
    {
        input_data = 1;
        expected_output = 2;
        checkFunction(run);
    }

private:
    int input_data;
    int expected_output;
    void checkFunction(int func(int))
    {
        TS_ASSERT_EQUALS(func(input_data), expected_output);
    }
};
