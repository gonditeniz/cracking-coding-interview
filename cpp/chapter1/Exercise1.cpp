#include <map>

bool uniqueCharacters(std::string str)
{
    std::map<char, int> charMap;
    for(std::string::iterator it = str.begin(); it != str.end(); ++it) {
        if (charMap[(*it)] > 0) {
            return false;
        } else {
            charMap[(*it)] = 0;
        }
    }
    return true;
}
