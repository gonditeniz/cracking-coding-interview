#include <cxxtest/TestSuite.h>
#include "Exercise2.cpp"

class Exercise2Suite : public CxxTest::TestSuite
{
public:
    void test1(void)
    {
        input_data = new char[(strlen("caracola")+1)*sizeof(char)];
        strcpy(input_data, "caracola");
        expected_output = new char[(strlen("caracola")+1)*sizeof(char)];
        strcpy(expected_output, "alocarac");

        checkFunction(run);

        delete input_data;
        delete expected_output;
    }

private:
    char* input_data;
    char* expected_output;
    void checkFunction(void func(char*))
    {
        func(input_data);
        TS_ASSERT_EQUALS(input_data, expected_output);
    }
};
