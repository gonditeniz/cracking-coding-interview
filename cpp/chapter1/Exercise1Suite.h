#include <cxxtest/TestSuite.h>
#include "Exercise1.cpp"

class Exercise1Suite : public CxxTest::TestSuite
{
public:
    void test1(void)
    {
        input_data = "hola";
        expected_output = true;
        checkFunction(uniqueCharacters);
    }

    void test2(void)
    {
        input_data = "holo";
        expected_output = true;
        checkFunction(uniqueCharacters);
    }

private:
    std::string input_data;
    bool expected_output;
    void checkFunction(bool func(std::string))
    {
        TS_ASSERT_EQUALS(func(input_data), expected_output);
    }
};
