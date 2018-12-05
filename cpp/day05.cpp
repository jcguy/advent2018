#include <fstream>
#include <iostream>
#include <stack>
#include <string>
#include <vector>

size_t react_length(std::vector<char> &polymer) {
    std::stack<char> stack;

    for (char c : polymer) {
        if (stack.empty()) {
            stack.push(c);
        } else if (abs(c - stack.top()) == 32) {
            stack.pop();
        } else {
            stack.push(c);
        }
    }

    return stack.size();
}


size_t a(std::vector<char> &polymer) {
    return react_length(polymer);
}


size_t b(std::vector<char> &polymer) {
    size_t shortest_length = 999999;
    for (char l = 'a'; l <= 'z'; l++) {
        std::vector<char> modified_polymer;
        for (char c : polymer) {
            if ((c != l) && (abs(c - l) != 32)) {
                modified_polymer.push_back(c);
            }
        }

        size_t modified_length = react_length(modified_polymer);
        if (modified_length < shortest_length) {
            shortest_length = modified_length;
        }
    }

    return shortest_length;
}


int main() {
    std::ifstream infile("../input/input.05");
    std::string input;

    infile >> input;
    infile.close();

    std::vector<char> polymer(input.begin(), input.end());

    std::cout << "Part a:\t" << a(polymer) << "\nPart b:\t" << b(polymer) << "\n";
}
