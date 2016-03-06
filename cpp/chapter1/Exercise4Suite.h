#include <cxxtest/TestSuite.h>
#include "Exercise4.cpp"

class Exercise4Suite : public CxxTest::TestSuite
{
public:
    void test1(void)
    {
        input_data = new char[20];
        strcpy(input_data, "hola hola");
        length = 9;
        expected_output = new char[20];
        strcpy(expected_output, "hola%20hola");
        checkFunction(run);
        delete input_data;
        delete expected_output;
    }
    
    void test2(void)
    {
        input_data = new char[20];
        strcpy(input_data, "hola hola hola");
        length = 14;
        expected_output = new char[20];
        strcpy(expected_output, "hola%20hola%20hola");
        checkFunction(run);
        delete input_data;
        delete expected_output;
    }

private:
    char* input_data;
    int length;
    char* expected_output;
    void checkFunction(void func(char*, int))
    {
        func(input_data, length);
        TS_ASSERT_EQUALS(input_data, expected_output);
    }
};
